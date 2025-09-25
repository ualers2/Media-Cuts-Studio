// TasksPage.tsx
import React, { useEffect, useState } from 'react';
import TaskComponent from '../components/TaskComponent';

interface TasksPageProps {
  videoUrl: string;
}
const TasksPage: React.FC<TasksPageProps> = ({
  videoUrl
}) => {

  const [ytChannel, setYtChannel] = useState('');
  const [apiKey, setApiKey] = useState(''); 
  useEffect(() => {
    const config = localStorage.getItem('user_config');
    if (config) {
      const parsedConfig = JSON.parse(config);
      setYtChannel(parsedConfig.ytChannel ?? '');
      setApiKey(parsedConfig.apiKey ?? '');
    }
  }, []);

  return (
    <div className="min-h-screen p-6 space-y-6 bg-white dark:bg-gray-950 transition-colors duration-300">
      <TaskComponent
        ytChannel={ytChannel}
        setYtChannel={setYtChannel}
        apiKey={apiKey}
        setApiKey={setApiKey} 
        videoUrl={videoUrl}
      />
    </div>
  );
};

export default TasksPage;