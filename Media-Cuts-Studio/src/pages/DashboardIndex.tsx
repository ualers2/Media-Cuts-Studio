
import React from 'react';
import Layout from '@/components/Layout';
import DashboardPage from '@/components/DashboardPage';
import DashboardSheduler from '@/components/save/DashboardSheduler';
import ProtectedRoute from '@/components/ProtectedRoute';

const DashboardIndex = () => {
  return (
    <ProtectedRoute>
      <Layout>
        <DashboardPage />
        {/* <DashboardSheduler /> */}
      </Layout>          
    </ProtectedRoute>
  );
};

export default DashboardIndex;
