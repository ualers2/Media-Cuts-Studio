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
  Clock,
  Plus,
  TrendingUp,
  Users
} from 'lucide-react';
import { BsTiktok } from 'react-icons/bs';
import { usePost } from '@/contexts/PostContext';
import { useNavigate } from 'react-router-dom';
import Layout from '@/components/Layout';

const socialIcons = {
  youtube: Youtube,
  instagram: Instagram,
  facebook: Facebook,
  twitter: Twitter,
  tiktok: BsTiktok
};

const socialColors = {
  youtube: 'text-red-500 hover:text-red-600',
  instagram: 'text-pink-500 hover:text-pink-600',
  facebook: 'text-blue-500 hover:text-blue-600',
  twitter: 'text-sky-500 hover:text-sky-600',
  tiktok: 'text-pink-500 hover:text-pink-600'
};

const monthNames = [
  'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
  'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
];

const weekDays = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb'];

export default function Calendar() {
  const { posts, fetchPosts, getPostsForDate } = usePost();
  const navigate = useNavigate();

  const [currentDate, setCurrentDate] = useState(new Date());
  const [selectedDate, setSelectedDate] = useState<Date | null>(null);
  const [statusFilter, setStatusFilter] = useState<string>('all');
  const [socialFilter, setSocialFilter] = useState<string>('all');
  const [viewMode, setViewMode] = useState<'month' | 'week'>('month');
  const [channelFilter, setChannelFilter] = useState<string>('all');
  const [isAnimating, setIsAnimating] = useState(false);

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
        posts: filteredPosts.filter(post => new Date(post.scheduledAt).toDateString() === day.toDateString())
      });
    }

    // Current month's days
    for (let i = 1; i <= daysInMonth; i++) {
      const day = new Date(year, month, i);
      days.push({
        date: day,
        isCurrentMonth: true,
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
        posts: filteredPosts.filter(post => new Date(post.scheduledAt).toDateString() === day.toDateString())
      });
    }

    return days;
  };

  const navigateMonth = (direction: 'prev' | 'next') => {
    setIsAnimating(true);
    setTimeout(() => setIsAnimating(false), 300);
    
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

  // Stats para o dashboard
  const totalPosts = filteredPosts.length;
  const scheduledPosts = filteredPosts.filter(p => p.status === 'scheduled').length;
  const publishedPosts = filteredPosts.filter(p => p.status === 'published').length;

  return (
    <Layout>
      <div className="space-y-8 animate-in fade-in duration-500">
        {/* Header with improved typography and spacing */}
        <div className="space-y-4">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-4xl font-bold tracking-tight bg-gradient-to-r from-foreground to-foreground/70 bg-clip-text">
                Calendário
              </h1>
              <p className="text-lg text-muted-foreground mt-2">
                Visualize e gerencie seus posts agendados
              </p>
            </div>
            
            <Button 
              onClick={() => navigate('/new-post')}
              className="bg-gradient-to-r from-primary to-primary/80 hover:from-primary/90 hover:to-primary/70 shadow-lg hover:shadow-xl transition-all duration-300 transform hover:scale-105"
              size="lg"
            >
              <Plus className="h-5 w-5 mr-2" />
              Novo Post
            </Button>
          </div>

          {/* Stats Cards */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <Card className="border-0 shadow-lg bg-gradient-to-br from-blue-50 to-blue-100/50 dark:from-blue-900/10 dark:to-blue-800/5 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1">
              <CardContent className="p-6">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-sm font-medium text-blue-600 dark:text-blue-400">Total de Posts</p>
                    <p className="text-3xl font-bold text-blue-700 dark:text-blue-300">{totalPosts}</p>
                  </div>
                  <div className="p-3 bg-blue-100 dark:bg-blue-900/20 rounded-full">
                    <TrendingUp className="h-6 w-6 text-blue-600 dark:text-blue-400" />
                  </div>
                </div>
              </CardContent>
            </Card>

            <Card className="border-0 shadow-lg bg-gradient-to-br from-green-50 to-green-100/50 dark:from-green-900/10 dark:to-green-800/5 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1">
              <CardContent className="p-6">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-sm font-medium text-green-600 dark:text-green-400">Agendados</p>
                    <p className="text-3xl font-bold text-green-700 dark:text-green-300">{scheduledPosts}</p>
                  </div>
                  <div className="p-3 bg-green-100 dark:bg-green-900/20 rounded-full">
                    <Clock className="h-6 w-6 text-green-600 dark:text-green-400" />
                  </div>
                </div>
              </CardContent>
            </Card>

            <Card className="border-0 shadow-lg bg-gradient-to-br from-purple-50 to-purple-100/50 dark:from-purple-900/10 dark:to-purple-800/5 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1">
              <CardContent className="p-6">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-sm font-medium text-purple-600 dark:text-purple-400">Publicados</p>
                    <p className="text-3xl font-bold text-purple-700 dark:text-purple-300">{publishedPosts}</p>
                  </div>
                  <div className="p-3 bg-purple-100 dark:bg-purple-900/20 rounded-full">
                    <Check className="h-6 w-6 text-purple-600 dark:text-purple-400" />
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>

        {/* Enhanced Filters */}
        <Card className="border-0 shadow-lg">
          <CardContent className="p-6">
            <div className="flex flex-wrap gap-4 items-center">
              <div className="flex items-center gap-2 text-sm font-medium">
                <Filter className="h-4 w-4" />
                Filtros:
              </div>
              
              <div className="flex flex-wrap gap-3">
                <Select value={statusFilter} onValueChange={setStatusFilter}>
                  <SelectTrigger className="w-[180px] border-2 hover:border-primary/50 transition-colors">
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
                  <SelectTrigger className="w-[180px] border-2 hover:border-primary/50 transition-colors">
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

                <Select value={channelFilter} onValueChange={setChannelFilter}>
                  <SelectTrigger className="w-[180px] border-2 hover:border-primary/50 transition-colors">
                    <SelectValue placeholder="Canal" />
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
            </div>
          </CardContent>
        </Card>

        {/* Enhanced Calendar */}
        <Card className="border-0 shadow-xl bg-gradient-to-br from-card to-card/50">
          <CardHeader className="pb-4">
            <div className="flex items-center justify-between">
              <CardTitle className="flex items-center gap-3 text-2xl">
                <div className="p-2 bg-primary/10 rounded-lg">
                  <CalendarIcon className="h-6 w-6 text-primary" />
                </div>
                <span className="bg-gradient-to-r from-foreground to-foreground/70 bg-clip-text">
                  {monthNames[currentDate.getMonth()]} {currentDate.getFullYear()}
                </span>
              </CardTitle>
              
              <div className="flex items-center gap-2">
                <Button
                  variant="outline"
                  size="sm"
                  onClick={() => navigateMonth('prev')}
                  className="hover:bg-primary/10 hover:border-primary/50 transition-all duration-200"
                >
                  <ChevronLeft className="h-4 w-4" />
                </Button>
                <Button
                  variant="outline"
                  size="sm"
                  onClick={() => setCurrentDate(new Date())}
                  className="px-4 hover:bg-primary hover:text-primary-foreground transition-all duration-200"
                >
                  Hoje
                </Button>
                <Button
                  variant="outline"
                  size="sm"
                  onClick={() => navigateMonth('next')}
                  className="hover:bg-primary/10 hover:border-primary/50 transition-all duration-200"
                >
                  <ChevronRight className="h-4 w-4" />
                </Button>
              </div>
            </div>
          </CardHeader>
          
          <CardContent className="p-6">
            <div className={`grid grid-cols-7 gap-2 transition-opacity duration-300 ${isAnimating ? 'opacity-50' : 'opacity-100'}`}>
              {/* Enhanced Week days header */}
              {weekDays.map(day => (
                <div
                  key={day}
                  className="p-4 text-center text-sm font-semibold text-muted-foreground bg-muted/30 rounded-lg"
                >
                  {day}
                </div>
              ))}

              {/* Enhanced Calendar days */}
              {days.map((day, index) => {
                const dayPosts = getPostsForDay(day.date);
                
                return (
                  <div
                    key={index}
                    className={`
                      min-h-[120px] p-3 border-2 cursor-pointer transition-all duration-300 rounded-xl group
                      ${day.isCurrentMonth 
                        ? 'bg-card hover:bg-accent/50 border-border hover:border-primary/30' 
                        : 'bg-muted/20 hover:bg-muted/40 border-muted'
                      }
                      ${isToday(day.date) 
                        ? 'bg-primary/10 border-primary shadow-lg ring-2 ring-primary/20' 
                        : ''
                      }
                      ${isSelected(day.date) 
                        ? 'ring-2 ring-primary border-primary shadow-xl scale-105' 
                        : 'hover:scale-102'
                      }
                      ${dayPosts.length > 0 ? 'hover:shadow-lg' : ''}
                    `}
                    onClick={() => setSelectedDate(day.date)}
                  >
                    <div className="flex items-center justify-between mb-2">
                      <span className={`text-sm font-semibold transition-colors ${
                        day.isCurrentMonth ? 'text-foreground' : 'text-muted-foreground'
                      } ${isToday(day.date) ? 'text-primary font-bold' : ''}`}>
                        {day.date.getDate()}
                      </span>
                      {dayPosts.length > 0 && (
                        <Badge 
                          variant="secondary" 
                          className="text-xs bg-primary/10 text-primary border-primary/20 animate-in fade-in duration-300"
                        >
                          {dayPosts.length}
                        </Badge>
                      )}
                    </div>

                    <div className="space-y-1">
                      {dayPosts.slice(0, 2).map((post, postIndex) => (
                        <div
                          key={post.id}
                          className={`text-xs p-2 rounded-lg transition-all duration-200 hover:scale-105 cursor-pointer backdrop-blur-sm animate-in slide-in-from-bottom-2 ${
                            post.status === 'scheduled' ? 'bg-blue-100 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300 hover:bg-blue-200 dark:hover:bg-blue-900/50' :
                            post.status === 'published' ? 'bg-green-100 dark:bg-green-900/30 text-green-700 dark:text-green-300 hover:bg-green-200 dark:hover:bg-green-900/50' :
                            post.status === 'error' ? 'bg-red-100 dark:bg-red-900/30 text-red-700 dark:text-red-300 hover:bg-red-200 dark:hover:bg-red-900/50' :
                            'bg-muted text-muted-foreground hover:bg-muted/80'
                          }`}
                          title={`${formatTime(post.scheduledAt)} - ${post.title}`}
                          style={{
                            animationDelay: `${postIndex * 50}ms`
                          }}
                        >
                          <div className="font-medium truncate">{formatTime(post.scheduledAt)}</div>
                          <div className="truncate opacity-80">{post.title}</div>
                        </div>
                      ))}
                      {dayPosts.length > 2 && (
                        <div className="text-xs text-center p-1 rounded bg-muted/50 text-muted-foreground font-medium animate-in fade-in duration-300">
                          +{dayPosts.length - 2} mais
                        </div>
                      )}
                    </div>
                  </div>
                );
              })}
            </div>
          </CardContent>
        </Card>

        {/* Enhanced Selected Date Posts */}
        {selectedDate && (
          <Card className="border-0 shadow-xl bg-gradient-to-br from-card to-accent/5 animate-in slide-in-from-bottom-4 duration-500">
            <CardHeader className="pb-4">
              <div className="flex items-center justify-between">
                <div>
                  <CardTitle className="text-xl flex items-center gap-2">
                    <div className="p-2 bg-primary/10 rounded-lg">
                      <List className="h-5 w-5 text-primary" />
                    </div>
                    Posts para {selectedDate.toLocaleDateString('pt-BR', {
                      weekday: 'long',
                      year: 'numeric',
                      month: 'long',
                      day: 'numeric'
                    })}
                  </CardTitle>
                  <CardDescription className="text-base mt-1">
                    {selectedDatePosts.length} post(s) encontrado(s)
                  </CardDescription>
                </div>
                
                <Button
                  variant="outline"
                  onClick={() => setSelectedDate(null)}
                  className="hover:bg-muted"
                >
                  Fechar
                </Button>
              </div>
            </CardHeader>
            
            <CardContent>
              {selectedDatePosts.length === 0 ? (
                <div className="text-center py-12 animate-in fade-in duration-300">
                  <div className="p-4 bg-muted/30 rounded-full w-fit mx-auto mb-4">
                    <CalendarIcon className="h-8 w-8 text-muted-foreground" />
                  </div>
                  <h3 className="text-lg font-semibold mb-2">Nenhum post agendado</h3>
                  <p className="text-muted-foreground mb-6">
                    Que tal agendar um post para esta data?
                  </p>
                  <Button
                    onClick={() => navigate('/new-post')}
                    className="bg-gradient-to-r from-primary to-primary/80 hover:from-primary/90 hover:to-primary/70 shadow-lg hover:shadow-xl transition-all duration-300"
                    size="lg"
                  >
                    <Plus className="h-5 w-5 mr-2" />
                    Agendar Post
                  </Button>
                </div>
              ) : (
                <div className="space-y-4">
                  {selectedDatePosts.map((post, index) => (
                    <div
                      key={post.id}
                      className="group p-6 border-2 border-border hover:border-primary/30 rounded-xl bg-card hover:bg-accent/30 transition-all duration-300 hover:shadow-lg animate-in slide-in-from-left-4"
                      style={{
                        animationDelay: `${index * 100}ms`
                      }}
                    >
                      <div className="flex items-start justify-between">
                        <div className="flex-1">
                          <div className="flex items-center gap-3 mb-3">
                            <h3 className="font-semibold text-lg group-hover:text-primary transition-colors">
                              {post.title}
                            </h3>
                            <StatusBadge status={post.status} />
                          </div>

                          <div className="flex items-center gap-6 text-sm text-muted-foreground mb-3">
                            <div className="flex items-center gap-2 bg-muted/50 px-3 py-1 rounded-full">
                              <Clock className="h-4 w-4" />
                              {formatTime(post.scheduledAt)}
                            </div>

                            <div className="flex gap-2">
                              {post.socialNetworks.map(network => {
                                const Icon = socialIcons[network as keyof typeof socialIcons];
                                const colorClass = socialColors[network as keyof typeof socialColors];
                                return (
                                  <div 
                                    key={network} 
                                    className="p-2 bg-muted/50 rounded-full hover:scale-110 transition-transform duration-200"
                                    title={network}
                                  >
                                    <Icon className={`h-4 w-4 ${colorClass} transition-colors`} />
                                  </div>
                                );
                              })}
                            </div>
                          </div>

                          {post.description && (
                            <p className="text-muted-foreground leading-relaxed line-clamp-2 bg-muted/20 p-3 rounded-lg">
                              {post.description}
                            </p>
                          )}
                        </div>

                        <div className="flex gap-2 ml-4">
                          <Button
                            variant="outline"
                            size="sm"
                            onClick={() => navigate(`/posts/${post.id}`)}
                            className="hover:bg-primary hover:text-primary-foreground transition-all duration-200"
                          >
                            <Eye className="h-4 w-4" />
                          </Button>
                          <Button
                            variant="outline"
                            size="sm"
                            onClick={() => navigate(`/posts/${post.id}/edit`)}
                            className="hover:bg-primary hover:text-primary-foreground transition-all duration-200"
                          >
                            <Edit className="h-4 w-4" />
                          </Button>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </CardContent>
          </Card>
        )}
      </div>
    </Layout>
  );
}