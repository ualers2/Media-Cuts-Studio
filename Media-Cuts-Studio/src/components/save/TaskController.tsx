import React, { useState, useEffect } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Badge } from '@/components/ui/badge';
import { Search, Play, Trash2, Loader2, RefreshCw } from 'lucide-react'; // Adicionado RefreshCw para o botão de atualizar
import { toast } from '@/hooks/use-toast';

// Interfaces (mantidas as mesmas)
interface Task {
  task_id: string;
  mode: string;
  scheduled_time: string;
  yt_channel: string;
  status: 'Running' | 'Completed' | 'Created';
}

interface TaskControllerProps {
  userId: string | null;
}

const TaskController: React.FC<TaskControllerProps> = ({ userId }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [filter, setFilter] = useState<'all' | 'running' | 'completed'>('all');
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(false);
  const [selected, setSelected] = useState<string[]>([]);

  const VITE_LANDING_API = import.meta.env.VITE_LANDING_API;
  const apiUrl = import.meta.env.VITE_API_URL;

  // Função para buscar tarefas da API
  const fetchTasks = async () => {
    if (!userId) return;
    setLoading(true);
    try {
      const res = await fetch(`${VITE_LANDING_API}/api/user-tasks/${userId}`);
      if (!res.ok) throw new Error('Falha ao carregar tarefas');
      const data = await res.json();
      const raw = data.tasks;
      const list: Task[] = Array.isArray(raw)
        ? raw
        : raw && typeof raw === 'object'
        ? Object.values(raw)
        : [];
      setTasks(list);
    } catch (err) {
      console.error(err);
      setTasks([]);
      toast({ title: 'Erro ao carregar tarefas', variant: 'destructive' });
    } finally {
      setLoading(false);
    }
  };

  // Função para deletar uma tarefa
  const deleteTask = async (taskId: string) => {
    if (!userId) return;
    try {
      const res = await fetch(`${apiUrl}/api/Media_Cuts_Studio/Shortify/Mode/Delete`, {
        method: 'POST',
        headers: {
          'X-API-KEY': localStorage.getItem('api_key') || '',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ task_id: taskId, user_email: localStorage.getItem('user_email'), api_key: localStorage.getItem('api_key') }),
      });
      if (!res.ok) throw await res.json();
      toast({ title: 'Tarefa deletada', variant: 'destructive' });
      fetchTasks();
    } catch (err) {
      console.error(err);
      toast({ title: 'Erro ao deletar', variant: 'destructive' });
    }
  };

  // Efeito para carregar tarefas e configurar o intervalo de atualização
  useEffect(() => {
    fetchTasks();
    const iv = setInterval(fetchTasks, 60000); // Atualiza a cada 60 segundos
    return () => clearInterval(iv); // Limpa o intervalo ao desmontar o componente
  }, [userId, VITE_LANDING_API]); // Adicionado VITE_LANDING_API às dependências para re-fetch se mudar

  // Lógica de filtragem e busca de tarefas
  const filteredTasks = tasks.filter((t) => {
    const matchSearch = `${t.mode} ${t.yt_channel} ${t.scheduled_time} ${t.status}`
      .toLowerCase()
      .includes(searchTerm.toLowerCase());
    const matchFilter =
      filter === 'all' ||
      (filter === 'running' && t.status === 'Running') ||
      (filter === 'completed' && (t.status === 'Completed' || t.status === 'Created')); // Assumindo 'Created' também não é 'Running'
    return matchSearch && matchFilter;
  });

  // Lógica de seleção de tarefas
  const toggleSelect = (id: string) => {
    setSelected((s) => (s.includes(id) ? s.filter((x) => x !== id) : [...s, id]));
  };
  const selectAll = () => setSelected(filteredTasks.map((t) => t.task_id));
  const clearSelect = () => setSelected([]);

  // Definição das colunas para o layout de grade
  const gridCols = { gridTemplateColumns: '40px 1.2fr 1.5fr 180px auto 60px' }; // Ajustado para melhor visualização

  return (
    // Card principal que contém toda a UI do controlador
    <Card className="max-w-6xl mx-auto my-8 p-6 shadow-xl rounded-lg border-l-4 border-blue-600
                    bg-white dark:bg-gray-800 dark:border-blue-700 text-gray-900 dark:text-gray-100">
      <CardHeader className="pb-4">
        <CardTitle className="text-3xl font-bold flex items-center gap-3 text-gray-800 dark:text-gray-100">
          <RefreshCw size={28} className="text-blue-600 dark:text-blue-400" />
          Gerenciar Tarefas
        </CardTitle>
        <p className="text-gray-600 dark:text-gray-400 mt-1">Visualize e controle todas as suas tarefas de agendamento.</p>
      </CardHeader>

      <CardContent className="space-y-6">
        {/* Seção de Busca e Filtro */}
        <div className="flex flex-col sm:flex-row items-center gap-4 p-4 rounded-lg shadow-sm
                        bg-gray-50 dark:bg-gray-700"> {/* Fundo da barra de busca/filtro */}
          <div className="relative flex-1 w-full">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 dark:text-gray-300" size={18} />
            {/* Input de busca - shadcn/ui Input já tem suporte a dark mode */}
            <Input
              placeholder="Buscar tarefas por canal, modo ou status..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="pl-10 pr-4 py-2 w-full border rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent
                         bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 border-gray-300 dark:border-gray-600"
            />
          </div>
          <div className="flex gap-2 flex-wrap justify-center sm:justify-start">
            {(['all', 'running', 'completed'] as const).map((f) => (
              <Button
                key={f}
                variant={filter === f ? 'default' : 'outline'}
                size="sm"
                onClick={() => setFilter(f)}
                className={`rounded-full px-4 py-1 text-sm transition-colors duration-200
                            ${filter === f
                    ? 'bg-blue-600 text-white hover:bg-blue-700 dark:bg-blue-700 dark:hover:bg-blue-800' // Botão ativo
                    : 'bg-white text-gray-700 hover:bg-gray-100 dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 dark:hover:bg-gray-600' // Botão inativo
                  }`}
              >
                {f === 'all' ? 'Todas' : f === 'running' ? 'Executando' : 'Concluídas'}
              </Button>
            ))}
          </div>
          <Button
            size="sm"
            onClick={fetchTasks}
            disabled={loading}
            className="bg-green-500 hover:bg-green-600 text-white shadow-md rounded-md flex items-center gap-1
                       dark:bg-green-600 dark:hover:bg-green-700"
          >
            {loading ? <Loader2 size={16} className="animate-spin" /> : <RefreshCw size={16} />}
            {loading ? 'Atualizando...' : 'Atualizar'}
          </Button>
        </div>

        {/* Exibição de Tarefas */}
        {loading && tasks.length === 0 ? ( // Mostra um spinner de carregamento se for o carregamento inicial
          <div className="flex justify-center items-center h-40 text-gray-600 dark:text-gray-400">
            <Loader2 className="h-8 w-8 animate-spin text-blue-500 dark:text-blue-400" />
            <p className="ml-3">Carregando tarefas...</p>
          </div>
        ) : filteredTasks.length === 0 && !loading ? ( // Mostra mensagem de "nenhuma tarefa" se não houver tarefas e não estiver carregando
          <div className="p-8 text-center rounded-lg shadow-inner
                          bg-gray-100 dark:bg-gray-800 text-gray-500 dark:text-gray-400">
            <p className="text-lg font-medium">Nenhuma tarefa encontrada.</p>
            <p className="text-sm mt-2">Ajuste seus filtros ou agende uma nova tarefa.</p>
          </div>
        ) : (
          <div className="overflow-x-auto border rounded-lg shadow-md
                          bg-white dark:bg-gray-800 dark:border-gray-700">
            {/* Cabeçalho da tabela */}
            <div
              className="grid gap-4 p-4 text-sm font-semibold sticky top-0 border-b rounded-t-lg
                         bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-200 border-gray-200 dark:border-gray-600"
              style={gridCols}
            >
              <input
                type="checkbox"
                checked={selected.length === filteredTasks.length && filteredTasks.length > 0}
                onChange={(e) => (e.target.checked ? selectAll() : clearSelect())}
                className="form-checkbox h-4 w-4 text-blue-600 rounded dark:bg-gray-800 dark:border-gray-600 dark:checked:bg-blue-600 dark:checked:border-blue-600"
              />
              <div>Modo</div>
              <div className="truncate">Canal YouTube</div>
              <div className="truncate">Agendado Para</div>
              <div>Status</div>
              <div>Ações</div>
            </div>

            {/* Linhas da tabela */}
            <div className="divide-y divide-gray-200 dark:divide-gray-700">
              {filteredTasks.map((t) => (
                <div
                  key={t.task_id}
                  className="grid gap-4 p-4 items-center transition-colors
                             hover:bg-blue-50 dark:hover:bg-gray-700" // Cor de hover
                  style={gridCols}
                >
                  <input
                    type="checkbox"
                    checked={selected.includes(t.task_id)}
                    onChange={() => toggleSelect(t.task_id)}
                    className="form-checkbox h-4 w-4 text-blue-600 rounded dark:bg-gray-800 dark:border-gray-600 dark:checked:bg-blue-600 dark:checked:border-blue-600"
                  />
                  <div className="flex items-center gap-2 font-medium text-gray-800 dark:text-gray-100">
                    <Play size={16} className={t.status === 'Running' ? 'text-green-500 animate-pulse' : 'text-gray-400 dark:text-gray-500'} />
                    <span>{t.mode}</span>
                  </div>
                  <div className="text-gray-600 dark:text-gray-400 truncate text-sm">{t.yt_channel}</div>
                  <div className="text-gray-600 dark:text-gray-400 whitespace-nowrap text-sm">{t.scheduled_time}</div>
                  <div>
                    <Badge
                      className={`font-semibold text-xs px-2 py-1 rounded-full border
                                  ${t.status === 'Running'
                          ? 'bg-green-100 text-green-700 border-green-300 dark:bg-green-900 dark:text-green-300 dark:border-green-700'
                          : t.status === 'Completed'
                            ? 'bg-blue-100 text-blue-700 border-blue-300 dark:bg-blue-900 dark:text-blue-300 dark:border-blue-700'
                            : 'bg-gray-100 text-gray-700 border-gray-300 dark:bg-gray-700 dark:text-gray-300 dark:border-gray-600'
                        }`}
                    >
                      {t.status.toUpperCase()}
                    </Badge>
                  </div>
                  <Button
                    size="sm"
                    variant="ghost"
                    onClick={() => deleteTask(t.task_id)}
                    aria-label={`Deletar tarefa ${t.task_id}`}
                    className="text-red-500 hover:bg-red-50 hover:text-red-700 rounded-md p-2
                               dark:text-red-400 dark:hover:bg-red-900 dark:hover:text-red-300"
                  >
                    <Trash2 size={16} />
                  </Button>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Ações em Massa */}
        {selected.length > 0 && (
          <div className="flex justify-end gap-2 p-4 border-t rounded-b-lg shadow-sm
                          bg-white dark:bg-gray-800 dark:border-gray-700">
            <Button
              size="sm"
              variant="outline"
              onClick={clearSelect}
              className="rounded-md
                         border-gray-300 text-gray-700 hover:bg-gray-100
                         dark:border-gray-600 dark:text-gray-300 dark:hover:bg-gray-700"
            >
              Limpar Seleção ({selected.length})
            </Button>
            <Button
              size="sm"
              onClick={() => {
                // Aqui você pode adicionar um modal de confirmação antes de deletar múltiplos
                selected.forEach(deleteTask);
                setSelected([]); // Limpa a seleção após a ação
              }}
              className="bg-red-500 hover:bg-red-600 text-white shadow-md rounded-md
                         dark:bg-red-600 dark:hover:bg-red-700"
            >
              <Trash2 size={16} className="mr-2" />
              Excluir Selecionados
            </Button>
          </div>
        )}
      </CardContent>
    </Card>
  );
};

export default TaskController;