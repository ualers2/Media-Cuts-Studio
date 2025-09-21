// Tasks.tsx
import React from 'react';
import Layout from '@/components/Layout';
import TasksPage from '@/pages/TasksPage';
import ProtectedRoute from '@/components/ProtectedRoute';
import { useLocation } from 'react-router-dom';

const Tasks = () => {
  const location = useLocation();
  const params = new URLSearchParams(location.search);
  const videoUrl = params.get('video_url') || '';


  return (
    <ProtectedRoute>
      <Layout>
        <TasksPage videoUrl={videoUrl} />
      </Layout>
    </ProtectedRoute>
  );
};

export default Tasks;
