// image-refresher-react\src\pages\TaskController.tsx
import React from 'react';
import Layout from '@/components/Layout';
import TaskControllerPage from '@/components/save/TaskControllerPage';
import ProtectedRoute from '@/components/ProtectedRoute';

const TaskController = () => {
  return (
    <ProtectedRoute>
      <Layout>
        <TaskControllerPage />
      </Layout>
    </ProtectedRoute>
  );
};

export default TaskController;
