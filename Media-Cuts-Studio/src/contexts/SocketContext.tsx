// webproject\src\contexts\SocketContext.tsx
import React, {
  createContext,
  ReactNode,
  useContext,
  useEffect,
  useState,
} from 'react';
import { getSocket, initSocket } from '@/utils/socket';
import { toast } from '@/hooks/use-toast';

type ZipFile = {
  filename: string;
  zip_base64: string;
};

// MODIFICAÇÃO PRINCIPAL AQUI: Adiciona projectName ao VideoFile
export type VideoFile = {
  id: string;
  title: string;
  urltumbnail: string;
  descricao: string;
  hashtags: string[];
  minutagemdeInicio: string;
  minutagemdeFim: string;
  filename: string;
  video_base64: string;
  projectName?: string; // Novo campo para associar ao projeto
};

type FieldsState = {
  Mode: string;
  Mediabase: string;
  'Weather Forecast': string;
  'Created at': string;
  Status: string;
  TiktokAccount: string;
  YtChannel: string;
  Target: string;
  'Cuts Duration': string;
  'Thread id': string;
};

type SocketContextData = {
  progress: number;
  Mode: string;
  YtChannel: string;
  Status: string;
  TiktokAccount: string;
  runningTime: string;
  logMessages: string[];
  agentLogs: string[];
  zipFile: ZipFile | null;
  videoFiles: VideoFile[];
  fields: FieldsState;
  timerActive: boolean;
  finishedTimer: boolean;
  setTimerActive: React.Dispatch<React.SetStateAction<boolean>>;
  clearFinishedTimer: () => void;
  // Adiciona a funcionalidade de projetos para o contexto
  projects: { name: string; videos: VideoFile[] }[];
};

const SocketContext = createContext<SocketContextData | undefined>(undefined);

export const SocketProvider = ({ children }: { children: ReactNode }) => {
  const [timerActive, setTimerActive] = useState<boolean>(false);
  const [finishedTimer, setFinishedTimer] = useState<boolean>(false);
  const clearFinishedTimer = () => setFinishedTimer(false);

  const [videoFiles, setVideoFiles] = useState<VideoFile[]>(() => {
    try {
      const savedVideos = localStorage.getItem('socket_videoFiles');
      return savedVideos ? JSON.parse(savedVideos) : [];
    } catch (e) {
      console.error('Falha ao carregar vídeos do localStorage:', e);
      return [];
    }
  });

  // Estado para armazenar os projetos (agrupamento de vídeos)
  const [projects, setProjects] = useState<{ name: string; videos: VideoFile[] }[]>(() => {
    try {
      const savedProjects = localStorage.getItem('socket_projects');
      return savedProjects ? JSON.parse(savedProjects) : [];
    } catch (e) {
      console.error('Falha ao carregar projetos do localStorage:', e);
      return [];
    }
  });

  useEffect(() => {
    try {
      localStorage.setItem('socket_videoFiles', JSON.stringify(videoFiles));
    } catch (e) {
      console.error('Falha ao salvar vídeos no localStorage:', e);
    }
  }, [videoFiles]);

  // Salva os projetos no localStorage
  useEffect(() => {
    try {
      localStorage.setItem('socket_projects', JSON.stringify(projects));
    } catch (e) {
      console.error('Falha ao salvar projetos no localStorage:', e);
    }
  }, [projects]);


  const [progress, setProgress] = useState<number>(() => {
    const saved = localStorage.getItem('socket_progress');
    return saved ? Number(saved) : 0;
  });

  const [Mode, setMode] = useState<string>(() => {
    const saved = localStorage.getItem('socket_Mode');
    return saved || 'process';
  });
  const [Status, setStatus] = useState<string>(() => {
    const saved = localStorage.getItem('socket_Status');
    return saved || '';
  });

  const [TiktokAccount, setTiktokAccount] = useState<string>(() => {
    const saved = localStorage.getItem('socket_TiktokAccount');
    return saved || '';
  });

  const [YtChannel, setYtChannel] = useState<string>(() => {
    const saved = localStorage.getItem('socket_YtChannel');
    return saved || '';
  });

  const [runningTime, setRunningTime] = useState<string>(() => {
    const saved = localStorage.getItem('socket_runningTime');
    return saved || '00:00';
  });

  const [logMessages, setLogMessages] = useState<string[]>(() => {
    const saved = localStorage.getItem('socket_logMessages');
    return saved ? JSON.parse(saved) : [];
  });

  const [agentLogs, setAgentLogs] = useState<string[]>(() => {
    const saved = localStorage.getItem('socket_agentLogs');
    return saved ? JSON.parse(saved) : [];
  });

  const [zipFile, setZipFile] = useState<ZipFile | null>(null);

  const [fields, setFields] = useState<FieldsState>(() => {
    const saved = localStorage.getItem('socket_fields');
    if (saved) {
      return JSON.parse(saved);
    }
    return {
      Mode: '',
      Mediabase: '',
      'Weather Forecast': '',
      'Created at': '',
      Status: '',
      TiktokAccount: '',
      YtChannel: '',
      Target: '',
      'Cuts Duration': '',
      'Thread id': '',
    };
  });

  const persistProgress = (value: number) => {
    localStorage.setItem('socket_progress', String(value));
    setProgress(value);
  };
  const persistMode = (name: string) => {
    localStorage.setItem('socket_Mode', String(name));
    setMode(name);
  };
  const persistStatus = (name: string) => {
    localStorage.setItem('socket_Status', String(name));
    setStatus(name);
  };
  const persistTiktokAccount = (name: string) => {
    localStorage.setItem('socket_TiktokAccount', String(name));
    setTiktokAccount(name);
  };
  const persistYtChannel = (name: string) => {
    localStorage.setItem('socket_YtChannel', String(name));
    setYtChannel(name);
  };

  const persistRunningTime = (value: string) => {
    localStorage.setItem('socket_runningTime', value);
    setRunningTime(value);
  };

  const persistLogMessage = (msg: string) => {
    setLogMessages(prev => {
      const novo = [...prev, msg];
      localStorage.setItem('socket_logMessages', JSON.stringify(novo));
      return novo;
    });
  };

  const persistAgentLog = (msg: string) => {
    setAgentLogs(prev => {
      const novo = [...prev, msg];
      localStorage.setItem('socket_agentLogs', JSON.stringify(novo));
      return novo;
    });
  };

  const persistFieldUpdate = (chave: keyof FieldsState, valor: string) => {
    setFields(prev => {
      const updated = { ...prev, [chave]: valor };
      localStorage.setItem('socket_fields', JSON.stringify(updated));
      return updated;
    });
  };

  // Define a type for the incoming video payload structure, including projectName
  type IncomingVideoPayload = {
    type: 'video';
    message: {
      id: string;
      title: string;
      urltumbnail: string;
      descricao: string;
      hashtags: string | string[]; // Pode vir como string ou array
      minutagemdeInicio: string;
      minutagemdeFim: string;
      filename: string;
      message: string; // Base64 string do vídeo
      projectName?: string; // Novo campo esperado do backend
    };
  };

  const setupSocketListeners = (socketInstance: ReturnType<typeof getSocket>) => {
    if (!socketInstance) return;

    const API_KEY = localStorage.getItem('api_key');
    if (!API_KEY) {
      console.warn('[SocketContext] API_KEY não encontrada no localStorage');
      return;
    }

    if (socketInstance.connected) {
      persistLogMessage('🔗 SocketContext: já conectado ao servidor Socket.IO');
    }

    socketInstance.on('connect', () => {
      persistLogMessage('🔗 SocketContext: conectado ao servidor Socket.IO');
    });

    socketInstance.on('disconnect', () => {
      persistLogMessage('❌ SocketContext: desconectado do servidor Socket.IO');
    });

    socketInstance.on('webhook_data', (data: any) => {
      const payload = data[API_KEY];
      if (!payload) return;

      const { type, message } = payload;

      switch (type) {
        case 'info': {
          persistLogMessage(String(message));
          break;
        }
        case 'progress': {
          const num = Number(message);
          persistProgress(num);
          break;
        }
        case 'finish_timer_loader_shortify': {
          setTimerActive(false);
          setFinishedTimer(true);
          break;
        }
        case 'target': {
          persistFieldUpdate('Target', String(message));
          break;
        }
        case 'mediabase': {
          persistFieldUpdate('Mediabase', String(message));
          break;
        }
        case 'Thread': {
          persistFieldUpdate('Thread id', String(message));
          break;
        }
        case 'Createdat': {
          persistFieldUpdate('Created at', String(message));
          break;
        }
        case 'Mode': {
          persistFieldUpdate('Mode', String(message));
          persistMode(String(message));
          break;
        }
        case 'Status': {
          persistFieldUpdate('Status', String(message));
          persistStatus(String(message));
          break;
        }
        case 'tiktokAccount':
        case 'tiktokaccount':
        case 'TiktokAccount': {
          persistFieldUpdate('TiktokAccount', String(message));
          persistTiktokAccount(String(message));
          break;
        }
        case 'YtChannel': {
          persistFieldUpdate('YtChannel', String(message));
          persistYtChannel(String(message));
          break;
        }

        case 'weather_forecast': {
          persistFieldUpdate('Weather Forecast', String(message));
          break;
        }
        case 'cuts_duration': {
          persistFieldUpdate('Cuts Duration', `${String(message)} seconds`);
          break;
        }
        case 'timestamp': {
          persistRunningTime(String(message));
          break;
        }
        case 'agent_log': {
          persistAgentLog(String(message));
          break;
        }
        case 'notification': {
          persistLogMessage(`🔔 NOTIFICAÇÃO: ${String(message)}`);
          break;
        }
        case 'zip': {
          const { filename, title, urltumbnail, descricao, hashtags, minutagemdeInicio, minutagemdeFim, message: zipBase64 } = payload as {
            type: 'zip';
            title: string;
            urltumbnail: string;
            descricao: string;
            hashtags: string;
            minutagemdeInicio: string;
            minutagemdeFim: string;
            filename: string;
            message: string;
          };
          setZipFile({ filename, zip_base64: zipBase64 });
          break;
        }
        case 'video': {
          const videoData = payload as IncomingVideoPayload;
          const {
            id,
            title,
            urltumbnail,
            descricao,
            hashtags: rawHashtags, // Renomeado para evitar conflito
            minutagemdeInicio,
            minutagemdeFim,
            filename,
            message: videoBase64,
            projectName, // Captura o projectName
          } = videoData.message;

          let hashtags: string[] = [];
          if (Array.isArray(rawHashtags)) {
            hashtags = rawHashtags;
          } else if (typeof rawHashtags === 'string' && rawHashtags) {
            hashtags = rawHashtags.split(',').map(tag => tag.trim());
          }

          const newVideo: VideoFile = {
            id,
            title,
            urltumbnail,
            descricao,
            hashtags,
            minutagemdeInicio,
            minutagemdeFim,
            filename,
            video_base64: videoBase64,
            projectName, // Armazena o projectName
          };

          setVideoFiles(prev => {
            // Evita duplicatas com base no filename e base64
            if (prev.some(v => v.filename === newVideo.filename && v.video_base64 === newVideo.video_base64)) {
              return prev;
            }
            return [...prev, newVideo];
          });

          // Lógica para adicionar o vídeo ao projeto correspondente
          if (projectName) {
            setProjects(prevProjects => {
              const existingProjectIndex = prevProjects.findIndex(p => p.name === projectName);
              if (existingProjectIndex !== -1) {
                // Se o projeto já existe, adiciona o vídeo a ele, evitando duplicatas dentro do projeto
                const updatedProject = { ...prevProjects[existingProjectIndex] };
                if (!updatedProject.videos.some(v => v.filename === newVideo.filename && v.video_base64 === newVideo.video_base64)) {
                  updatedProject.videos = [...updatedProject.videos, newVideo];
                }
                const updatedProjects = [...prevProjects];
                updatedProjects[existingProjectIndex] = updatedProject;
                return updatedProjects;
              } else {
                // Se o projeto não existe, cria um novo com este vídeo
                return [...prevProjects, { name: projectName, videos: [newVideo] }];
              }
            });
          }
          break;
        }
        default: {
          console.warn(`[SocketContext] evento "${type}" desconhecido`, payload);
          break;
        }
      }
    });
  };

  useEffect(() => {
    const apiKey = localStorage.getItem('api_key');
    if (apiKey) {
      let socketInst = getSocket();
      if (!socketInst) {
        socketInst = initSocket(apiKey);
      }
      setupSocketListeners(socketInst);
    }

    const onStorageChange = (e: StorageEvent) => {
      if (e.key === 'api_key' && e.newValue) {
        const newApiKey = e.newValue;
        let socketInst = getSocket();
        if (!socketInst) {
          socketInst = initSocket(newApiKey);
          setupSocketListeners(socketInst);
        }
      }
      if (e.key === 'api_key' && e.newValue === null) {
        const socketInst = getSocket();
        if (socketInst) {
          socketInst.disconnect();
        }
      }
    };
    window.addEventListener('storage', onStorageChange);

    return () => {
      window.removeEventListener('storage', onStorageChange);
      const socketInst = getSocket();
      if (socketInst) {
        socketInst.off('webhook_data');
        socketInst.off('connect');
        socketInst.off('disconnect');
      }
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <SocketContext.Provider
      value={{
        timerActive,
        finishedTimer,
        setTimerActive,
        clearFinishedTimer,
        progress,
        Mode,
        YtChannel,
        Status,
        TiktokAccount,
        runningTime,
        logMessages,
        agentLogs,
        zipFile,
        videoFiles,
        fields,
        projects, // Disponibiliza os projetos no contexto
      }}
    >
      {children}
    </SocketContext.Provider>
  );
};

export const useSocketContext = (): SocketContextData => {
  const context = useContext(SocketContext);
  if (!context) {
    throw new Error(
      'useSocketContext deve ser usado dentro de um SocketProvider'
    );
  }
  return context;
};