// web_project\src\components\TasksGramFlowPage.tsx
import React, { useEffect, useState } from 'react';
import TaskGramFlowScheduler from './TaskGramFlowScheduler';

const TasksGramFlowPage: React.FC = () => {
  const [scheduleMode, setScheduleMode] = useState('date');
  const [timezone, setTimezone] = useState('America/Sao_Paulo');
  const [apiKey, setApiKey] = useState(''); 


  useEffect(() => {
    const config = localStorage.getItem('user_config_GramFlow');
    if (config) {
      const parsedConfig = JSON.parse(config);
      setScheduleMode(parsedConfig.scheduleMode ?? 'date');
      setDateTime(parsedConfig.dateTime ?? '');
      setTimezone(parsedConfig.timezone ?? 'America/Sao_Paulo');
      setScheduleMonthly(parsedConfig.scheduleMonthly ?? false);
      setYtChannel(parsedConfig.ytChannel ?? '');
      setApiKey(parsedConfig.apiKey ?? ''); // Carregando, mas não usado.
      setCuttingSeconds(parsedConfig.cuttingSeconds ?? 60);
    }
  }, []);

  return (
    <div className="min-h-screen p-6 space-y-6 bg-white dark:bg-gray-950 transition-colors duration-300">
      <TaskGramFlowScheduler
        scheduleMode={scheduleMode}
        setScheduleMode={setScheduleMode}
        timezone={timezone}
        setTimezone={setTimezone}
        apiKey={apiKey}
        setApiKey={setApiKey} 
      />
    </div>
  );
};

export default TasksGramFlowPage;