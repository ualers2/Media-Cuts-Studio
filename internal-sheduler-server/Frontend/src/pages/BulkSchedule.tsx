import React, { useState, useEffect } from 'react'
import {
  Card, CardHeader, CardTitle, CardDescription, CardContent
} from '@/components/ui/card'
import { Tabs, TabsList, TabsTrigger, TabsContent } from '@/components/ui/tabs'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Table, TableHeader, TableRow, TableHead, TableBody, TableCell } from '@/components/ui/table'
import { Progress } from '@/components/ui/progress'
import { Alert, AlertDescription } from '@/components/ui/alert'
import {
  Upload,
  FileText,
  Play,
  CheckCircle,
  Clock,
  AlertCircle,
  Youtube
} from 'lucide-react'
import { BsTiktok } from 'react-icons/bs'
import { toast } from '@/hooks/use-toast'
import axios from 'axios'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'

interface BulkPostData {
  visibility?: string
  category_id?: string
  filename: string
  title: string
  description: string
  tags: string
  // schedule_time continua existindo para manter compatibilidade com o backend
  schedule_time: string
  // novos campos de UI para facilitar edição/colagem de horários
  schedule_date?: string // 'YYYY-MM-DD'
  schedule_clock?: string // 'HH:MM'
  social_networks: string[]
  status: 'pending' | 'uploading' | 'uploaded' | 'processing' | 'success' | 'error'
  error?: string
  localUrl?: string
}

interface Channel {
  id: string;
  nome: string;
  socialNetwork: 'youtube' | 'tiktok';
}

export default function BulkSchedule() {
  const apiUrl = import.meta.env.VITE_BACKEND_URL as string

  const [step, setStep] = useState(1)
  const [files, setFiles] = useState<File[]>([])
  const [jsonFile, setJsonFile] = useState<File | null>(null)
  const [bulkPosts, setBulkPosts] = useState<BulkPostData[]>([])
  const [uploading, setUploading] = useState(false)
  const [processing, setProcessing] = useState(false)
  const [processedCount, setProcessedCount] = useState(0)
  const [formData, setFormData] = useState({
    canalId: '',
    canalTikTokId: '',
    visibility: 'public' as 'public' | 'private' | 'unlisted',

  })

  const [channels, setChannels] = useState<Channel[]>([])
  const [loadingChannels, setLoadingChannels] = useState(true)

  const BACKEND_URL = import.meta.env.VITE_BACKEND_URL

  const youtubeChannels = channels.filter(c => c.socialNetwork === 'youtube')
  const tikTokChannels = channels.filter(c => c.socialNetwork === 'tiktok')

  useEffect(() => {
    const fetchChannels = async () => {
      try {
        const response = await fetch(`${BACKEND_URL}/api/canais`)
        if (!response.ok) {
          throw new Error(`Erro ao carregar canais: ${response.statusText}`)
        }
        const data = await response.json()
        setChannels(data)
        setFormData(prev => ({
          ...prev,
          canalId: data.find((c: Channel) => c.socialNetwork === 'youtube')?.id || '',
          canalTikTokId: data.find((c: Channel) => c.socialNetwork === 'tiktok')?.id || ''
        }))
      } catch (error) {
        console.error("Falha ao carregar canais:", error)
        toast({
          title: "Erro",
          description: "Falha ao carregar a lista de canais. Verifique o backend.",
          variant: "destructive"
        })
      } finally {
        setLoadingChannels(false)
      }
    }
    fetchChannels()
  }, [])

  const handleFilesChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFiles(Array.from(e.target.files || []))
  }

  const uploadMediaBulk = async () => {
    if (!files.length) {
      toast({ title: 'Erro', description: 'Selecione ao menos um arquivo.', variant: 'destructive' })
      return
    }
    setUploading(true)
    const form = new FormData()
    files.forEach(f => form.append('files[]', f))
    try {
      await axios.post(`${apiUrl}/api/upload-media-bulk`, form, {
        headers: { 'Content-Type': 'multipart/form-data' },
        timeout: 3600 * 1000  // 1 hora em milissegundos
      })
      const initial = bulkPosts.map(p => ({ ...p, status: 'uploaded' }))
      setBulkPosts(initial)
      setStep(2)
    } catch (err: any) {
      toast({ title: 'Erro no upload', description: err.message, variant: 'destructive' })
    } finally {
      setUploading(false)
    }
  }

  // utilitário para normalizar horário (entrada livre) para HH:MM
  const pad = (s: string | number) => String(s).padStart(2, '0')
  const normalizeClock = (input: string) => {
    if (!input) return ''
    const cleaned = input.trim()
    // aceita formatos: H, H:M, HH:MM, H:MM
    const parts = cleaned.split(':')
    let hh = parts[0] || '00'
    let mm = parts[1] || '00'
    hh = hh.replace(/[^0-9]/g, '')
    mm = mm.replace(/[^0-9]/g, '')
    if (hh.length === 0) hh = '00'
    if (hh.length === 1) hh = '0' + hh
    if (mm.length === 1) mm = mm + '0'
    if (mm.length === 0) mm = '00'
    // validar limites básicos
    const hnum = Math.min(23, Math.max(0, parseInt(hh, 10) || 0))
    const mnum = Math.min(59, Math.max(0, parseInt(mm, 10) || 0))
    return `${pad(hnum)}:${pad(mnum)}`
  }

  const handleJsonChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const f = e.target.files?.[0]
    if (!f) return
    setJsonFile(f)
    const reader = new FileReader()
    reader.onload = ev => {
      try {
        const arr = JSON.parse(ev.target?.result as string)
        if (!Array.isArray(arr)) throw new Error('JSON deve ser um array')
        const posts: BulkPostData[] = arr.map((item: any) => {
          const schedule_time_raw = item.schedule_time || ''
          let schedule_date = ''
          let schedule_clock = ''
          // tenta extrair 'YYYY-MM-DD HH:MM(:SS)?' -> date + clock
          const m = String(schedule_time_raw).match(/^(\d{4}-\d{2}-\d{2})\s+(\d{1,2}:\d{1,2})(:\d{1,2})?$/)
          if (m) {
            schedule_date = m[1]
            schedule_clock = normalizeClock(m[2])
          }
          return ({
            visibility: item.visibility,
            category_id: item.category_id || '24',
            filename: item.filename,
            title: item.title || '',
            description: item.description || '',
            tags: item.tags || '',
            schedule_time: schedule_time_raw || '',
            schedule_date,
            schedule_clock,
            social_networks: item.social_networks || [],
            status: 'pending'
          })
        })
        setBulkPosts(posts)
      } catch (error: any) {
        toast({ title: 'Erro JSON', description: error.message, variant: 'destructive' })
      }
    }
    reader.readAsText(f)
  }

  const validateMapping = (): string[] => {
    const errs: string[] = []
    bulkPosts.forEach((p, i) => {
      if (!p.title?.trim()) errs.push(`Linha ${i + 1}: título obrigatório`)
      // agora validamos data e hora separadamente (favor colar no formato HH:MM no campo hora)
      if (!(p.schedule_date && p.schedule_date.trim())) errs.push(`Linha ${i + 1}: data de agendamento obrigatória`)
      if (!(p.schedule_clock && p.schedule_clock.trim())) errs.push(`Linha ${i + 1}: horário de agendamento obrigatório (formato HH:MM)`)      
      if (!p.social_networks.length) errs.push(`Linha ${i + 1}: selecione ao menos uma rede`)
      if (!files.find(f => f.name === p.filename)) errs.push(`Linha ${i + 1}: arquivo ${p.filename} não existe`)
    })
    return errs
  }

  const processBulkPosts = async () => {
    const errs = validateMapping()
    if (errs.length) {
      toast({ title: 'Erros de validação', description: errs.join('\n'), variant: 'destructive' })
      return
    }
    setProcessing(true)
    setProcessedCount(0)
    const payload = bulkPosts.map(p => {
      // se usuário editou data+hora no UI, montamos schedule_time no formato aceito pelo backend
      let schedule_time_final = p.schedule_time
      if (p.schedule_date && p.schedule_clock) {
        const clock = normalizeClock(p.schedule_clock)
        schedule_time_final = `${p.schedule_date} ${clock}:00`
      } else if (p.schedule_time) {
        // tenta garantir que esteja no formato 'YYYY-MM-DD HH:MM:SS'
        const m = String(p.schedule_time).match(/^(\d{4}-\d{2}-\d{2})\s+(\d{1,2}:\d{1,2})(:\d{1,2})?$/)
        if (m) {
          schedule_time_final = `${m[1]} ${normalizeClock(m[2])}:00`
        }
      }

      return ({
        ...p,
        visibility: formData.visibility,
        canal_id: formData.canalId,
        canal_id_tiktok: formData.canalTikTokId,
        category_id: p.category_id,
        filename: p.filename,
        description: p.description,
        tags: p.tags,
        schedule_time: schedule_time_final,
        social_networks: p.social_networks
      })
    })

    try {
      await axios.post(`${apiUrl}/api/process-bulk-posts`, payload)
      setStep(3)
    } catch (err: any) {
      toast({ title: 'Erro no agendamento', description: err.message, variant: 'destructive' })
    } finally {
      setProcessing(false)
    }
  }

  const getIcon = (status: BulkPostData['status']) => {
    switch (status) {
      case 'processing': return <Clock className="h-4 w-4 animate-spin" />
      case 'success': return <CheckCircle className="h-4 w-4 text-green-600" />
      case 'error': return <AlertCircle className="h-4 w-4 text-red-600" />
      default: return <Clock className="h-4 w-4 text-gray-400" />
    }
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold">Agendamento em Massa</h1>
        <p className="text-muted-foreground">Envie arquivos e JSON para agendar vários posts de uma vez.</p>
      </div>

      <Tabs value={step.toString()} className="w-full">
        <TabsList className="grid grid-cols-3 w-full">
          <TabsTrigger value="1">1. Upload</TabsTrigger>
          <TabsTrigger value="2" disabled={step < 2}>2. Mapeamento</TabsTrigger>
          <TabsTrigger value="3" disabled={step < 3}>3. Acompanhamento</TabsTrigger>
        </TabsList>

        <TabsContent value="1" className="space-y-6">
          <Card>
            <CardHeader>
              <CardTitle><Upload className="inline h-5 w-5" /> Arquivos</CardTitle>
              <CardDescription>Selecione vídeos/imagens</CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <Input type="file" multiple accept="image/*,video/*" onChange={handleFilesChange} />
              {files.length > 0 && <p>{files.length} arquivo(s) selecionado(s)</p>}
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle><FileText className="inline h-5 w-5" /> JSON de Metadados</CardTitle>
              <CardDescription>Formato: array de objetos</CardDescription>
            </CardHeader>
            <CardContent>
              <Input type="file" accept=".json" onChange={handleJsonChange} />
              {jsonFile && <p>Carregado: {jsonFile.name}</p>}
            </CardContent>
          </Card>

          {/* Canal YouTube */}
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <Youtube className="h-5 w-5" />
                Canal do YouTube
              </CardTitle>
              <CardDescription>
                Selecione o canal do YouTube onde o Short será publicado.
              </CardDescription>
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
                <Select
                  value={formData.canalId}
                  onValueChange={(value) => setFormData(prev => ({ ...prev, canalId: value }))}
                  required
                >
                  <SelectTrigger>
                    <SelectValue placeholder="Selecione um canal" />
                  </SelectTrigger>
                  <SelectContent>
                    {youtubeChannels.map((channel) => (
                      <SelectItem key={channel.id} value={channel.id}>
                        {channel.nome}
                      </SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              )}
            </CardContent>
          </Card>

          {/* Canal TikTok */}
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <BsTiktok className="h-5 w-5" />
                Canal do TikTok
              </CardTitle>
              <CardDescription>
                Selecione o canal do TikTok onde o Post será publicado.
              </CardDescription>
            </CardHeader>
            <CardContent>
              {loadingChannels ? (
                <p className="text-muted-foreground">Carregando canais TikTok...</p>
              ) : tikTokChannels.length === 0 ? (
                <Alert>
                  <AlertDescription>
                    Nenhum canal TikTok configurado. Adicione no backend.
                  </AlertDescription>
                </Alert>
              ) : (
                <Select
                  value={formData.canalTikTokId}
                  onValueChange={(value) => setFormData(prev => ({ ...prev, canalTikTokId: value }))}
                  required
                >
                  <SelectTrigger>
                    <SelectValue placeholder="Selecione um canal TikTok" />
                  </SelectTrigger>
                  <SelectContent>
                    {tikTokChannels.map((channel) => (
                      <SelectItem key={channel.id} value={channel.id}>
                        {channel.nome}
                      </SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              )}
            </CardContent>
          </Card>

          {/* Adicione o novo Card para Visibilidade aqui */}
          <Card>
            <CardHeader>
              <CardTitle>Visibilidade</CardTitle>
              <CardDescription>
                Selecione a visibilidade padrão para todos os posts.
              </CardDescription>
            </CardHeader>
            <CardContent>
              <Select
                value={formData.visibility}
                onValueChange={(value: 'public' | 'private' | 'unlisted') =>
                  setFormData(prev => ({ ...prev, visibility: value }))
                }
              >
                <SelectTrigger>
                  <SelectValue placeholder="Selecione a visibilidade" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="public">Público</SelectItem>
                  <SelectItem value="private">Privado</SelectItem>
                  <SelectItem value="unlisted">Não Listado</SelectItem>
                </SelectContent>
              </Select>
            </CardContent>
          </Card>

          <div className="flex justify-end gap-2">
            <Button variant="outline" disabled={uploading} onClick={() => {
              setFiles([]); setJsonFile(null); setBulkPosts([])
            }}>Limpar</Button>
            <Button onClick={uploadMediaBulk} disabled={uploading || !files.length || !jsonFile}>
              {uploading ? 'Enviando...' : 'Enviar e Continuar'}
            </Button>
          </div>
        </TabsContent>

        {/* Passo 2 */}
        <TabsContent value="2" className="space-y-6">
          <Card>
            <CardHeader>
              <CardTitle>Revisão de Posts</CardTitle>
              <CardDescription>Confira antes de agendar</CardDescription>
            </CardHeader>
            <CardContent>
              <Table>
                <TableHeader>
                  <TableRow>
                    <TableHead>Arquivo</TableHead><TableHead>Título</TableHead>
                    <TableHead>Data / Horário</TableHead><TableHead>Redes</TableHead><TableHead>Status</TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  {bulkPosts.map((p, i) => (
                    <TableRow key={i}>
                      <TableCell>{p.filename}</TableCell>
                      <TableCell>
                        <Input
                          value={p.title}
                          onChange={e => {
                            const arr = [...bulkPosts]
                            arr[i].title = e.target.value
                            setBulkPosts(arr)
                          }}
                        />
                      </TableCell>
                      <TableCell>
                        <div className="flex gap-2">
                          <Input
                            type="date"
                            value={p.schedule_date || (p.schedule_time ? p.schedule_time.slice(0, 10) : '')}
                            onChange={e => {
                              const arr = [...bulkPosts]
                              arr[i].schedule_date = e.target.value
                              // se já existir um horário digitado, montar schedule_time
                              if (arr[i].schedule_date && arr[i].schedule_clock) {
                                arr[i].schedule_time = `${arr[i].schedule_date} ${normalizeClock(arr[i].schedule_clock)}:00`
                              } else {
                                arr[i].schedule_time = ''
                              }
                              setBulkPosts(arr)
                            }}
                          />

                          <Input
                            type="text"
                            placeholder="HH:MM (cole aqui)"
                            value={p.schedule_clock || (p.schedule_time ? p.schedule_time.slice(11, 16) : '')}
                            onChange={e => {
                              const arr = [...bulkPosts]
                              arr[i].schedule_clock = e.target.value
                              // normalizar e montar schedule_time se data existir
                              if (arr[i].schedule_date && arr[i].schedule_clock) {
                                arr[i].schedule_time = `${arr[i].schedule_date} ${normalizeClock(arr[i].schedule_clock)}:00`
                              } else {
                                arr[i].schedule_time = ''
                              }
                              setBulkPosts(arr)
                            }}
                          />
                        </div>
                      </TableCell>
                      <TableCell>{p.social_networks.join(', ')}</TableCell>
                      <TableCell>{getIcon(p.status)}</TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </CardContent>
          </Card>
          <div className="flex justify-end gap-2">
            <Button variant="outline" onClick={() => setStep(1)}>Voltar</Button>
            <Button onClick={processBulkPosts} disabled={processing}>
              {processing ? 'Processando...' : <><Play className="h-4 w-4 mr-1" /> Agendar Tudo</>}
            </Button>
          </div>
        </TabsContent>

        {/* Passo 3 */}
        <TabsContent value="3" className="space-y-6">
          <Alert>
            <AlertCircle className="h-4 w-4" />
            <AlertDescription>
              Lote enviado para processamento assíncrono. Acompanhe o progresso abaixo.
            </AlertDescription>
          </Alert>
          <Card>
            <CardHeader>
              <CardTitle><Clock className="inline h-5 w-5" /> Progresso</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <Progress value={(processedCount / (bulkPosts.length || 1)) * 100} />
              {bulkPosts.map((p, i) => (
                <div key={i} className="flex items-center gap-2">
                  {getIcon(p.status)} <span>{p.title}</span>
                </div>
              ))}
            </CardContent>
          </Card>
          <div className="flex justify-end">
            <Button onClick={() => window.location.reload()}>Novo Lote</Button>
          </div>
        </TabsContent>
      </Tabs>
    </div>
  )
}
