import { useEffect, useMemo, useState } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Badge } from '@/components/ui/badge';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
// import { StatusBadge } from '@/components/ui/status-badge';


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
  Clock
} from 'lucide-react';
import { BsTiktok } from 'react-icons/bs';
import { useNavigate } from 'react-router-dom';
import { toast } from '@/hooks/use-toast';
const statusMap = {
  draft: { icon: Pencil, label: 'Rascunho', color: 'text-yellow-500' },
  scheduled: { icon: Clock, label: 'Agendado', color: 'text-blue-500' },
  published: { icon: Check, label: 'Publicado', color: 'text-green-500' },
  error: { icon: AlertTriangle, label: 'Erro', color: 'text-red-500' },
  canceled: { icon: AlertTriangle, label: 'Canceled', color: 'text-red-500' }
};

export function StatusBadge({ status }: { status: string }) {
  const data = statusMap[status];

  if (!data) {
    return <Badge className="text-gray-500">Desconhecido</Badge>;
  }

  const Icon = data.icon;

  return (
    <Badge className={data.color}>
      <Icon className="mr-1 h-4 w-4" />
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
  youtube: 'text-youtube',
  instagram: 'text-instagram',
  facebook: 'text-facebook',
  twitter: 'text-twitter',
  tiktok: 'text-pink-500'
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
  // Define a URL base do backend a partir das variáveis de ambiente do Vite
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
        
        // Normaliza socialNetworks como array
        const normalized = rawPosts.map((p: any) => ({
          ...p,
          socialNetworks: Array.isArray(p.socialNetworks)
            ? p.socialNetworks
            : // se vier string JSON, tenta parsear, senão retorna vazio
              (() => {
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
        // Pode adicionar uma chamada DELETE futura aqui
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

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-3xl font-bold tracking-tight">Lista de Posts</h2>
        <p className="text-muted-foreground">Gerencie todos os seus posts agendados e publicados</p>
      </div>

      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <Filter className="h-5 w-5" />
            Filtros e Busca
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
            <Input
              placeholder="Buscar posts..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
            />

            <Select value={statusFilter} onValueChange={setStatusFilter}>
              <SelectTrigger>
                <SelectValue placeholder="Status" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="all">Todos os Status</SelectItem>
                <SelectItem value="draft">Rascunho</SelectItem>
                <SelectItem value="scheduled">Agendado</SelectItem>
                <SelectItem value="published">Publicado</SelectItem>
                <SelectItem value="error">Erro</SelectItem>
              </SelectContent>
            </Select>

            <Select value={socialFilter} onValueChange={setSocialFilter}>
              <SelectTrigger>
                <SelectValue placeholder="Rede Social" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="all">Todas as Redes</SelectItem>
                <SelectItem value="youtube">YouTube</SelectItem>
                <SelectItem value="instagram">Instagram</SelectItem>
                <SelectItem value="facebook">Facebook</SelectItem>
                <SelectItem value="twitter">Twitter</SelectItem>
              </SelectContent>
            </Select>

            <Select
              value={`${sortBy}-${sortOrder}`}
              onValueChange={(value) => {
                const [field, order] = value.split('-');
                setSortBy(field);
                setSortOrder(order as 'asc' | 'desc');
              }}
            >
              <SelectTrigger>
                <SelectValue placeholder="Ordenar por" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="scheduledAt-desc">Data Agendada (Desc)</SelectItem>
                <SelectItem value="scheduledAt-asc">Data Agendada (Asc)</SelectItem>
                <SelectItem value="createdAt-desc">Criação (Desc)</SelectItem>
                <SelectItem value="createdAt-asc">Criação (Asc)</SelectItem>
                <SelectItem value="title-asc">Título (A-Z)</SelectItem>
                <SelectItem value="title-desc">Título (Z-A)</SelectItem>
                <SelectItem value="status-asc">Status</SelectItem>
              </SelectContent>
            </Select>
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <List className="h-5 w-5" />
            Posts ({posts.length})
          </CardTitle>
        </CardHeader>
        <CardContent>
          {loading ? (
            <p>Carregando posts...</p>
          ) : posts.length === 0 ? (
            <div className="text-center py-8">
              <p className="text-muted-foreground">Nenhum post encontrado com os filtros aplicados.</p>
              <Button onClick={() => navigate('/new-post')} className="mt-4">
                Criar Primeiro Post
              </Button>
            </div>
          ) : (
            <div className="rounded-md border">
              <Table>
                <TableHeader>
                  <TableRow>
                    <TableHead onClick={() => handleSort('title')} className="cursor-pointer">Título</TableHead>
                    <TableHead>Redes Sociais</TableHead>
                    <TableHead onClick={() => handleSort('scheduledAt')} className="cursor-pointer">Agendamento</TableHead>
                    <TableHead onClick={() => handleSort('status')} className="cursor-pointer">Status</TableHead>
                    <TableHead onClick={() => handleSort('createdAt')} className="cursor-pointer">Criado em</TableHead>
                    <TableHead>Ações</TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  {posts.map((post) => (
                    <TableRow key={post.id} className="hover:bg-muted/50">
                      <TableCell>
                        <p className="font-semibold">{post.title}</p>
                        <p className="text-sm text-muted-foreground truncate">{post.description}</p>
                        {(post.tags || []).length > 0 && (
                          <div className="flex gap-1 mt-1">
                            {post.tags.slice(0, 2).map((tag: string) => (
                              <Badge key={tag} variant="secondary" className="text-xs">{tag}</Badge>
                            ))}
                            {post.tags.length > 2 && (
                              <Badge variant="secondary" className="text-xs">+{post.tags.length - 2}</Badge>
                            )}
                          </div>
                        )}
                      </TableCell>
                      <TableCell>
                        <div className="flex gap-2">
                          {post.socialNetworks.map((network: string) => {
                            // Ícone e classe de cor de cada rede
                            const Icon = socialIcons[network as keyof typeof socialIcons] || List;
                            const colorClass = socialColors[network as keyof typeof socialColors] || 'text-gray-500';
                            return (
                              <Icon
                                key={network}
                                className={`h-4 w-4 ${colorClass}`}
                                title={network}
                              />
                            );
                          })}
                        </div>
                      </TableCell>
                      <TableCell>{formatDate(post.scheduledAt)}</TableCell>
                      <TableCell><StatusBadge status={post.status} /></TableCell>
                      <TableCell>{formatDate(post.createdAt)}</TableCell>
                      <TableCell>
                        <DropdownMenu>
                          <DropdownMenuTrigger asChild>
                            <Button variant="ghost" className="h-8 w-8 p-0">
                              <MoreHorizontal className="h-4 w-4" />
                            </Button>
                          </DropdownMenuTrigger>
                          <DropdownMenuContent align="end">
                            <DropdownMenuItem onClick={() => navigate(`/posts/${post.id}`)}>
                              <Eye className="mr-2 h-4 w-4" /> Visualizar
                            </DropdownMenuItem>
                            <DropdownMenuItem onClick={() => navigate(`/posts/${post.id}/edit`)}>
                              <Edit className="mr-2 h-4 w-4" /> Editar
                            </DropdownMenuItem>
                            <DropdownMenuItem onClick={() => handleDuplicatePost(post)}>
                              <Copy className="mr-2 h-4 w-4" /> Duplicar
                            </DropdownMenuItem>
                            {post.status === 'published' && (
                              <DropdownMenuItem>
                                <ExternalLink className="mr-2 h-4 w-4" /> Ver no YouTube
                              </DropdownMenuItem>
                            )}
                            <DropdownMenuItem onClick={() => handleDeletePost(post.id)} className="text-destructive">
                              <Trash2 className="mr-2 h-4 w-4" /> Excluir
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
  );
}
