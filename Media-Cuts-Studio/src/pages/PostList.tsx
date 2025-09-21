import { useEffect, useMemo, useState } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Badge } from '@/components/ui/badge';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow
} from '@/components/ui/table';
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu';
import {
  Search,
  Filter,
  MoreHorizontal,
  Edit,
  Eye,
  Copy,
  Trash2,
  ExternalLink,
  Youtube,
  Instagram,
  Facebook,
  Twitter,
  List,
  Pencil,
  AlertTriangle,
  Check,
  Clock,
  Plus,
  ChevronUp,
  ChevronDown,
  Calendar,
  Users,
  TrendingUp,
  FileText,
  Settings,
  Loader2
} from 'lucide-react';
import { BsTiktok } from 'react-icons/bs';
import { useNavigate } from 'react-router-dom';
import { toast } from '@/hooks/use-toast';
import Layout from '@/components/Layout';

const statusMap = {
  draft: { icon: Pencil, label: 'Rascunho', color: 'bg-yellow-100 text-yellow-800 border-yellow-200', dotColor: 'bg-yellow-500' },
  scheduled: { icon: Clock, label: 'Agendado', color: 'bg-blue-100 text-blue-800 border-blue-200', dotColor: 'bg-blue-500' },
  published: { icon: Check, label: 'Publicado', color: 'bg-green-100 text-green-800 border-green-200', dotColor: 'bg-green-500' },
  error: { icon: AlertTriangle, label: 'Erro', color: 'bg-red-100 text-red-800 border-red-200', dotColor: 'bg-red-500' },
  canceled: { icon: AlertTriangle, label: 'Cancelado', color: 'bg-gray-100 text-gray-800 border-gray-200', dotColor: 'bg-gray-500' }
};

export function StatusBadge({ status }: { status: string }) {
  const data = statusMap[status];

  if (!data) {
    return (
      <Badge variant="outline" className="bg-gray-50 text-gray-600 border-gray-200">
        <span className="w-2 h-2 bg-gray-400 rounded-full mr-2"></span>
        Desconhecido
      </Badge>
    );
  }

  const Icon = data.icon;

  return (
    <Badge variant="outline" className={`${data.color} font-medium`}>
      <span className={`w-2 h-2 ${data.dotColor} rounded-full mr-2`}></span>
      {data.label}
    </Badge>
  );
}

const socialIcons = {
  youtube: Youtube,
  instagram: Instagram,
  facebook: Facebook,
  twitter: Twitter,
  tiktok: BsTiktok
};

const socialColors = {
  youtube: 'text-red-600 bg-red-50',
  instagram: 'text-pink-600 bg-pink-50',
  facebook: 'text-blue-600 bg-blue-50',
  twitter: 'text-sky-600 bg-sky-50',
  tiktok: 'text-pink-600 bg-pink-50'
};

const socialNames = {
  youtube: 'YouTube',
  instagram: 'Instagram',
  facebook: 'Facebook',
  twitter: 'Twitter',
  tiktok: 'TikTok'
};

export default function PostList() {
  const navigate = useNavigate();

  const [posts, setPosts] = useState<any[]>([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [statusFilter, setStatusFilter] = useState<string>('all');
  const [socialFilter, setSocialFilter] = useState<string>('all');
  const [sortBy, setSortBy] = useState<string>('scheduledAt');
  const [sortOrder, setSortOrder] = useState<'asc' | 'desc'>('desc');
  const [loading, setLoading] = useState(false);
  const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;

  useEffect(() => {
    const fetchPosts = async () => {
      setLoading(true);
      try {
        const params = new URLSearchParams({
          searchQuery,
          status: statusFilter,
          socialNetwork: socialFilter,
          sortBy,
          sortOrder,
          page: '1',
          limit: '1500',
        });
        const res = await fetch(`${BACKEND_URL}/api/posts?${params}`);
        const { posts: rawPosts = [] } = await res.json();
        
        const normalized = rawPosts.map((p: any) => ({
          ...p,
          socialNetworks: Array.isArray(p.socialNetworks)
            ? p.socialNetworks
            : (() => {
                try { return JSON.parse(p.socialNetworks); }
                catch { return []; }
              })()
        }));
        
        setPosts(normalized);
      } catch (err) {
        console.error('Erro ao buscar posts:', err);
        toast({ title: 'Erro', description: 'Não foi possível carregar os posts.' });
      } finally {
        setLoading(false);
      }
    };
    fetchPosts();
  }, [searchQuery, statusFilter, socialFilter, sortBy, sortOrder]);

  const handleSort = (field: string) => {
    if (sortBy === field) {
      setSortOrder(sortOrder === 'asc' ? 'desc' : 'asc');
    } else {
      setSortBy(field);
      setSortOrder('asc');
    }
  };

  const handleDeletePost = async (postId: string) => {
    if (confirm('Tem certeza que deseja excluir este post?')) {
      try {
        toast({ title: 'Simulação de exclusão', description: 'Excluir implementado no futuro.' });
      } catch (error) {
        toast({ title: 'Erro', description: 'Não foi possível excluir o post.' });
      }
    }
  };

  const handleDuplicatePost = (post: any) => {
    navigate('/new-post', {
      state: {
        duplicate: {
          title: `${post.title} (Cópia)`,
          description: post.description,
          tags: (post.tags || []).join(', '),
          socialNetworks: post.socialNetworks,
          visibility: post.visibility || 'public'
        }
      }
    });
  };

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleString('pt-BR');
  };

  const getSortIcon = (field: string) => {
    if (sortBy !== field) return null;
    return sortOrder === 'asc' ? <ChevronUp className="h-4 w-4" /> : <ChevronDown className="h-4 w-4" />;
  };

  // Estatísticas básicas
  const stats = useMemo(() => {
    const total = posts.length;
    const published = posts.filter(p => p.status === 'published').length;
    const scheduled = posts.filter(p => p.status === 'scheduled').length;
    const drafts = posts.filter(p => p.status === 'draft').length;
    
    return { total, published, scheduled, drafts };
  }, [posts]);

  return (
    <Layout>
      <div className="space-y-8">
        {/* Header com ação principal */}
        <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
          <div>
            <h1 className="text-4xl font-bold tracking-tight bg-gradient-to-r from-gray-900 to-gray-600 bg-clip-text text-transparent">
              Gerenciador de Posts
            </h1>
            <p className="text-lg text-muted-foreground mt-2">
              Organize, agende e publique conteúdo em múltiplas plataformas
            </p>
          </div>
          <Button 
            onClick={() => navigate('/new-post')} 
            size="lg"
            className="bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800 shadow-lg hover:shadow-xl transition-all duration-200"
          >
            <Plus className="h-5 w-5 mr-2" />
            Novo Post
          </Button>
        </div>

        {/* Cards de estatísticas */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <Card className="bg-gradient-to-br from-blue-50 to-blue-100 border-blue-200">
            <CardContent className="p-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-blue-600 text-sm font-medium">Total de Posts</p>
                  <p className="text-3xl font-bold text-blue-900">{stats.total}</p>
                </div>
                <FileText className="h-8 w-8 text-blue-600" />
              </div>
            </CardContent>
          </Card>
          
          <Card className="bg-gradient-to-br from-green-50 to-green-100 border-green-200">
            <CardContent className="p-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-green-600 text-sm font-medium">Publicados</p>
                  <p className="text-3xl font-bold text-green-900">{stats.published}</p>
                </div>
                <TrendingUp className="h-8 w-8 text-green-600" />
              </div>
            </CardContent>
          </Card>
          
          <Card className="bg-gradient-to-br from-orange-50 to-orange-100 border-orange-200">
            <CardContent className="p-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-orange-600 text-sm font-medium">Agendados</p>
                  <p className="text-3xl font-bold text-orange-900">{stats.scheduled}</p>
                </div>
                <Calendar className="h-8 w-8 text-orange-600" />
              </div>
            </CardContent>
          </Card>
          
          <Card className="bg-gradient-to-br from-purple-50 to-purple-100 border-purple-200">
            <CardContent className="p-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-purple-600 text-sm font-medium">Rascunhos</p>
                  <p className="text-3xl font-bold text-purple-900">{stats.drafts}</p>
                </div>
                <Pencil className="h-8 w-8 text-purple-600" />
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Filtros e Busca */}
        <Card className="shadow-lg border-0 bg-white">
          <CardHeader className="bg-gradient-to-r from-gray-50 to-gray-100 border-b">
            <CardTitle className="flex items-center gap-3 text-xl">
              <div className="p-2 bg-blue-100 rounded-lg">
                <Filter className="h-5 w-5 text-blue-600" />
              </div>
              Filtros e Pesquisa
            </CardTitle>
            <CardDescription>Use os filtros abaixo para encontrar posts específicos</CardDescription>
          </CardHeader>
          <CardContent className="p-6">
            <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
              <div className="lg:col-span-1">
                <label className="text-sm font-medium text-gray-700 mb-2 block">Buscar</label>
                <div className="relative">
                  <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 h-4 w-4 text-gray-400" />
                  <Input
                    placeholder="Digite título, descrição..."
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                    className="pl-10 h-11 border-gray-300 focus:border-blue-500 focus:ring-blue-500"
                  />
                </div>
              </div>

              <div>
                <label className="text-sm font-medium text-gray-700 mb-2 block">Status</label>
                <Select value={statusFilter} onValueChange={setStatusFilter}>
                  <SelectTrigger className="h-11 border-gray-300 focus:border-blue-500 focus:ring-blue-500">
                    <SelectValue placeholder="Filtrar por status" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="all">📋 Todos os Status</SelectItem>
                    <SelectItem value="draft">✏️ Rascunho</SelectItem>
                    <SelectItem value="scheduled">⏰ Agendado</SelectItem>
                    <SelectItem value="published">✅ Publicado</SelectItem>
                    <SelectItem value="error">⚠️ Erro</SelectItem>
                  </SelectContent>
                </Select>
              </div>

              <div>
                <label className="text-sm font-medium text-gray-700 mb-2 block">Rede Social</label>
                <Select value={socialFilter} onValueChange={setSocialFilter}>
                  <SelectTrigger className="h-11 border-gray-300 focus:border-blue-500 focus:ring-blue-500">
                    <SelectValue placeholder="Filtrar por rede" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="all">🌐 Todas as Redes</SelectItem>
                    <SelectItem value="youtube">🎥 YouTube</SelectItem>
                    <SelectItem value="instagram">📸 Instagram</SelectItem>
                    <SelectItem value="facebook">👥 Facebook</SelectItem>
                    <SelectItem value="twitter">🐦 Twitter</SelectItem>
                  </SelectContent>
                </Select>
              </div>

              <div>
                <label className="text-sm font-medium text-gray-700 mb-2 block">Ordenação</label>
                <Select
                  value={`${sortBy}-${sortOrder}`}
                  onValueChange={(value) => {
                    const [field, order] = value.split('-');
                    setSortBy(field);
                    setSortOrder(order as 'asc' | 'desc');
                  }}
                >
                  <SelectTrigger className="h-11 border-gray-300 focus:border-blue-500 focus:ring-blue-500">
                    <SelectValue placeholder="Ordenar por" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="scheduledAt-desc">📅 Data Agendada (↓)</SelectItem>
                    <SelectItem value="scheduledAt-asc">📅 Data Agendada (↑)</SelectItem>
                    <SelectItem value="createdAt-desc">🗓️ Criação (↓)</SelectItem>
                    <SelectItem value="createdAt-asc">🗓️ Criação (↑)</SelectItem>
                    <SelectItem value="title-asc">📝 Título (A-Z)</SelectItem>
                    <SelectItem value="title-desc">📝 Título (Z-A)</SelectItem>
                    <SelectItem value="status-asc">📊 Status</SelectItem>
                  </SelectContent>
                </Select>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Lista de Posts */}
        <Card className="shadow-lg border-0 bg-white">
          <CardHeader className="bg-gradient-to-r from-gray-50 to-gray-100 border-b">
            <div className="flex items-center justify-between">
              <CardTitle className="flex items-center gap-3 text-xl">
                <div className="p-2 bg-green-100 rounded-lg">
                  <List className="h-5 w-5 text-green-600" />
                </div>
                Posts Cadastrados
                <Badge variant="outline" className="bg-blue-50 text-blue-700 border-blue-200 ml-2">
                  {posts.length} {posts.length === 1 ? 'item' : 'itens'}
                </Badge>
              </CardTitle>
            </div>
          </CardHeader>
          <CardContent className="p-0">
            {loading ? (
              <div className="flex items-center justify-center py-16">
                <div className="text-center space-y-4">
                  <Loader2 className="h-8 w-8 animate-spin text-blue-600 mx-auto" />
                  <p className="text-gray-600 font-medium">Carregando posts...</p>
                </div>
              </div>
            ) : posts.length === 0 ? (
              <div className="text-center py-16 space-y-6">
                <div className="mx-auto w-16 h-16 bg-gray-100 rounded-full flex items-center justify-center">
                  <FileText className="h-8 w-8 text-gray-400" />
                </div>
                <div className="space-y-2">
                  <h3 className="text-xl font-semibold text-gray-900">Nenhum post encontrado</h3>
                  <p className="text-gray-500 max-w-md mx-auto">
                    {searchQuery || statusFilter !== 'all' || socialFilter !== 'all'
                      ? 'Tente ajustar os filtros ou criar um novo post.'
                      : 'Comece criando seu primeiro post para gerenciar seu conteúdo.'
                    }
                  </p>
                </div>
                <Button 
                  onClick={() => navigate('/new-post')} 
                  size="lg"
                  className="bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800"
                >
                  <Plus className="h-5 w-5 mr-2" />
                  Criar Primeiro Post
                </Button>
              </div>
            ) : (
              <div className="overflow-x-auto">
                <Table>
                  <TableHeader>
                    <TableRow className="bg-gray-50 border-b-2">
                      <TableHead 
                        onClick={() => handleSort('title')} 
                        className="cursor-pointer hover:bg-gray-100 transition-colors font-semibold text-gray-700 py-4"
                      >
                        <div className="flex items-center gap-2">
                          📝 Título {getSortIcon('title')}
                        </div>
                      </TableHead>
                      <TableHead className="font-semibold text-gray-700 py-4">🌐 Redes Sociais</TableHead>
                      <TableHead 
                        onClick={() => handleSort('scheduledAt')} 
                        className="cursor-pointer hover:bg-gray-100 transition-colors font-semibold text-gray-700 py-4"
                      >
                        <div className="flex items-center gap-2">
                          📅 Agendamento {getSortIcon('scheduledAt')}
                        </div>
                      </TableHead>
                      <TableHead 
                        onClick={() => handleSort('status')} 
                        className="cursor-pointer hover:bg-gray-100 transition-colors font-semibold text-gray-700 py-4"
                      >
                        <div className="flex items-center gap-2">
                          📊 Status {getSortIcon('status')}
                        </div>
                      </TableHead>
                      <TableHead 
                        onClick={() => handleSort('createdAt')} 
                        className="cursor-pointer hover:bg-gray-100 transition-colors font-semibold text-gray-700 py-4"
                      >
                        <div className="flex items-center gap-2">
                          🗓️ Criado em {getSortIcon('createdAt')}
                        </div>
                      </TableHead>
                      <TableHead className="font-semibold text-gray-700 py-4 text-center">⚙️ Ações</TableHead>
                    </TableRow>
                  </TableHeader>
                  <TableBody>
                    {posts.map((post, index) => (
                      <TableRow 
                        key={post.id} 
                        className="hover:bg-blue-50/50 transition-all duration-200 group border-b"
                      >
                        <TableCell className="py-6">
                          <div className="space-y-2">
                            <h3 className="font-semibold text-gray-900 text-lg leading-snug group-hover:text-blue-900 transition-colors">
                              {post.title}
                            </h3>
                            <p className="text-gray-600 text-sm leading-relaxed line-clamp-2">
                              {post.description}
                            </p>
                            {(post.tags || []).length > 0 && (
                              <div className="flex flex-wrap gap-2 mt-3">
                                {post.tags.slice(0, 3).map((tag: string) => (
                                  <Badge 
                                    key={tag} 
                                    variant="secondary" 
                                    className="text-xs bg-gray-100 text-gray-700 hover:bg-gray-200 transition-colors"
                                  >
                                    #{tag}
                                  </Badge>
                                ))}
                                {post.tags.length > 3 && (
                                  <Badge variant="secondary" className="text-xs bg-blue-100 text-blue-700">
                                    +{post.tags.length - 3} tags
                                  </Badge>
                                )}
                              </div>
                            )}
                          </div>
                        </TableCell>
                        <TableCell className="py-6">
                          <div className="flex flex-wrap gap-2">
                            {post.socialNetworks.map((network: string) => {
                              const Icon = socialIcons[network as keyof typeof socialIcons] || List;
                              const colorClass = socialColors[network as keyof typeof socialColors] || 'text-gray-600 bg-gray-100';
                              const name = socialNames[network as keyof typeof socialNames] || network;
                              
                              return (
                                <div
                                  key={network}
                                  className={`flex items-center gap-2 px-3 py-2 rounded-full ${colorClass} font-medium text-sm transition-all hover:scale-105`}
                                  title={name}
                                >
                                  <Icon className="h-4 w-4" />
                                  <span className="hidden sm:inline">{name}</span>
                                </div>
                              );
                            })}
                          </div>
                        </TableCell>
                        <TableCell className="py-6">
                          <div className="space-y-1">
                            <div className="font-medium text-gray-900">
                              {formatDate(post.scheduledAt)}
                            </div>
                          </div>
                        </TableCell>
                        <TableCell className="py-6">
                          <StatusBadge status={post.status} />
                        </TableCell>
                        <TableCell className="py-6">
                          <div className="text-gray-600 text-sm">
                            {formatDate(post.createdAt)}
                          </div>
                        </TableCell>
                        <TableCell className="py-6">
                          <DropdownMenu>
                            <DropdownMenuTrigger asChild>
                              <Button 
                                variant="ghost" 
                                className="h-10 w-10 p-0 rounded-full hover:bg-blue-100 transition-all duration-200 group-hover:bg-blue-100"
                              >
                                <MoreHorizontal className="h-5 w-5 text-gray-600" />
                              </Button>
                            </DropdownMenuTrigger>
                            <DropdownMenuContent align="end" className="w-56">
                              <DropdownMenuItem 
                                onClick={() => navigate(`/posts/${post.id}`)}
                                className="cursor-pointer"
                              >
                                <Eye className="mr-3 h-4 w-4 text-blue-600" />
                                <span className="font-medium">Visualizar</span>
                              </DropdownMenuItem>
                              <DropdownMenuItem 
                                onClick={() => navigate(`/posts/${post.id}/edit`)}
                                className="cursor-pointer"
                              >
                                <Edit className="mr-3 h-4 w-4 text-green-600" />
                                <span className="font-medium">Editar</span>
                              </DropdownMenuItem>
                              <DropdownMenuItem 
                                onClick={() => handleDuplicatePost(post)}
                                className="cursor-pointer"
                              >
                                <Copy className="mr-3 h-4 w-4 text-purple-600" />
                                <span className="font-medium">Duplicar</span>
                              </DropdownMenuItem>
                              {post.status === 'published' && (
                                <DropdownMenuItem className="cursor-pointer">
                                  <ExternalLink className="mr-3 h-4 w-4 text-orange-600" />
                                  <span className="font-medium">Ver no YouTube</span>
                                </DropdownMenuItem>
                              )}
                              <DropdownMenuItem 
                                onClick={() => handleDeletePost(post.id)} 
                                className="text-red-600 hover:text-red-700 hover:bg-red-50 cursor-pointer"
                              >
                                <Trash2 className="mr-3 h-4 w-4" />
                                <span className="font-medium">Excluir</span>
                              </DropdownMenuItem>
                            </DropdownMenuContent>
                          </DropdownMenu>
                        </TableCell>
                      </TableRow>
                    ))}
                  </TableBody>
                </Table>
              </div>
            )}
          </CardContent>
        </Card>
      </div>
    </Layout>
  );
}