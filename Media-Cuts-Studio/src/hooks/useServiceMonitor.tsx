// hooks/useServiceMonitor.ts
import { useState, useCallback, useEffect } from 'react';

// Define the Service type directly or ensure it's available from a shared types file
// For this example, I'll define it here. In a real project, keep it in '@/types/service'.
export type Service = {
  name: string;
  url: string;
  type: 'api' | 'website';
  status: 'online' | 'offline' | 'warning' | 'unknown';
  lastChecked: Date;
  responseTime?: number;
  message?: string;
};

export const useServiceMonitor = () => {
  const [services, setServices] = useState<Service[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  // Assuming VITE_LANDING_API points to the base URL of your backend
  const VITE_LANDING_API = import.meta.env.VITE_LANDING_API || 'http://localhost:5000'; // Fallback for development

  const updateAllServices = useCallback(async () => {
    setIsLoading(true);
    try {
      // Fetch the latest status from the backend endpoint
      const response = await fetch(`${VITE_LANDING_API}/api/status/latest`);

      if (!response.ok) {
        console.error('Failed to fetch latest service status from backend:', response.statusText);
        // Set services to a state indicating an error or keep previous state
        setServices(prevServices => prevServices.map(service => ({
          ...service,
          status: 'unknown',
          message: 'Failed to fetch status from backend',
          lastChecked: new Date(),
        })));
        return;
      }

      const data = await response.json();
      
      const timestampKeys = Object.keys(data);
      if (timestampKeys.length === 0) {
        console.warn('Nenhum timestamp retornado do backend');
        return;
      }

      // Encontra a chave cujo objeto tem o timestamp interno mais recente:
      const latestTimestampKey = timestampKeys.reduce((latestKey, currentKey) => {
        // timestamp vindo do backend, ex: "2025-07-01T23:33:53.797180Z"
        const latestTs   = new Date(data[latestKey].timestamp).getTime();
        const currentTs  = new Date(data[currentKey].timestamp).getTime();
        return currentTs > latestTs ? currentKey : latestKey;
      }, timestampKeys[0]);

      console.log('Chave mais recente encontrada:', latestTimestampKey);
      const latestStatusData = data[latestTimestampKey];


      if (latestStatusData && latestStatusData.services) {
        // Map the backend data to the frontend Service type, converting date strings back to Date objects
        const updatedServices: Service[] = latestStatusData.services.map((service: any) => ({
          name: service.name,
          url: service.url,
          type: service.type,
          status: service.status,
          lastChecked: new Date(service.lastChecked), // Convert ISO string back to Date object
          responseTime: service.responseTime,
          message: service.message,
        }));
        setServices(updatedServices);
        console.log('Service status fetched successfully from backend.');
      } else {
        console.warn('No service data found in the latest status response from backend.');
        setServices([]); // Clear services if no data is found
      }
    } catch (error) {
      console.error('Error fetching service status from backend:', error);
      // Set services to an error state
      setServices(prevServices => prevServices.map(service => ({
        ...service,
        status: 'offline',
        message: `Network error: ${error instanceof Error ? error.message : 'Unknown error'}`,
        lastChecked: new Date(),
      })));
    } finally {
      setIsLoading(false);
    }
  }, [VITE_LANDING_API]);

  // Initial fetch when the component mounts
  useEffect(() => {
    updateAllServices();
  }, [updateAllServices]);

  return {
    services,
    isLoading,
    updateAllServices,
  };
};