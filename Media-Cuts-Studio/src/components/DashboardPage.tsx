import React, { useEffect, useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts';
import { Plus, Upload, Calendar, List, TrendingUp, Clock, CheckCircle, AlertCircle, KeyRound, Activity, Zap } from 'lucide-react';

const DashboardPage = () => {
  const [taskData, setTaskData] = useState([]);
  const [NumberaccountData, setNumberaccountData] = useState(0);
  const [accountData, setAccountData] = useState([]);
  const [stats, setStats] = useState([]);
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    setStats(prevStats =>
      prevStats.map(stat => {
        if (stat.title === 'Active Accounts') {
          return { ...stat, value: `${accountData.length}` };
        }
        return stat;
      })
    );
  }, [accountData]);

  const API_URL = import.meta.env.VITE_API_URL;
  const apiKey = localStorage.getItem('api_key');
  const userEmail = localStorage.getItem('user_email');

  const processTasks = (tasks) => {
    const total = tasks.length;
    const completed = tasks.filter(t => t.status === 'Completed');
    const running = tasks.filter(t => t.status === 'Running');

    const trends = [
      { name: 'Tasks', totaltasks: tasks.length, completed: completed.length, pending: running.length }
    ];

    setTaskData(trends);

    setActivities(prev => [
      ...completed.slice(0, 3).map(c => ({
        action: 'Task completed',
        item: c.title || 'Unnamed Task',
        time: new Date(c.completed_at).toLocaleTimeString()
      })),
      ...prev
    ]);
  };

  const fetchTasks = async () => {
    try {
      const res = await fetch(`${API_URL}/api/user-tasks/${userEmail}`);
      const json = await res.json();
      console.log('user-tasks?', json);

      let tasksArray = [];
      if (json.tasks && typeof json.tasks === 'object' && !Array.isArray(json.tasks)) {
        tasksArray = Object.values(json.tasks);
      } else if (Array.isArray(json.tasks)) {
        tasksArray = json.tasks;
      }

      console.log('user-tasks Array? ', tasksArray);
      processTasks(tasksArray);
    } catch (error) {
      console.error('Erro ao buscar tarefas:', error);
    }
  };

  const fetchAccounts = async () => {
    if (!apiKey) {
      console.warn('fetchAccounts: apiKey ausente no localStorage.');
      return;
    }

    try {
      const res = await fetch(`${API_URL}/api/accounts/active`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ api_key: apiKey })
      });

      if (!res.ok) {
        console.error(`fetchAccounts: resposta HTTP com erro. status=${res.status}`);
        return;
      }

      const data = await res.json();
      console.log('accounts data?', data);
      setNumberaccountData(data.length);

      if (!Array.isArray(data)) {
        console.warn('fetchAccounts: esperado array, mas recebeu:', data);
        return;
      }

      const platforms = data.reduce((acc, account) => {
        if (account.platform) {
          acc[account.platform] = (acc[account.platform] || 0) + 1;
        }
        return acc;
      }, {});
      console.log('platforms data?', platforms);

      const formatted = Object.entries(platforms).map(([name, value]) => ({
        name,
        value,
        color: '#' + Math.floor(Math.random() * 16777215).toString(16)
      }));
      console.log('formatted data?', formatted);
      setAccountData(formatted);

      const lastCount = Number(localStorage.getItem('last_account_count') || '0');
      if (data.length > lastCount) {
        const nova = data[data.length - 1];
        setActivities(prev => [
          {
            action: 'New account added',
            item: `${nova.platform} - ${nova.username}`,
            time: 'now'
          },
          ...prev
        ]);
        localStorage.setItem('last_account_count', `${data.length}`);
      }

    } catch (error) {
      console.error('Erro ao buscar contas (catch):', error);
    }
  };

  useEffect(() => {
    const total       = taskData.length > 0 ? taskData[0].totaltasks   : 0;
    const completed   = taskData.length > 0 ? taskData[0].completed : 0;
    const running     = taskData.length > 0 ? taskData[0].pending   : 0;
    const todayCount  = completed;
    const total_accounts  =  NumberaccountData;

    console.log(`Total Tasks? ${total}`)
    console.log(`total_accounts? ${total_accounts}`)
    setStats([
      { title: 'Total Tasks',     value: `${total}`,          change: '', color: 'text-green-600' },
      { title: 'Active Accounts',  value: `${total_accounts}`, change: '', color: 'text-blue-600' },
      { title: 'Completed Today', value: `${todayCount}`,     change: '', color: 'text-primary-purple' },
      { title: 'Processing',      value: `${running}`,        change: '', color: 'text-orange-500' },
    ]);
  }, [taskData, accountData, NumberaccountData]);

  useEffect(() => {
    fetchTasks();
    fetchAccounts();

    const interval = setInterval(fetchAccounts, 60 * 60 * 1000);
    return () => clearInterval(interval);
  }, []);

  const quickActions = [
    {
      title: 'Novo Post',
      description: 'Criar e agendar um post individual',
      icon: Plus,
      color: 'bg-gradient-to-r from-blue-500 to-blue-600 hover:from-blue-600 hover:to-blue-700'
    },
    {
      title: 'Agendamento em Massa',
      description: 'Upload múltiplos posts de uma vez',
      icon: Upload,
      color: 'bg-gradient-to-r from-emerald-500 to-emerald-600 hover:from-emerald-600 hover:to-emerald-700'
    },
    {
      title: 'Ver Calendário',
      description: 'Visualizar posts no calendário',
      icon: Calendar,
      color: 'bg-gradient-to-r from-purple-500 to-purple-600 hover:from-purple-600 hover:to-purple-700'
    },
    {
      title: 'Lista de Posts',
      description: 'Gerenciar todos os posts',
      icon: List,
      color: 'bg-gradient-to-r from-indigo-500 to-indigo-600 hover:from-indigo-600 hover:to-indigo-700'
    },
    {
      title: 'Autenticar Conta',
      description: 'Conectar sua conta do Google para uploads',
      icon: KeyRound,
      color: 'bg-gradient-to-r from-red-500 to-red-600 hover:from-red-600 hover:to-red-700'
    }
  ];

  const getDashboardStats = () => {
    return {
      today: 5,
      week: 12,
      month: 48,
      draft: 8,
      scheduled: 15,
      published: 127,
      error: 2
    };
  };

  const schedulerStats = getDashboardStats();

  const statCards = [
    {
      title: 'Posts Hoje',
      value: schedulerStats.today,
      description: 'Agendados para hoje',
      icon: Clock,
      color: 'text-primary-purple'
    },
    {
      title: 'Esta Semana',
      value: schedulerStats.week,
      description: 'Posts desta semana',
      icon: TrendingUp,
      color: 'text-success'
    },
    {
      title: 'Este Mês',
      value: schedulerStats.month,
      description: 'Posts deste mês',
      icon: Calendar,
      color: 'text-warning'
    }
  ];

  const statusCards = [
    {
      title: 'Rascunho',
      value: schedulerStats.draft,
      description: 'Posts em rascunho',
      icon: Clock,
      color: 'text-muted-foreground'
    },
    {
      title: 'Agendados',
      value: schedulerStats.scheduled,
      description: 'Aguardando publicação',
      icon: Calendar,
      color: 'text-primary-purple'
    },
    {
      title: 'Publicados',
      value: schedulerStats.published,
      description: 'Publicados com sucesso',
      icon: CheckCircle,
      color: 'text-success'
    },
    {
      title: 'Erros',
      value: schedulerStats.error,
      description: 'Falharam na publicação',
      icon: AlertCircle,
      color: 'text-error'
    }
  ];

  return (
    <div className="min-h-screen bg-gradient-background transition-all duration-300">

      {/* Header */}
      <div className="sticky top-0 z-10 bg-gradient-hero/90 backdrop-blur-md shadow-lg border-b border-transparent">
        <div className="px-4 sm:px-6 lg:px-8 py-5 sm:py-6">
          <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3">
            <div>
              <h1 className="text-2xl sm:text-3xl lg:text-4xl font-extrabold text-black tracking-tight">Media Cuts Studio</h1>
              <p className="mt-1 text-sm sm:text-base text-black/90">Acompanhe o que está acontecendo com a criação de conteúdo hoje.</p>
            </div>

          </div>
        </div>
      </div>

      <div className="px-4 sm:px-6 lg:px-8 py-6 space-y-6">

        {/* Main stats */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          {stats.map((stat, index) => (
            <Card key={index} className="group rounded-2xl bg-white/80 dark:bg-gray-900/70 backdrop-blur-sm border border-gray-200/40 dark:border-gray-800/40 shadow transition-transform duration-200 hover:scale-[1.02]">
              <CardContent className="p-4">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-xs sm:text-sm font-medium text-gray-text dark:text-gray-400">{stat.title}</p>
                    <p className="mt-1 text-xl sm:text-2xl font-bold text-gray-900 dark:text-white">{stat.value}</p>
                  </div>
                  <div className={`text-sm font-medium ${stat.color}`}>{stat.change}</div>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>

        {/* Overview */}
        <section>
          <h3 className="text-base sm:text-lg font-semibold mb-4 text-gray-900 dark:text-white flex items-center gap-2">
            <TrendingUp className="h-5 w-5 text-white/90" />
            Visão Geral
          </h3>

          <div className="grid gap-4 md:grid-cols-3">
            {statCards.map((stat) => (
              <Card key={stat.title} className="rounded-xl bg-white/80 dark:bg-gray-900/70 backdrop-blur-sm border border-gray-200/40 dark:border-gray-800/40 hover:shadow-md transition-shadow duration-200">
                <CardHeader className="flex items-center justify-between py-3">
                  <CardTitle className="text-sm font-medium text-gray-700 dark:text-gray-200">{stat.title}</CardTitle>
                  <stat.icon className={`h-5 w-5 ${stat.color}`} />
                </CardHeader>
                <CardContent className="py-2">
                  <div className="text-2xl font-extrabold">{stat.value}</div>
                  <p className="text-sm text-gray-600 dark:text-gray-400">{stat.description}</p>
                </CardContent>
              </Card>
            ))}
          </div>
        </section>

        {/* Status dos Posts */}
        <section>
          <h3 className="text-base sm:text-lg font-semibold mb-4 text-gray-900 dark:text-white flex items-center gap-2">
            <Activity className="h-5 w-5 text-white/90" />
            Status dos Posts
          </h3>
          <div className="grid gap-4 md:grid-cols-4">
            {statusCards.map((status) => (
              <Card key={status.title} className="rounded-xl bg-white/80 dark:bg-gray-900/70 border border-gray-200/40 dark:border-gray-800/40 hover:shadow-md transition-shadow duration-200">
                <CardHeader className="flex items-center justify-between py-3">
                  <CardTitle className="text-sm font-medium text-gray-700 dark:text-gray-200">{status.title}</CardTitle>
                  <status.icon className={`h-5 w-5 ${status.color}`} />
                </CardHeader>
                <CardContent className="py-2">
                  <div className="text-2xl font-extrabold">{status.value}</div>
                  <p className="text-sm text-gray-600 dark:text-gray-400">{status.description}</p>
                </CardContent>
              </Card>
            ))}
          </div>
        </section>

        {/* Quick Actions */}
        <section>
          <h3 className="text-base sm:text-lg font-semibold mb-4 text-gray-900 dark:text-white flex items-center gap-2">
            <Zap className="h-5 w-5 text-white/90" />
            Ações Rápidas
          </h3>

          <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
            {quickActions.map((action) => (
              <Card key={action.title} className="cursor-pointer rounded-xl overflow-hidden bg-gradient-card/80 hover:scale-[1.01] transition-transform duration-150">
                <CardHeader className="p-4">
                  <div className="flex items-start gap-4">
                    <div className={`w-12 h-12 rounded-lg flex items-center justify-center ${action.color} shadow-sm`}> 
                      <action.icon className="h-6 w-6 text-white" />
                    </div>
                    <div>
                      <CardTitle className="text-sm font-medium text-white">{action.title}</CardTitle>
                      <p className="text-xs text-white/80 mt-1">{action.description}</p>
                    </div>
                  </div>
                </CardHeader>
                <CardContent className="p-4">
                  <Button variant="ghost" className="w-full rounded-full border border-white/20 text-white/90">Acessar</Button>
                </CardContent>
              </Card>
            ))}
          </div>
        </section>

        {/* Charts */}
        <div className="grid grid-cols-1 xl:grid-cols-2 gap-4">
          <Card className="rounded-xl bg-white/80 dark:bg-gray-900/70 border border-gray-200/40 dark:border-gray-800/40 shadow">
            <CardHeader>
              <CardTitle className="text-sm sm:text-base lg:text-lg text-gray-800 dark:text-gray-100">Task Completion Trends</CardTitle>
            </CardHeader>
            <CardContent>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={taskData}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" className="dark:stroke-gray-600" />
                  <XAxis dataKey="name" stroke="#64748b" />
                  <YAxis stroke="#64748b" />
                  <Tooltip
                    contentStyle={{ backgroundColor: 'rgb(31 41 55)', borderColor: 'rgb(75 85 99)', color: 'rgb(243 244 246)' }}
                    labelStyle={{ color: 'rgb(243 244 246)' }}
                  />
                  <Bar dataKey="completed" fill="#22c55e" name="Completed" />
                  <Bar dataKey="pending" fill="#f59e0b" name="Pending" />
                </BarChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>

          <Card className="rounded-xl bg-white/80 dark:bg-gray-900/70 border border-gray-200/40 dark:border-gray-800/40 shadow">
            <CardHeader>
              <CardTitle className="text-sm sm:text-base lg:text-lg text-gray-800 dark:text-gray-100">Account Distribution</CardTitle>
            </CardHeader>
            <CardContent>
              <ResponsiveContainer width="100%" height={300}>
                <PieChart>
                  <Pie
                    data={accountData}
                    cx="50%"
                    cy="50%"
                    innerRadius={60}
                    outerRadius={100}
                    paddingAngle={5}
                    dataKey="value"
                  >
                    {accountData.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={entry.color} />
                    ))}
                  </Pie>
                  <Tooltip
                    contentStyle={{ backgroundColor: 'rgb(31 41 55)', borderColor: 'rgb(75 85 99)', color: 'rgb(243 244 246)' }}
                    labelStyle={{ color: 'rgb(243 244 246)' }}
                  />
                </PieChart>
              </ResponsiveContainer>

              <div className="flex flex-wrap justify-center gap-3 mt-4 text-gray-800 dark:text-gray-200">
                {accountData.map((item, index) => (
                  <div key={index} className="flex items-center gap-2 text-sm">
                    <div className="w-3 h-3 rounded-full" style={{ backgroundColor: item.color }} aria-hidden />
                    <span>{item.name}</span>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Recent Activity */}
        <Card className="rounded-xl bg-white/80 dark:bg-gray-900/70 border border-gray-200/40 dark:border-gray-800/40 shadow">
          <CardHeader>
            <CardTitle className="text-sm sm:text-base lg:text-lg text-gray-800 dark:text-gray-100">Recent Activity</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-3">
              {activities.map((activity, index) => (
                <div
                  key={index}
                  className="flex items-center justify-between py-2 border-b last:border-0 border-gray-200/50 dark:border-gray-800/50"
                >
                  <div>
                    <p className="font-medium text-sm text-gray-900 dark:text-white">{activity.action}</p>
                    <p className="text-xs text-gray-600 dark:text-gray-400">{activity.item}</p>
                  </div>
                  <span className="text-xs text-gray-500 dark:text-gray-400">{activity.time}</span>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>

      </div>
    </div>
  );
};

export default DashboardPage;
