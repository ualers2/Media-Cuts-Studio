// TaskComponent.tsx

import React, { useEffect, useRef, useState  } from 'react';
import { Link as LinkIcon } from 'lucide-react';
import { Calendar, Clapperboard, Clock, AlertCircle, ChevronDown, ChevronUp, Play, Settings, Hash, Type, Video, Users, Palette, Globe, Loader2, Info  } from 'lucide-react';
import { useNavigate } from 'react-router-dom';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { useShortifyScheduler } from '@/hooks/useShortifyScheduler';
import { Select, SelectTrigger, SelectContent, SelectItem, SelectValue } from '@/components/ui/select';
import { useQuery } from '@tanstack/react-query';
import { toast } from '@/hooks/use-toast';
import { Popover, PopoverTrigger, PopoverContent } from '@/components/ui/popover';
import 'react-datepicker/dist/react-datepicker.css';
import {
  Dialog,
  DialogTrigger,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogDescription,
  DialogFooter,
} from '@/components/ui/dialog';
import { useSocketContext } from '@/contexts/SocketContext';

import { StartShortifyPayload, ScheduleResult, ScheduleConfig, EditionThemeOption, ShortifyOption, LegendsThemeOption, ChannelVideosResponse, TaskSchedulerProps,VideoProps, Account, ExpandedSections } from '@/lib/api';

import { slogans, LegendsthemeOptions, EditionthemeOptions, ShortifyOptions} from '@/constants/task';
import { useTaskHandlers } from '@/components/TaskHelpers';

const TaskComponent: React.FC<TaskSchedulerProps> = ({
  ytChannel,
  setYtChannel,
  apiKey,
  setApiKey,
  videoUrl
}) => {
  const [cuttingSeconds, setCuttingSeconds] = useState<number[]>([30, 60, 120]);
  const [cuttingSecondsInput, setCuttingSecondsInput] = useState(cuttingSeconds.join(", "));

  const [startTime, setStartTime] = useState<number | null>(null);
  const [elapsed, setElapsed] = useState(0);
  const [hasStartedTimer, setHasStartedTimer] = useState(false);
  const [selectedAccount, setSelectedAccount] = useState<string>('');
  const [downloadToPanelEnabled, setDownloadToPanelEnabled] = useState(true);
  const [secondsScheduleTiktokVideo, setSecondsScheduleTiktokVideo] = useState(1200);
  const [dateTime, setDateTime] = useState<Date | null>(null);
  const [frequencyDays, setFrequencyDays] = useState<number>(7);
  const [selectedEditionTheme, setSelectedEditionTheme] = useState<string>('AI Vertical Fusion');
  const [selectedThemeLegends, setSelectedThemeLegends] = useState<string>('Revelation Effect - Tema Classico');
  const [themeSettings, setThemeSettings] = useState<Record<string, any>>({});
  const [selectedMode, setselectedMode] = useState<string>('Studio-Startup');
  const [hashtagsForTiktokCuts, setHashtagsForTiktokCuts] = useState('');
  const [hashtagsForTiktokCutsEnabled, setHashtagsForTiktokCutsEnabled] = useState(false);
  const [hashtagsAutoEnabled, setHashtagsAutoEnabled] = useState(true);
  const [titleForTiktokCuts, setTitleForTiktokCuts] = useState('');
  const [titleForTiktokCutsEnabled, setTitleForTiktokCutsEnabled] = useState(false);
  const [titleAutoEnabled, setTitleAutoEnabled] = useState(true);
  const [customTitleEnabled, setCustomTitleEnabled] = useState(false);
  const [videoTitle, setVideoTitle] = useState('');
  const [videoTitleForLatestVideo, setVideoTitleForLatestVideo] = useState('');
  const [latestEnabled, setLatestEnabled] = useState(true);
  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [loadingLatest, setLoadingLatest] = useState(false);
  const [tooltipOpen, setTooltipOpen] = useState(false);
  const [videos, setVideos] = useState<VideoProps[]>([]);
  const [loadedVideoIds, setLoadedVideoIds] = useState<string[]>([]);
  const [isLoadingVideos, setIsLoadingVideos] = useState(false);
  const [thumbnailurl, setThumbnailurl] = useState("");
  const [isPasteDialogOpen, setIsPasteDialogOpen] = useState(false);
  const [pastedUrl, setPastedUrl] = useState('');
  const [isLinkConfirmed, setIsLinkConfirmed] = useState(false);
  const [expandedSections, setExpandedSections] = useState<ExpandedSections>({
    schedule: true,
    video: true,
    content: false,
    account: true,
    advanced: true
  });
  const [formErrors, setFormErrors] = useState<Record<string, string>>({});
  const navigate = useNavigate();
  const { startShortify, isLoading, error, clearError } = useShortifyScheduler();
  const { runningTime, timerActive, finishedTimer, setTimerActive, clearFinishedTimer } = useSocketContext();
  const isAICuration = selectedMode === 'AI Curation';
  const hasRunPaste = useRef(false);
  const [includeHorizontal, setIncludeHorizontal] = useState(true);
  const [includeVertical, setIncludeVertical] = useState(true);
  const [currentSloganIndex, setCurrentSloganIndex] = useState(0);
  const [displayText, setDisplayText] = useState("");
  const [typing, setTyping] = useState(true);
  const [hasTypedChannel, setHasTypedChannel] = useState(false);
  const user_email = localStorage.getItem('user_email');
  const VITE_API_URL = import.meta.env.VITE_API_URL || 'http://localhost:3001';

  const {
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
  } = useTaskHandlers(
    VITE_API_URL,
    thumbnailurl,
    includeHorizontal,
    includeVertical,
    user_email,
    selectedThemeLegends,
    selectedEditionTheme,
    apiKey,
    cuttingSeconds,
    themeSettings,
    selectedAccount,
    downloadToPanelEnabled,
    customTitleEnabled,
    videoTitle,
    videoTitleForLatestVideo,
    latestEnabled,
    pastedUrl,
    secondsScheduleTiktokVideo,
    titleForTiktokCutsEnabled,
    titleForTiktokCuts,
    hashtagsForTiktokCutsEnabled,
    hashtagsForTiktokCuts,
    selectedMode,
    ytChannel,
    expandedSections,
    loadedVideoIds,
    startShortify,
    setExpandedSections,
    setLoadedVideoIds,
    setVideos,
    setIsDialogOpen,
    setIsLoadingVideos,
    setIsLinkConfirmed,
    setPastedUrl,
    setVideoTitleForLatestVideo,
    setVideoTitle,
    setThumbnailurl,
    setCustomTitleEnabled,
    setLatestEnabled,
    setLoadingLatest,
    setYtChannel,
    setIsPasteDialogOpen,
    setSelectedEditionTheme,
    setThemeSettings,
    setSelectedThemeLegends,
    setApiKey,
    clearError,
    navigate,
  );

  useEffect(() => {
    let timeout;
    if (typing) {
      if (displayText.length < slogans[currentSloganIndex].length) {
        timeout = setTimeout(() => {
          setDisplayText(slogans[currentSloganIndex].slice(0, displayText.length + 1));
        }, 25);
      } else {
        timeout = setTimeout(() => setTyping(false), 1500);
      }
    } else {
      if (displayText.length > 0) {
        timeout = setTimeout(() => {
          setDisplayText(displayText.slice(0, -1));
        }, 25);
      } else {
        setCurrentSloganIndex((currentSloganIndex + 1) % slogans.length);
        setTyping(true);
      }
    }

    return () => clearTimeout(timeout);
  }, [displayText, typing, currentSloganIndex]);

  useEffect(() => {
    if (!hasStartedTimer) return;

    const interval = setInterval(() => {
      if (startTime) {
        setElapsed(Date.now() - startTime);
      }
    }, 1000);

    return () => clearInterval(interval);
  }, [hasStartedTimer, startTime]);

  useEffect(() => {
    try {
      localStorage.setItem('downloadToPanelEnabled', JSON.stringify(downloadToPanelEnabled));
    } catch (e) {
      console.error('Failed to save downloadToPanelEnabled to localStorage', e);
    }
  }, [downloadToPanelEnabled]);
  useEffect(() => {
    const defaultTheme = ShortifyOptions.find(t => t.name === selectedMode);
    if (defaultTheme) setselectedMode(defaultTheme.name);
  }, []);
  useEffect(() => {
    const defaultTheme = LegendsthemeOptions.find(t => t.name === selectedThemeLegends);
    if (defaultTheme) {
      setThemeSettings(defaultTheme.settings);
    }
  }, [selectedThemeLegends]);  
  useEffect(() => {
    const defaultTheme = EditionthemeOptions.find(t => t.name === selectedEditionTheme);
    if (defaultTheme) setSelectedEditionTheme(defaultTheme.name);
  }, []);
  useEffect(() => {
    if (selectedMode === 'AI Curation') {
      // Bloqueia custom title
      setTitleForTiktokCutsEnabled(false);
      setTitleAutoEnabled(true);
      // Bloqueia custom hashtags
      setHashtagsForTiktokCutsEnabled(false);
      setHashtagsAutoEnabled(true);
    }
  }, [selectedMode]);
  useEffect(() => {
      if (dateTime) {
          const now = new Date();
          const diffInMilliseconds = dateTime.getTime() - now.getTime();
          // Garante no mínimo 20 minutos (1201 segundos)
          const seconds = Math.max(1201, Math.floor(diffInMilliseconds / 1000));
          setSecondsScheduleTiktokVideo(seconds);
      } else {
          setSecondsScheduleTiktokVideo(0);
      }
  }, [dateTime]);

  const {
    data: accounts,
    isLoading: loadingAccounts,
    error: accountsError,
  } = useQuery<Account[], Error>({
    queryKey: ['activeAccounts', 'tiktok'],  // opcionalmente inclua o filtro na key
    queryFn: async () => {
      if (!VITE_API_URL) {
        console.warn('VITE_API_URL not defined. Using mock accounts data.');
        return [
          { id: '2', platform: 'Tiktok', username: '@user2_mock', status: 'active' },
        ];
      }

      const res = await fetch(`${VITE_API_URL}/api/proxy/accounts/active`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ api_key: localStorage.getItem('api_key') }),
      });

      if (!res.ok) throw new Error('Failed to load accounts');
      const allAccounts: Account[] = await res.json();
      console.log('Active accounts received:', allAccounts);

      // Retorna apenas as de plataforma Tiktok
      return allAccounts.filter(acc => acc.platform === 'Tiktok');
    },
  });

  
  useEffect(() => {
    if (videoUrl && !hasRunPaste.current) {
      // Pré-preenche e abre automaticamente o modal de colar link
      setPastedUrl(videoUrl);
      setIsLinkConfirmed(true);
      setIsPasteDialogOpen(true);
      hasRunPaste.current = true;    // marca que já rodou
    }
  }, [videoUrl]);

  return (
    <div className="max-w-4xl mx-auto space-y-6 p-4
                    bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-gray-100 transition-colors duration-300">

      {/* Header */}
      <Card className="border-0 shadow-lg
                        bg-gradient-to-r from-blue-50 to-purple-50
                        dark:from-blue-900 dark:to-purple-900">
        <CardHeader>
          <CardTitle className="flex items-center gap-3 text-2xl text-gray-900 dark:text-gray-100">
            <div className="p-2 bg-blue-500 rounded-lg shadow-md shadow-blue-300/30 dark:shadow-blue-900/30">
              <Clapperboard className="text-white" size={24} />
            </div>
            Bem vindo ao Media Cuts
          </CardTitle>
          <p className="text-gray-600 dark:text-gray-400 text-sm h-6">
            {displayText}
            <span className="animate-pulse">|</span>
          </p>
        </CardHeader>
      </Card>

      {/* Error Display */}
      {error && (
        <Card className="border-red-200 bg-red-50 dark:border-red-700 dark:bg-red-950">
          <CardContent className="p-4">
            <div className="flex items-center gap-2 text-red-700 dark:text-red-300">
              <AlertCircle size={16} />
              <span className="text-sm">{error}</span>
            </div>
          </CardContent>
        </Card>
      )}
      {/* Video Source Configuration */}
      <Card className="border-l-4 border-l-green-500 dark:border-l-green-700
                      bg-white dark:bg-gray-800">
        <CardHeader
          className="cursor-pointer hover:bg-gray-50 transition-colors dark:hover:bg-gray-700"
          onClick={() => toggleSection('video')}
        >
          <CardTitle className="flex items-center justify-between text-gray-900 dark:text-gray-100">
            <div className="flex items-center gap-2">
              <Video size={20} className="text-gray-700 dark:text-gray-300" />
              Configurações do projeto
            </div>
            {expandedSections.video ? <ChevronUp size={20} className="text-gray-700 dark:text-gray-300" /> : <ChevronDown size={20} className="text-gray-700 dark:text-gray-300" />}
          </CardTitle>
        </CardHeader>

        {expandedSections.video && (
          <CardContent className="space-y-6">

            {/* Mode Settings */}
            <div>
              <label className="block text-sm font-medium mb-2 flex items-center gap-2 text-gray-700 dark:text-gray-300">
                <Palette size={16} className="text-gray-700 dark:text-gray-300" />
                Modelo de IA
              </label>

              <Select
                value={selectedMode}
                onValueChange={(value) => setselectedMode(value)}
              >
                <SelectTrigger className="w-full
                                           bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 border-gray-300 dark:border-gray-600">
                  <SelectValue placeholder="Selecione um tema" />
                </SelectTrigger>
                <SelectContent className="bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100">
                  {ShortifyOptions.map((theme) => (
                    <SelectItem value={theme.name} className="flex justify-between hover:bg-gray-100 dark:hover:bg-gray-700">
                      {theme.name}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>


            {/* Youtube Selection + Paste Link */}
            <div className="flex gap-2">
              <Input
                placeholder="Insira o nome do canal sem @"
                value={ytChannel}
                 onChange={(e) => {
                  const val = e.target.value;
                  setYtChannel(val);
                  // Ativa os seletores apenas após detectar digitação no campo de canal
                  setHasTypedChannel(val.trim().length > 0);
                  if (isLinkConfirmed) setIsLinkConfirmed(false); // <-- Isso reativa os seletores
                 }}
                className={`${formErrors.ytChannel ? 'border-red-500' : ''}
                          flex-1 bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 border-gray-300 dark:border-gray-600`}
              />

              {/* Botão/Entrada de Link */}
              <Dialog open={isPasteDialogOpen} onOpenChange={setIsPasteDialogOpen}>
                <DialogTrigger asChild>
                  <button
                    type="button"
                    className={`flex-1 flex items-center gap-2 px-3 py-2 text-sm rounded-md border transition-colors
                      ${
                        isLinkConfirmed
                          ? 'ring-2 ring-green-500 bg-green-50 dark:bg-green-900 dark:ring-green-600 text-green-700 dark:text-green-300 border-green-400 dark:border-green-600'
                          : 'bg-white dark:bg-gray-800 text-gray-800 dark:text-gray-200 border-gray-300 dark:border-gray-600 hover:bg-gray-50 dark:hover:bg-gray-700'
                      }`}
                  >
                    <LinkIcon
                      className={isLinkConfirmed ? 'text-green-600 dark:text-green-400' : 'text-indigo-600 dark:text-indigo-400'}
                      size={18}
                    />
                    Insira o link de um video
                  </button>
                </DialogTrigger>

                <DialogContent className="max-w-md bg-white dark:bg-gray-800 border dark:border-gray-700">
                  <DialogHeader>
                    <DialogTitle className="text-gray-900 dark:text-gray-100">Colar link do vídeo</DialogTitle>
                    <DialogDescription className="text-gray-600 dark:text-gray-400">
                      Cole um link de vídeo do YouTube abaixo para nossa IA processá-lo
                    </DialogDescription>
                  </DialogHeader>

                  <input
                    type="text"
                    value={pastedUrl}
                    onChange={(e) => setPastedUrl(e.target.value)}
                    placeholder="https://www.youtube.com/watch?v=..."
                    className="w-full p-2 mt-2 border border-gray-300 dark:border-gray-600 rounded-md bg-white dark:bg-gray-900 text-gray-900 dark:text-white"
                  />

                  <DialogFooter className="mt-4">
                    <Button
                      onClick={() => {
                        handlePasteUrl(pastedUrl);

                      }}
                      disabled={!pastedUrl}
                    >
                      Confirmar
                    </Button>
                  </DialogFooter>
                </DialogContent>
              </Dialog>
            </div>




            {/* Video Selection */}
            <div className="space-y-3">
              <h4 className="font-medium text-gray-900 dark:text-gray-100">Seleção de Vídeo</h4>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                <Dialog
                    open={isDialogOpen}
                    onOpenChange={(open) => {
                      if (open) {
                        // Bloqueia abrir enquanto o usuário não digitou o canal ou quando há link colado
                        if (!hasTypedChannel || isLinkConfirmed) {
                          toast({
                            title: 'Informe o canal',
                            description: 'Digite o nome do canal antes de selecionar um vídeo específico.',
                            variant: 'default',
                          });
                          return; // impede abrir
                        }
                        // Limpa o vídeo mais recente ao abrir o modal
                        setVideoTitleForLatestVideo('');
                        setLatestEnabled(false);
                      }
                      setIsDialogOpen(open);
                    }}
                  >
                  <DialogTrigger asChild>
                    <div className={(!hasTypedChannel || isLinkConfirmed) ? 'pointer-events-none opacity-50' : ''}>
                      <Card className={`cursor-pointer transition-all hover:shadow-md
                                        bg-white dark:bg-gray-800 border dark:border-gray-700
                                        ${customTitleEnabled ? 'ring-2 ring-blue-500 bg-blue-50 dark:bg-blue-900 dark:ring-blue-600' : 'hover:bg-gray-50 dark:hover:bg-gray-700'}`}>
                        <CardContent className="p-4">
                          <div className="flex items-center gap-2">
                            <Video size={20} className={customTitleEnabled ? 'text-blue-600 dark:text-blue-400' : 'text-gray-400 dark:text-gray-500'} />
                            <div>
                              <p className="font-medium text-sm text-gray-900 dark:text-gray-100">Vídeo específico</p>
                              <p className="text-xs text-gray-500 dark:text-gray-400">
                                {customTitleEnabled && videoTitle ? videoTitle.substring(0, 30) + '...' : 'Selecione um vídeo específico do canal'}
                              </p>
                            </div>
                          </div>
                        </CardContent>
                      </Card>
                    </div>
                  </DialogTrigger>



                  <DialogContent
                    className="max-w-md
                              bg-white dark:bg-gray-800 border dark:border-gray-700
                              text-gray-900 dark:text-gray-100">
                    <DialogHeader>
                      <DialogTitle className="text-gray-900 dark:text-gray-100">Escolha o vídeo</DialogTitle>
                      <DialogDescription className="text-gray-600 dark:text-gray-400">
                        Selecione entre vídeos recentes ou carregue mais
                      </DialogDescription>
                    </DialogHeader>

                    <div className="space-y-3">
                      {isLoadingVideos ? (
                        <div className="flex justify-center py-10 text-gray-600 dark:text-gray-400">
                          <Loader2 className="animate-spin text-blue-500 dark:text-blue-400" />
                        </div>
                      ) : (
                        videos.map(video => {
                          const thumb = video.thumbnail || (video as any).thumbnails?.[0]?.url || 'https://placehold.co/120x90/aabbcc/ffffff?text=No+Thumb';
                          return (
                            <Card
                              key={video.id}
                              className="cursor-pointer transition-colors
                                        bg-white dark:bg-gray-900 border dark:border-gray-700
                                        hover:bg-gray-50 dark:hover:bg-gray-700"
                              onClick={() => {
                                handleSelectVideo(video);

                              }}
                            >
                              <CardContent className="p-3">
                                <div className="flex items-center gap-3">
                                  <img
                                    src={thumb}
                                    alt={video.title}
                                    className="w-16 h-12 rounded object-cover"
                                    onError={(e) => (e.currentTarget.src = 'https://placehold.co/120x90/aabbcc/ffffff?text=No+Thumb')}
                                  />
                                  <div className="flex-1">
                                    <p className="font-medium text-sm line-clamp-2 text-gray-900 dark:text-gray-100">{video.title}</p>
                                  </div>
                                </div>
                              </CardContent>
                            </Card>
                          );
                        })
                      )}
                    </div>

                    <DialogFooter className="flex flex-col gap-2 md:flex-row md:justify-between mt-4">
                      <Button
                        variant="outline"
                        onClick={async () => {
                          setVideos([]);
                          setLoadedVideoIds([]);
                          const primeiros = await fetchVideos();
                          setVideos(primeiros);
                          setLoadedVideoIds(primeiros.map(v => v.id));
                        }}
                        disabled={isLoadingVideos}
                        className="bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300 border-gray-300 dark:border-gray-600 hover:bg-gray-100 dark:hover:bg-gray-700 w-full md:w-auto"
                      >
                        Carregar vídeos mais recentes
                      </Button>

                      <Button
                        variant="outline"
                        onClick={handleLoadMore}
                        disabled={isLoadingVideos || videos.length === 0}
                        className="bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300 border-gray-300 dark:border-gray-600 hover:bg-gray-100 dark:hover:bg-gray-700 w-full md:w-auto"
                      >
                        Carregar mais 5 vídeos
                      </Button>

                    </DialogFooter>
                  </DialogContent>



                </Dialog>
                <Card
                  className={
                    (!hasTypedChannel || loadingLatest || isLinkConfirmed)
                      ? `cursor-pointer transition-all pointer-events-none opacity-50`
                      : `cursor-pointer transition-all ${
                          videoTitleForLatestVideo
                            ? 'ring-2 ring-green-500 bg-green-50 dark:bg-green-900 dark:ring-green-600'
                            : 'hover:bg-gray-50 dark:hover:bg-gray-700'
                        }`
                  }
                  onClick={() => {
                    if (!hasTypedChannel) {
                      toast({
                        title: 'Informe o canal',
                        description: 'Digite o nome do canal antes de usar o vídeo mais recente.',
                        variant: 'default',
                      });
                      return;
                    }
                    handleFetchLatest();
                  }}
                >
                  <CardContent className="p-4">
                    <div className="flex items-center gap-2">
                      {loadingLatest ? (
                        <Loader2 className="animate-spin text-gray-600 dark:text-gray-400" size={20} />
                      ) : (
                        <Clock
                          size={20}
                          className={
                            videoTitleForLatestVideo
                              ? 'text-green-600 dark:text-green-400'
                              : 'text-gray-400 dark:text-gray-500'
                          }
                        />
                      )}
                      <div>
                        <p className="font-medium text-sm text-gray-900 dark:text-gray-100">
                          Vídeo mais recente
                        </p>
                        <p className="text-xs text-gray-500 dark:text-gray-400">
                          {videoTitleForLatestVideo
                            ? videoTitleForLatestVideo.substring(0, 30) + '...'
                            : loadingLatest
                              ? 'Loading...'
                              : 'Usar o video mais recente do canal'}
                        </p>
                      </div>
                    </div>
                  </CardContent>
                </Card>

              </div>
            </div>


            {/* Cutting Settings */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label className="flex items-center gap-1 text-sm font-medium mb-2 text-gray-700 dark:text-gray-300">
                  Duração do corte (segundos)

                  {isAICuration && (
                    <Popover
                      open={tooltipOpen}
                      onOpenChange={setTooltipOpen}
                    >
                      <PopoverTrigger asChild>
                        <Info
                          size={16}
                          className="text-gray-400 dark:text-gray-500 cursor-help"
                          onMouseEnter={() => setTooltipOpen(true)}
                          onMouseLeave={() => setTooltipOpen(false)}
                        />
                      </PopoverTrigger>
                      <PopoverContent
                        className="w-40 p-2 bg-white dark:bg-gray-800 text-sm text-gray-900 dark:text-gray-100 border dark:border-gray-700 rounded shadow"
                        onMouseEnter={() => setTooltipOpen(true)}
                        onMouseLeave={() => setTooltipOpen(false)}
                      >
                        Você pode inserir múltiplos valores separados por vírgula
                      </PopoverContent>
                    </Popover>
                  )}
                </label>

                <Input
                  type="text"
                  disabled={isAICuration}
                  value={cuttingSecondsInput}
                  onChange={(e) => {
                    setCuttingSecondsInput(e.target.value);
                  }}
                  onBlur={() => {
                    const values = cuttingSecondsInput
                      .split(",")
                      .map(v => parseInt(v.trim(), 10))
                      .filter(v => !isNaN(v) && v > 0);
                    setCuttingSeconds(values);
                  }}
                  placeholder="90, 120, 160"
                  className="bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 border-gray-300 dark:border-gray-600"
                />
              </div>
            </div>

            
            {/* Caixa Horizontal */}
            <div>
              <label className="block text-sm font-medium mb-2 text-gray-700 dark:text-gray-300">
                Tipos de vídeos a incluir
              </label>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                <Card
                  className={`cursor-pointer transition-all hover:shadow-md
                              bg-white dark:bg-gray-800 border dark:border-gray-700
                              ${includeHorizontal ? 'ring-2 ring-green-500 bg-green-50 dark:bg-green-900 dark:ring-green-600' : 'hover:bg-gray-50 dark:hover:bg-gray-700'}`}
                  onClick={() => setIncludeHorizontal(!includeHorizontal)}
                >
                  <CardContent className="p-3 flex items-center gap-2">
                    <div className={`w-4 h-4 rounded-full border-2 ${includeHorizontal ? 'bg-green-500 border-green-500' : 'border-gray-300 dark:border-gray-600'}`} />
                    <span className="font-medium text-sm text-gray-900 dark:text-gray-100">
                      Horizontais
                    </span>
                  </CardContent>
                </Card>

                <Card
                  className={`cursor-pointer transition-all hover:shadow-md
                              bg-white dark:bg-gray-800 border dark:border-gray-700
                              ${includeVertical ? 'ring-2 ring-green-500 bg-green-50 dark:bg-green-900 dark:ring-green-600' : 'hover:bg-gray-50 dark:hover:bg-gray-700'}`}
                  onClick={() => setIncludeVertical(!includeVertical)}
                >
                  <CardContent className="p-3 flex items-center gap-2">
                    <div className={`w-4 h-4 rounded-full border-2 ${includeVertical ? 'bg-green-500 border-green-500' : 'border-gray-300 dark:border-gray-600'}`} />
                    <span className="font-medium text-sm text-gray-900 dark:text-gray-100">
                      Verticais
                    </span>
                  </CardContent>
                </Card>
              </div>
            </div>

            {/* Tema do Projeto */}
            <div className="mt-4">
              {/* <h4 className="font-medium flex items-center gap-2 text-gray-900 dark:text-gray-100 mb-2">
                <Palette size={16} className="text-gray-700 dark:text-gray-300" />
                Tema do Projeto
              </h4> */}

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {/* Tema de legendas */}
                <div>
                  <label className="block text-sm font-medium mb-2 text-gray-700 dark:text-gray-300">Tema de legendas</label>
                  <Select
                    value={selectedThemeLegends}
                    onValueChange={(value) => handleThemeChange(value)}
                  >
                    <SelectTrigger className="w-full bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 border-gray-300 dark:border-gray-600">
                      <SelectValue placeholder="Selecione um tema" />
                    </SelectTrigger>
                    <SelectContent className="bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100">
                      {LegendsthemeOptions.map((theme) => (
                        <Popover key={theme.name}>
                          <PopoverTrigger asChild>
                            <SelectItem value={theme.name} className="flex justify-between hover:bg-gray-100 dark:hover:bg-gray-700">
                              {theme.name}
                            </SelectItem>
                          </PopoverTrigger>
                          <PopoverContent side="right" align="center" className="w-40 p-2 bg-white dark:bg-gray-800 border dark:border-gray-700">
                            <img src={theme.gif} alt={`Preview do tema ${theme.name}`} className="w-full h-auto rounded" />
                          </PopoverContent>
                        </Popover>
                      ))}
                    </SelectContent>
                  </Select>
                </div>

                {/* Tema da edição */}
                <div>
                  <label className="block text-sm font-medium mb-2 text-gray-700 dark:text-gray-300">Tema da edição</label>
                  <Select value={selectedEditionTheme} onValueChange={handleEditionThemeChange}>
                    <SelectTrigger className="w-full bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 border-gray-300 dark:border-gray-600">
                      <SelectValue placeholder="Selecione um tema de edição" />
                    </SelectTrigger>
                    <SelectContent className="bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100">
                      {EditionthemeOptions.map(theme => (
                        <SelectItem key={theme.name} value={theme.name} className="hover:bg-gray-100 dark:hover:bg-gray-700">{theme.name}</SelectItem>
                      ))}
                    </SelectContent>
                  </Select>
                </div>

              </div>
            </div>

          </CardContent>
        )}
      </Card>

      {/* Action Button */}
      <Card className="border-0 shadow-lg
                      bg-gradient-to-r from-green-50 to-blue-50
                      dark:from-green-900 dark:to-blue-900">
        <CardContent className="p-6">
          <div className="flex flex-col items-center space-y-4">
            {hasStartedTimer && (
              <div className="text-center">
                <div className="text-3xl font-mono font-bold text-blue-600 dark:text-blue-400">
                  {formatElapsed(elapsed)}
                </div>
                <p className="text-sm text-gray-600 dark:text-gray-400">Scheduling in progress...</p>
              </div>
            )}

            <Button
              onClick={handleStartShortify}
              disabled={hasStartedTimer || isLoading}
              size="lg"
              className="w-full max-w-md h-12 text-lg font-semibold shadow-lg
                         bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700
                         dark:from-blue-700 dark:to-purple-700 dark:hover:from-blue-800 dark:hover:to-purple-800"
            >
              {isLoading ? (
                <div className="flex items-center gap-2">
                  <Loader2 className="animate-spin text-white" size={20} />
                  Starting...
                </div>
              ) : hasStartedTimer ? (
                <div className="flex items-center gap-2">
                  <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse" />
                  Processing...
                </div>
              ) : (
                <div className="flex items-center gap-2">
                  <Play size={20} className="text-white" />
                  Start Shortify
                </div>
              )}
            </Button>

            {!hasStartedTimer && !isLoading && (
              <p className="text-sm text-gray-500 dark:text-gray-400 text-center max-w-md">
                Make sure all required fields are filled before starting the process
              </p>
            )}
          </div>
        </CardContent>
      </Card>

      {/* Progress Indicator */}

    </div>
  );
};

export default TaskComponent;
