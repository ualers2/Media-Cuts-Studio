// image-refresher-react\src\hooks\useGramFlowScheduler.ts
import { useState, useCallback } from 'react';


interface ScheduleConfig {
  scheduleMode: 'date';
  dateTime: Date | null;
  timezone: string;
  user_email: string;
  ig_username: string;
  ig_password: string;
  api_key: string;
  upload_video: boolean;
  upload_image: boolean;
  title: string;
  description: string;
  tags: string;
  // Add uploadedFile to the ScheduleConfig interface
  uploadedFile: File | null;
}

interface ScheduleResult {
  scheduledTime: string | string[]; // This can be a string or string array
  mode: 'date';
  timezone: string;
  user_email: string;
  ig_username: string;
  ig_password: string;
  api_key: string;
  upload_video: boolean;
  upload_image: boolean;
  title: string;
  description: string;
  tags: string;
}
// importe no topo do arquivo 
const sanitizeDateForServer = (date: Date): string => {
  return formatForServer(date);
};
// Helper para formatar Date para o formato exigido pelo servidor: 'YYYY-MM-DD HH:MM:SS'
function formatForServer(d: Date): string {
  const pad = (n: number) => n.toString().padStart(2, '0');
  const year = d.getFullYear();
  const month = pad(d.getMonth() + 1);
  const day = pad(d.getDate());
  const hours = pad(d.getHours());
  const minutes = pad(d.getMinutes());
  const seconds = pad(d.getSeconds());
  return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
}
export const useGramFlowScheduler = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const scheduleGramFlow = useCallback((config: ScheduleConfig): ScheduleResult | null => {
    const { scheduleMode, user_email, upload_video, upload_image,
      dateTime, timezone, title, description, tags,
      ig_username, ig_password, api_key
    } = config;

    try {

      if (scheduleMode === 'date') {
        if (!(dateTime instanceof Date)) {
          throw new Error('Data inválida');
        }
        const scheduledTime = formatForServer(dateTime);

        console.log('Agendamento único (Date Mode):', scheduledTime);
        return {
          scheduledTime,
          mode: 'date',
          timezone,
          user_email,
          ig_username,
          ig_password,
          api_key,
          upload_video,
          upload_image,
          title,
          description,
          tags,
        };
      } else {
        // Mode Weekly - you'll need to define how scheduledTime is set here
        // For now, let's assume it always returns a single string for date mode
        // If you expand to weekly, you'll need to handle string[] carefully
        return null; // Or throw an error, depending on desired behavior for unsupported mode
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Erro desconhecido');
      return null;
    }
  }, []);

  const startGramFlow = useCallback(async (config: ScheduleConfig) => {
    setIsLoading(true);
    setError(null);
    const apiUrl = import.meta.env.VITE_API_URL;
    // const VITE_LANDING_API = import.meta.env.VITE_LANDING_API; // Not used directly in fetch call here
    try {
      // Validações
      if (config.scheduleMode === 'date') {
        if (!config.dateTime) {
          throw new Error('Data e horário são obrigatórios no modo Date');
        }
      }

      const scheduleResult = scheduleGramFlow(config);
      if (!scheduleResult) {
        throw new Error('Falha ao criar agendamento');
      }

      // use diretamente o Date que veio do usuário
      if (!config.dateTime) {
        throw new Error('Data inválida');
      }

      console.log(`dateTime? ${config.dateTime}`)
      const dateTimeString = sanitizeDateForServer(config.dateTime);


      console.log(`user_email? ${localStorage.getItem('user_email')}`)
      console.log(`dateTimeField? ${dateTimeString}`)

      // Monta o payload como FormData
      const formData = new FormData();
      formData.append('timezone', scheduleResult.timezone);
      formData.append('mode', scheduleResult.mode);
      formData.append('date_time', dateTimeString); 
      formData.append('ig_username', scheduleResult.ig_username);
      formData.append('ig_password', scheduleResult.ig_password);
      formData.append('api_key', localStorage.getItem('api_key') || 'teste');
      formData.append('user_email', config.user_email);
      formData.append('upload_video', String(config.upload_video));
      formData.append('upload_image', String(config.upload_image));
      formData.append('title', config.title);
      formData.append('description', config.description);
      formData.append('tags', config.tags);

      if (config.uploadedFile) {
        formData.append('file', config.uploadedFile, config.uploadedFile.name); // Add filename for robustness
      }

      console.log(`api_key ${scheduleResult.api_key}`);
      console.log(`FormData payload created. ${formData}`);

      console.log(`${apiUrl}/api/Media_Cuts_Studio/InstagramUploader`);
      const resp = await fetch(`${apiUrl}/api/Media_Cuts_Studio/InstagramUploader`, {
        method: 'POST',
        headers: {
          'X-API-KEY': localStorage.getItem('api_key') || ''
        },
        body: formData 
      });

      if (!resp.ok) {
        const text = await resp.text();
        throw new Error(`Erro ${resp.status}: ${text}`);
      }
      const resp_json = await resp.json();
      console.log(`GramFlow? ${resp_json}`)
      console.log('GramFlow iniciado com sucesso');
      return scheduleResult;
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Erro ao iniciar GramFlow');
      throw err;
    } finally {
      setIsLoading(false);
    }
  }, [scheduleGramFlow]);

  return {
    scheduleGramFlow,
    startGramFlow,
    isLoading,
    error,
    clearError: () => setError(null)
  };
};