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
  Youtube,
  Calendar,
  Eye,
  Settings,
  RefreshCw,
  FileVideo,
  Image as ImageIcon,
  Sparkles,
  Zap
} from 'lucide-react'
import { BsTiktok } from 'react-icons/bs'
import { toast } from '@/hooks/use-toast'
import axios from 'axios'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'
import Layout from '@/components/Layout';
import LoaderOverlay from "@/components/LoaderOverlay"

interface BulkPostData {
  visibility?: string
  category_id?: string
  filename: string
  title: string
  description: string
  tags: string
  token_id: string
  batch_id: string
  schedule_time: string
  schedule_date?: string
  schedule_clock?: string
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

  const BACKEND_URL = import.meta.env.VITE_BACKEND_URL
  const VITE_BULK_BACKEND_URL = import.meta.env.VITE_BULK_BACKEND_URL


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
      const res = await axios.post(`${VITE_BULK_BACKEND_URL}/api/upload-media-bulk`, form, {
        headers: { 'Content-Type': 'multipart/form-data' },
        timeout: 3600 * 1000
      })

      const filesMap: Array<any> = res.data.files || []

      const updatedPosts = bulkPosts.map(p => {
        const match = filesMap.find(f => f.original_filename === p.filename || f.safe_filename === p.filename)
        if (match) {
          return { ...p, status: 'uploaded', batch_id: match.batch_id, token_id: match.token_id, original_filename: match.original_filename }
        }
        return { ...p }
      })

      setBulkPosts(updatedPosts)
      setStep(2)
    } catch (err: any) {
      toast({ title: 'Erro no upload', description: err?.message || 'Erro desconhecido', variant: 'destructive' })
    } finally {
      setUploading(false)
    }
  }

  const pad = (s: string | number) => String(s).padStart(2, '0')
  const normalizeClock = (input: string) => {
    if (!input) return ''
    const cleaned = input.trim()
    const parts = cleaned.split(':')
    let hh = parts[0] || '00'
    let mm = parts[1] || '00'
    hh = hh.replace(/[^0-9]/g, '')
    mm = mm.replace(/[^0-9]/g, '')
    if (hh.length === 0) hh = '00'
    if (hh.length === 1) hh = '0' + hh
    if (mm.length === 1) mm = mm + '0'
    if (mm.length === 0) mm = '00'
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
      if (!(p.schedule_date && p.schedule_date.trim())) errs.push(`Linha ${i + 1}: data de agendamento obrigatória`)
      if (!(p.schedule_clock && p.schedule_clock.trim())) errs.push(`Linha ${i + 1}: horário de agendamento obrigatório (formato HH:MM)`)      
      if (!p.social_networks.length) errs.push(`Linha ${i + 1}: selecione ao menos uma rede`)
      if (!p.token_id) errs.push(`Linha ${i + 1}: arquivo ${p.filename} não foi enviado corretamente (token_id faltando)`)
      if (!p.batch_id) errs.push(`Linha ${i + 1}: arquivo ${p.filename} não foi enviado corretamente (batch_id faltando)`)
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
      let schedule_time_final = p.schedule_time
      if (p.schedule_date && p.schedule_clock) {
        const clock = normalizeClock(p.schedule_clock)
        schedule_time_final = `${p.schedule_date} ${clock}:00`
      } else if (p.schedule_time) {
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
        token_id: p.token_id,
        batch_id: p.batch_id,
        filename: p.filename,
        description: p.description,
        tags: p.tags,
        schedule_time: schedule_time_final,
        social_networks: p.social_networks
      })
    })

    try {
      await axios.post(`${BACKEND_URL}/api/process-bulk-posts`, payload)

      const updated = bulkPosts.map(p => ({ ...p, status: 'success' }))
      setBulkPosts(updated)
      setProcessedCount(updated.length)
      setStep(3)
    } catch (err: any) {
      toast({ title: 'Erro no agendamento', description: err.message, variant: 'destructive' })
    } finally {
      setProcessing(false)
    }
  }

  const getIcon = (status: BulkPostData['status']) => {
    switch (status) {
      case 'processing': return <Clock className="h-4 w-4 animate-spin text-blue-500" />
      case 'success': return <CheckCircle className="h-4 w-4 text-green-500" />
      case 'error': return <AlertCircle className="h-4 w-4 text-red-500" />
      default: return <Clock className="h-4 w-4 text-gray-400" />
    }
  }

  const getFileIcon = (filename: string) => {
    const ext = filename.split('.').pop()?.toLowerCase()
    return ['mp4', 'avi', 'mov', 'wmv', 'flv', 'webm'].includes(ext || '') 
      ? <FileVideo className="h-4 w-4 text-blue-500" />
      : <ImageIcon className="h-4 w-4 text-green-500" />
  }

  return (
    <Layout>
      <div className="min-h-screen bg-gradient-to-br from-slate-50 via-white to-blue-50">
        {uploading && (
          <LoaderOverlay message="Aguarde enquanto todos seus vídeos estão sendo upados..." />
        )}
        {processing && (
          <LoaderOverlay message="Aguarde enquanto todos os seus vídeos estão sendo agendados..." />
        )}

        <div className="max-w-6xl mx-auto p-6 space-y-8">
          {/* Header Section */}
          <div className="text-center space-y-4">
            <div className="inline-flex items-center justify-center w-16 h-16 bg-gradient-to-r from-blue-500 to-purple-600 rounded-2xl shadow-lg mb-4">
              <Sparkles className="h-8 w-8 text-white" />
            </div>
            <h1 className="text-4xl font-bold bg-gradient-to-r from-gray-900 to-gray-600 bg-clip-text text-transparent">
              Agendamento em Massa
            </h1>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Otimize seu workflow enviando múltiplos arquivos e configurações de uma só vez
            </p>
          </div>

          {/* Progress Steps */}
          <div className="flex justify-center">
            <div className="flex items-center space-x-4">
              {[1, 2, 3].map((s) => (
                <div key={s} className="flex items-center">
                  <div className={`
                    flex items-center justify-center w-10 h-10 rounded-full border-2 transition-all duration-300
                    ${step >= s 
                      ? 'bg-blue-500 border-blue-500 text-white shadow-lg' 
                      : 'border-gray-300 text-gray-400 bg-white'
                    }
                  `}>
                    {s}
                  </div>
                  {s < 3 && (
                    <div className={`w-16 h-0.5 mx-2 transition-colors duration-300 ${
                      step > s ? 'bg-blue-500' : 'bg-gray-300'
                    }`} />
                  )}
                </div>
              ))}
            </div>
          </div>

          <Tabs value={step.toString()} className="w-full">
            <TabsList className="grid grid-cols-3 w-full max-w-md mx-auto h-12 bg-white border border-gray-200 rounded-xl shadow-sm">
              <TabsTrigger value="1" className="rounded-lg data-[state=active]:bg-blue-500 data-[state=active]:text-white">
                <Upload className="h-4 w-4 mr-2" />
                Upload
              </TabsTrigger>
              <TabsTrigger value="2" disabled={step < 2} className="rounded-lg data-[state=active]:bg-blue-500 data-[state=active]:text-white">
                <Settings className="h-4 w-4 mr-2" />
                Configurar
              </TabsTrigger>
              <TabsTrigger value="3" disabled={step < 3} className="rounded-lg data-[state=active]:bg-blue-500 data-[state=active]:text-white">
                <Zap className="h-4 w-4 mr-2" />
                Resultado
              </TabsTrigger>
            </TabsList>

            <TabsContent value="1" className="space-y-6 mt-8">
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                {/* Files Upload */}
                <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm hover:shadow-xl transition-all duration-300">
                  <CardHeader className="pb-4">
                    <CardTitle className="flex items-center space-x-3">
                      <div className="p-2 bg-blue-100 rounded-lg">
                        <Upload className="h-5 w-5 text-blue-600" />
                      </div>
                      <span>Arquivos de Mídia</span>
                    </CardTitle>
                    <CardDescription className="text-gray-600">
                      Selecione vídeos ou imagens para upload
                    </CardDescription>
                  </CardHeader>
                  <CardContent className="space-y-4">
                    <div className="relative">
                      <Input 
                        type="file" 
                        multiple 
                        accept="image/*,video/*" 
                        onChange={handleFilesChange}
                        className="h-12 border-dashed border-2 border-gray-300 hover:border-blue-400 focus:border-blue-500 transition-colors"
                      />
                    </div>
                    {files.length > 0 && (
                      <div className="bg-blue-50 p-4 rounded-lg border border-blue-200">
                        <div className="flex items-center space-x-2 text-blue-700">
                          <CheckCircle className="h-4 w-4" />
                          <span className="font-medium">{files.length} arquivo(s) selecionado(s)</span>
                        </div>
                        <div className="mt-2 space-y-1">
                          {files.slice(0, 3).map((file, i) => (
                            <div key={i} className="flex items-center space-x-2 text-sm text-blue-600">
                              {getFileIcon(file.name)}
                              <span>{file.name}</span>
                            </div>
                          ))}
                          {files.length > 3 && (
                            <span className="text-xs text-blue-500">... e mais {files.length - 3} arquivo(s)</span>
                          )}
                        </div>
                      </div>
                    )}
                  </CardContent>
                </Card>

                {/* JSON Upload */}
                <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm hover:shadow-xl transition-all duration-300">
                  <CardHeader className="pb-4">
                    <CardTitle className="flex items-center space-x-3">
                      <div className="p-2 bg-green-100 rounded-lg">
                        <FileText className="h-5 w-5 text-green-600" />
                      </div>
                      <span>Configuração JSON</span>
                    </CardTitle>
                    <CardDescription className="text-gray-600">
                      Arquivo JSON com metadados dos posts
                    </CardDescription>
                  </CardHeader>
                  <CardContent>
                    <div className="relative">
                      <Input 
                        type="file" 
                        accept=".json" 
                        onChange={handleJsonChange}
                        className="h-12 border-dashed border-2 border-gray-300 hover:border-green-400 focus:border-green-500 transition-colors"
                      />
                    </div>
                    {jsonFile && (
                      <div className="mt-4 bg-green-50 p-4 rounded-lg border border-green-200">
                        <div className="flex items-center space-x-2 text-green-700">
                          <CheckCircle className="h-4 w-4" />
                          <span className="font-medium">Carregado: {jsonFile.name}</span>
                        </div>
                        <div className="mt-2 text-sm text-green-600">
                          {bulkPosts.length} post(s) configurado(s)
                        </div>
                      </div>
                    )}
                  </CardContent>
                </Card>
              </div>

              {/* Channel Configuration */}
              <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                {/* YouTube Channel */}
                <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm hover:shadow-xl transition-all duration-300">
                  <CardHeader className="pb-4">
                    <CardTitle className="flex items-center space-x-3">
                      <div className="p-2 bg-red-100 rounded-lg">
                        <Youtube className="h-5 w-5 text-red-600" />
                      </div>
                      <span>YouTube</span>
                    </CardTitle>
                    <CardDescription>Canal para publicação</CardDescription>
                  </CardHeader>
                  <CardContent>
                    {loadingChannels ? (
                      <div className="flex items-center space-x-2 text-gray-500">
                        <RefreshCw className="h-4 w-4 animate-spin" />
                        <span>Carregando...</span>
                      </div>
                    ) : youtubeChannels.length === 0 ? (
                      <Alert className="border-orange-200 bg-orange-50">
                        <AlertCircle className="h-4 w-4 text-orange-500" />
                        <AlertDescription className="text-orange-700">
                          Nenhum canal configurado
                        </AlertDescription>
                      </Alert>
                    ) : (
                      <Select
                        value={formData.canalId}
                        onValueChange={(value) => setFormData(prev => ({ ...prev, canalId: value }))}
                      >
                        <SelectTrigger className="h-12">
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

                {/* TikTok Channel */}
                <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm hover:shadow-xl transition-all duration-300">
                  <CardHeader className="pb-4">
                    <CardTitle className="flex items-center space-x-3">
                      <div className="p-2 bg-gray-100 rounded-lg">
                        <BsTiktok className="h-5 w-5 text-gray-800" />
                      </div>
                      <span>TikTok</span>
                    </CardTitle>
                    <CardDescription>Canal para publicação</CardDescription>
                  </CardHeader>
                  <CardContent>
                    {loadingChannels ? (
                      <div className="flex items-center space-x-2 text-gray-500">
                        <RefreshCw className="h-4 w-4 animate-spin" />
                        <span>Carregando...</span>
                      </div>
                    ) : tikTokChannels.length === 0 ? (
                      <Alert className="border-orange-200 bg-orange-50">
                        <AlertCircle className="h-4 w-4 text-orange-500" />
                        <AlertDescription className="text-orange-700">
                          Nenhum canal configurado
                        </AlertDescription>
                      </Alert>
                    ) : (
                      <Select
                        value={formData.canalTikTokId}
                        onValueChange={(value) => setFormData(prev => ({ ...prev, canalTikTokId: value }))}
                      >
                        <SelectTrigger className="h-12">
                          <SelectValue placeholder="Selecione um canal" />
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

                {/* Visibility */}
                <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm hover:shadow-xl transition-all duration-300">
                  <CardHeader className="pb-4">
                    <CardTitle className="flex items-center space-x-3">
                      <div className="p-2 bg-purple-100 rounded-lg">
                        <Eye className="h-5 w-5 text-purple-600" />
                      </div>
                      <span>Visibilidade</span>
                    </CardTitle>
                    <CardDescription>Configuração padrão</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <Select
                      value={formData.visibility}
                      onValueChange={(value: 'public' | 'private' | 'unlisted') =>
                        setFormData(prev => ({ ...prev, visibility: value }))
                      }
                    >
                      <SelectTrigger className="h-12">
                        <SelectValue />
                      </SelectTrigger>
                      <SelectContent>
                        <SelectItem value="public">🌐 Público</SelectItem>
                        <SelectItem value="private">🔒 Privado</SelectItem>
                        <SelectItem value="unlisted">👁️ Não Listado</SelectItem>
                      </SelectContent>
                    </Select>
                  </CardContent>
                </Card>
              </div>

              <div className="flex justify-center space-x-4 pt-6">
                <Button 
                  variant="outline" 
                  disabled={uploading} 
                  onClick={() => {
                    setFiles([]); setJsonFile(null); setBulkPosts([])
                  }}
                  className="h-12 px-6"
                >
                  <RefreshCw className="h-4 w-4 mr-2" />
                  Limpar
                </Button>
                <Button 
                  onClick={uploadMediaBulk} 
                  disabled={uploading || !files.length || !jsonFile}
                  className="h-12 px-8 bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 shadow-lg"
                >
                  {uploading ? (
                    <>
                      <RefreshCw className="h-4 w-4 mr-2 animate-spin" />
                      Enviando...
                    </>
                  ) : (
                    <>
                      <Upload className="h-4 w-4 mr-2" />
                      Enviar e Continuar
                    </>
                  )}
                </Button>
              </div>
            </TabsContent>

            <TabsContent value="2" className="space-y-6 mt-8">
              <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm">
                <CardHeader>
                  <CardTitle className="flex items-center space-x-3">
                    <div className="p-2 bg-blue-100 rounded-lg">
                      <Settings className="h-5 w-5 text-blue-600" />
                    </div>
                    <span>Revisão e Configuração</span>
                  </CardTitle>
                  <CardDescription>
                    Revise e ajuste os dados antes do agendamento
                  </CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="overflow-x-auto">
                    <Table>
                      <TableHeader>
                        <TableRow>
                          <TableHead className="w-48">Arquivo</TableHead>
                          <TableHead className="min-w-64">Título</TableHead>
                          <TableHead className="w-80">Agendamento</TableHead>
                          <TableHead className="w-32">Redes</TableHead>
                          <TableHead className="w-20">Status</TableHead>
                        </TableRow>
                      </TableHeader>
                      <TableBody>
                        {bulkPosts.map((p, i) => (
                          <TableRow key={i} className="hover:bg-gray-50/50">
                            <TableCell>
                              <div className="flex items-center space-x-2">
                                {getFileIcon(p.filename)}
                                <span className="truncate max-w-36" title={p.filename}>
                                  {p.filename}
                                </span>
                              </div>
                            </TableCell>
                            <TableCell>
                              <Input
                                value={p.title}
                                onChange={e => {
                                  const arr = [...bulkPosts]
                                  arr[i].title = e.target.value
                                  setBulkPosts(arr)
                                }}
                                className="min-w-60"
                                placeholder="Digite o título..."
                              />
                            </TableCell>
                            <TableCell>
                              <div className="flex space-x-2">
                                <div className="relative">
                                  <Calendar className="absolute left-3 top-1/2 transform -translate-y-1/2 h-4 w-4 text-gray-400" />
                                  <Input
                                    type="date"
                                    value={p.schedule_date || (p.schedule_time ? p.schedule_time.slice(0, 10) : '')}
                                    onChange={e => {
                                      const arr = [...bulkPosts]
                                      arr[i].schedule_date = e.target.value
                                      if (arr[i].schedule_date && arr[i].schedule_clock) {
                                        arr[i].schedule_time = `${arr[i].schedule_date} ${normalizeClock(arr[i].schedule_clock)}:00`
                                      } else {
                                        arr[i].schedule_time = ''
                                      }
                                      setBulkPosts(arr)
                                    }}
                                    className="pl-10 w-36"
                                  />
                                </div>
                                <div className="relative">
                                  <Clock className="absolute left-3 top-1/2 transform -translate-y-1/2 h-4 w-4 text-gray-400" />
                                  <Input
                                    type="text"
                                    placeholder="HH:MM"
                                    value={p.schedule_clock || (p.schedule_time ? p.schedule_time.slice(11, 16) : '')}
                                    onChange={e => {
                                      const arr = [...bulkPosts]
                                      arr[i].schedule_clock = e.target.value
                                      if (arr[i].schedule_date && arr[i].schedule_clock) {
                                        arr[i].schedule_time = `${arr[i].schedule_date} ${normalizeClock(arr[i].schedule_clock)}:00`
                                      } else {
                                        arr[i].schedule_time = ''
                                      }
                                      setBulkPosts(arr)
                                    }}
                                    className="pl-10 w-24"
                                  />
                                </div>
                              </div>
                            </TableCell>
                            <TableCell>
                              <div className="flex flex-wrap gap-1">
                                {p.social_networks.map(network => (
                                  <span key={network} className="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-blue-100 text-blue-800">
                                    {network}
                                  </span>
                                ))}
                              </div>
                            </TableCell>
                            <TableCell>
                              <div className="flex justify-center">
                                {getIcon(p.status)}
                              </div>
                            </TableCell>
                          </TableRow>
                        ))}
                      </TableBody>
                    </Table>
                  </div>
                </CardContent>
              </Card>
              
              <div className="flex justify-center space-x-4 pt-6">
                <Button 
                  variant="outline" 
                  onClick={() => setStep(1)}
                  className="h-12 px-6"
                >
                  ← Voltar
                </Button>
                <Button 
                  onClick={processBulkPosts} 
                  disabled={processing}
                  className="h-12 px-8 bg-gradient-to-r from-green-500 to-blue-600 hover:from-green-600 hover:to-blue-700 shadow-lg"
                >
                  {processing ? (
                    <>
                      <RefreshCw className="h-4 w-4 mr-2 animate-spin" />
                      Processando...
                    </>
                  ) : (
                    <>
                      <Play className="h-4 w-4 mr-2" />
                      Agendar Todos ({bulkPosts.length})
                    </>
                  )}
                </Button>
              </div>
            </TabsContent>

            <TabsContent value="3" className="space-y-6 mt-8">
              <div className="text-center space-y-6">
                <div className="inline-flex items-center justify-center w-24 h-24 bg-gradient-to-r from-green-400 to-blue-500 rounded-full shadow-lg animate-pulse">
                  <CheckCircle className="h-12 w-12 text-white" />
                </div>
                
                <Alert className="max-w-2xl mx-auto border-green-200 bg-gradient-to-r from-green-50 to-blue-50">
                  <CheckCircle className="h-5 w-5 text-green-600" />
                  <AlertDescription className="text-lg text-green-800 font-medium">
                    🎉 Todos os agendamentos foram concluídos com sucesso!
                  </AlertDescription>
                </Alert>
              </div>

              <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm max-w-4xl mx-auto">
                <CardHeader>
                  <CardTitle className="flex items-center space-x-3 justify-center">
                    <div className="p-2 bg-green-100 rounded-lg">
                      <Zap className="h-5 w-5 text-green-600" />
                    </div>
                    <span>Progresso Final</span>
                  </CardTitle>
                </CardHeader>
                <CardContent className="space-y-6">
                  <div className="space-y-3">
                    <div className="flex justify-between text-sm text-gray-600">
                      <span>Progresso</span>
                      <span>{processedCount}/{bulkPosts.length}</span>
                    </div>
                    <Progress 
                      value={(processedCount / (bulkPosts.length || 1)) * 100} 
                      className="h-3 rounded-full"
                    />
                  </div>
                  
                  <div className="grid gap-3 max-h-96 overflow-y-auto">
                    {bulkPosts.map((p, i) => (
                      <div key={i} className="flex items-center justify-between p-4 bg-gray-50/50 rounded-lg border border-gray-200/50 hover:bg-gray-100/50 transition-colors">
                        <div className="flex items-center space-x-3">
                          {getIcon(p.status)}
                          <div className="flex items-center space-x-2">
                            {getFileIcon(p.filename)}
                            <span className="font-medium text-gray-900">{p.title}</span>
                          </div>
                        </div>
                        <div className="flex items-center space-x-2">
                          {p.social_networks.map(network => (
                            <span key={network} className="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-blue-100 text-blue-700">
                              {network}
                            </span>
                          ))}
                        </div>
                      </div>
                    ))}
                  </div>
                </CardContent>
              </Card>
              
              <div className="flex justify-center pt-6">
                <Button 
                  onClick={() => window.location.reload()}
                  className="h-12 px-8 bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 shadow-lg"
                >
                  <Sparkles className="h-4 w-4 mr-2" />
                  Novo Lote
                </Button>
              </div>
            </TabsContent>
          </Tabs>
        </div>
      </div>
    </Layout>
  )
}