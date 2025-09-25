// image-refresher-react\src\pages\Tasks.tsx
import React from 'react';
import Layout from '@/components/Layout';
import TasksGramFlowPage from '@/components/save/TasksGramFlowPage';
import ProtectedRoute from '@/components/ProtectedRoute';

const TasksGramFlow = () => {
  return (
    <ProtectedRoute>
      <Layout>
        <TasksGramFlowPage />
      </Layout>
    </ProtectedRoute>
  );
};

export default TasksGramFlow;
