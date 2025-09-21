// Front-end\postflow-forge\src\pages\NewPost.tsx
import { useState, useEffect } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Textarea } from '@/components/ui/textarea';
import { Checkbox } from '@/components/ui/checkbox';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { Alert, AlertDescription } from '@/components/ui/alert';
import { Upload, Calendar, Clock, CheckCircle, Youtube } from 'lucide-react';
import { usePost } from '@/contexts/PostContext';
import { useNavigate } from 'react-router-dom';
import { toast } from '@/hooks/use-toast';
import { BsTiktok } from 'react-icons/bs';

// Define a URL base do backend a partir das variáveis de ambiente do Vite
const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;

const socialNetworks = [
  { id: 'youtube', name: 'YouTube', color: 'text-youtube' },
  { id: 'tiktok', name: 'TikTok', color: 'text-pink-500' }, // <-- Novo
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
    socialNetworks: ['youtube', 'tiktok'] as string[],
    visibility: 'public' as 'public' | 'private' | 'unlisted',
    canalId: '',
    canalTikTokId: ''  // novo
  });

  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [previewUrl, setPreviewUrl] = useState<string | null>(null);
  const [channels, setChannels] = useState<Channel[]>([]);
  const [loadingChannels, setLoadingChannels] = useState(true);
  const youtubeChannels = channels.filter(c => c.socialNetwork === 'youtube');
  const tikTokChannels = channels.filter(c => c.socialNetwork === 'tiktok');
  const todayLocal = new Date();
  todayLocal.setMinutes(todayLocal.getMinutes() - todayLocal.getTimezoneOffset()); 
  const minDate = todayLocal.toISOString().split('T')[0];

  useEffect(() => {
    const fetchChannels = async () => {
      try {
        const response = await fetch(`${BACKEND_URL}/api/canais`);
        if (!response.ok) throw new Error(`Erro ao carregar canais: ${response.statusText}`);
        const data: Channel[] = await response.json();
        setChannels(data);
        // Predefine seleções iniciais
        const yt = data.find(c => c.socialNetwork === 'youtube');
        const tt = data.find(c => c.socialNetwork === 'tiktok');
        setFormData(prev => ({
          ...prev,
          canalId: yt?.id || '',
          canalTikTokId: tt?.id || 'nada'
        }));
      } catch (error) {
        console.error('Falha ao carregar canais:', error);
        toast({ title: 'Erro', description: 'Falha ao carregar canais. Verifique o backend.', variant: 'destructive' });
      } finally {
        setLoadingChannels(false);
      }
    };
    fetchChannels();
  }, []);

  const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      setSelectedFile(file);
      const url = URL.createObjectURL(file);
      setPreviewUrl(url);
    }
  };

  const handleSocialNetworkChange = (networkId: string, checked: boolean) => {
    setFormData(prev => {
      const current = new Set(prev.socialNetworks);
      if (checked) current.add(networkId);
      else current.delete(networkId);
      return { ...prev, socialNetworks: Array.from(current) };
    });
  };
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!formData.title.trim()) {
      toast({
        title: "Erro",
        description: "O título é obrigatório",
        variant: "destructive"
      });
      return;
    }

    if (!formData.scheduledDate || !formData.scheduledTime) {
      toast({
        title: "Erro",
        description: "Data e hora de agendamento são obrigatórias",
        variant: "destructive"
      });
      return;
    }

    if (!selectedFile) {
      toast({
        title: "Erro",
        description: "Por favor, selecione um arquivo de vídeo para o Short.",
        variant: "destructive"
      });
      return;
    }

    // if (!formData.canalId) {
    //   toast({
    //     title: "Erro",
    //     description: "Por favor, selecione um canal do YouTube.",
    //     variant: "destructive"
    //   });
    //   return;
    // }

    setIsSubmitting(true);

    try {
      const scheduledAtISO = `${formData.scheduledDate} ${formData.scheduledTime}:00`;

      const postFormData = new FormData();
      postFormData.append('video_file', selectedFile);
      postFormData.append('title', formData.title);
      postFormData.append('description', formData.description);
      postFormData.append('video_tags', formData.tags);
      postFormData.append('scheduled_publish_at', scheduledAtISO);
      postFormData.append('privacy_status', formData.visibility);
      // postFormData.append('canal_id', formData.canalId);
      postFormData.append('ia_gen_title', 'false');
      postFormData.append('category_id', '22');
      postFormData.append('socialNetworks', JSON.stringify(formData.socialNetworks));
      console.log(`socialNetworks ${formData.socialNetworks}`)
      postFormData.append('canal_id', formData.canalId);
      postFormData.append('canal_id_tiktok', formData.canalTikTokId);
      console.log(`canalId ${formData.canalId}`)
      console.log(`canal_id_tiktok ${formData.canalTikTokId}`)
      // Usa a URL do backend configurada
      const response = await fetch(`${BACKEND_URL}/api/posts/agendar`, {
        method: 'POST',
        body: postFormData,
      });

      const responseData = await response.json();

      if (!response.ok) {
        throw new Error(responseData.error || 'Falha ao agendar o Short');
      }

      // // Adicione o post ao contexto (se ainda estiver usando para gerenciamento local)
      // addPost({
      //   id: responseData.short_id || 'nada',
      //   title: formData.title,
      //   description: formData.description,
      //   tags: formData.tags.split(',').map(tag => tag.trim()).filter(Boolean),
      //   scheduledAt: scheduledAtISO,
      //   socialNetworks: formData.socialNetworks,
      //   status: responseData.status || 'pendente', // ou outro valor default aceito por StatusBadge
      //   visibility: formData.visibility,
      //   media: selectedFile ? {
      //     filename: selectedFile.name,
      //     type: selectedFile.type.startsWith('video/') ? 'video' : 'image',
      //     url: previewUrl || ''
      //   } : undefined
      // });

      toast({
        title: "Sucesso!",
        description: "Short agendado com sucesso para o YouTube!",
      });

      navigate('/posts');
    } catch (error: any) {
      console.error("Erro ao agendar o Short:", error);
      toast({
        title: "Erro",
        description: error.message || "Falha ao agendar o Short. Tente novamente.",
        variant: "destructive"
      });
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="max-w-2xl mx-auto space-y-6">
      <div>
        <h2 className="text-3xl font-bold tracking-tight">Novo Post </h2>
        <p className="text-muted-foreground">
          Crie e agende um novo Shorts ou Tiktok para o seu canal.
        </p>
      </div>

      <form onSubmit={handleSubmit} className="space-y-6">
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Upload className="h-5 w-5" />
              Mídia
            </CardTitle>
            <CardDescription>
              Faça upload do arquivo de vídeo para o seu Shorts ou Tiktok.
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <Input
                type="file"
                accept="video/*"
                onChange={handleFileSelect}
                className="cursor-pointer"
                required
              />
              {previewUrl && (
                <div className="mt-4">
                  {selectedFile?.type.startsWith('video/') ? (
                    <video src={previewUrl} controls className="max-w-full h-48 rounded-lg" />
                  ) : (
                    <img src={previewUrl} alt="Preview" className="max-w-full h-48 object-cover rounded-lg" />
                  )}
                  <p className="text-sm text-muted-foreground mt-2">
                    {selectedFile?.name} ({(selectedFile?.size || 0 / (1024 * 1024)).toFixed(2)} MB)
                  </p>
                </div>
              )}
              {selectedFile && !selectedFile.type.startsWith('video/') && (
                <Alert variant="destructive">
                  <AlertDescription>
                    O arquivo selecionado não é um vídeo. Por favor, selecione um arquivo de vídeo.
                  </AlertDescription>
                </Alert>
              )}
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Detalhes do Post</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div>
              <Label htmlFor="title">Título *</Label>
              <Input
                id="title"
                value={formData.title}
                onChange={(e) => setFormData(prev => ({ ...prev, title: e.target.value }))}
                placeholder="Título do seu Post"
                required
              />
            </div>

            <div>
              <Label htmlFor="description">Descrição</Label>
              <Textarea
                id="description"
                value={formData.description}
                onChange={(e) => setFormData(prev => ({ ...prev, description: e.target.value }))}
                placeholder="Descrição do seu Post"
                rows={4}
              />
            </div>

            <div>
              <Label htmlFor="tags">Tags</Label>
              <Input
                id="tags"
                value={formData.tags}
                onChange={(e) => setFormData(prev => ({ ...prev, tags: e.target.value }))}
                placeholder="tag1, tag2, tag3"
              />
              <p className="text-sm text-muted-foreground mt-1">
                Separe as tags com vírgulas
              </p>
            </div>

            <div>
              <Label htmlFor="visibility">Visibilidade</Label>
              <Select value={formData.visibility} onValueChange={(value: any) =>
                setFormData(prev => ({ ...prev, visibility: value }))
              }>
                <SelectTrigger>
                  <SelectValue placeholder="Selecione a visibilidade" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="public">Público</SelectItem>
                  <SelectItem value="private">Privado</SelectItem>
                  <SelectItem value="unlisted">Não Listado</SelectItem>
                </SelectContent>
              </Select>
            </div>
          </CardContent>
        </Card>


        {/* Canal YouTube */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2"><Youtube className="h-5 w-5" /> Canal do YouTube</CardTitle>
            <CardDescription>Selecione o canal do YouTube onde o Post será publicado.</CardDescription>
          </CardHeader>
          <CardContent>
            {loadingChannels ? (
              <p className="text-muted-foreground">Carregando canais...</p>
            ) : youtubeChannels.length === 0 ? (
              <Alert>
                <AlertDescription>
                  Nenhum canal do YouTube configurado. Por favor, adicione um canal no backend.
                </AlertDescription>
              </Alert>
            ) : (
              <Select value={formData.canalId} onValueChange={v => setFormData(prev => ({ ...prev, canalId: v }))} required>
                <SelectTrigger><SelectValue placeholder="Selecione um canal YouTube" /></SelectTrigger>
                <SelectContent>
                  {youtubeChannels.map(channel => (
                    <SelectItem key={channel.id} value={channel.id}>{channel.nome}</SelectItem>
                  ))}
                </SelectContent>
              </Select>
            )}
          </CardContent>
        </Card>



        {/* Canal TikTok - filtrado e condicional */}
        {formData.socialNetworks.includes('tiktok') && (
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2"><BsTiktok className="h-5 w-5" /> Canal do TikTok</CardTitle>
              <CardDescription>Selecione o canal do Tiktok onde o Post será publicado.</CardDescription>
            </CardHeader>
            <CardContent>
              {loadingChannels ? (
                <p className="text-muted-foreground">Carregando canais TikTok...</p>
              ) : (
                (() => {
                  if (!tikTokChannels.length) {
                    return (
                      <Alert>
                        <AlertDescription>
                          Nenhum canal TikTok configurado. Adicione no backend.
                        </AlertDescription>
                      </Alert>
                    );
                  }
                  return (
                    <Select value={formData.canalTikTokId} onValueChange={v => setFormData(prev => ({ ...prev, canalTikTokId: v }))} required>
                      <SelectTrigger><SelectValue placeholder="Selecione um canal TikTok" /></SelectTrigger>
                      <SelectContent>
                        {tikTokChannels.map(ch => <SelectItem key={ch.id} value={ch.id}>{ch.nome}</SelectItem>)}
                      </SelectContent>
                    </Select>
                  );
                })()
              )}
            </CardContent>
          </Card>
        )}

        <Card>
          <CardHeader>
            <CardTitle>Redes Sociais</CardTitle>
            <CardDescription>
              Selecione onde você deseja publicar este post .
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-2 gap-4">
              {socialNetworks.map((network) => (
                <div key={network.id} className="flex items-center space-x-2">
                  <Checkbox
                    id={network.id}
                    checked={formData.socialNetworks.includes(network.id)}
                    onCheckedChange={(checked) =>
                      handleSocialNetworkChange(network.id, checked as boolean)
                    }
                    // disabled={network.id !== 'youtube'}
                  />
                  <Label
                    htmlFor={network.id}
                    className={`font-medium ${network.color}`}
                  >
                    {network.name}
                  </Label>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Calendar className="h-5 w-5" />
              Agendamento
            </CardTitle>
            <CardDescription>
              Selecione A data e hora da publicação este post.
            </CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="grid grid-cols-2 gap-4">
              <div>
                <Label htmlFor="date">Data *</Label>
                <Input
                  id="date"
                  type="date"
                  value={formData.scheduledDate}
                  onChange={(e) => setFormData(prev => ({ ...prev, scheduledDate: e.target.value }))}
                  min={minDate}
                  required
                />
              </div>
              <div>
                <Label htmlFor="time">Hora *</Label>
                  <Input
                    id="time"
                    type="text"
                    inputMode="numeric"
                    pattern="^([01]\d|2[0-3]):([0-5]\d)$"
                    placeholder="HH:MM"
                    value={formData.scheduledTime}
                    onChange={(e) => setFormData(prev => ({ ...prev, scheduledTime: e.target.value }))}
                    required
                  />
              </div>
            </div>
            <Alert>
              <Clock className="h-4 w-4" />
              <AlertDescription>
                Horário baseado no fuso horário GMT-3 (Brasília)
              </AlertDescription>
            </Alert>
          </CardContent>
        </Card>

        <div className="flex gap-4">
          <Button
            type="submit"
            disabled={isSubmitting || loadingChannels || channels.length === 0}
            className="flex-1"
          >
            {isSubmitting ? (
              <>
                <Clock className="mr-2 h-4 w-4 animate-spin" />
                Agendando...
              </>
            ) : (
              <>
                <CheckCircle className="mr-2 h-4 w-4" />
                Agendar Post
              </>
            )}
          </Button>

          <Button
            type="button"
            variant="ghost"
            onClick={() => navigate('/posts')}
          >
            Cancelar
          </Button>
        </div>
      </form>
    </div>
  );
}