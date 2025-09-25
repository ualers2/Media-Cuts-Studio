// src/components/ProjectHelpers.tsx
import React from 'react';
import { toast } from 'react-hot-toast';
import { ProjectVideo } from '@/contexts/ProjectsContext';
import { runWithLimit } from '@/utils/previewQueue';

// Componente Spinner
const Spinner = ({ className = 'h-4 w-4 mr-2' }: { className?: string }) => (
  <svg className={`animate-spin ${className}`} xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z"></path>
  </svg>
);

// Ícones
const StarIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-1 text-yellow-500" viewBox="0 0 20 20" fill="currentColor">
    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
  </svg>
);

const LightbulbIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-1.5 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
    <path d="M11 3a1 1 0 10-2 0v1a1 1 0 102 0V3zM15.657 5.757a1 1 0 00-1.414-1.414l-.707.707a1 1 0 001.414 1.414l.707-.707zM18 10a1 1 0 01-1 1h-1a1 1 0 110-2h1a1 1 0 011 1zM5.05 6.464A1 1 0 106.464 5.05l-.707-.707a1 1 0 00-1.414 1.414l.707.707zM5 10a1 1 0 01-1 1H3a1 1 0 110-2h1a1 1 0 011 1zM8 16v-1h4v1a2 2 0 11-4 0zM12 14c.015-.34.208-.646.477-.859a4 4 0 10-4.954 0c.27.213.462.519.477.859h4z" />
  </svg>
);

const ClockIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-white inline-block align-text-bottom" viewBox="0 0 20 20" fill="currentColor">
    <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z" clipRule="evenodd" />
  </svg>
);

// Função utilitária para criar blob de chunks
function createBlobFromChunks(chunks: Uint8Array[], mimeType = 'video/mp4'): Blob {
  const totalLength = chunks.reduce((acc, c) => acc + c.length, 0);
  const u8 = new Uint8Array(totalLength);
  let offset = 0;
  for (const chunk of chunks) {
    u8.set(chunk, offset);
    offset += chunk.length;
  }
  return new Blob([u8], { type: mimeType });
}

// Função para remover duplicatas por ID
function uniqueById(videos: ProjectVideo[]): ProjectVideo[] {
  const map = new Map<string, ProjectVideo>();
  for (const v of videos) {
    if (!map.has(v.id)) map.set(v.id, v);
  }
  return Array.from(map.values());
}

// Hook personalizado para gerenciar handlers de projeto
export const useProjectHandlers = (
  videomanager_URL: string,
  setSelectedProject: React.Dispatch<React.SetStateAction<{ name: string; progress: number, url_original: string; } | undefined>>,
  setSelectedProjectVideos: React.Dispatch<React.SetStateAction<ProjectVideo[]>>,
  setShowVideoModal: React.Dispatch<React.SetStateAction<boolean>>,
  setShowLoggerModal: React.Dispatch<React.SetStateAction<boolean>>,
  setDownloadingIds: React.Dispatch<React.SetStateAction<string[]>>,
  setDownloadProgress: React.Dispatch<React.SetStateAction<Record<string, number>>>,
  setDownloadingAll: React.Dispatch<React.SetStateAction<boolean>>,
  setToggleUtilizado: React.Dispatch<React.SetStateAction<boolean>>,
  downloadingIds: string[],
  downloadingAll: boolean,
  selectedProject: { name: string; progress: number } | undefined,
  selectedProjectVideos: ProjectVideo[],
  toggleProjectDeleted: (projectName: string) => void
) => {
  
  const handleProjectClick = (name: string, videos: ProjectVideo[], url_original: string, progress: number) => {
    setSelectedProject({ name, progress, url_original });
    if (progress < 29) {
      setShowLoggerModal(true);
    } else {
      setSelectedProjectVideos(uniqueById(videos));
      setShowVideoModal(true);
    }
  };

  const handleDownloadMetadata = async () => {
    if (!selectedProject) {
      toast.error('Nenhum projeto selecionado.', { position: 'bottom-center' });
      return;
    }

    const toastId = toast.loading('Gerando JSON de metadados...', { position: 'bottom-center' });

    try {
      const user_email = localStorage.getItem('user_email') || '';
      const apiKey = localStorage.getItem('api_key') || '';

      const resp = await fetch(
        `${videomanager_URL}/api/projects/metadata/${encodeURIComponent(user_email)}/${encodeURIComponent(selectedProject.name)}`,
        {
          method: 'GET',
          headers: {
            'Authorization': `Bearer ${apiKey}`,
            'X-User-Id': user_email,
          },
        }
      );

      if (!resp.ok) {
        let errText = 'Erro ao buscar metadados.';
        try {
          const ejson = await resp.json();
          errText = ejson.message || errText;
        } catch (_) {}
        throw new Error(errText);
      }

      const json = await resp.json();

      // Normaliza o nome do arquivo para download
      const safeName = `${selectedProject.name.replace(/\s+/g, '_')}_metadata.json`;

      const blob = new Blob([JSON.stringify(json, null, 2)], { type: 'application/json' });
      const url = window.URL.createObjectURL(blob);

      const a = document.createElement('a');
      a.href = url;
      a.download = safeName;
      document.body.appendChild(a);
      a.click();
      a.remove();

      window.URL.revokeObjectURL(url);

      toast.success('Metadados prontos para download (.json)!', { id: toastId });
    } catch (err: any) {
      toast.error(`Falha ao gerar metadados: ${err.message || err}`, { id: toastId });
      console.error(err);
    }
  };

  const handleDownloadAll = async () => {
    if (downloadingAll) return;
    if (!selectedProjectVideos || selectedProjectVideos.length === 0) {
      toast.error('Nenhum vídeo para baixar.', { position: 'bottom-center' });
      return;
    }
    if (!selectedProject) {
      toast.error('Projeto não selecionado.', { position: 'bottom-center' });
      return;
    }

    setDownloadingAll(true);
    // dá chance para o React/browser aplicar o re-render e propagar allowLoad=false aos VideoPreview
    await new Promise((resolve) => requestAnimationFrame(resolve));

    const toastId = toast.loading('Iniciando download em lote...', { position: 'bottom-center' });

    try {
      // função que realiza um download único
      const downloadOne = async (video: ProjectVideo) => {
        const videoId = video.id!;
        setDownloadingIds(prev => (prev.includes(videoId) ? prev : [...prev, videoId]));
        setDownloadProgress(prev => ({ ...prev, [videoId]: 0 }));

        try {
          // monta URL otimizada com nome do projeto
          const projectNameEncoded = encodeURIComponent(selectedProject!.name);
          const downloadUrl = `${videomanager_URL}/api/projects/${projectNameEncoded}/videos/${videoId}/download`;

          const response = await fetch(downloadUrl, {
            method: 'GET',
            headers: {
              'Authorization': `Bearer ${localStorage.getItem('api_key')}`,
              'X-User-Id': localStorage.getItem('user_email'),
            },
          });

          if (!response.ok) {
            const error = await response.json().catch(() => ({}));
            throw new Error(error.message || `Erro ao baixar vídeo ${video.filename}`);
          }
          if (!response.body) throw new Error("Corpo da resposta não disponível.");

          const totalLength = parseInt(response.headers.get('Content-Length') || '0', 10);
          const reader = response.body.getReader();
          const chunks: Uint8Array[] = [];
          let receivedLength = 0;

          while (true) {
            const { done, value } = await reader.read();
            if (done) break;
            if (value) {
              chunks.push(value);
              receivedLength += value.length;
              if (totalLength > 0) {
                const percent = Math.round((receivedLength / totalLength) * 100);
                setDownloadProgress(prev => ({ ...prev, [videoId]: percent }));
              } else {
                setDownloadProgress(prev => ({ ...prev, [videoId]: -1 }));
              }
            }
          }

          const blob = createBlobFromChunks(chunks, 'video/mp4');
          const url = window.URL.createObjectURL(blob);
          const a = document.createElement('a');
          a.href = url;
          a.download = video.filename;
          document.body.appendChild(a);
          a.click();
          a.remove();
          window.URL.revokeObjectURL(url);

          toast.success(`Download de "${video.filename}" concluído.`, { position: 'bottom-center' });
        } finally {
          setDownloadingIds(prev => prev.filter(id => id !== videoId));
          setDownloadProgress(prev => {
            const copy = { ...prev };
            delete copy[videoId];
            return copy;
          });
        }
      };

      // Executa os downloads um-a-um respeitando o limite de concorrência do runWithLimit
      for (const video of selectedProjectVideos) {
        await runWithLimit(() => downloadOne(video));
      }

      toast.success('Todos os vídeos foram baixados com sucesso!', { id: toastId });
    } catch (err: any) {
      toast.error(`Erro no download em lote: ${err?.message || err}`, { id: toastId });
      console.error(err);
    } finally {
      setDownloadingAll(false);
      setDownloadingIds([]);
      setDownloadProgress({});
    }
  };

  const handleDownloadClick = async (videoId: string, filename: string) => {
    // evita clique duplo quando já baixando
    if (downloadingIds.includes(videoId) || downloadingAll) return;
    if (!selectedProject) {
      toast.error('Projeto não selecionado.', { position: 'bottom-center' });
      return;
    }

    setDownloadingIds(prev => [...prev, videoId]);
    setDownloadProgress(prev => ({ ...prev, [videoId]: 0 }));

    // monta URL otimizada com nome do projeto
    const projectNameEncoded = encodeURIComponent(selectedProject.name);
    const downloadUrl = `${videomanager_URL}/api/projects/${projectNameEncoded}/videos/${videoId}/download`;
    const toastId = toast.loading('Iniciando download...', { position: 'bottom-center' });

    try {
      const response = await fetch(downloadUrl, {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('api_key')}`,
          'X-User-Id': localStorage.getItem('user_email'),
        },
      });

      if (!response.ok) {
        const error = await response.json().catch(() => ({}));
        throw new Error(error.message || `Erro ao baixar vídeo ${filename}`);
      }

      if (!response.body) {
        throw new Error("Corpo da resposta não disponível.");
      }

      const totalLength = parseInt(response.headers.get('Content-Length') || '0', 10);
      const reader = response.body.getReader();
      const chunks: Uint8Array[] = [];
      let receivedLength = 0;

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        if (value) {
          chunks.push(value);
          receivedLength += value.length;

          if (totalLength > 0) {
            const percent = Math.round((receivedLength / totalLength) * 100);
            setDownloadProgress(prev => ({ ...prev, [videoId]: percent }));
          } else {
            // quando o total é desconhecido, usa -1 para indicar atividade sem % exata
            setDownloadProgress(prev => ({ ...prev, [videoId]: -1 }));
          }
        }
      }

      const blob = createBlobFromChunks(chunks, 'video/mp4');
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      a.remove();
      window.URL.revokeObjectURL(url);

      toast.success('Download concluído!', { id: toastId });
    } catch (err: any) {
      toast.error(`Falha no download: ${err?.message || err}`, { id: toastId });
      console.error(err);
    } finally {
      // limpar estado
      setDownloadingIds(prev => prev.filter(id => id !== videoId));
      setDownloadProgress(prev => {
        const copy = { ...prev };
        delete copy[videoId];
        return copy;
      });
    }
  };

  const handleCopyAll = (title: string, hashtags?: string[]) => {
    const normalized = hashtags
      ?.map(h => `#${h.replace(/^[#\s]+/, '')}`) // remove # e espaços extras
      .join(' ');

    let formatted = `${title}${normalized ? ' ' + normalized : ''}`;

    // garante no máximo 98 caracteres
    if (formatted.length > 98) {
      formatted = formatted.slice(0, 98);
    }

    navigator.clipboard.writeText(formatted);
    toast.success('Título e hashtags copiados!', { position: 'bottom-center' });
  };

  const handleCopyHashtags = (hashtags?: string[]) => {
    const normalized = hashtags
      ?.map(h => `#${h.replace(/^[#\s]+/, '')}`) // remove # e espaços do começo
      .join(' ');
    const formatted = normalized ? normalized : '';
    navigator.clipboard.writeText(formatted);
    toast.success('Hashtags copiadas!', { position: 'bottom-center' });
  };

  const handleCopyTitle = (title: string) => {
    let formatted = `${title}`;

    // garante no máximo 98 caracteres
    if (formatted.length > 98) {
      formatted = formatted.slice(0, 98);
    }
    navigator.clipboard.writeText(formatted);
    toast.success('Título copiado!', { position: 'bottom-center' });
  };

  const handleToggleUtilizado = async (projectName: string, currentState: boolean) => {
    try {
      const user_email = localStorage.getItem('user_email') || '';
      const apiKey = localStorage.getItem('api_key') || '';

      const resp = await fetch(`${videomanager_URL}/api/projects/${encodeURIComponent(projectName)}/mark-utilizado`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${apiKey}`,
          'X-User-Id': user_email,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ utilizado: !currentState }),
      });

      if (!resp.ok) throw new Error('Falha ao atualizar status');

      localStorage.setItem(`utilizado:${projectName}`, (!currentState).toString());
      setToggleUtilizado(prev => !prev);
      toast.success(`Projeto marcado como ${!currentState ? 'utilizado' : 'não utilizado'}`, { position: 'bottom-center' });
    } catch (err: any) {
      console.error(err);
      toast.error(`Erro ao marcar projeto: ${err.message || err}`);
    }
  };

  const handleDeleteProject = async (projectName: string) => {
    if (!confirm(`Deseja realmente excluir o projeto "${projectName}"? Esta ação não pode ser desfeita.`)) return;

    try {
      const user_email = localStorage.getItem('user_email') || '';
      const apiKey = localStorage.getItem('api_key') || '';

      const resp = await fetch(`${videomanager_URL}/api/projects/${encodeURIComponent(projectName)}`, {
        method: 'DELETE',
        headers: {
          'Authorization': `Bearer ${apiKey}`,
          'X-User-Id': user_email,
        },
      });

      const json = await resp.json();
      if (!resp.ok) throw new Error(json.message || 'Erro ao excluir projeto.');

      toast.success(json.message);

      // Atualiza lista de projetos localmente sem recarregar
      toggleProjectDeleted(projectName);

    } catch (err: any) {
      console.error(err);
      toast.error(`Falha ao excluir projeto: ${err.message || err}`);
    }
  };

  return {
    handleProjectClick,
    handleDownloadMetadata,
    handleDownloadAll,
    handleDownloadClick,
    handleCopyAll,
    handleCopyHashtags,
    handleCopyTitle,
    handleToggleUtilizado,
    handleDeleteProject,
  };
};

// Função utilitária para formatação de tempo
export const formatDuration = (startTime: string, endTime: string): string => {
  if (!startTime || !endTime) return '';
  
  const toSeconds = (time: string): number => {
    const parts = time.split(':').map(Number);
    if (parts.length === 3) {
      const [h, m, s] = parts;
      return h * 3600 + m * 60 + s;
    } else if (parts.length === 2) {
      const [m, s] = parts;
      return m * 60 + s;
    } else if (parts.length === 1) {
      return parts[0];
    }
    return 0;
  };
  
  const duration = toSeconds(endTime) - toSeconds(startTime);
  const min = Math.floor(duration / 60);
  const sec = duration % 60;
  return `${min}m${sec.toString().padStart(2, '0')}s`;
};

// Função utilitária para determinar cor da barra de progresso
export const getProgressBarColor = (progress: number): string => {
  if (progress < 70) return 'bg-green-500';
  if (progress < 90) return 'bg-yellow-500';
  return 'bg-red-500';
};

// Função utilitária para filtrar projetos
export const filterProjects = (
  projects: any[],
  searchTerm: string,
  filter: 'todos' | 'utilizados' | 'nao-utilizados'
) => {
  return projects
    .filter((project) =>
      project.name.toLowerCase().includes(searchTerm.toLowerCase())
    )
    .filter((project) => {
      if (filter === 'utilizados') return project.used === true;
      if (filter === 'nao-utilizados') return project.used === false;
      return true; // todos
    });
};

// Exportações dos componentes
export {
  Spinner,
  StarIcon,
  LightbulbIcon,
  ClockIcon,
  uniqueById,
  createBlobFromChunks,
};