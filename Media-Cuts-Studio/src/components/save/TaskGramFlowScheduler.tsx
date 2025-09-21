// src/components/TaskGramFlowScheduler.tsx

import React, { useEffect, useRef, useState } from 'react';

// import { Textarea } from '@/components/ui/textarea'; // Não está sendo usado, pode ser removido
import { Calendar, Clock, AlertCircle, ChevronDown, ChevronUp,  Type as TypeIcon, Play, Settings, Hash, Type, Video, Video as VideoIcon, Users, Palette, Globe, Loader2 } from 'lucide-react';
import { useNavigate } from 'react-router-dom';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import { useGramFlowScheduler } from '@/hooks/useGramFlowScheduler';
import { Select, SelectTrigger, SelectContent, SelectItem, SelectValue } from '@/components/ui/select';
import { useQuery } from '@tanstack/react-query';
import { toast } from '@/hooks/use-toast';
import { useSocketContext } from '@/contexts/SocketContext';
import ReactDatePicker from 'react-datepicker';
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
import { Popover, PopoverTrigger, PopoverContent } from '@/components/ui/popover';


// -------------------------------
// Interfaces (mantidas as mesmas)
interface Account {
  id: string;  
  platform: string;
  username: string;
  status: string;
}

interface Video {
  id: string;
  title: string;
  thumbnail: string;
}

interface ChannelVideosResponse {
  status: string;
  channel: string;
  limit: number;
  videos: Video[];
}

interface LegendsThemeOption {
  name: string;
  gif: string;
  settings: Record<string, any>;
}

interface EditionThemeOption {
  name: string;
}

interface TaskSchedulerProps {
  scheduleMode: 'date';
  setScheduleMode: React.Dispatch<React.SetStateAction<'date'>>;
  dayWeekly: string;
  setDayWeekly: React.Dispatch<React.SetStateAction<string>>;
  timeWeekly: string;
  setTimeWeekly: React.Dispatch<React.SetStateAction<string>>;
  timezone: string;
  setTimezone: React.Dispatch<React.SetStateAction<string>>;
  apiKey: string;
  setApiKey: React.Dispatch<React.SetStateAction<string>>;
  cuttingSeconds: number;
  setCuttingSeconds: React.Dispatch<React.SetStateAction<number>>;
}

const TaskScheduler: React.FC<TaskSchedulerProps> = ({
  scheduleMode,
  setScheduleMode,
  timezone,
  setTimezone,
  apiKey,
  setApiKey,

}) => {
  const [startTime, setStartTime] = useState<number | null>(null);
  const [elapsed, setElapsed] = useState(0);
  const [hasStartedTimer, setHasStartedTimer] = useState(false);
  const [selectedAccount, setSelectedAccount] = useState<string>('');
  const [dateTime, setDateTime] = useState<Date | null>(null);
  const [latestEnabled, setLatestEnabled] = useState(true);
  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [uploadedFile, setUploadedFile] = useState<File | null>(null);
  const [expandedSections, setExpandedSections] = useState({ schedule: true, media: true, content: false, account: false, advanced: false });
  const [isImage, setIsImage] = useState(false);
  const [isVideo, setIsVideo] = useState(false);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [tags, setTags] = useState('');

  const [formErrors, setFormErrors] = useState<Record<string, string>>({});
  
  const navigate = useNavigate();
  
  // Hooks e contextos reais da versão 1 
  const { startGramFlow, isLoading, error, clearError } = useGramFlowScheduler();
  const { runningTime, timerActive, finishedTimer, setTimerActive, clearFinishedTimer } = useSocketContext();

  const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:3000'; // Fallback para ambiente de desenvolvimento/mock
  const VITE_LANDING_API = import.meta.env.VITE_LANDING_API || 'http://localhost:3001'; // Fallback para ambiente de desenvolvimento/mock

  const {
    data: accounts,
    isLoading: loadingAccounts,
    error: accountsError,
  } = useQuery<Account[], Error>({
    queryKey: ['activeAccounts', 'instagram'],  // opcionalmente inclua o filtro na key
    queryFn: async () => {
      if (!VITE_LANDING_API) {
        console.warn('VITE_LANDING_API not defined. Using mock accounts data.');
        return [
          { id: '2', platform: 'Instagram', username: '@user2_mock', status: 'active' },
        ];
      }

      const res = await fetch(`${VITE_LANDING_API}/api/proxy/accounts/active`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ api_key: localStorage.getItem('api_key') }),
      });

      if (!res.ok) throw new Error('Failed to load accounts');
      const allAccounts: Account[] = await res.json();
      console.log('Active accounts received:', allAccounts);

      // Retorna apenas as de plataforma Instagram
      return allAccounts.filter(acc => acc.platform === 'Instagram');
    },
  });


  // Funções de manipulação de UX (da versão 2)
  const toggleSection = (section: keyof typeof expandedSections) => {
    setExpandedSections(prev => ({
      ...prev,
      [section]: !prev[section]
    }));
  };

  const handleFile = (file: File) => {
    setUploadedFile(file);
    const type = file.type;
    setIsImage(type.startsWith('image/'));
    setIsVideo(type.startsWith('video/'));
  };

  const handleFileDrop = (e: React.DragEvent) => {
    e.preventDefault();
    const file = e.dataTransfer.files[0];
    if(file) handleFile(file);
  };
  const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0] || null;
    if(file) handleFile(file);
    else {
      setUploadedFile(null);
      setIsImage(false);
      setIsVideo(false);
    }
  };

  const validateForm = () => {
    const errors: Record<string, string> = {};
    
    
    if (!selectedAccount) {
      errors.selectedAccount = 'Please select an account';
    }
    
    // Substituído ReactDatePicker por input nativo, ajuste a validação para o formato de string
    if (scheduleMode === 'date' && !dateTime) { 
      errors.dateTime = 'Please select date and time';
    }

    setFormErrors(errors);
    return Object.keys(errors).length === 0;
  };


  // Lógica de início do GramFlow (combinada da versão 1 e 2)
  const handleStartGramFlow = async () => {
    if(!validateForm()) return toast({ title:'Erro', description:'Preencha os campos obrigatórios', variant:'destructive' });
    clearError();
    try {
      setApiKey(localStorage.getItem('api_key') || '');
      const user_email = localStorage.getItem('user_email');
      const api_key = localStorage.getItem('api_key');
      console.log(`selectedAccount? ${selectedAccount}`);
      console.log(`user_email? ${user_email}`);

      const resp = await fetch(`${VITE_LANDING_API}/api/account-instagram`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          api_key: localStorage.getItem('api_key'),
          ig_username: selectedAccount
        }),
      });
      if (!resp.ok) throw new Error('Erro ao buscar credenciais Instagram');

      // const respose = await resp.json();
      // console.log(respose);

      const { ig_username, ig_password } = await resp.json();
      console.log(`ig_username? ${ig_username}`);
      console.log(`ig_password? ${ig_password}`);

      const payload = {
        dateTime: dateTime, 
        timezone: timezone,
        scheduleMode: scheduleMode,
        ig_username: ig_username,
        ig_password: ig_password,
        api_key: api_key,
        user_email: user_email,
        upload_video: isVideo,
        upload_image: isImage,
        title,
        description,
        tags: tags, 
        uploadedFile: uploadedFile,
      };


      console.log("Final Payload:", payload);

      await startGramFlow(payload); 
      const now = Date.now();
      setStartTime(now);
      setHasStartedTimer(true);

    } catch (err) {
      // Erro já é tratado pelo hook e exibido no componente via `error` state
      console.error("Error starting Shortify:", err);
    }
  };


  // Lógica do Timer (da versão 1)
  useEffect(() => {
    if (!hasStartedTimer) return;

    const interval = setInterval(() => {
      if (startTime) {
        setElapsed(Date.now() - startTime);
      }
    }, 1000);

    return () => clearInterval(interval);
  }, [hasStartedTimer, startTime]);

  // Efeito para `finishedTimer` (da versão 1)
  useEffect(() => {
    if (finishedTimer && hasStartedTimer) {
      // Para o cronômetro
      setHasStartedTimer(false);
      // Mostra toast
      toast({
        title: 'Shortify started successfully',
        description: 'Navigate to the process tab to follow the editing of the cuts',
        variant: 'default',
        duration: 5000,
      });
      // Reseta
      setStartTime(null);
      setElapsed(0);
      clearFinishedTimer();
    }
  }, [finishedTimer, hasStartedTimer, clearFinishedTimer]); // Dependências corrigidas

  function formatElapsed(ms: number) {
    const totalSec = Math.floor(ms / 1000);
    const h = String(Math.floor(totalSec / 3600)).padStart(2,'0');
    const m = String(Math.floor((totalSec % 3600) / 60)).padStart(2,'0');
    const s = String(totalSec % 60).padStart(2,'0');
    return `${h}:${m}:${s}`;
  }

  // Helper para formatar Date para input datetime-local
  const formatDateTimeLocal = (date: Date | null) => {
    if (!date) return '';
    const year = date.getFullYear();
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const day = date.getDate().toString().padStart(2, '0');
    const hours = date.getHours().toString().padStart(2, '0');
    const minutes = date.getMinutes().toString().padStart(2, '0');
    return `${year}-${month}-${day}T${hours}:${minutes}`;
  };

  return (
    <div className="max-w-4xl mx-auto space-y-6 p-4
                    bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-gray-100 transition-colors duration-300">
      {/* Header */}
      <Card className="border-0 shadow-lg
                      bg-gradient-to-r from-blue-50 to-purple-50
                      dark:from-blue-900 dark:to-purple-900">
        <CardHeader>
          <CardTitle className="flex items-center gap-3 text-2xl text-gray-900 dark:text-gray-100">
            <div className="p-2 bg-blue-500 rounded-lg">
              <Calendar className="text-white" size={24} />
            </div>
            GramFlow
          </CardTitle>
          <p className="text-gray-600 dark:text-gray-400 text-sm">
            Configure your automated video processing schedule with custom settings
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

      {/* Schedule Configuration */}
      <Card className="border-l-4 border-l-blue-500 dark:border-l-blue-700
                      bg-white dark:bg-gray-800">
        <CardHeader
          className="cursor-pointer transition-colors
                     hover:bg-gray-50 dark:hover:bg-gray-700"
          onClick={() => toggleSection('schedule')}
        >
          <CardTitle className="flex items-center justify-between text-gray-900 dark:text-gray-100">
            <div className="flex items-center gap-2">
              <Clock size={20} className="text-gray-700 dark:text-gray-300" />
              Schedule Configuration
            </div>
            {expandedSections.schedule ? <ChevronUp size={20} className="text-gray-700 dark:text-gray-300" /> : <ChevronDown size={20} className="text-gray-700 dark:text-gray-300" />}
          </CardTitle>
        </CardHeader>

        {expandedSections.schedule && (
          <CardContent className="space-y-6">
            {/* Schedule Mode Toggle */}
            <div className="grid grid-cols-2 gap-4">
              <Card
                className={`cursor-pointer transition-all hover:shadow-md
                            bg-white dark:bg-gray-800 border dark:border-gray-700
                            ${scheduleMode === 'date'
                    ? 'ring-2 ring-purple-500 bg-purple-50 dark:bg-purple-900 dark:ring-purple-600'
                    : 'hover:bg-gray-50 dark:hover:bg-gray-700'
                  }`}
                onClick={() => setScheduleMode('date')}
              >
                <CardContent className="p-4 text-center">
                  <div className="flex flex-col items-center gap-2">
                    <Clock size={24} className={scheduleMode === 'date' ? 'text-purple-600 dark:text-purple-400' : 'text-gray-400 dark:text-gray-500'} />
                    <h3 className="font-medium text-gray-900 dark:text-gray-100">Date Mode</h3>
                    <p className="text-sm text-gray-500 dark:text-gray-400">Execute once</p>
                  </div>
                </CardContent>
              </Card>
            </div>


            {/* Date Configuration */}
            {scheduleMode === 'date' && (
              <Card className="border-purple-200 bg-purple-50 dark:border-purple-700 dark:bg-purple-950">
                <CardContent className="p-4 space-y-4">
                  <h4 className="font-medium text-purple-800 dark:text-purple-300">Date & Time Settings</h4>
                  <div>
                    <label className="block text-sm font-medium mb-2 text-gray-700 dark:text-gray-300">Execution Date and Time</label>
                    <Input
                      type="datetime-local"
                      value={formatDateTimeLocal(dateTime)}
                      onChange={(e) => setDateTime(new Date(e.target.value))}
                      className={`w-full px-3 py-2 border rounded ${formErrors.dateTime ? 'border-red-500' : ''}
                                 bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 border-gray-300 dark:border-gray-600`}
                    />
                    {formErrors.dateTime && <p className="text-red-500 text-xs mt-1">{formErrors.dateTime}</p>}
                  </div>
                </CardContent>
              </Card>
            )}

            {/* Timezone Selection */}
            <div>
              <h4 className="font-medium mb-3 flex items-center gap-2 text-gray-900 dark:text-gray-100">
                <Globe size={16} className="text-gray-700 dark:text-gray-300" />
                Timezone
              </h4>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                {[
                  { value: 'America/Sao_Paulo', label: 'São Paulo Time Zone', flag: '🇧🇷' },
                  { value: 'UTC', label: 'UTC Time Zone', flag: '🌍' }
                ].map(tz => (
                  <Card
                    key={tz.value}
                    className={`cursor-pointer transition-all hover:shadow-md
                                bg-white dark:bg-gray-800 border dark:border-gray-700
                                ${timezone === tz.value
                        ? 'ring-2 ring-green-500 bg-green-50 dark:bg-green-900 dark:ring-green-600'
                        : 'hover:bg-gray-50 dark:hover:bg-gray-700'
                      }`}
                    onClick={() => setTimezone(tz.value)}
                  >
                    <CardContent className="p-3">
                      <div className="flex items-center gap-2">
                        <span className="text-lg">{tz.flag}</span>
                        <span className="font-medium text-gray-900 dark:text-gray-100">{tz.label}</span>
                      </div>
                    </CardContent>
                  </Card>
                ))}
              </div>
            </div>
          </CardContent>
        )}
      </Card>

      {/* Media (Video & Image) */}
      <Card className="border-l-4 border-l-green-500 dark:border-l-green-700 bg-white dark:bg-gray-800">
        <CardHeader onClick={() => toggleSection('media')} className="cursor-pointer hover:bg-gray-50 dark:hover:bg-gray-700">
          <CardTitle className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <VideoIcon size={20} />
              <span>Video & Image</span>
            </div>
            {expandedSections.media ? <ChevronUp size={20}/> : <ChevronDown size={20}/>}
          </CardTitle>
        </CardHeader>
        {expandedSections.media && (
          <CardContent className="space-y-4">
            <div
              className="border-2 border-dashed border-gray-300 dark:border-gray-600 p-6 rounded-lg text-center"
              onDragOver={e => e.preventDefault()}
              onDrop={handleFileDrop}
            >
              {!uploadedFile ? (
                <>  
                  <p>Arraste e solte um reel ou imagem aqui, ou</p>
                  <label className="cursor-pointer text-blue-600 dark:text-blue-400">
                    selecione um arquivo
                    <input type="file" accept="video/*,image/*" className="hidden" onChange={handleFileSelect} />
                  </label>
                </>
              ) : (
                <p>Arquivo: {uploadedFile.name} ({isImage ? 'Imagem' : isVideo ? 'Vídeo' : 'Outro'})</p>
              )}
            </div>
          </CardContent>
        )}
      </Card>

      {/* Content Settings */}
      <Card className="border-l-4 border-l-orange-500 dark:border-l-orange-700 bg-white dark:bg-gray-800">
        <CardHeader onClick={() => toggleSection('content')} className="cursor-pointer hover:bg-gray-50 dark:hover:bg-gray-700">
          <CardTitle className="flex items-center justify-between">
            <div className="flex items-center gap-2"><TypeIcon size={20}/> Content Settings</div>
            {expandedSections.content ? <ChevronUp size={20}/> : <ChevronDown size={20}/>}
          </CardTitle>
        </CardHeader>
        {expandedSections.content && (
          <CardContent className="space-y-4">
            <div>
              <label className="block text-sm font-medium mb-1">Title</label>
              <Input value={title} onChange={e => setTitle(e.target.value)} className="w-full" />
              {formErrors.title && <p className="text-red-600 text-xs mt-1">{formErrors.title}</p>}
            </div>
            <div>
              <label className="block text-sm font-medium mb-1">Description</label>
              <Textarea value={description} onChange={e => setDescription(e.target.value)} className="w-full" rows={3} />
              {formErrors.description && <p className="text-red-600 text-xs mt-1">{formErrors.description}</p>}
            </div>
            <div>
              <label className="block text-sm font-medium mb-1">Tags (separadas por vírgula)</label>
              <Input value={tags} onChange={e => setTags(e.target.value)} className="w-full" />
            </div>
          </CardContent>
        )}
      </Card>

      {/* Account Selection */}
      <Card className="border-l-4 border-l-indigo-500 dark:border-l-indigo-700
                      bg-white dark:bg-gray-800">
        <CardHeader
          className="cursor-pointer hover:bg-gray-50 transition-colors dark:hover:bg-gray-700"
          onClick={() => toggleSection('account')}
        >
          <CardTitle className="flex items-center justify-between text-gray-900 dark:text-gray-100">
            <div className="flex items-center gap-2">
              <Users size={20} className="text-gray-700 dark:text-gray-300" />
              Account Settings
            </div>
            {expandedSections.account ? <ChevronUp size={20} className="text-gray-700 dark:text-gray-300" /> : <ChevronDown size={20} className="text-gray-700 dark:text-gray-300" />}
          </CardTitle>
        </CardHeader>

        {expandedSections.account && (
          <CardContent className="space-y-4">
            <div>
              <label className="block text-sm font-medium mb-2 text-gray-700 dark:text-gray-300">Active Account</label>
              <Select
                value={selectedAccount}
                onValueChange={setSelectedAccount}
                disabled={loadingAccounts || !!accountsError}
              >
                <SelectTrigger className={`w-full ${formErrors.selectedAccount ? 'border-red-500' : ''}
                                           bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 border-gray-300 dark:border-gray-600`}>
                  <SelectValue
                    placeholder={
                      loadingAccounts
                        ? 'Loading accounts...'
                        : accountsError
                          ? 'Error loading'
                          : 'Select an active account'
                    }
                  />
                </SelectTrigger>
                <SelectContent className="bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100">
                  {accounts?.map(acc => (
                    <SelectItem key={acc.id} value={acc.username} className="hover:bg-gray-100 dark:hover:bg-gray-700">
                      <div className="flex items-center gap-2">
                        <div className={`w-2 h-2 rounded-full ${
                          acc.platform === 'TikTok' ? 'bg-black dark:bg-gray-200' :
                            acc.platform === 'Instagram' ? 'bg-pink-500 dark:bg-pink-400' : 'bg-blue-500 dark:bg-blue-400'
                        }`} />
                        {acc.platform} – {acc.username}
                      </div>
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
              {formErrors.selectedAccount && <p className="text-red-500 text-xs mt-1">{formErrors.selectedAccount}</p>}
            </div>

            <Button
              variant="outline"
              onClick={() => navigate('/accounts')}
              className="w-full
                         bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300 border-gray-300 dark:border-gray-600 hover:bg-gray-100 dark:hover:bg-gray-700"
            >
              + Add New Account
            </Button>
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
                <p className="text-sm text-gray-600 dark:text-gray-400">Processing in progress...</p>
              </div>
            )}

            <Button
              onClick={handleStartGramFlow}
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
                  Start GramFlow
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
      {hasStartedTimer && (
        <Card className="border-green-200 bg-green-50 dark:border-green-700 dark:bg-green-950">
          <CardContent className="p-4">
      
            <div className="mt-2 bg-green-200 dark:bg-green-800 rounded-full h-2">
              <div
                className="bg-green-500 h-2 rounded-full animate-pulse"
                style={{ width: '45%' }}
              />
            </div>
          </CardContent>
        </Card>
      )}
    </div>
  );
};

export default TaskScheduler;
