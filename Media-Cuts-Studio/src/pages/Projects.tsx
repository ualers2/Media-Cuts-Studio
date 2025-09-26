// src/pages/Projects.tsx
import React, { useEffect, useRef, useState } from 'react';
import { useSocketContext } from '@/contexts/SocketContext';
import Layout from '@/components/Layout';
import ProtectedRoute from '@/components/ProtectedRoute';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Dialog, DialogContent, DialogClose } from '@/components/ui/dialog';
import { Button } from '@/components/ui/button';
import { useProjectsContext, ProjectVideo } from '@/contexts/ProjectsContext';
import { toast } from '@/hooks/use-toast';
import { Bot } from 'lucide-react';
import VideoPreview from "@/components/VideoPreview";

import { 
  useProjectHandlers, 
  Spinner, 
  StarIcon, 
  LightbulbIcon, 
  ClockIcon, 
  filterProjects, 
  formatDuration, 
  getProgressBarColor 
} from '@/components/ProjectHelpers';

const Projects = () => {
  const { logMessages } = useSocketContext();
  const { 
    projects, 
    loadingProjects, 
    errorProjects, 
    loadProjects, 
    toggleProjectUsed, 
    toggleProjectDeleted 
  } = useProjectsContext();
  
  // Estados do componente
  const [showVideoModal, setShowVideoModal] = useState(false);
  const [showLoggerModal, setShowLoggerModal] = useState(false);
  const [selectedProject, setSelectedProject] = useState<{ name: string; progress: number, url_original: string; }>();
  const [selectedProjectVideos, setSelectedProjectVideos] = useState<ProjectVideo[]>([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [filter, setFilter] = useState<'todos' | 'utilizados' | 'nao-utilizados'>('todos');
  const [toggleUtilizado, setToggleUtilizado] = useState(false);
  const [downloadingIds, setDownloadingIds] = useState<string[]>([]);
  const [downloadProgress, setDownloadProgress] = useState<Record<string, number>>({});
  const [downloadingAll, setDownloadingAll] = useState(false);
  
  const videomanager_URL = import.meta.env.VITE_VIDEO_MANAGER_URL;
  const videosContainerRef = useRef<HTMLDivElement>(null);

  // Usar o hook customizado para handlers
  const {
    handleProjectClick,
    handleDownloadMetadata,
    handleDownloadAll,
    handleDownloadClick,
    handleCopyAll,
    handleCopyHashtags,
    handleCopyTitle,
    handleToggleUtilizado,
    handleDeleteProject,
  } = useProjectHandlers(
    videomanager_URL,
    setSelectedProject,
    setSelectedProjectVideos,
    setShowVideoModal,
    setShowLoggerModal,
    setDownloadingIds,
    setDownloadProgress,
    setDownloadingAll,
    setToggleUtilizado,
    downloadingIds,
    downloadingAll,
    selectedProject,
    selectedProjectVideos,
    toggleProjectDeleted
  );

  // Carregamento inicial dos projetos
  useEffect(() => {
    const userId = localStorage.getItem('user_email');
    if (userId) {
      loadProjects().catch(err => {
        console.error('Erro ao carregar projetos no mount:', err);
      });
    } 
  }, [loadProjects]);

  // Estados de carregamento e erro
  if (loadingProjects) {
    return (
      <ProtectedRoute>
        <Layout>
          <div className="p-6 text-center text-gray-600 dark:text-gray-400">
            <Spinner className="h-8 w-8 mx-auto mb-4" />
            Carregando projetos...
          </div>
        </Layout>
      </ProtectedRoute>
    );
  }

  if (errorProjects) {
    return (
      <ProtectedRoute>
        <Layout>
          <div className="p-6 text-center text-red-600 dark:text-red-400">
            Erro ao carregar projetos: {errorProjects}
          </div>
        </Layout>
      </ProtectedRoute>
    );
  }

  // Filtrar projetos usando a função helper
  const filteredProjects = filterProjects(projects, searchTerm, filter);
  const project = filteredProjects[0]; 

  return (
    <ProtectedRoute>
      <Layout>
        <div className="p-6 space-y-8 bg-background-light dark:bg-black min-h-screen text-gray-dark dark:text-white transition-colors duration-300">
          <h1 className="text-3xl font-bold mb-6">Meus Projetos</h1>
          
          {/* Filtros de busca + Refresh */}
          <div className="mb-4 flex flex-col md:flex-row md:items-center md:space-x-4 space-y-2 md:space-y-0">
            <input
              type="text"
              placeholder="Buscar por nome do projeto..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full md:w-1/2 px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-800 dark:text-white"
            />

            <select
              value={filter}
              onChange={(e) => setFilter(e.target.value as typeof filter)}
              className="w-full md:w-auto px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-800 text-gray-900 dark:text-white shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <option value="todos">Todos os projetos</option>
              <option value="utilizados">Somente utilizados</option>
              <option value="nao-utilizados">Somente não utilizados</option>
            </select>

            {/* Botão Refresh */}
            <Button
              variant="outline"
              onClick={() => {
                const userId = localStorage.getItem('user_email');
                if (userId) {
                  loadProjects({ force: true }).then(() => {
                    console.log("Projetos atualizados!");
                    // window.location.reload();
                  })
                }
              }}
              className="flex items-center gap-2"
            >
              🔄 Atualizar Projetos
            </Button>
          </div>
          {/* Lista de projetos */}
          {filteredProjects.length === 0 ? (
            <p className="text-center text-gray-600 dark:text-gray-400">
              {projects.length === 0 
                ? "Nenhum projeto salvo. Novos cortes da IA aparecerão aqui!"
                : "Nenhum projeto encontrado com os filtros aplicados."
              }
            </p>
          ) : (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
              {filteredProjects.map((project) => {
                const progress = parseFloat(project.progress_percent);
                return (
                  <Card
                    key={project.name}
                    className="relative z-0 bg-white dark:bg-deep-purple border dark:border-border-dark shadow-lg hover:shadow-xl transition-shadow duration-300 cursor-pointer"
                    onClick={() => handleProjectClick(project.name, project.videos, project.url_original, progress)}
                  >
                    {/* Botões de ação para projetos completos */}
                    {progress === 100 && (
                      <div className="absolute bottom-2 right-2 flex gap-2">
                        <Button
                          variant="ghost"
                          size="sm"
                          onClick={(e) => {
                            e.stopPropagation();
                            const wasUsed = project.used;
                            toggleProjectUsed(project.name, !wasUsed);
                            handleToggleUtilizado(project.name, wasUsed);
                          }}
                        >
                          {project.used ? '✓ Utilizado' : 'Marcar'}
                        </Button>

                        <Button
                          variant="destructive"
                          size="sm"
                          onClick={(e) => {
                            e.stopPropagation();
                            handleDeleteProject(project.name);
                          }}
                          className="text-xs rounded px-2 py-1"
                        >
                          ❌ Excluir
                        </Button>
                      </div>
                    )}

                    {/* Badge "Novo" */}
                    {project.isNew && (
                      <span className="absolute top-2 right-2 z-10 bg-green-500 text-white text-xs font-bold px-2 py-1 rounded-full animate-pulse">
                        NOVO
                      </span>
                    )}

                    {/* Thumbnail */}
                    <div className="relative w-full h-40 bg-gray-200 dark:bg-gray-700 overflow-hidden flex items-center justify-center">
                      {project.thumbnail_url ? (
                        <img
                          src={project.thumbnail_url}
                          alt={`Thumbnail ${project.name}`}
                          className="w-full h-full object-cover"
                        />
                      ) : (
                        <span className="text-gray-500 dark:text-gray-400">
                          Sem thumbnail
                        </span>
                      )}
                    </div>

                    <CardHeader className="p-4">
                      <CardTitle className="text-lg font-semibold truncate">
                        {project.name}
                      </CardTitle>
                      <p className="text-xs mt-1 text-gray-500 dark:text-gray-400">
                        Modelo de IA: <span className="font-medium text-blue-600">{project.model_ai}</span>
                      </p>
                    </CardHeader>

                    <CardContent className="px-4 pb-4 pt-0">
                      <p className="text-sm text-gray-600 dark:text-gray-400">
                        Total: <span className="font-semibold">{project.videos.length}</span>
                      </p>
                    </CardContent>

                    {/* Barra de progresso ou estado de falha */}
                    {project.status === "Failed" ? (
                      <div className="px-4 pb-4">
                        <div className="flex justify-center mb-1 text-xs font-semibold text-red-600 dark:text-red-400">
                          ❌ Projeto falhou
                        </div>
                        <div className="w-full h-2 bg-red-600 rounded-full" />
                      </div>
                    ) : (
                      progress < 100 && progress >= 0 && (
                        <div className="px-4 pb-4">
                          <div className="flex justify-center mb-1 text-xs font-semibold text-gray-700 dark:text-gray-300">
                            <ClockIcon /> {project.progress_percent}% Do Projeto Concluído
                          </div>
                          <div className="relative">
                            <div className="w-full h-2 bg-gray-300 dark:bg-gray-700 rounded-full overflow-hidden">
                              <div
                                className={`h-full transition-all duration-300 ${getProgressBarColor(progress)}`}
                                style={{ width: `${progress}%` }}
                              />
                            </div>
                          </div>
                        </div>
                      )
                    )}
                  </Card>
                );
              })}
            </div>
          )}

          {/* Modal de Vídeos */}
          <Dialog open={showVideoModal} onOpenChange={setShowVideoModal}>
            <DialogContent className="max-w-6xl max-h-[90vh] p-6 bg-white dark:bg-gray-800 rounded-lg shadow-xl overflow-hidden">
              <div className="flex justify-between items-center mb-4">
                <div className="flex items-center space-x-2">
                  <h2
                  className="text-xl font-semibold"> Vídeos do Projeto: {selectedProject?.name}
                  </h2>
                  <Button
                    size="sm"
                    variant="outline"
                    onClick={(e) => {
                      e.stopPropagation(); // evita que clique abra o modal
                      if (selectedProject?.url_original) {
                        navigator.clipboard.writeText(selectedProject?.url_original);
                        toast({
                          title: 'Copiado!',
                          description: 'Link do vídeo copiado!',
                          variant: 'default',
                          duration: 5000,
                        });
                      } else {
                        toast({
                          title: 'URL',
                          description: 'URL do vídeo não disponível.',
                          variant: 'default',
                          duration: 5000,
                        });
                      }
                    }}
                    className="h-6 px-2 text-xs"
                  >
                    🔗 Copiar Link 
                  </Button>
                </div>
                <DialogClose asChild>
                  <Button
                    variant="ghost"
                    className="p-2 rounded-full"
                    aria-label="Fechar"
                  >
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </Button>
                </DialogClose>
              </div>

              {/* Botões de ação */}
              <div className="flex justify-start gap-2 mb-4">
                <Button
                  onClick={handleDownloadAll}
                  disabled={downloadingAll}
                  className="inline-flex items-center px-3 py-1.5 text-sm text-white bg-gradient-to-r from-green-600 to-blue-600 hover:from-green-700 hover:to-blue-700 dark:from-green-700 dark:to-blue-700 dark:hover:from-green-800 dark:hover:to-blue-800 rounded-md shadow-lg transition-colors duration-300 disabled:opacity-50"
                >
                  {downloadingAll ? (
                    <Spinner className="h-4 w-4 mr-1" />
                  ) : (
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-1" fill="currentColor" viewBox="0 0 24 24">
                      <path d="M5 20h14v-2H5v2zm7-18L5.33 9h4.17v6h5V9h4.17L12 2z" />
                    </svg>
                  )}
                  {downloadingAll ? 'Baixando...' : 'Baixar todos em 4K'}
                </Button>

                <Button
                  variant="outline"
                  size="sm"
                  onClick={(e) => { 
                    e.stopPropagation(); 
                    handleDownloadMetadata(); 
                  }}
                  className="inline-flex items-center px-3 py-1.5 text-sm rounded-md shadow-sm"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-2" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <path d="M12 3v12" strokeLinecap="round" strokeLinejoin="round" />
                    <path d="M8 11l4 4 4-4" strokeLinecap="round" strokeLinejoin="round" />
                    <path d="M21 21H3" strokeLinecap="round" strokeLinejoin="round" />
                  </svg>
                  Baixar metadados (.json)
                </Button>
              </div>

              {/* Lista de vídeos */}
              {selectedProjectVideos.length === 0 ? (
                <p className="text-center text-gray-600 dark:text-gray-400">
                  Nenhum vídeo neste projeto.
                </p>
              ) : (
                <div className="max-h-[70vh] overflow-y-auto pr-2" ref={videosContainerRef}>
                  {selectedProjectVideos.map((video, index) => (
                    <Card key={video.id} className="mb-4 bg-gray-50 dark:bg-gray-700 border dark:border-gray-600">
                      <CardHeader className="py-3 px-4">
                        <CardTitle className="text-lg font-semibold flex justify-between items-center">
                          <span className="truncate">{`#${index + 1} ${video.title}`}</span>
                          <Button
                            variant="outline"
                            size="sm"
                            className="text-xs ml-2 shrink-0"
                            onClick={(e) => {
                              e.stopPropagation();
                              handleCopyTitle(video.title);
                            }}
                          >
                            📋 Copiar Título
                          </Button>
                        </CardTitle>
                      </CardHeader>
                      
                      <CardContent className="px-4 pb-4 grid grid-cols-1 md:grid-cols-3 gap-4">
                        {/* Preview do vídeo */}
                        <div className="md:col-span-1 flex flex-col items-center justify-center relative">
                          <VideoPreview
                            video={video}
                            previewEndpoint={`${videomanager_URL}/api/projects/${selectedProject?.name}/videos/${video.id}/preview`}
                            isOpen={showVideoModal}
                            allowLoad={!downloadingAll}
                          />
                          <Button
                            variant="secondary"
                            size="sm"
                            className="absolute bottom-2 right-2 bg-black/50 text-white rounded-full p-2 hover:bg-black/70"
                            onClick={(e) => {
                              e.stopPropagation();
                              const videoElement = e.currentTarget.parentElement?.querySelector('video');
                              if (videoElement) {
                                if (videoElement.paused) {
                                  videoElement.play();
                                } else {
                                  videoElement.pause();
                                }
                              }
                            }}
                          >
                            ▶️
                          </Button>
                        </div> 

                        {/* Informações do vídeo */}
                        <div className="md:col-span-2 flex flex-col space-y-3">
                          {/* Métricas */}
                          <div className="flex items-center space-x-4 text-sm flex-wrap gap-2">
                            {video.potencial_de_viralizacao && (
                              <span className="flex items-center bg-yellow-100 dark:bg-yellow-900 text-yellow-800 dark:text-yellow-200 font-bold px-2.5 py-1 rounded-full">
                                <StarIcon /> Potencial: {video.potencial_de_viralizacao}/10
                              </span>
                            )}
                            {video.sentimento_principal && (
                              <span className="capitalize bg-purple-100 dark:bg-purple-900 text-purple-800 dark:text-purple-200 font-medium px-2.5 py-1 rounded-full">
                                Sentimento: {video.sentimento_principal}
                              </span>
                            )}
                          </div>

                          {/* Justificativa da IA */}
                          {video.justificativa && (
                            <div className="text-sm text-gray-700 dark:text-gray-300 bg-blue-50 dark:bg-gray-600/50 p-3 rounded-md">
                              <p className="flex items-center font-medium mb-2 text-purple-600 dark:text-purple-300">
                                <Bot className="w-4 h-4 mr-1 text-purple-500" />
                                Justificativa da IA
                              </p>
                              <p className="pl-5">{video.justificativa}</p>
                            </div>
                          )}

                          {/* Descrição */}
                          {video.descricao && (
                            <p className="text-sm text-gray-700 dark:text-gray-300 line-clamp-3">
                              <strong>Descrição:</strong> {video.descricao}
                            </p>
                          )}

                          {/* Hashtags */}
                          {video.hashtags?.length > 0 && (
                            <div>
                              <div className="flex items-center justify-between">
                                <strong className="text-sm font-medium text-gray-700 dark:text-gray-300">Hashtags:</strong>
                                <Button
                                  variant="ghost"
                                  size="sm"
                                  className="text-xs text-blue-600 dark:text-blue-300"
                                  onClick={(e) => {
                                    e.stopPropagation();
                                    handleCopyHashtags(video.hashtags);
                                  }}
                                >
                                  📋 Copiar hashtags
                                </Button>
                              </div>
                              <div className="flex flex-wrap gap-1 mt-1">
                                {video.hashtags.map((tag, i) => (
                                  <span
                                    key={i}
                                    className="bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 text-xs font-medium px-2.5 py-0.5 rounded-full"
                                  >
                                    #{tag}
                                  </span>
                                ))}
                              </div>
                            </div>
                          )}

                          {/* Tempo do vídeo */}
                          {(video.minutagemdeInicio || video.minutagemdeFim) && (
                            <div className="text-sm text-gray-700 dark:text-gray-300">
                              <strong>Tempo:</strong> {video.minutagemdeInicio || '00:00'} – {video.minutagemdeFim || 'Fim'}
                              {video.minutagemdeInicio && video.minutagemdeFim && (
                                <span className="ml-2 text-gray-500">
                                  ({formatDuration(video.minutagemdeInicio, video.minutagemdeFim)})
                                </span>
                              )}
                            </div>
                          )}

                          {/* Botões de ação do vídeo */}
                          <div className="flex justify-between items-center pt-2 gap-2">
                            <Button
                              variant="outline"
                              size="sm"
                              className="text-xs"
                              onClick={(e) => {
                                e.stopPropagation();
                                handleCopyAll(video.title, video.hashtags);
                              }}
                            >
                              📋 Copiar Título e Hashtags
                            </Button>

                            <Button
                              onClick={(e) => {
                                e.stopPropagation();
                                handleDownloadClick(video.id!, video.filename);
                              }}
                              disabled={downloadingAll || downloadingIds.includes(video.id!)}
                              className={`inline-flex items-center px-4 py-2 text-white rounded-md shadow-lg transition-colors duration-300 ${
                                downloadingAll || downloadingIds.includes(video.id!) 
                                  ? 'opacity-70 cursor-not-allowed bg-gray-500' 
                                  : 'bg-gradient-to-r from-primary-purple to-accent-blue hover:from-primary-purple-dark hover:to-accent-blue'
                              }`}
                            >
                              {downloadingIds.includes(video.id!) ? (
                                <>
                                  <Spinner className="h-4 w-4 mr-2" />
                                  {downloadProgress[video.id!] === -1 ? 'Baixando...' : `${downloadProgress[video.id!] ?? 0}%`}
                                </>
                              ) : (
                                <>
                                  <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-2" fill="currentColor" viewBox="0 0 24 24">
                                    <path d="M5 20h14v-2H5v2zm7-18L5.33 9h4.17v6h5V9h4.17L12 2z" />
                                  </svg>
                                  Baixar em 4K
                                </>
                              )}
                            </Button>
                          </div>
                        </div>
                      </CardContent>
                    </Card>
                  ))}
                </div>
              )}
            </DialogContent>
          </Dialog>

          {/* Modal de Logger */}
          <Dialog open={showLoggerModal} onOpenChange={setShowLoggerModal}>
            <DialogContent className="max-w-4xl max-h-[80vh] p-6 bg-white dark:bg-gray-800 rounded-lg shadow-xl">
              <div className="flex justify-between items-center mb-4">
                <h2 className="text-2xl font-semibold text-gray-900 dark:text-gray-100">
                  Processo: {selectedProject?.name}
                </h2>
                <DialogClose asChild>
                  <Button variant="ghost" className="p-2 rounded-full" aria-label="Fechar">
                    ✕
                  </Button>
                </DialogClose>
              </div>
              
              <div className="space-y-4">
                <div>
                  <h3 className="font-medium mb-2 flex items-center">
                    <LightbulbIcon />
                    Info Logs
                  </h3>
                  <textarea
                    readOnly
                    value={logMessages.join('\n')}
                    className="w-full h-60 p-3 text-sm font-mono rounded resize-none bg-gray-100 dark:bg-gray-900 text-gray-800 dark:text-gray-200 border border-gray-200 dark:border-gray-700 focus:outline-none"
                    placeholder="Aguardando logs do processo..."
                  />
                </div>
              </div>
            </DialogContent>
          </Dialog>
        </div>
      </Layout>
    </ProtectedRoute>
  );
};

export default Projects;