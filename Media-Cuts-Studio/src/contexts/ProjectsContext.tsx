// src/contexts/ProjectsContext.tsx
import React, { createContext, useContext, useState, useEffect, useCallback, ReactNode } from 'react';
import { toast } from 'react-hot-toast';

export interface ProjectVideo {
  id: string; // O ID do vídeo gerado pelo servidor
  title: string;
  descricao?: string;
  hashtags?: string[];
  minutagemdeInicio?: string;
  minutagemdeFim?: string;
  urltumbnail?: string;
  filename: string; // Nome original do arquivo para download
  uploadedAt?: string; // Carimbo de data/hora do upload
  justificativa?: string;
  sentimento_principal?: string;
  potencial_de_viralizacao?: number;
  type_project?: string;
}

export interface Project {
  name: string;
  model_ai: string;
  used?: boolean;
  progress_percent: string;
  url_original: string;
  status: string;
  thumbnail_url: string;
  createdAt: string;
  videos: ProjectVideo[];
  isNew?: boolean; 
}
type LoadOptions = { force?: boolean };
interface ProjectsContextType {
  projects: Project[];
  loadingProjects: boolean;
  errorProjects: string | null;
  
  fetchUserProjects: (userId: string) => Promise<void>; // Expor a função para recarregar
  loadProjects: (userId: string | null, options?: LoadOptions) => Promise<void>;
  toggleProjectUsed;
  toggleProjectDeleted;
}

const ProjectsContext = createContext<ProjectsContextType | undefined>(undefined);

// Cache settings
const CACHE_KEY_PREFIX = 'projects_cache_v1'; // incremente a versão se mudar esquema
const DEFAULT_TTL_MINUTES = parseInt(import.meta.env.VITE_PROJECTS_CACHE_TTL_MIN || '10', 10); // default 10 minutos

function nowMs() {
  return Date.now();
}

function setStorage(key: string, value: any) {
  try {
    const s = JSON.stringify(value);
    if (typeof sessionStorage !== 'undefined') {
      sessionStorage.setItem(key, s);
    } else {
      localStorage.setItem(key, s);
    }
  } catch (err) {
    try {
      localStorage.setItem(key, JSON.stringify(value));
    } catch (_) {}
  }
}

function getStorage(key: string) {
  try {
    const raw = (typeof sessionStorage !== 'undefined') ? sessionStorage.getItem(key) : localStorage.getItem(key);
    if (!raw) return null;
    return JSON.parse(raw);
  } catch (err) {
    try {
      const raw2 = localStorage.getItem(key);
      if (!raw2) return null;
      return JSON.parse(raw2);
    } catch (_) {
      return null;
    }
  }
}

export const ProjectsProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [projects, setProjects] = useState<Project[]>([]);
  const [loadingProjects, setLoadingProjects] = useState<boolean>(true);
  const [errorProjects, setErrorProjects] = useState<string | null>(null);
  const videomanager_URL = import.meta.env.VITE_VIDEO_MANAGER_URL;  
  const userId = localStorage.getItem('user_email')

  // atualizar estado local ao marcar usado / deletar
  const toggleProjectUsed = (projectName: string, used: boolean) => {
    setProjects(prevProjects =>
      prevProjects.map(p =>
        p.name === projectName ? { ...p, used } : p
      )
    );
    const key = `${CACHE_KEY_PREFIX}:${userId}`;
    const cache = getStorage(key);
    if (cache && Array.isArray(cache.projects)) {
      const updated = cache.projects.map((p: Project) => p.name === projectName ? { ...p, used } : p);
      setStorage(key, { projects: updated, ts: cache.ts });
    }
  };

  const toggleProjectDeleted = (projectName: string) => {
    setProjects(prevProjects =>
      prevProjects.filter(p => p.name !== projectName)
    );
    const key = `${CACHE_KEY_PREFIX}:${userId}`;
    const cache = getStorage(key);
    if (cache && Array.isArray(cache.projects)) {
      const updated = cache.projects.filter((p: Project) => p.name !== projectName);
      setStorage(key, { projects: updated, ts: cache.ts });
    }
  };

  // Normalização / pós-processamento comum
  function normalizeAndSort(data: Project[]): Project[] {
    const filteredProjects = data.filter(project => {
      return !project.videos.some(video => video.type_project === 'files');
    });

    const sortedProjects = filteredProjects.sort((a, b) => {
      const dateA = new Date(a.createdAt).getTime();
      const dateB = new Date(b.createdAt).getTime();
      return dateB - dateA;
    });

    const projectsWithNewFlag = sortedProjects.map((project, index) => ({
      ...project,
      isNew: index < 2,
    }));

    return projectsWithNewFlag;
  }


  const fetchUserProjects = useCallback(async () => {
    setLoadingProjects(true);
    setErrorProjects(null);
    try {
      const response = await fetch(`${videomanager_URL}/api/projects`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'X-User-Id': userId,
        },
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({ message: 'Erro desconhecido.' }));
        throw new Error(errorData.message || `Erro ao buscar projetos: ${response.statusText}`);
      }

      const data: Project[] = await response.json();

      // 1. FILTRO: Filtra projetos que não tenham nenhum vídeo com type_project 'files'
      const filteredProjects = data.filter(project => {
        return !project.videos.some(video => video.type_project === 'files');
      });

      // 2. ORDENAÇÃO: Ordena os projetos pela data de criação (mais recentes primeiro)
      const sortedProjects = filteredProjects.sort((a, b) => {
        const dateA = new Date(a.createdAt).getTime();
        const dateB = new Date(b.createdAt).getTime();
        return dateB - dateA; // Para ordenar do mais novo para o mais antigo
      });

      // 3. MARCAR COMO "NOVO": Marca os 1 ou 2 primeiros projetos como "novo"
      const projectsWithNewFlag = sortedProjects.map((project, index) => {
        // Marca como "novo" os 2 primeiros projetos (índices 0 e 1)
        return {
          ...project,
          isNew: index < 2,
        };
      });
      const processed = normalizeAndSort(projectsWithNewFlag);


      setProjects(processed); // Define os projetos processados
      setErrorProjects(null);
      
      // salva no cache com timestamp
      const key = `${CACHE_KEY_PREFIX}:${userId}`;
      setStorage(key, { projects: processed, ts: nowMs() });
      console.log('Projetos carregados, filtrados e marcados:', processed);

    } catch (error: any) {
      console.error('Falha ao carregar projetos:', error);
      setErrorProjects(error.message);
      toast.error(`Falha ao carregar projetos: ${error.message}`);
    } finally {
      setLoadingProjects(false);
    }
  }, []);


  // loadProjects usa cache primeiro, a menos que force=true
  const loadProjects = useCallback(async (options?: LoadOptions) => {
    if (!userId) {
      setProjects([]);
      setLoadingProjects(false);
      return;
    }

    const key = `${CACHE_KEY_PREFIX}:${userId}`;
    const ttlMinutes = DEFAULT_TTL_MINUTES;
    const cache = getStorage(key);

    // quando não for forçar e cache válido -> usar cache
    if (!options?.force && cache && cache.ts) {
      const ageMin = (nowMs() - cache.ts) / (1000 * 60);
      if (ageMin <= ttlMinutes && Array.isArray(cache.projects)) {
        setProjects(cache.projects);
        setLoadingProjects(false);
        setErrorProjects(null);
        return;
      }
    }

    // caso contrário -> buscar servidor e atualizar cache
    await fetchUserProjects();
  }, [fetchUserProjects]);

  // // Carregar projetos quando o componente for montado ou o usuário mudar
  // useEffect(() => {
  //   if (user_) {
  //     fetchUserProjects(user_);
  //   } else {
  //     setProjects([]); // Limpa projetos se não houver usuário logado
  //     setLoadingProjects(false);
  //   }
  // }, [user_, fetchUserProjects]); // Refetch quando o usuário mudar ou a função fetchUserProjects mudar

  const contextValue = {
    projects,
    loadingProjects,
    errorProjects,
    fetchUserProjects, 
    loadProjects,
    toggleProjectUsed,
    toggleProjectDeleted
  };

  return (
    <ProjectsContext.Provider value={contextValue}>
      {children}
    </ProjectsContext.Provider>
  );
};

export const useProjectsContext = () => {
  const context = useContext(ProjectsContext);
  if (context === undefined) {
    throw new Error('useProjectsContext must be used within a ProjectsProvider');
  }
  return context;
};