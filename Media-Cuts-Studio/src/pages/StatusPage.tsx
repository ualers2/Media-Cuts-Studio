
// webproject\src\pages\StatusPage.tsx
import React, { useState, useEffect } from 'react';
import { StatusCard } from '@/components/StatusCard';
import { StatusLegend } from '@/components/StatusLegend';
import { useServiceMonitor } from '@/hooks/useServiceMonitor';
import { RefreshCw } from 'lucide-react';
import { Button } from '@/components/ui/button';

const StatusPage = () => {
  const { services, isLoading, updateAllServices } = useServiceMonitor();
  const [lastUpdate, setLastUpdate] = useState<Date>(new Date());

  const handleRefresh = async () => {
    await updateAllServices();
    setLastUpdate(new Date()); // Update lastUpdate after fetching new data
  };

  useEffect(() => {
    // Initial fetch when component mounts (already handled by useServiceMonitor's useEffect)
    // We only need to set the initial lastUpdate time here if services are loaded immediately
    if (services.length > 0) {
        setLastUpdate(new Date());
    }

    const interval = setInterval(() => {
      updateAllServices();
      setLastUpdate(new Date()); // Update lastUpdate after each interval fetch
    }, 60000); // Update every minute

    return () => clearInterval(interval);
  }, [updateAllServices, services.length]); // Add services.length to dependencies to re-evaluate if services are initially empty

  const calculateUptime = () => {
    if (services.length === 0) return '0.0';
    const onlineServices = services.filter(service => service.status === 'online').length;
    return ((onlineServices / services.length) * 100).toFixed(1);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 p-4 font-sans">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="flex items-center justify-between mb-8">
          <div className="flex items-center space-x-4">
            <div className="w-12 h-12 bg-blue-600 rounded-lg flex items-center justify-center">
              <div className="w-8 h-8 bg-white rounded transform rotate-45 relative">
                <div className="absolute inset-1 bg-blue-600 rounded"></div>
              </div>
            </div>
            <div>
              <h1 className="text-3xl font-bold text-slate-800">Media Cuts Studio</h1>
              <p className="text-slate-600">Service Status Monitor</p>
            </div>
          </div>
          
          <div className="flex items-center space-x-4">
            <div className="text-right">
              <div className="text-sm text-slate-600">
                {new Date().toLocaleDateString('pt-BR', {
                  year: 'numeric',
                  month: '2-digit',
                  day: '2-digit',
                  hour: '2-digit',
                  minute: '2-digit',
                  second: '2-digit'
                })} (GMT-03:00)
              </div>
              <div className="text-xs text-slate-500">
                Last update: {lastUpdate.toLocaleTimeString('pt-BR')}
              </div>
            </div>
            <Button 
              onClick={handleRefresh} 
              disabled={isLoading}
              variant="outline"
              size="sm"
              className="flex items-center space-x-2 rounded-md shadow-sm hover:bg-slate-50"
            >
              <RefreshCw className={`h-4 w-4 ${isLoading ? 'animate-spin' : ''}`} />
              <span>Refresh</span>
            </Button>
          </div>
        </div>

        {/* Overview Stats */}
        <div className="bg-white rounded-lg shadow-sm border p-6 mb-8">
          <h2 className="text-xl font-semibold text-slate-800 mb-4">Overview</h2>
          <div className="flex items-center justify-between">
            <div className="text-sm text-slate-600">Overall System Status</div>
            <div className="flex items-center space-x-4">
              <span className="text-sm font-medium text-slate-700">
                Uptime: {calculateUptime()}%
              </span>
              <div className="w-24 h-2 bg-slate-200 rounded-full overflow-hidden">
                <div 
                  className="h-full bg-green-500 transition-all duration-500 rounded-full"
                  style={{ width: `${calculateUptime()}%` }}
                ></div>
              </div>
            </div>
          </div>
        </div>

        {/* Services Grid */}
        <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 mb-8">
          {services.length > 0 ? (
            services.map((service) => (
              <StatusCard 
                key={service.name} 
                service={service}
                isLoading={isLoading} // Pass isLoading to StatusCard if needed for visual feedback
              />
            ))
          ) : (
            <div className="col-span-full text-center text-slate-500 py-10">
              {isLoading ? 'Loading services...' : 'No services to display or failed to load.'}
            </div>
          )}
        </div>

        {/* Legend */}
        <StatusLegend />
      </div>
    </div>
  );
};

export default StatusPage;
