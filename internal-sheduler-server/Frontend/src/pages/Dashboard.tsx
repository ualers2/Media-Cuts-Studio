import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Plus, Upload, Calendar, List, TrendingUp, Clock, CheckCircle, AlertCircle, KeyRound } from 'lucide-react'; // Importe KeyRound ou outro ícone relevante
import { usePost } from '@/contexts/PostContext';
import { useNavigate } from 'react-router-dom';

export default function Dashboard() {
  const { getDashboardStats } = usePost();
  const navigate = useNavigate();

  const stats = getDashboardStats();

  const statCards = [
    {
      title: 'Posts Hoje',
      value: stats.today,
      description: 'Agendados para hoje',
      icon: Clock,
      color: 'text-primary'
    },
    {
      title: 'Esta Semana',
      value: stats.week,
      description: 'Posts desta semana',
      icon: TrendingUp,
      color: 'text-success'
    },
    {
      title: 'Este Mês',
      value: stats.month,
      description: 'Posts deste mês',
      icon: Calendar,
      color: 'text-warning'
    }
  ];

  const statusCards = [
    {
      title: 'Rascunho',
      value: stats.draft,
      description: 'Posts em rascunho',
      icon: Clock,
      color: 'text-muted-foreground'
    },
    {
      title: 'Agendados',
      value: stats.scheduled,
      description: 'Aguardando publicação',
      icon: Calendar,
      color: 'text-primary'
    },
    {
      title: 'Publicados',
      value: stats.published,
      description: 'Publicados com sucesso',
      icon: CheckCircle,
      color: 'text-success'
    },
    {
      title: 'Erros',
      value: stats.error,
      description: 'Falharam na publicação',
      icon: AlertCircle,
      color: 'text-error'
    }
  ];

  const quickActions = [
    {
      title: 'Novo Post',
      description: 'Criar e agendar um post individual',
      icon: Plus,
      action: () => navigate('/new-post'),
      color: 'bg-primary hover:bg-primary/90'
    },
    {
      title: 'Agendamento em Massa',
      description: 'Upload múltiplos posts de uma vez',
      icon: Upload,
      action: () => navigate('/bulk-schedule'),
      color: 'bg-success hover:bg-success/90'
    },
    {
      title: 'Ver Calendário',
      description: 'Visualizar posts no calendário',
      icon: Calendar,
      action: () => navigate('/calendar'),
      color: 'bg-warning hover:bg-warning/90'
    },
    {
      title: 'Lista de Posts',
      description: 'Gerenciar todos os posts',
      icon: List,
      action: () => navigate('/posts'),
      color: 'bg-primary-light hover:bg-primary-light/90'
    },
    // NOVO CARD DE AUTENTICAÇÃO
    {
      title: 'Autenticar Conta',
      description: 'Conectar sua conta do Google para uploads',
      icon: KeyRound, // Ícone para autenticação
      action: () => navigate('/authenticate-account'), // Nova rota para a autenticação
      color: 'bg-blue-500 hover:bg-blue-600' // Cor diferente para destacar
    }
  ];

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-3xl font-bold tracking-tight">Dashboard</h2>
        <p className="text-muted-foreground">
          Visão geral da sua plataforma de agendamento de posts
        </p>
      </div>

      {/* Stats Cards */}
      <div className="grid gap-4 md:grid-cols-3">
        {statCards.map((stat) => (
          <Card key={stat.title}>
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-medium">{stat.title}</CardTitle>
              <stat.icon className={`h-4 w-4 ${stat.color}`} />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">{stat.value}</div>
              <p className="text-xs text-muted-foreground">{stat.description}</p>
            </CardContent>
          </Card>
        ))}
      </div>

      {/* Status Cards */}
      <div>
        <h3 className="text-lg font-semibold mb-4">Status dos Posts</h3>
        <div className="grid gap-4 md:grid-cols-4">
          {statusCards.map((status) => (
            <Card key={status.title}>
              <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                <CardTitle className="text-sm font-medium">{status.title}</CardTitle>
                <status.icon className={`h-4 w-4 ${status.color}`} />
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold">{status.value}</div>
                <p className="text-xs text-muted-foreground">{status.description}</p>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>

      {/* Quick Actions */}
      <div>
        <h3 className="text-lg font-semibold mb-4">Ações Rápidas</h3>
        <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
          {quickActions.map((action) => (
            <Card key={action.title} className="cursor-pointer hover:shadow-lg transition-shadow">
              <CardHeader>
                <div className={`w-12 h-12 rounded-lg ${action.color} flex items-center justify-center mb-2`}>
                  <action.icon className="h-6 w-6 text-white" />
                </div>
                <CardTitle className="text-base">{action.title}</CardTitle>
                <CardDescription className="text-sm">{action.description}</CardDescription>
              </CardHeader>
              <CardContent>
                <Button onClick={action.action} variant="outline" className="w-full">
                  Acessar
                </Button>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </div>
  );
}
