// src/pages/Process.tsx
import React, { useEffect, useRef, useState } from 'react';
import { useSocketContext, VideoFile } from '@/contexts/SocketContext';
import Layout from '@/components/Layout';
import ProtectedRoute from '@/components/ProtectedRoute';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Progress } from '@/components/ui/progress';
import { Dialog, DialogTrigger, DialogContent, DialogClose } from '@/components/ui/dialog';
import { Button } from '@/components/ui/button';
import { toast } from 'react-hot-toast'; // Ensure this import is correct

const Process = () => {
  const { progress, runningTime, logMessages, agentLogs, videoFiles, fields } = useSocketContext();
  const [showVideoModal, setShowVideoModal] = useState(false);

  const infoLogsRef = useRef<HTMLTextAreaElement>(null);
  const agentLogsRef = useRef<HTMLTextAreaElement>(null);

  // Opens modal when a new video arrives
  useEffect(() => {
    if (videoFiles.length > 0) {
      setShowVideoModal(true);
    }
  }, [videoFiles]);

  useEffect(() => {
    if (infoLogsRef.current) {
      infoLogsRef.current.scrollTop = infoLogsRef.current.scrollHeight;
    }
  }, [logMessages]);

  useEffect(() => {
    if (agentLogsRef.current) {
      agentLogsRef.current.scrollTop = agentLogsRef.current.scrollHeight;
    }
  }, [agentLogs]);

  return (
    <ProtectedRoute>
      <Layout>
        <div className="p-6 space-y-8 bg-gray-50 dark:bg-gray-900 min-h-screen text-gray-900 dark:text-gray-100 transition-colors duration-300">
          {/* Card de campos */}
          <Card className="bg-white dark:bg-gray-800 border dark:border-gray-700 shadow-sm">
            <CardHeader>
              <CardTitle className="text-gray-900 dark:text-gray-100">Process Management</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              {Object.entries(fields).map(([label, value], index) => (
                <div key={index} className="flex items-center gap-3">
                  <span className="font-medium text-gray-700 dark:text-gray-300 min-w-[140px]">{label}:</span>
                  <div className="flex-1 text-sm text-gray-600 dark:text-gray-400">{value}</div>
                </div>
              ))}

              <div className="space-y-2">
                <div className="flex justify-between">
                  <span className="font-medium text-gray-700 dark:text-gray-300">Progress Create:</span>
                  <span className="text-sm text-gray-500 dark:text-gray-400">{progress}%</span>
                </div>
                <Progress value={progress} className="h-2" />

                <div className="flex justify-between">
                  <span className="font-medium text-gray-700 dark:text-gray-300">Running time:</span>
                  <span className="text-sm text-gray-500 dark:text-gray-400">{runningTime}</span>
                </div>
              </div>
            </CardContent>
          </Card>

          {/* Botão para abrir modal de vídeos manualmente */}
          {/* {videoFiles.length > 0 && (
            <Button onClick={() => setShowVideoModal(true)} className="fixed bottom-6 right-6 z-50">
              Ver vídeos ({videoFiles.length})
            </Button>
          )} */}

          {/* Modal de download de vídeos */}
          <Dialog open={showVideoModal} onOpenChange={setShowVideoModal}>
            <DialogTrigger asChild>
              {/* empty, we use the button above */}
              <></>
            </DialogTrigger>
            <DialogContent className="max-w-xl p-6 bg-white dark:bg-gray-800 rounded-lg shadow-xl"> {/* Aumentado o max-w para acomodar mais conteúdo */}
              <div className="flex justify-between items-center mb-4">
                <h2 className="text-2xl font-semibold text-gray-900 dark:text-gray-100">Vídeos Disponíveis</h2>
                <DialogClose asChild>
                  <Button
                    variant="ghost"
                    className="text-gray-500 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-700 p-2 rounded-full"
                    aria-label="Fechar"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      className="h-6 w-6"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth={2}
                        d="M6 18L18 6M6 6l12 12"
                      />
                    </svg>
                  </Button>
                </DialogClose>
              </div>

              {videoFiles.length === 0 ? (
                <p className="text-center text-gray-600 dark:text-gray-400">Nenhum vídeo disponível no momento.</p>
              ) : (
                <div className="max-h-[70vh] overflow-y-auto pr-2"> {/* Aumentado a altura máxima para melhor visualização */}
                  {videoFiles.map((video: VideoFile, idx: number) => (
                    <Card key={idx} className="mb-4 bg-gray-50 dark:bg-gray-700 border dark:border-gray-600 overflow-hidden"> {/* Adicionado overflow-hidden */}
                      <CardHeader className="py-3 px-4">
                        <CardTitle className="text-lg font-semibold text-gray-900 dark:text-gray-100">
                          {video.title}
                        </CardTitle>
                      </CardHeader>
                      <CardContent className="px-4 pb-4 grid grid-cols-1 md:grid-cols-3 gap-4"> {/* Usando grid para layout responsivo */}
                        {video.urltumbnail && (
                          <div className="md:col-span-1 flex justify-center items-center">
                            <img
                              src={video.urltumbnail}
                              alt={`Thumbnail do vídeo ${video.title}`}
                              className="rounded-md object-cover w-full h-32 md:h-full max-w-full"
                              style={{ maxHeight: '150px' }} // Altura máxima para a thumbnail
                            />
                          </div>
                        )}
                        <div className={`flex flex-col ${video.urltumbnail ? 'md:col-span-2' : 'md:col-span-3'}`}> {/* Ajusta o span dependendo da thumbnail */}
                          {video.descricao && (
                            <p className="text-sm text-gray-700 dark:text-gray-300 mb-2 line-clamp-3"> {/* Limita a descrição a 3 linhas */}
                              <strong className="font-medium">Descrição:</strong> {video.descricao}
                            </p>
                          )}
                          {video.hashtags && video.hashtags.length > 0 && (
                            <div className="mb-2">
                              <strong className="text-sm font-medium text-gray-700 dark:text-gray-300">Hashtags:</strong>
                              <div className="flex flex-wrap gap-1 mt-1">
                                {video.hashtags.map((tag, tagIdx) => (
                                  <span key={tagIdx} className="bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 text-xs font-medium px-2.5 py-0.5 rounded-full">
                                    #{tag}
                                  </span>
                                ))}
                              </div>
                            </div>
                          )}
                          {(video.minutagemdeInicio || video.minutagemdeFim) && (
                            <div className="text-sm text-gray-700 dark:text-gray-300 mb-4">
                              <strong className="font-medium">Tempo:</strong>{' '}
                              {video.minutagemdeInicio || '00:00'} - {video.minutagemdeFim || 'Fim'}
                            </div>
                          )}
                          <div className="flex justify-end mt-auto"> {/* Move o botão para o final e alinha à direita */}
                            <a
                              href={`data:video/mp4;base64,${video.video_base64}`}
                              download={video.filename}
                              className="inline-flex items-center justify-center px-5 py-2 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 dark:bg-blue-700 dark:hover:bg-blue-800 transition-colors duration-200"
                              onClick={() => toast.success('Download iniciado...', { position: 'bottom-center' })}
                            >
                              <svg
                                xmlns="http://www.w3.org/2000/svg"
                                className="h-5 w-5 mr-2"
                                viewBox="0 0 20 20"
                                fill="currentColor"
                              >
                                <path
                                  fillRule="evenodd"
                                  d="M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm3.293-7.707a1 1 0 011.414 0L9 10.586V3a1 1 0 112 0v7.586l1.293-1.293a1 1 0 111.414 1.414l-3 3a1 1 0 01-1.414 0l-3-3a1 1 0 010-1.414z"
                                  clipRule="evenodd"
                                />
                              </svg>
                              Baixar
                            </a>
                          </div>
                        </div>
                      </CardContent>
                    </Card>
                  ))}
                </div>
              )}
            </DialogContent>
          </Dialog>

          {/* Card de Info Logs */}
          <Card className="bg-white dark:bg-gray-800 border dark:border-gray-700 shadow-sm">
            <CardHeader>
              <CardTitle className="text-gray-900 dark:text-gray-100">Info Logs</CardTitle>
            </CardHeader>
            <CardContent>
              <textarea
                ref={infoLogsRef}
                value={logMessages.join('\n')}
                readOnly
                className="w-full h-48 p-2 text-sm font-mono rounded resize-none
                               bg-gray-100 dark:bg-gray-900 text-gray-800 dark:text-gray-200
                               border border-gray-200 dark:border-gray-700" // Added border for better visibility in dark mode
              />
            </CardContent>
          </Card>
        </div>
      </Layout>
    </ProtectedRoute>
  );
};

export default Process;