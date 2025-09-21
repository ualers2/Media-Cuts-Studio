// src/App.tsx
import "./tailwind.css";
import './vars.css';
import React from 'react';
import { TooltipProvider } from './components/ui/tooltip';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

// Importe todos os seus componentes de página
import Projects from './pages/Projects';
import Index from './pages/Index';
import SignupCheckout from './pages/SignupCheckout';
import Login from './pages/Login';
import DashboardIndex from './pages/DashboardIndex';
import MyAccount from './pages/MyAccount';
import NotFound from './pages/NotFound';
import StatusPage from './pages/StatusPage';
import CheckoutSuccess from './pages/CheckoutSuccess';
import CheckoutError from './pages/CheckoutError';
import PrivacyPolicy from './pages/PrivacyPolicy';
import TermsOfService from './pages/TermsOfService';
import LeadCapture from './pages/LeadCapture';

import AuthenticateAccount from './pages/AuthenticateAccount';
import BulkSchedule from './pages/BulkSchedule';
import Calendar from './pages/Calendar';
import NewPost from './pages/NewPost';
import PostList from './pages/PostList';
import Tasks from './pages/Tasks';


import { PostProvider } from './contexts/PostContext';
import { ThemeProvider } from './contexts/ThemeContext';
import { SocketProvider } from './contexts/SocketContext';
import { AuthProvider } from './contexts/AuthContext';
import { ProjectsProvider } from './contexts/ProjectsContext'; // Importe o ProjectsProvider
import ProtectedRoute from './components/ProtectedRoute';

// Importe os componentes de toast
import { Toaster } from "./components/ui/toaster";
import { Toaster as Sonner } from "./components/ui/sonner";

const queryClient = new QueryClient();

const App = () => (
  <ThemeProvider>
    <QueryClientProvider client={queryClient}>
      <TooltipProvider>
        <Toaster />
        <Sonner />
        <AuthProvider>
          <PostProvider>
            <ProjectsProvider> {/* ProjectsProvider deve envolver o BrowserRouter/Routes */}
              <BrowserRouter>
                <SocketProvider> {/* SocketProvider pode envolver as Routes ou apenas as rotas que precisam dele */}
                  
                  <Routes>
                    {/* Rota pública, sem necessidade de autenticacao */}
                    <Route path="/" element={<Index />} />
                    <Route path="/login" element={<Login />} />
                    <Route path="/status" element={<StatusPage />} />
                    <Route path="/checkout" element={<SignupCheckout />} />
                    <Route path="/checkout/sucess" element={<CheckoutSuccess />} />
                    <Route path="/checkout/cancel" element={<CheckoutError />} />
                    <Route path="/privacy-policy" element={<PrivacyPolicy />} />
                    <Route path="/terms-of-use" element={<TermsOfService />} />
                    <Route path="/leads-form" element={<LeadCapture />} />
                    

                    {/* Rotas protegidas: só acessa se estiver autenticado */}
                    <Route
                      path="/dashboard"
                      element={
                        <ProtectedRoute>
                          <DashboardIndex />
                        </ProtectedRoute>
                      }
                    />

                    <Route
                      path="/shortify"
                      element={
                        <ProtectedRoute>
                          <Tasks />
                        </ProtectedRoute>
                      }
                    />
                    <Route
                      path="/posts"
                      element={
                        <ProtectedRoute>
                          <PostList />
                        </ProtectedRoute>
                      }
                    />
                    <Route
                      path="/calendar"
                      element={
                        <ProtectedRoute>
                          <Calendar />
                        </ProtectedRoute>
                      }
                    />
                    <Route
                      path="/bulk-schedule"
                      element={
                        <ProtectedRoute>
                          <BulkSchedule />
                        </ProtectedRoute>
                      }
                    />
                    <Route
                      path="/authenticate-account"
                      element={
                        <ProtectedRoute>
                          <AuthenticateAccount />
                        </ProtectedRoute>
                      }
                    />
                    <Route
                      path="/new-post"
                      element={
                        <ProtectedRoute>
                          <NewPost />
                        </ProtectedRoute>
                      }
                    />
                    <Route
                      path="/projects"
                      element={
                        <ProtectedRoute>
                          <Projects />
                        </ProtectedRoute>
                      }
                    />
                    
                    <Route
                      path="/my-account"
                      element={
                        <ProtectedRoute>
                          <MyAccount />
                        </ProtectedRoute>
                      }
                    />


                    {/* Caso nenhuma rota seja encontrada */}
                    <Route path="*" element={<NotFound />} />
                  </Routes>


                </SocketProvider>
              </BrowserRouter>
            </ProjectsProvider> 
          </PostProvider>          
        </AuthProvider>
      </TooltipProvider>
    </QueryClientProvider>
  </ThemeProvider>
);

export default App;