// src/components/ProjectHelpers.tsx
import React from 'react';
import { toast } from '@/hooks/use-toast';
import { ProjectVideo } from '@/contexts/ProjectsContext';
import { runWithLimit } from '@/utils/previewQueue';

import { StartShortifyPayload, ScheduleResult, ScheduleConfig, EditionThemeOption, ShortifyOption, LegendsThemeOption, ChannelVideosResponse, TaskSchedulerProps,VideoProps, Account, ExpandedSections } from '@/lib/api';

import { slogans, LegendsthemeOptions, EditionthemeOptions, ShortifyOptions} from '@/constants/task';
import { useProjectsContext } from '@/contexts/ProjectsContext';

export const useTaskHandlers = (

    VITE_LANDING_API: string,
    thumbnailurl: string,
    includeHorizontal: boolean,
    includeVertical: boolean,
    user_email: string,
    selectedThemeLegends: string,
    selectedEditionTheme: string,
    apiKey: string,
    cuttingSeconds: number[],
    themeSettings: Record<string, any>,
    selectedAccount: string,
    downloadToPanelEnabled: boolean,
    customTitleEnabled: boolean,
    videoTitle: string,
    videoTitleForLatestVideo: string,
    latestEnabled: boolean,
    pastedUrl: string,
    secondsScheduleTiktokVideo: number,
    titleForTiktokCutsEnabled: boolean,
    titleForTiktokCuts: string,
    hashtagsForTiktokCutsEnabled: boolean,
    hashtagsForTiktokCuts: string,
    selectedMode: string,
    ytChannel: string,
    apiUrl: string,
    expandedSections: ExpandedSections,
    loadedVideoIds: string[],

  startShortify: (payload: StartShortifyPayload) => Promise<ScheduleResult>,
  setExpandedSections: React.Dispatch<React.SetStateAction<ExpandedSections>>,
  setLoadedVideoIds: React.Dispatch<React.SetStateAction<string[]>>,
  setVideos: React.Dispatch<React.SetStateAction<VideoProps[]>>,
  setIsDialogOpen: React.Dispatch<React.SetStateAction<boolean>>,
  setIsLoadingVideos: React.Dispatch<React.SetStateAction<boolean>>,
  setIsLinkConfirmed: React.Dispatch<React.SetStateAction<boolean>>,
  setPastedUrl: React.Dispatch<React.SetStateAction<string>>,
  setVideoTitleForLatestVideo: React.Dispatch<React.SetStateAction<string>>,
  setVideoTitle: React.Dispatch<React.SetStateAction<string>>,
  setThumbnailurl: React.Dispatch<React.SetStateAction<string>>,
  setCustomTitleEnabled: React.Dispatch<React.SetStateAction<boolean>>,
  setLatestEnabled: React.Dispatch<React.SetStateAction<boolean>>,
  setLoadingLatest: React.Dispatch<React.SetStateAction<boolean>>,
  setYtChannel: React.Dispatch<React.SetStateAction<string>>,
  setIsPasteDialogOpen: React.Dispatch<React.SetStateAction<boolean>>,
  setSelectedEditionTheme: React.Dispatch<React.SetStateAction<string>>,
  setThemeSettings: React.Dispatch<React.SetStateAction<Record<string, any>>>,
  setSelectedThemeLegends: React.Dispatch<React.SetStateAction<string>>,
  setApiKey: React.Dispatch<React.SetStateAction<string>>,
  clearError: () => void,
  navigate: (path: string) => void

) => {
  const { loadProjects } = useProjectsContext();


  const handleThemeChange = (themeName: string) => {
    setSelectedThemeLegends(themeName);
    const theme = LegendsthemeOptions.find(t => t.name === themeName);
    setThemeSettings(theme?.settings || {});
  };
  const handleEditionThemeChange = (themeName: string) => {
    setSelectedEditionTheme(themeName);
  };
  const handleStartShortify = async () => {
    // if (!validateForm()) {
    //   toast({
    //     title: 'Form validation failed',
    //     description: 'Please fill in all required fields',
    //     variant: 'destructive',
    //   });
    //   return;
    // }

    clearError(); // Limpa erros anteriores do hook

    try {
      setApiKey(localStorage.getItem('api_key') || ''); // Garante que a API key esteja atualizada
    

      if (user_email && VITE_LANDING_API) { // Adicionado verificação para VITE_LANDING_API
        const configPayload = {
          // scheduleMode,
          // dayWeekly,
          // timeWeekly,
          // dateTime: dateTime, // Converte Date para string ISO\
          // timezone,
          // scheduleMonthly,
          ytChannel,
          cuttingSeconds,
        };

        await fetch(`${VITE_LANDING_API}/api/user-config/${user_email}`, {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(configPayload),
        });
      } else if (!user_email) {
        console.warn('user_email not found in localStorage. Config not saved.');
      } else {
        console.warn('VITE_LANDING_API not defined. Config not saved.');
      }

      console.log(`selectedAccount? ${selectedAccount}`);
      const payload = {
        // scheduleMode: scheduleMode,
        // dayWeekly: dayWeekly,
        // timeWeekly: timeWeekly,
        thumbnail_url: thumbnailurl,
        includeHorizontal: includeHorizontal,
        includeVertical: includeVertical,
        ytChannel: ytChannel,
        user_email: user_email,
        legendstheme: selectedThemeLegends,
        editiontheme: selectedEditionTheme,
        apiKey: apiKey,
        cuttingSeconds: cuttingSeconds,
        customSettings: themeSettings,
        username_account: selectedAccount,
        downloadToPanelEnabled: downloadToPanelEnabled,
        customTitleEnabled: customTitleEnabled,
        videoTitle: videoTitle,
        videoTitleForLatestVideo: videoTitleForLatestVideo,
        latestEnabled: latestEnabled,
        pastedUrl: pastedUrl, 
        secondsScheduleTiktokVideo: secondsScheduleTiktokVideo,
        titleForTiktokCutsEnabled: titleForTiktokCutsEnabled,
        titleForTiktokCuts: titleForTiktokCuts,
        hashtagsForTiktokCutsEnabled: hashtagsForTiktokCutsEnabled,
        hashtagsForTiktokCuts: hashtagsForTiktokCuts,
        ShortifyMode: selectedMode
      };

      console.log("Final Payload:", payload);

      await startShortify(payload); // Chama a lógica real de início do Shortify do hook
      // const now = Date.now();
      // setStartTime(now);
      // setHasStartedTimer(true);

      // Força recarregar os projetos sem usar cache para que o novo projeto apareça imediatamente
      try {
        const userId = user_email || localStorage.getItem('user_email') || null;
        if (userId) {
          await loadProjects(userId, { force: true });
          console.log('Projetos recarregados (force=true)');
        }
      } catch (err) {
        console.warn('Falha ao recarregar projetos após startShortify:', err);
      }

      navigate('/projects');
      // setTimeout(() => {
      //   window.location.reload();
      // }, 100); // Pequeno delay para garantir que o redirecionamento ocorra antes do refresh
      
      // O toast de sucesso agora é acionado pelo useEffect que observa `finishedTimer`
    } catch (err) {
      // Erro já é tratado pelo hook e exibido no componente via `error` state
      console.error("Error starting Shortify:", err);
    }
  };

  const handlePasteUrl = (url: string) => {
    if (!url.includes('youtube.com') && !url.includes('youtu.be')) {
      toast({ title: 'URL inválida', description: 'Por favor, insira um link do YouTube.' });
      return;
    }
    console.log('Link colado:', url);
    setIsLinkConfirmed(true);
    setYtChannel('');
    setCustomTitleEnabled(false);
    setLatestEnabled(false);
    setVideoTitleForLatestVideo('');
    setIsPasteDialogOpen(false);
  };
  const handleFetchLatest = async () => {
    if (!apiUrl || !ytChannel.trim()) {
      toast({
        title: 'Error',
        description: 'YouTube Channel and API URL are required to fetch latest video.',
        variant: 'destructive',
        duration: 3000,
      });
      console.warn('Cannot fetch latest video: apiUrl or ytChannel missing.');
      setIsLinkConfirmed(false); // limpa botão verde
      setPastedUrl(''); // limpa link colado
      setCustomTitleEnabled(false);
      setLatestEnabled(true);
      setVideoTitleForLatestVideo('Mock Latest Video Title');
      toast({
        title: 'Latest video loaded (Mock)',
        description: `"Mock Latest Video Title"`,
        variant: 'default',
      });
      return;
    }
    setLoadingLatest(true);
    try {
      const res = await fetch(
        `${VITE_LANDING_API}/metrics/channel/youtube?channel=${ytChannel}&limit=1`
      );
      if (!res.ok) throw new Error('Error fetching latest video');
      const json = (await res.json()) as ChannelVideosResponse;
      const latest = json.videos[0];
      if (latest) {
        setCustomTitleEnabled(false);
        setLatestEnabled(true);
        setVideoTitle('');
        setIsLinkConfirmed(false); 
        setPastedUrl(''); // limpa link colado
        console.log(`thumbnail ${latest.thumbnail}`)
        setVideoTitleForLatestVideo(latest.title);
        setThumbnailurl(latest.thumbnail);
        
        // toast({
        //   title: 'Latest video loaded',
        //   description: `"${latest.title}"`,
        //   variant: 'default',
        // });
        setLoadingLatest(false);
      } else {
        toast({
          title: 'No video found',
          variant: 'default',
        });
        setLoadingLatest(false);
      }
    } catch (err: any) {
      toast({
        title: 'Error',
        description: err.message,
        variant: 'destructive',
        duration: 3000,
      });
      setLoadingLatest(false);
    }
  };
  const handleSelectVideo = (video: VideoProps) => {
    setIsLinkConfirmed(false); 
    setPastedUrl('');
    setVideoTitleForLatestVideo('');
    setVideoTitle(video.title);
    setThumbnailurl(video.thumbnail);
    setCustomTitleEnabled(true);
    setLatestEnabled(false);
    setIsDialogOpen(false); 
  };
  function formatElapsed(ms: number) {
    const totalSec = Math.floor(ms / 1000);
    const h = String(Math.floor(totalSec / 3600)).padStart(2,'0');
    const m = String(Math.floor((totalSec % 3600) / 60)).padStart(2,'0');
    const s = String(totalSec % 60).padStart(2,'0');
    return `${h}:${m}:${s}`;
  }
  const formatDateTimeLocal = (date: Date | null) => {
    if (!date) return '';
    const year = date.getFullYear();
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const day = date.getDate().toString().padStart(2, '0');
    const hours = date.getHours().toString().padStart(2, '0');
    const minutes = date.getMinutes().toString().padStart(2, '0');
    return `${year}-${month}-${day}T${hours}:${minutes}`;
  };
  const getMinDate = () => {
      const minDate = new Date();
      minDate.setMinutes(minDate.getMinutes() + 21);
      return minDate;
  };
  const getMaxDate = () => {
      const maxDate = new Date();
      maxDate.setDate(maxDate.getDate() + 9);
      maxDate.setHours(23, 59, 59, 999); 
      return maxDate;
  };
  const fetchVideos = async (excludeIds: string[] = []): Promise<VideoProps[]> => {
    setIsLoadingVideos(true);
    try {
      const params = new URLSearchParams({
        channel: ytChannel,
        limit: '5',
        // passe os ids já carregados para a API ignorar
        exclude: excludeIds.join(',')
      });
      const res = await fetch(`${VITE_LANDING_API}/metrics/channel/youtube?${params}`);
      if (!res.ok) throw new Error('Falha ao buscar vídeos');
      const json = await res.json() as ChannelVideosResponse;
      return json.videos;
    } finally {
      setIsLoadingVideos(false);
    }
  };
  const handleOpenModal = async () => {
    setVideos([]);           // limpa lista
    const primeiroLote = await fetchVideos();
    setVideos(primeiroLote);
    setIsDialogOpen(true);
  };
  const handleLoadMore = async () => {
    setVideos([]);
    const novos = await fetchVideos(loadedVideoIds);
    setVideos(prev => [...prev, ...novos]);
    setLoadedVideoIds(prev => [...prev, ...novos.map(v => v.id)]);
  };
  const toggleSection = (section: keyof typeof expandedSections) => {
    setExpandedSections(prev => ({
      ...prev,
      [section]: !prev[section]
    }));
  };


  return {
    handleThemeChange,
    handleEditionThemeChange,
    handleStartShortify,
    handleFetchLatest,
    handlePasteUrl,
    handleSelectVideo,
    handleOpenModal,
    handleLoadMore,
    fetchVideos,
    toggleSection,
    formatElapsed,
    formatDateTimeLocal,
    getMinDate,
    getMaxDate,
  };
};

