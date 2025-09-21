// Front-end/postflow-forge/src/pages/Calendar.tsx
import { useState, useMemo, useEffect } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { StatusBadge } from '@/components/ui/status-badge';
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from '@/components/ui/dialog';

import {
  ChevronLeft,
  ChevronRight,
  Calendar as CalendarIcon,
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
import { usePost } from '@/contexts/PostContext';
import { useNavigate } from 'react-router-dom';

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

const monthNames = [
  'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
  'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
];

const weekDays = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb'];

export default function Calendar() {
  const { posts, fetchPosts, getPostsForDate } = usePost(); // Importar fetchPosts
  const navigate = useNavigate();

  const [currentDate, setCurrentDate] = useState(new Date());
  const [selectedDate, setSelectedDate] = useState<Date | null>(null);
  const [statusFilter, setStatusFilter] = useState<string>('all');
  const [socialFilter, setSocialFilter] = useState<string>('all');
  const [viewMode, setViewMode] = useState<'month' | 'week'>('month'); // viewMode está no estado mas não está sendo usado para renderização
  const [channelFilter, setChannelFilter] = useState<string>('all');

  useEffect(() => {
    fetchPosts({ page: 1, limit: 1500 });
  }, [fetchPosts]);

  const filteredPosts = useMemo(() => {
    let filtered = posts;

    if (statusFilter !== 'all') {
      filtered = filtered.filter(post => post.status === statusFilter);
    }

    if (socialFilter !== 'all') {
      filtered = filtered.filter(post =>
        post.socialNetworks.includes(socialFilter)
      );
    }

    if (channelFilter !== 'all') {
      filtered = filtered.filter(post => 
        post.canal_id === channelFilter || post.canal_id_tiktok === channelFilter
      );
    }

    return filtered;
  }, [posts, statusFilter, socialFilter, channelFilter]);

  const getDaysInMonth = (date: Date) => {
    const year = date.getFullYear();
    const month = date.getMonth();
    const firstDay = new Date(year, month, 1);
    const lastDay = new Date(year, month + 1, 0);
    const daysInMonth = lastDay.getDate();
    const startingDayOfWeek = firstDay.getDay();

    const days = [];

    // Previous month's days
    for (let i = startingDayOfWeek - 1; i >= 0; i--) {
      const day = new Date(year, month, -i);
      days.push({
        date: day,
        isCurrentMonth: false,
        // Usar filteredPosts para obter os posts do dia
        posts: filteredPosts.filter(post => new Date(post.scheduledAt).toDateString() === day.toDateString())
      });
    }

    // Current month's days
    for (let i = 1; i <= daysInMonth; i++) {
      const day = new Date(year, month, i);
      days.push({
        date: day,
        isCurrentMonth: true,
        // Usar filteredPosts para obter os posts do dia
        posts: filteredPosts.filter(post => new Date(post.scheduledAt).toDateString() === day.toDateString())
      });
    }

    // Next month's days to complete the grid
    const remainingDays = 42 - days.length;
    for (let i = 1; i <= remainingDays; i++) {
      const day = new Date(year, month + 1, i);
      days.push({
        date: day,
        isCurrentMonth: false,
        // Usar filteredPosts para obter os posts do dia
        posts: filteredPosts.filter(post => new Date(post.scheduledAt).toDateString() === day.toDateString())
      });
    }

    return days;
  };

  const navigateMonth = (direction: 'prev' | 'next') => {
    setCurrentDate(prev => {
      const newDate = new Date(prev);
      if (direction === 'prev') {
        newDate.setMonth(newDate.getMonth() - 1);
      } else {
        newDate.setMonth(newDate.getMonth() + 1);
      }
      return newDate;
    });
  };

  const isToday = (date: Date) => {
    const today = new Date();
    return date.toDateString() === today.toDateString();
  };

  const isSelected = (date: Date) => {
    return selectedDate && date.toDateString() === selectedDate.toDateString();
  };

  const getPostsForDay = (date: Date) => {
    return filteredPosts.filter(post => {
      const postDate = new Date(post.scheduledAt);
      return postDate.toDateString() === date.toDateString();
    });
  };

  const formatTime = (dateString: string) => {
    return new Date(dateString).toLocaleTimeString('pt-BR', {
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  const days = getDaysInMonth(currentDate);
  const selectedDatePosts = selectedDate ? getPostsForDay(selectedDate) : [];


  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-3xl font-bold tracking-tight">Calendário</h2>
        <p className="text-muted-foreground">
          Visualize seus posts agendados em formato de calendário
        </p>
      </div>

      {/* Filters and Controls */}
      <div className="flex flex-wrap gap-4 items-center justify-between">
        <div className="flex gap-4">
          <Select value={statusFilter} onValueChange={setStatusFilter}>
            <SelectTrigger className="w-[180px]">
              <SelectValue placeholder="Filtrar por status" />
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
            <SelectTrigger className="w-[180px]">
              <SelectValue placeholder="Filtrar por rede" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="all">Todas as Redes</SelectItem>
              <SelectItem value="youtube">YouTube</SelectItem>
              <SelectItem value="instagram">Instagram</SelectItem>
              <SelectItem value="facebook">Facebook</SelectItem>
              <SelectItem value="twitter">Twitter</SelectItem>
            </SelectContent>
          </Select>

          <Select value={channelFilter} onValueChange={setChannelFilter}>
            <SelectTrigger className="w-[180px]">
              <SelectValue placeholder="Filtrar por canal" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="all">Todos os Canais</SelectItem>
              {Array.from(
                new Set(
                  posts.flatMap(post => [post.canal_id, post.canal_id_tiktok].filter(Boolean))
                )
              ).map(channel => (
                <SelectItem key={channel} value={channel}>
                  {channel}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>

        </div>

        {/* <div className="flex gap-2">
          <Button
            variant={viewMode === 'month' ? 'default' : 'outline'}
            onClick={() => setViewMode('month')}
          >
            Mês
          </Button>
          <Button
            variant={viewMode === 'week' ? 'default' : 'outline'}
            onClick={() => setViewMode('week')}
          >
            Semana
          </Button>
        </div> */}
      </div>

      {/* Calendar */}
      <Card>
        <CardHeader>
          <div className="flex items-center justify-between">
            <CardTitle className="flex items-center gap-2">
              <CalendarIcon className="h-5 w-5" />
              {monthNames[currentDate.getMonth()]} {currentDate.getFullYear()}
            </CardTitle>
            <div className="flex items-center gap-2">
              <Button
                variant="outline"
                size="sm"
                onClick={() => navigateMonth('prev')}
              >
                <ChevronLeft className="h-4 w-4" />
              </Button>
              <Button
                variant="outline"
                size="sm"
                onClick={() => setCurrentDate(new Date())}
              >
                Hoje
              </Button>
              <Button
                variant="outline"
                size="sm"
                onClick={() => navigateMonth('next')}
              >
                <ChevronRight className="h-4 w-4" />
              </Button>
            </div>
          </div>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-7 gap-1">
            {/* Week days header */}
            {weekDays.map(day => (
              <div
                key={day}
                className="p-2 text-center text-sm font-medium text-muted-foreground"
              >
                {day}
              </div>
            ))}

            {/* Calendar days */}
            {days.map((day, index) => {
              const dayPosts = getPostsForDay(day.date); // Agora usa a função local getPostsForDay
              
              return (
                <div
                  key={index}
                  className={`
                    min-h-[100px] p-2 border border-border cursor-pointer hover:bg-muted/50 transition-colors
                    ${day.isCurrentMonth ? 'bg-card' : 'bg-muted/20'}
                    ${isToday(day.date) ? 'bg-primary/10 border-primary' : ''}
                    ${isSelected(day.date) ? 'ring-2 ring-primary' : ''}
                  `}
                  onClick={() => setSelectedDate(day.date)}
                >
                  <div className="flex items-center justify-between mb-1">
                    <span className={`text-sm font-medium ${
                      day.isCurrentMonth ? 'text-foreground' : 'text-muted-foreground'
                    }`}>
                      {day.date.getDate()}
                    </span>
                    {dayPosts.length > 0 && (
                      <Badge variant="secondary" className="text-xs">
                        {dayPosts.length}
                      </Badge>
                    )}
                  </div>

                  <div className="space-y-1">
                    {dayPosts.slice(0, 3).map(post => (
                      <div
                        key={post.id}
                        className={`text-xs p-1 rounded truncate ${
                          post.status === 'scheduled' ? 'bg-primary/20 text-primary' :
                          post.status === 'published' ? 'bg-success/20 text-success' :
                          post.status === 'error' ? 'bg-error/20 text-error' :
                          'bg-muted text-muted-foreground'
                        }`}
                        title={`${formatTime(post.scheduledAt)} - ${post.title}`}
                      >
                        {formatTime(post.scheduledAt)} {post.title}
                      </div>
                    ))}
                    {dayPosts.length > 3 && (
                      <div className="text-xs text-muted-foreground text-center">
                        +{dayPosts.length - 3} mais
                      </div>
                    )}
                  </div>
                </div>
              );
            })}
          </div>
        </CardContent>
      </Card>

      {/* Selected Date Posts */}
      {selectedDate && (
        <Card>
          <CardHeader>
            <CardTitle>
              Posts para {selectedDate.toLocaleDateString('pt-BR', {
                weekday: 'long',
                year: 'numeric',
                month: 'long',
                day: 'numeric'
              })}
            </CardTitle>
            <CardDescription>
              {selectedDatePosts.length} post(s) encontrado(s)
            </CardDescription>
          </CardHeader>
          <CardContent>
            {selectedDatePosts.length === 0 ? (
              <div className="text-center py-8">
                <p className="text-muted-foreground">
                  Nenhum post agendado para esta data
                </p>
                <Button
                  onClick={() => navigate('/new-post')}
                  className="mt-4"
                >
                  Agendar Post
                </Button>
              </div>
            ) : (
              <div className="space-y-4">
                {selectedDatePosts.map(post => (
                  <div
                    key={post.id}
                    className="flex items-center justify-between p-4 border rounded-lg hover:bg-muted/50"
                  >
                    <div className="flex-1">
                      <div className="flex items-center gap-2 mb-2">
                        <h3 className="font-medium">{post.title}</h3>
                        <StatusBadge status={post.status} />
                      </div>

                      <div className="flex items-center gap-4 text-sm text-muted-foreground">
                        <div className="flex items-center gap-1">
                          <Clock className="h-4 w-4" />
                          {formatTime(post.scheduledAt)}
                        </div>

                        <div className="flex gap-1">
                          {post.socialNetworks.map(network => {
                            const Icon = socialIcons[network as keyof typeof socialIcons];
                            const colorClass = socialColors[network as keyof typeof socialColors];
                            return (
                              <span key={network} title={network}>
                                <Icon className={`h-4 w-4 ${colorClass}`} />
                              </span>
                            );
                          })}
                        </div>
                      </div>

                      {post.description && (
                        <p className="text-sm text-muted-foreground mt-2 line-clamp-2">
                          {post.description}
                        </p>
                      )}
                    </div>

                    <div className="flex gap-2">
                      <Button
                        variant="outline"
                        size="sm"
                        onClick={() => navigate(`/posts/${post.id}`)}
                      >
                        <Eye className="h-4 w-4" />
                      </Button>
                      <Button
                        variant="outline"
                        size="sm"
                        onClick={() => navigate(`/posts/${post.id}/edit`)}
                      >
                        <Edit className="h-4 w-4" />
                      </Button>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </CardContent>
        </Card>
      )}
    </div>
  );
}