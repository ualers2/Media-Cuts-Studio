import React, { useEffect, useState } from 'react';
import Layout from '../components/Layout';
import ProtectedRoute from '../components/ProtectedRoute';
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from '@/components/ui/card';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { Eye, EyeOff, Mail, Key, Server, Calendar, Bell, SlidersHorizontal } from "lucide-react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Switch } from '@/components/ui/switch';
import { Label } from '@/components/ui/label';

const MyAccount = () => {
  const [show, setShow] = useState(false);
  const [accountData, setAccountData] = useState({
    email: '',
    api_key: '',
    apiServer: '',
    expiration: '',
  });

  // useEffect para carregar dados do localStorage
  useEffect(() => {
    const data = localStorage.getItem('account_data');
    if (data) {
      setAccountData(JSON.parse(data));
    }
  }, []);

  return (
    <ProtectedRoute>
      <Layout>
        {/* Container principal para a página, centralizado e com padding responsivo */}
        <div className="p-4 md:p-8 bg-gray-50 dark:bg-gray-900 min-h-screen text-gray-900 dark:text-gray-100 transition-colors duration-300 flex justify-center items-start">
          {/* Card principal com um visual mais moderno e elevado */}
          <Card className="w-full max-w-4xl bg-white dark:bg-gray-800 border dark:border-gray-700 shadow-xl rounded-2xl overflow-hidden">
            <CardHeader className="p-6 md:p-8 border-b dark:border-gray-700 bg-gray-50 dark:bg-gray-900">
              <CardTitle className="flex items-center gap-3 text-2xl font-bold">
                <SlidersHorizontal size={24} /> Configurações da Conta
              </CardTitle>
              <CardDescription className="mt-1 text-gray-600 dark:text-gray-400">
                Gerencie suas informações de conta e preferências de notificação.
              </CardDescription>
            </CardHeader>

            <CardContent className="p-6 md:p-8">
              <Tabs defaultValue="settings" className="w-full">
                {/* Lista de abas com estilo aprimorado */}
                <TabsList className="bg-gray-200 dark:bg-gray-700 mb-6 rounded-lg p-1">
                  <TabsTrigger
                    value="settings"
                    className="data-[state=active]:bg-white data-[state=active]:text-gray-900 dark:data-[state=active]:bg-gray-900 dark:data-[state=active]:text-gray-100 dark:text-gray-300 data-[state=active]:shadow-sm rounded-md transition-all duration-200"
                  >
                    Informações
                  </TabsTrigger>
                  <TabsTrigger
                    value="notifications"
                    className="data-[state=active]:bg-white data-[state=active]:text-gray-900 dark:data-[state=active]:bg-gray-900 dark:data-[state=active]:text-gray-100 dark:text-gray-300 data-[state=active]:shadow-sm rounded-md transition-all duration-200"
                  >
                    Notificações
                  </TabsTrigger>
                </TabsList>

                {/* Conteúdo da aba de Informações */}
                <TabsContent value="settings" className="space-y-6">
                  <div className="space-y-4">
                    <h3 className="text-xl font-semibold mb-2 flex items-center gap-2">
                      <Key size={20} /> Detalhes da API
                    </h3>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                      {/* Campo de API Server */}
                      <div>
                        <Label htmlFor="apiServer" className="block text-sm font-medium mb-2 flex items-center gap-1">
                          <Server size={16} /> Servidor da API:
                        </Label>
                        <Input id="apiServer" value={accountData.apiServer ?? "#1 API Media Cuts Studio"} readOnly className="dark:bg-gray-700 dark:border-gray-600 dark:text-gray-200" />
                      </div>

                      {/* Campo de Chave API com botão de visibilidade */}
                      <div>
                        <Label htmlFor="apiKey" className="block text-sm font-medium mb-2 flex items-center gap-1">
                          <Key size={16} /> Chave API:
                        </Label>
                        <div className="relative">
                          <Input
                            id="apiKey"
                            type={show ? "text" : "password"}
                            value={accountData.api_key ?? ""}
                            readOnly
                            className="pr-10 dark:bg-gray-700 dark:border-gray-600 dark:text-gray-200"
                          />
                          <Button
                            type="button"
                            variant="ghost"
                            size="icon"
                            onClick={() => setShow((prev) => !prev)}
                            className="absolute right-1 top-1/2 -translate-y-1/2 text-gray-600 dark:text-gray-400 hover:bg-gray-200 dark:hover:bg-gray-700 rounded-full"
                          >
                            {show ? <EyeOff size={16} /> : <Eye size={16} />}
                          </Button>
                        </div>
                      </div>

                      {/* Campo de Email */}
                      <div>
                        <Label htmlFor="email" className="block text-sm font-medium mb-2 flex items-center gap-1">
                          <Mail size={16} /> E-mail:
                        </Label>
                        <Input id="email" value={accountData.email ?? ""} readOnly className="dark:bg-gray-700 dark:border-gray-600 dark:text-gray-200" />
                      </div>

                      {/* Campo de Expiração da Licença */}
                      <div>
                        <Label htmlFor="expiration" className="block text-sm font-medium mb-2 flex items-center gap-1">
                          <Calendar size={16} /> Expiração da Licença:
                        </Label>
                        <Input id="expiration" value={accountData.expiration ?? ""} readOnly className="dark:bg-gray-700 dark:border-gray-600 dark:text-gray-200" />
                      </div>
                    </div>
                  </div>

                 
                  
                </TabsContent>

                {/* Conteúdo da aba de Notificações */}
                <TabsContent value="notifications" className="mt-4">
                  <div className="space-y-4">
                    <h3 className="text-xl font-semibold mb-2 flex items-center gap-2">
                      <Bell size={20} /> Configurações de Notificações
                    </h3>
                    <div className="flex items-center justify-between">
                      <Label htmlFor="app-notifications" className="text-base cursor-pointer">🔔 Notificações no Aplicativo</Label>
                      <Switch id="app-notifications" defaultChecked />
                    </div>
                  </div>
                </TabsContent>
              </Tabs>
            </CardContent>
          </Card>
        </div>
      </Layout>
    </ProtectedRoute>
  );
};

export default MyAccount;
