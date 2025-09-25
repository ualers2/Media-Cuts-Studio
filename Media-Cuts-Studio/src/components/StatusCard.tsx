
import { Badge } from '@/components/ui/badge';
import { Card, CardContent, CardHeader } from '@/components/ui/card';
import { Check, X, AlertTriangle, HelpCircle } from 'lucide-react';
import { Service } from '@/types/service';

interface StatusCardProps {
  service: Service;
  isLoading: boolean;
}

export const StatusCard = ({ service, isLoading }: StatusCardProps) => {
  const getStatusIcon = () => {
    if (isLoading) {
      return <div className="w-5 h-5 bg-slate-300 rounded-full animate-pulse" />;
    }
    
    switch (service.status) {
      case 'online':
        return <Check className="w-5 h-5 text-green-600" />;
      case 'offline':
        return <X className="w-5 h-5 text-red-600" />;
      case 'warning':
        return <AlertTriangle className="w-5 h-5 text-yellow-600" />;
      default:
        return <HelpCircle className="w-5 h-5 text-slate-400" />;
    }
  };

  const getStatusColor = () => {
    switch (service.status) {
      case 'online':
        return 'bg-green-50 border-green-200';
      case 'offline':
        return 'bg-red-50 border-red-200';
      case 'warning':
        return 'bg-yellow-50 border-yellow-200';
      default:
        return 'bg-slate-50 border-slate-200';
    }
  };

  const getBadgeVariant = () => {
    switch (service.status) {
      case 'online':
        return 'default' as const;
      case 'offline':
        return 'destructive' as const;
      case 'warning':
        return 'secondary' as const;
      default:
        return 'outline' as const;
    }
  };

  const getStatusText = () => {
    switch (service.status) {
      case 'online':
        return 'Online';
      case 'offline':
        return 'Offline';
      case 'warning':
        return 'Warning';
      default:
        return 'Unknown';
    }
  };

  return (
    <Card className={`transition-all duration-200 hover:shadow-md ${getStatusColor()}`}>
      <CardHeader className="pb-3">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-2">
            {getStatusIcon()}
            <h3 className="font-semibold text-slate-800 text-sm truncate">
              {service.name}
            </h3>
          </div>
        </div>
      </CardHeader>
      <CardContent className="pt-0">
        <div className="space-y-3">
          <div className="flex items-center justify-between">
            <Badge variant={getBadgeVariant()} className="text-xs">
              {getStatusText()}
            </Badge>
            {service.responseTime && (
              <span className="text-xs text-slate-500">
                {service.responseTime}ms
              </span>
            )}
          </div>
          
          <div className="text-xs text-slate-600 break-all">
            {service.url}
          </div>
          
          {service.message && (
            <div className="text-xs text-slate-500 bg-slate-100 rounded p-2 mt-2">
              {service.message}
            </div>
          )}
          
          <div className="text-xs text-slate-400">
            Last checked: {service.lastChecked.toLocaleTimeString('pt-BR')}
          </div>
        </div>
      </CardContent>
    </Card>
  );
};
