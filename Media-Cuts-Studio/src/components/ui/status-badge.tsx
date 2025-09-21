import { Badge } from '@/components/ui/badge';
import { cn } from '@/lib/utils';

import {
  AlertCircle, FileText, CheckCircle,
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
interface StatusBadgeProps {
  status: 'draft' | 'scheduled' | 'published' | 'error';
  className?: string;
}
const statusMap = {
  draft: { icon: Pencil, label: 'Rascunho', color: 'text-yellow-500' },
  scheduled: { icon: Clock, label: 'Agendado', color: 'text-blue-500' },
  published: { icon: Check, label: 'Publicado', color: 'text-green-500' },
  error: { icon: AlertTriangle, label: 'Erro', color: 'text-red-500' },
  canceled: { icon: AlertTriangle, label: 'Canceled', color: 'text-red-500' }
};
const statusConfig = {
  draft: {
    label: 'Rascunho',
    icon: FileText,
    className: 'bg-muted text-muted-foreground'
  },
  scheduled: {
    label: 'Agendado',
    icon: Clock,
    className: 'bg-primary/10 text-primary'
  },
  published: {
    label: 'Publicado',
    icon: CheckCircle,
    className: 'bg-success/10 text-success'
  },
  error: {
    label: 'Erro',
    icon: AlertCircle,
    className: 'bg-error/10 text-error'
  }
};

export function StatusBadge({ status }: { status: string }) {
  // 1) Normalize o valor
  const key = status.trim().toLowerCase();

  // 2) Tenta buscar o mapeamento
  const data = statusMap[key];

  // 3) Se não existir, renderiza um badge genérico
  if (!data) {
    console.warn(`[StatusBadge] status desconhecido: "${status}"`);
    return <Badge className="text-gray-500">Desconhecido</Badge>;
  }

  // 4) Se existir, renderiza normalmente
  const Icon = data.icon;
  return (
    <Badge className={data.color}>
      <Icon className="mr-1 h-4 w-4" />
      {data.label}
    </Badge>
  );
}