// image-refresher-react\src\hooks\useShortifyScheduler.ts
import { useState, useCallback } from 'react';
import { StartShortifyPayload, ScheduleResult, ScheduleConfig, EditionThemeOption, ShortifyOption, LegendsThemeOption, ChannelVideosResponse, TaskSchedulerProps,VideoProps, Account, ExpandedSections } from '@/lib/api';

function formatForServer(d: Date): string {
  const pad = (n: number) => n.toString().padStart(2, '0');
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`
    + ' '
    + `${pad(d.getHours())}:${pad(d.getMinutes())}:${pad(d.getSeconds())}`;
}
export const useShortifyScheduler = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const scheduleShortify = useCallback((config: ScheduleConfig): ScheduleResult | null => {
    const { ytChannel, apiKey, cuttingSeconds
     } = config;

    try {

      return {

        ytChannel,
        apiKey,
        cuttingSeconds

      };
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Erro desconhecido');
      return null;
    }
  }, []);

  const startShortify = useCallback(async (config: ScheduleConfig) => {
    setIsLoading(true);
    setError(null);
    let AccountCookies: string | null = null;
      
    const apiUrl = import.meta.env.VITE_API_URL;
    const VITE_LANDING_API = import.meta.env.VITE_LANDING_API;

    try {

      const scheduleResult = scheduleShortify(config);
      if (!scheduleResult) {
        throw new Error('Falha ao criar agendamento');
      }
      if (!scheduleResult) {
        throw new Error('Falha ao criar agendamento');
      }
      console.log(`user_email? ${localStorage.getItem('user_email')}`)
      console.log(`config.downloadToPanelEnabled? ${config.downloadToPanelEnabled}`)

      let payload: Record<string, any> = {
        pastedUrl: config.pastedUrl,
        thumbnail_url: config.thumbnail_url,
        includeHorizontal: config.includeHorizontal,
        includeVertical: config.includeVertical,
        canal_do_yt: scheduleResult.ytChannel,
        api_key: localStorage.getItem('api_key'),
        Cutting_seconds: scheduleResult.cuttingSeconds,
        user_email: config.user_email,
        downloadToPanelEnabled: config.downloadToPanelEnabled,
        legendstheme: config.legendstheme,
        editiontheme: config.editiontheme,
        TiktokAccount: config.username_account,
        TiktokAccountCookies: AccountCookies,
        customTitleEnabled: config.customTitleEnabled,
        videoTitle: config.videoTitle,
        videoTitleForLatestVideo: config.videoTitleForLatestVideo,
        latestEnabled: config.latestEnabled,
        secondsScheduleTiktokVideo: config.secondsScheduleTiktokVideo,
        titleForTiktokCutsEnabled: config.titleForTiktokCutsEnabled,
        titleForTiktokCuts: config.titleForTiktokCuts,
        hashtagsForTiktokCutsEnabled: config.hashtagsForTiktokCutsEnabled,
        hashtagsForTiktokCuts: config.hashtagsForTiktokCuts,
        ShortifyMode: config.ShortifyMode
      };

      if (config.customSettings) {
        payload = { ...payload, ...config.customSettings };
      }

      console.log('payload?', payload);
      console.log('api_key?', localStorage.getItem('api_key'));
      
      console.log(`${apiUrl}/api/Media_Cuts_Studio/Shortify/Mode/Create`);
      const resp = await fetch(`${apiUrl}/api/Media_Cuts_Studio/Shortify/Mode/Create`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-API-KEY': localStorage.getItem('api_key')
        },
        body: JSON.stringify(payload)
      });
      
      if (!resp.ok) {
        const text = await resp.text();
        throw new Error(`Erro ${resp.status}: ${text}`);
      }
      const resp_json = await resp.json();
      console.log(`Shortify? ${resp_json}`)
      // 3.4 - Feedback
      console.log('Shortify iniciado com sucesso');
      return scheduleResult;
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Erro ao iniciar Shortify');
      throw err;
    } finally {
      setIsLoading(false);
    }
  }, [scheduleShortify]);

  return {
    scheduleShortify,
    startShortify,
    isLoading,
    error,
    clearError: () => setError(null)
  };
};
