// image-refresher-react\src\pages\Accounts.tsx
import React from 'react';
import Layout from '@/components/Layout';
import AccountsPage from '@/components/save/AccountsPage';
import ProtectedRoute from '@/components/ProtectedRoute';

const Accounts = () => {
  return (
    <ProtectedRoute>
      <Layout>
        <AccountsPage />
      </Layout>
    </ProtectedRoute>
  );
};

export default Accounts;
