import { useState, useEffect } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Textarea } from '@/components/ui/textarea';
import { Checkbox } from '@/components/ui/checkbox';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { Alert, AlertDescription } from '@/components/ui/alert';
import { Badge } from '@/components/ui/badge';
import { Progress } from '@/components/ui/progress';
import { 
  Upload, 
  Calendar, 
  Clock, 
  CheckCircle, 
  Youtube, 
  Eye,
  EyeOff,
  Users,
  Tag,
  FileVideo,
  Sparkles,
  ArrowLeft,
  AlertTriangle,
  Info
} from 'lucide-react';
import { usePost } from '@/contexts/PostContext';
import { useNavigate } from 'react-router-dom';
import { toast } from '@/hooks/use-toast';
import { BsTiktok } from 'react-icons/bs';
import Layout from '@/components/Layout';

// Define a URL base do backend a partir das variáveis de ambiente do Vite
const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;

const socialNetworks = [
  { 
    id: 'youtube', 
    name: 'YouTube', 
    color: 'text-red-500',
    bgColor: 'bg-red-50 border-red-200',
    icon: Youtube,
    description: 'Alcance milhões com YouTube Shorts'
  },
  { 
    id: 'tiktok', 
    name: 'TikTok', 
    color: 'text-pink-500',
    bgColor: 'bg-pink-50 border-pink-200',
    icon: BsTiktok,
    description: 'Viral no TikTok com vídeos curtos'
  },
];

const visibilityOptions = [
  {
    value: 'public',
    label: 'Público',
    description: 'Visível para todos',
    icon: Users,
    color: 'text-green-600'
  },
  {
    value: 'private',
    label: 'Privado',
    description: 'Apenas você pode ver',
    icon: EyeOff,
    color: 'text-gray-600'
  },
  {
    value: 'unlisted',
    label: 'Não Listado',
    description: 'Apenas com link direto',
    icon: Eye,
    color: 'text-blue-600'
  }
];

interface Channel {
  id: string;
  nome: string;
  socialNetwork: 'youtube' | 'tiktok';
}

export default function NewPost() {
  const { addPost } = usePost();
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    title: '',
    description: '',
    tags: '',
    scheduledDate: '',
    scheduledTime: '',
    socialNetworks: ['youtube'] as string[],
    visibility: 'public' as 'public' | 'private' | 'unlisted',
    canalId: '',
    canalTikTokId: ''
  });

  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [previewUrl, setPreviewUrl] = useState<string | null>(null);
  const [channels, setChannels] = useState<Channel[]>([]);
  const [loadingChannels, setLoadingChannels] = useState(true);
  const [uploadProgress, setUploadProgress] = useState(0);
  const [currentStep, setCurrentStep] = useState(1);
  const [errors, setErrors] = useState<Record<string, string>>({});

  const youtubeChannels = channels.filter(c => c.socialNetwork === 'youtube');
  const tikTokChannels = channels.filter(c => c.socialNetwork === 'tiktok');
  
  const todayLocal = new Date();
  todayLocal.setMinutes(todayLocal.getMinutes() - todayLocal.getTimezoneOffset()); 
  const minDate = todayLocal.toISOString().split('T')[0];

  const steps = [
    { number: 1, title: 'Upload', description: 'Enviar vídeo' },
    { number: 2, title: 'Detalhes', description: 'Informações do post' },
    { number: 3, title: 'Canais', description: 'Selecionar plataformas' },
    { number: 4, title: 'Agendamento', description: 'Data e hora' },
  ];

  useEffect(() => {
    const fetchChannels = async () => {
      try {
        const response = await fetch(`${BACKEND_URL}/api/canais`);
        if (!response.ok) throw new Error(`Erro ao carregar canais: ${response.statusText}`);
        const data: Channel[] = await response.json();
        setChannels(data);
        
        const yt = data.find(c => c.socialNetwork === 'youtube');
        const tt = data.find(c => c.socialNetwork === 'tiktok');
        setFormData(prev => ({
          ...prev,
          canalId: yt?.id || '',
          canalTikTokId: tt?.id || ''
        }));
      } catch (error) {
        console.error('Falha ao carregar canais:', error);
        toast({ 
          title: 'Erro', 
          description: 'Falha ao carregar canais. Verifique o backend.', 
          variant: 'destructive' 
        });
      } finally {
        setLoadingChannels(false);
      }
    };
    fetchChannels();
  }, []);

  const validateForm = () => {
    const newErrors: Record<string, string> = {};

    if (!formData.title.trim()) {
      newErrors.title = 'Título é obrigatório';
    }

    if (!formData.scheduledDate) {
      newErrors.scheduledDate = 'Data é obrigatória';
    }

    if (!formData.scheduledTime) {
      newErrors.scheduledTime = 'Hora é obrigatória';
    }

    if (!selectedFile) {
      newErrors.file = 'Arquivo de vídeo é obrigatório';
    }

    if (formData.socialNetworks.length === 0) {
      newErrors.socialNetworks = 'Selecione pelo menos uma rede social';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      // Simular progresso de upload
      setUploadProgress(0);
      const interval = setInterval(() => {
        setUploadProgress(prev => {
          if (prev >= 100) {
            clearInterval(interval);
            return 100;
          }
          return prev + 10;
        });
      }, 200);

      setSelectedFile(file);
      const url = URL.createObjectURL(file);
      setPreviewUrl(url);
      setErrors(prev => ({ ...prev, file: '' }));
      
      if (currentStep === 1) {
        setTimeout(() => setCurrentStep(2), 2000);
      }
    }
  };

  const handleSocialNetworkChange = (networkId: string, checked: boolean) => {
    setFormData(prev => {
      const current = new Set(prev.socialNetworks);
      if (checked) {
        current.add(networkId);
      } else {
        current.delete(networkId);
      }
      return { ...prev, socialNetworks: Array.from(current) };
    });
    setErrors(prev => ({ ...prev, socialNetworks: '' }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!validateForm()) {
      toast({
        title: "Erro no formulário",
        description: "Por favor, corrija os erros antes de continuar",
        variant: "destructive"
      });
      return;
    }

    setIsSubmitting(true);

    try {
      const scheduledAtISO = `${formData.scheduledDate} ${formData.scheduledTime}:00`;

      const postFormData = new FormData();
      postFormData.append('video_file', selectedFile!);
      postFormData.append('title', formData.title);
      postFormData.append('description', formData.description);
      postFormData.append('video_tags', formData.tags);
      postFormData.append('scheduled_publish_at', scheduledAtISO);
      postFormData.append('privacy_status', formData.visibility);
      postFormData.append('ia_gen_title', 'false');
      postFormData.append('category_id', '22');
      postFormData.append('socialNetworks', JSON.stringify(formData.socialNetworks));
      postFormData.append('canal_id', formData.canalId);
      postFormData.append('canal_id_tiktok', formData.canalTikTokId);

      const response = await fetch(`${BACKEND_URL}/api/posts/agendar`, {
        method: 'POST',
        body: postFormData,
      });

      const responseData = await response.json();

      if (!response.ok) {
        throw new Error(responseData.error || 'Falha ao agendar o post');
      }

      toast({
        title: "🎉 Sucesso!",
        description: "Post agendado com sucesso para suas redes sociais!",
      });

      navigate('/posts');
    } catch (error: any) {
      console.error("Erro ao agendar o post:", error);
      toast({
        title: "Erro",
        description: error.message || "Falha ao agendar o post. Tente novamente.",
        variant: "destructive"
      });
    } finally {
      setIsSubmitting(false);
    }
  };

  const getStepStatus = (stepNumber: number) => {
    if (stepNumber < currentStep) return 'completed';
    if (stepNumber === currentStep) return 'current';
    return 'upcoming';
  };

  return (
    <Layout>
      <div className="max-w-4xl mx-auto space-y-8">
        {/* Header com navegação melhorada */}
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-4">
            <Button 
              variant="ghost" 
              size="sm"
              onClick={() => navigate('/posts')}
              className="flex items-center gap-2 text-muted-foreground hover:text-foreground"
            >
              <ArrowLeft className="h-4 w-4" />
              Voltar
            </Button>
            <div>
              <h1 className="text-4xl font-bold tracking-tight bg-gradient-to-r from-purple-600 to-pink-600 bg-clip-text text-transparent">
                Criar Novo Post
              </h1>
              <p className="text-lg text-muted-foreground">
                Publique seus vídeos no YouTube e TikTok simultaneamente
              </p>
            </div>
          </div>
          <div className="flex items-center gap-2">
            <Sparkles className="h-5 w-5 text-purple-500" />
            <Badge variant="secondary" className="bg-purple-50 text-purple-700">
              Multi-plataforma
            </Badge>
          </div>
        </div>

        {/* Progress Steps */}
        <Card className="p-6">
          <div className="flex items-center justify-between">
            {steps.map((step, index) => {
              const status = getStepStatus(step.number);
              return (
                <div key={step.number} className="flex items-center">
                  <div className="flex flex-col items-center">
                    <div className={`
                      w-10 h-10 rounded-full flex items-center justify-center text-sm font-medium transition-all duration-300
                      ${status === 'completed' 
                        ? 'bg-green-500 text-white' 
                        : status === 'current' 
                        ? 'bg-purple-500 text-white animate-pulse' 
                        : 'bg-gray-200 text-gray-500'
                      }
                    `}>
                      {status === 'completed' ? <CheckCircle className="h-5 w-5" /> : step.number}
                    </div>
                    <div className="mt-2 text-center">
                      <div className={`text-sm font-medium ${status === 'current' ? 'text-purple-600' : 'text-gray-500'}`}>
                        {step.title}
                      </div>
                      <div className="text-xs text-muted-foreground">
                        {step.description}
                      </div>
                    </div>
                  </div>
                  {index < steps.length - 1 && (
                    <div className={`flex-1 h-0.5 mx-4 transition-colors duration-300 ${
                      step.number < currentStep ? 'bg-green-500' : 'bg-gray-200'
                    }`} />
                  )}
                </div>
              );
            })}
          </div>
        </Card>

        <form onSubmit={handleSubmit} className="space-y-8">
          {/* Upload Section - Melhorada */}
          <Card className="overflow-hidden border-2 border-dashed border-gray-300 hover:border-purple-400 transition-colors duration-300">
            <CardHeader className="bg-gradient-to-r from-purple-50 to-pink-50">
              <CardTitle className="flex items-center gap-2 text-purple-700">
                <FileVideo className="h-5 w-5" />
                Upload do Vídeo
              </CardTitle>
              <CardDescription>
                Faça upload do seu vídeo para YouTube Shorts ou TikTok (máx. 100MB)
              </CardDescription>
            </CardHeader>
            <CardContent className="p-6">
              <div className="space-y-4">
                <Input
                  type="file"
                  accept="video/*"
                  onChange={handleFileSelect}
                  className="cursor-pointer file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-purple-50 file:text-purple-700 hover:file:bg-purple-100"
                  required
                />
                {errors.file && (
                  <Alert variant="destructive">
                    <AlertTriangle className="h-4 w-4" />
                    <AlertDescription>{errors.file}</AlertDescription>
                  </Alert>
                )}
                
                {uploadProgress > 0 && uploadProgress < 100 && (
                  <div className="space-y-2">
                    <div className="flex justify-between text-sm">
                      <span>Processando...</span>
                      <span>{uploadProgress}%</span>
                    </div>
                    <Progress value={uploadProgress} className="h-2" />
                  </div>
                )}

                {previewUrl && (
                  <div className="mt-6 space-y-3">
                    <div className="flex items-center gap-2 text-sm font-medium text-green-600">
                      <CheckCircle className="h-4 w-4" />
                      Vídeo carregado com sucesso!
                    </div>
                    <div className="relative">
                      <video 
                        src={previewUrl} 
                        controls 
                        className="w-full max-w-sm h-64 object-cover rounded-lg shadow-lg border"
                      />
                      <div className="absolute top-2 right-2">
                        <Badge className="bg-black/70 text-white">
                          {selectedFile?.type.split('/')[1]?.toUpperCase()}
                        </Badge>
                      </div>
                    </div>
                    <div className="text-sm text-muted-foreground bg-gray-50 p-3 rounded-lg">
                      <strong>{selectedFile?.name}</strong> • {((selectedFile?.size || 0) / (1024 * 1024)).toFixed(2)} MB
                    </div>
                  </div>
                )}
              </div>
            </CardContent>
          </Card>

          {/* Detalhes do Post - Melhorado */}
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <Tag className="h-5 w-5" />
                Detalhes do Post
              </CardTitle>
              <CardDescription>
                Adicione informações que ajudarão seu conteúdo a ser descoberto
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-6">
              <div>
                <Label htmlFor="title" className="text-base font-medium">
                  Título *
                </Label>
                <Input
                  id="title"
                  value={formData.title}
                  onChange={(e) => {
                    setFormData(prev => ({ ...prev, title: e.target.value }));
                    setErrors(prev => ({ ...prev, title: '' }));
                  }}
                  placeholder="Um título atrativo para seu vídeo..."
                  required
                  className={`mt-1 ${errors.title ? 'border-red-500' : ''}`}
                />
                {errors.title && (
                  <p className="text-sm text-red-500 mt-1">{errors.title}</p>
                )}
                <p className="text-sm text-muted-foreground mt-1">
                  {formData.title.length}/100 caracteres
                </p>
              </div>

              <div>
                <Label htmlFor="description" className="text-base font-medium">
                  Descrição
                </Label>
                <Textarea
                  id="description"
                  value={formData.description}
                  onChange={(e) => setFormData(prev => ({ ...prev, description: e.target.value }))}
                  placeholder="Descreva seu vídeo, use hashtags relevantes..."
                  rows={4}
                  className="mt-1 resize-none"
                />
                <p className="text-sm text-muted-foreground mt-1">
                  {formData.description.length}/500 caracteres
                </p>
              </div>

              <div>
                <Label htmlFor="tags" className="text-base font-medium">
                  Tags
                </Label>
                <Input
                  id="tags"
                  value={formData.tags}
                  onChange={(e) => setFormData(prev => ({ ...prev, tags: e.target.value }))}
                  placeholder="gaming, tutorial, dicas, review"
                  className="mt-1"
                />
                <p className="text-sm text-muted-foreground mt-1">
                  Separe as tags com vírgulas. Máximo 10 tags.
                </p>
              </div>

              <div>
                <Label className="text-base font-medium mb-3 block">
                  Visibilidade
                </Label>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
                  {visibilityOptions.map((option) => {
                    const IconComponent = option.icon;
                    return (
                      <div
                        key={option.value}
                        className={`p-4 rounded-lg border cursor-pointer transition-all duration-200 ${
                          formData.visibility === option.value
                            ? 'border-purple-300 bg-purple-50 ring-2 ring-purple-200'
                            : 'border-gray-200 hover:border-gray-300 hover:bg-gray-50'
                        }`}
                        onClick={() => setFormData(prev => ({ ...prev, visibility: option.value as any }))}
                      >
                        <div className="flex items-start gap-3">
                          <IconComponent className={`h-5 w-5 mt-0.5 ${option.color}`} />
                          <div>
                            <div className="font-medium">{option.label}</div>
                            <div className="text-sm text-muted-foreground">{option.description}</div>
                          </div>
                        </div>
                      </div>
                    );
                  })}
                </div>
              </div>
            </CardContent>
          </Card>

          {/* Redes Sociais - Atualizado para evitar nested-button / loops */}
          <Card>
            <CardHeader>
              <CardTitle>Plataformas de Publicação</CardTitle>
              <CardDescription>
                Escolha onde você deseja publicar este conteúdo
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {socialNetworks.map((network) => {
                  const IconComponent = network.icon;
                  const isSelected = formData.socialNetworks.includes(network.id);

                  return (
                    <div
                      key={network.id}
                      className={`p-4 rounded-lg border-2 transition-all duration-300 cursor-pointer ${
                        isSelected
                          ? `${network.bgColor} border-current shadow-md scale-105`
                          : 'border-gray-200 hover:border-gray-300 hover:shadow-sm'
                      }`}
                      onClick={() => handleSocialNetworkChange(network.id, !isSelected)}
                      role="button"
                      tabIndex={0}
                      onKeyDown={(e) => {
                        if (e.key === 'Enter' || e.key === ' ') {
                          e.preventDefault();
                          handleSocialNetworkChange(network.id, !isSelected);
                        }
                      }}
                    >
                      <label className="flex items-center gap-3 cursor-pointer select-none">
                        {/* input nativo (não é button) — para evitar nested-button issues */}
                        <input
                          type="checkbox"
                          checked={isSelected}
                          onChange={(e) => handleSocialNetworkChange(network.id, e.target.checked)}
                          onClick={(e) => e.stopPropagation()} // evita disparar o onClick do pai duas vezes
                          className="w-4 h-4 rounded border-gray-300"
                          aria-checked={isSelected}
                          aria-label={network.name}
                        />

                        <div className="flex-1">
                          <div className="flex items-center gap-2">
                            <IconComponent className={`h-5 w-5 ${network.color}`} />
                            <span className="font-medium">{network.name}</span>
                          </div>
                          <p className="text-sm text-muted-foreground mt-1">
                            {network.description}
                          </p>
                        </div>
                      </label>
                    </div>
                  );
                })}
              </div>

              {errors.socialNetworks && (
                <Alert variant="destructive" className="mt-4">
                  <AlertTriangle className="h-4 w-4" />
                  <AlertDescription>{errors.socialNetworks}</AlertDescription>
                </Alert>
              )}
            </CardContent>
          </Card>
          {/* Canais - Melhorado */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {/* Canal YouTube */}
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Youtube className="h-5 w-5 text-red-500" />
                  Canal do YouTube
                </CardTitle>
                <CardDescription>
                  Selecione onde publicar no YouTube
                </CardDescription>
              </CardHeader>
              <CardContent>
                {loadingChannels ? (
                  <div className="flex items-center gap-2 text-muted-foreground">
                    <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-gray-900"></div>
                    Carregando canais...
                  </div>
                ) : youtubeChannels.length === 0 ? (
                  <Alert>
                    <Info className="h-4 w-4" />
                    <AlertDescription>
                      Nenhum canal YouTube configurado.
                    </AlertDescription>
                  </Alert>
                ) : (
                  <Select 
                    value={formData.canalId} 
                    onValueChange={v => setFormData(prev => ({ ...prev, canalId: v }))}
                  >
                    <SelectTrigger>
                      <SelectValue placeholder="Selecione um canal" />
                    </SelectTrigger>
                    <SelectContent>
                      {youtubeChannels.map(channel => (
                        <SelectItem key={channel.id} value={channel.id}>
                          <div className="flex items-center gap-2">
                            <Youtube className="h-4 w-4 text-red-500" />
                            {channel.nome}
                          </div>
                        </SelectItem>
                      ))}
                    </SelectContent>
                  </Select>
                )}
              </CardContent>
            </Card>

            {/* Canal TikTok */}
            {formData.socialNetworks.includes('tiktok') && (
              <Card>
                <CardHeader>
                  <CardTitle className="flex items-center gap-2">
                    <BsTiktok className="h-5 w-5 text-pink-500" />
                    Canal do TikTok
                  </CardTitle>
                  <CardDescription>
                    Selecione onde publicar no TikTok
                  </CardDescription>
                </CardHeader>
                <CardContent>
                  {loadingChannels ? (
                    <div className="flex items-center gap-2 text-muted-foreground">
                      <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-gray-900"></div>
                      Carregando canais TikTok...
                    </div>
                  ) : tikTokChannels.length === 0 ? (
                    <Alert>
                      <Info className="h-4 w-4" />
                      <AlertDescription>
                        Nenhum canal TikTok configurado.
                      </AlertDescription>
                    </Alert>
                  ) : (
                    <Select 
                      value={formData.canalTikTokId} 
                      onValueChange={v => setFormData(prev => ({ ...prev, canalTikTokId: v }))}
                    >
                      <SelectTrigger>
                        <SelectValue placeholder="Selecione um canal TikTok" />
                      </SelectTrigger>
                      <SelectContent>
                        {tikTokChannels.map(channel => (
                          <SelectItem key={channel.id} value={channel.id}>
                            <div className="flex items-center gap-2">
                              <BsTiktok className="h-4 w-4 text-pink-500" />
                              {channel.nome}
                            </div>
                          </SelectItem>
                        ))}
                      </SelectContent>
                    </Select>
                  )}
                </CardContent>
              </Card>
            )}
          </div>

          {/* Agendamento - Melhorado */}
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <Calendar className="h-5 w-5" />
                Agendamento
              </CardTitle>
              <CardDescription>
                Defina quando seu post será publicado
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-6">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                  <Label htmlFor="date" className="text-base font-medium">
                    Data de Publicação *
                  </Label>
                  <Input
                    id="date"
                    type="date"
                    value={formData.scheduledDate}
                    onChange={(e) => {
                      setFormData(prev => ({ ...prev, scheduledDate: e.target.value }));
                      setErrors(prev => ({ ...prev, scheduledDate: '' }));
                    }}
                    min={minDate}
                    required
                    className={`mt-1 ${errors.scheduledDate ? 'border-red-500' : ''}`}
                  />
                  {errors.scheduledDate && (
                    <p className="text-sm text-red-500 mt-1">{errors.scheduledDate}</p>
                  )}
                </div>
                
                <div>
                  <Label htmlFor="time" className="text-base font-medium">
                    Horário *
                  </Label>
                  <Input
                    id="time"
                    type="text"
                    inputMode="numeric"
                    pattern="^([01]\d|2[0-3]):([0-5]\d)$"
                    placeholder="14:30"
                    value={formData.scheduledTime}
                    onChange={(e) => {
                      setFormData(prev => ({ ...prev, scheduledTime: e.target.value }));
                      setErrors(prev => ({ ...prev, scheduledTime: '' }));
                    }}
                    required
                    className={`mt-1 ${errors.scheduledTime ? 'border-red-500' : ''}`}
                  />
                  {errors.scheduledTime && (
                    <p className="text-sm text-red-500 mt-1">{errors.scheduledTime}</p>
                  )}
                </div>
              </div>
              
              <Alert className="border-blue-200 bg-blue-50">
                <Clock className="h-4 w-4 text-blue-600" />
                <AlertDescription className="text-blue-800">
                  Horário baseado no fuso horário GMT-3 (Brasília). 
                  Recomendamos publicar entre 18h-21h para melhor engajamento.
                </AlertDescription>
              </Alert>
            </CardContent>
          </Card>

          {/* Botões de Ação - Melhorados */}
          <div className="flex flex-col sm:flex-row gap-4">
            <Button
              type="submit"
              disabled={isSubmitting || loadingChannels || channels.length === 0}
              size="lg"
              className="flex-1 bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700 text-white font-semibold py-3 h-auto transition-all duration-300 transform hover:scale-[1.02] disabled:hover:scale-100"
            >
              {isSubmitting ? (
                <div className="flex items-center gap-2">
                  <div className="animate-spin rounded-full h-5 w-5 border-2 border-white border-t-transparent" />
                  Agendando seu conteúdo...
                </div>
              ) : (
                <div className="flex items-center gap-2">
                  <Sparkles className="h-5 w-5" />
                  Agendar Publicação
                </div>
              )}
            </Button>

            <Button
              type="button"
              variant="outline"
              size="lg"
              onClick={() => navigate('/posts')}
              className="sm:w-auto w-full border-2 hover:bg-gray-50 font-medium py-3 h-auto"
            >
              <ArrowLeft className="mr-2 h-4 w-4" />
              Cancelar
            </Button>
          </div>

          {/* Resumo do Post - Novo */}
          {(formData.title || formData.socialNetworks.length > 0 || selectedFile) && (
            <Card className="border-2 border-dashed border-purple-200 bg-purple-50/30">
              <CardHeader>
                <CardTitle className="flex items-center gap-2 text-purple-700">
                  <Eye className="h-5 w-5" />
                  Resumo da Publicação
                </CardTitle>
                <CardDescription>
                  Confira como ficará seu post antes de agendar
                </CardDescription>
              </CardHeader>
              <CardContent>
                <div className="space-y-4">
                  {formData.title && (
                    <div>
                      <Label className="text-sm font-medium text-gray-600">Título</Label>
                      <p className="text-lg font-semibold mt-1">{formData.title}</p>
                    </div>
                  )}
                  
                  {formData.socialNetworks.length > 0 && (
                    <div>
                      <Label className="text-sm font-medium text-gray-600">Será publicado em</Label>
                      <div className="flex gap-2 mt-2">
                        {formData.socialNetworks.map(networkId => {
                          const network = socialNetworks.find(n => n.id === networkId);
                          const IconComponent = network?.icon;
                          return network ? (
                            <Badge key={networkId} variant="secondary" className="flex items-center gap-1">
                              {IconComponent && <IconComponent className={`h-3 w-3 ${network.color}`} />}
                              {network.name}
                            </Badge>
                          ) : null;
                        })}
                      </div>
                    </div>
                  )}
                  
                  {formData.scheduledDate && formData.scheduledTime && (
                    <div>
                      <Label className="text-sm font-medium text-gray-600">Agendado para</Label>
                      <p className="font-medium mt-1">
                        {new Date(`${formData.scheduledDate} ${formData.scheduledTime}`).toLocaleString('pt-BR', {
                          weekday: 'long',
                          year: 'numeric',
                          month: 'long',
                          day: 'numeric',
                          hour: '2-digit',
                          minute: '2-digit'
                        })}
                      </p>
                    </div>
                  )}
                  
                  {selectedFile && (
                    <div>
                      <Label className="text-sm font-medium text-gray-600">Arquivo</Label>
                      <div className="flex items-center gap-2 mt-1">
                        <FileVideo className="h-4 w-4 text-purple-600" />
                        <span className="text-sm">{selectedFile.name}</span>
                        <Badge variant="outline" className="text-xs">
                          {((selectedFile.size) / (1024 * 1024)).toFixed(1)} MB
                        </Badge>
                      </div>
                    </div>
                  )}
                </div>
              </CardContent>
            </Card>
          )}

          {/* Dicas de Otimização - Novo */}
          <Card className="bg-gradient-to-br from-blue-50 to-indigo-50 border-blue-200">
            <CardHeader>
              <CardTitle className="flex items-center gap-2 text-blue-700">
                <Info className="h-5 w-5" />
                Dicas para Melhor Desempenho
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
                <div className="space-y-2">
                  <div className="font-medium text-blue-700">📱 Para TikTok:</div>
                  <ul className="space-y-1 text-blue-600">
                    <li>• Vídeos verticais (9:16) funcionam melhor</li>
                    <li>• Use hashtags trending</li>
                    <li>• Publique entre 18h-21h</li>
                    <li>• Máximo 15-60 segundos</li>
                  </ul>
                </div>
                <div className="space-y-2">
                  <div className="font-medium text-blue-700">🎥 Para YouTube:</div>
                  <ul className="space-y-1 text-blue-600">
                    <li>• Thumbnails chamativas são essenciais</li>
                    <li>• Títulos com 60 caracteres</li>
                    <li>• Use palavras-chave relevantes</li>
                    <li>• Máximo 60 segundos para Shorts</li>
                  </ul>
                </div>
              </div>
            </CardContent>
          </Card>
        </form>

        {/* Footer com informações adicionais */}
        <div className="text-center text-sm text-muted-foreground pb-8">
          <p>
            Seus vídeos serão processados e publicados automaticamente no horário agendado.
            <br />
            Para dúvidas ou suporte, entre em contato conosco.
          </p>
        </div>
      </div>
    </Layout>
  );
}