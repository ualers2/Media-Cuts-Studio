
export interface Service {
  name: string;
  url: string;
  type: 'api' | 'website';
  status: 'online' | 'offline' | 'warning' | 'unknown';
  lastChecked: Date;
  responseTime?: number;
  message?: string;
}
