import { Toaster } from "@/components/ui/toaster";
import { Toaster as Sonner } from "@/components/ui/sonner";
import { TooltipProvider } from "@/components/ui/tooltip";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { AuthProvider, useAuth } from "@/contexts/AuthContext";
import { PostProvider } from "@/contexts/PostContext";
import { LoginForm } from "@/components/auth/LoginForm";
import { Layout } from "@/components/layout/Layout";
import Dashboard from "./pages/Dashboard";
import NewPost from "./pages/NewPost";
import BulkSchedule from "./pages/BulkSchedule";
import Calendar from "./pages/Calendar";
import PostList from "./pages/PostList";
import NotFound from "./pages/NotFound";
import AuthenticateAccount from './pages/AuthenticateAccount'; // O novo componente

const queryClient = new QueryClient();

function ProtectedRoute({ children }: { children: React.ReactNode }) {
  const { user, isLoading } = useAuth();
  
  if (isLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-primary"></div>
      </div>
    );
  }
  
  if (!user) {
    return <LoginForm />;
  }
  
  return <>{children}</>;
}

function AppRoutes() {
  return (
    <Routes>
      <Route path="/login" element={<LoginForm />} />
      <Route path="/" element={
        <ProtectedRoute>
          <Layout />
        </ProtectedRoute>
      }>
        <Route path="/authenticate-account" element={<AuthenticateAccount />} />
        <Route index element={<Dashboard />} />
        <Route path="new-post" element={<NewPost />} />
        <Route path="bulk-schedule" element={<BulkSchedule />} />
        <Route path="calendar" element={<Calendar />} />
        <Route path="posts" element={<PostList />} />
        <Route path="settings" element={<div>Configurações em desenvolvimento</div>} />
      </Route>
      <Route path="*" element={<NotFound />} />
    </Routes>
  );
}

const App = () => (
  <QueryClientProvider client={queryClient}>
    <AuthProvider>
      <PostProvider>
        <TooltipProvider>
          <Toaster />
          <Sonner />
          <BrowserRouter>
            <AppRoutes />
          </BrowserRouter>
        </TooltipProvider>
      </PostProvider>
    </AuthProvider>
  </QueryClientProvider>
);

export default App;
