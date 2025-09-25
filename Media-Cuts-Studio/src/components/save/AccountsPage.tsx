import React, { useState, useEffect } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogFooter } from '@/components/ui/dialog';
import { Textarea } from '@/components/ui/textarea';

const AccountsPage: React.FC = () => {
  const [newAccountUsername, setNewAccountUsername] = useState('');
  const [cookieInput, setCookieInput] = useState('');
  const [newIgUsername, setNewIgUsername] = useState('');
  const [newIgPassword, setNewIgPassword] = useState('');
  const [showTikTokModal, setShowTikTokModal] = useState(false);
  const [accounts, setAccounts] = useState<any[]>([]);
  const apiUrl = import.meta.env.VITE_LANDING_API;

  useEffect(() => {
    fetch(`${apiUrl}/api/accounts/active`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ api_key: localStorage.getItem('api_key') }),
    })
      .then(res => res.json())
      .then(setAccounts)
      .catch(console.error);
  }, []);

  // Funções para TikTok
  const handleOpenTikTokModal = () => {
    setCookieInput('');
    setShowTikTokModal(true);
  };

  const handleSaveTikTok = () => {
    fetch(`${apiUrl}/api/new-account/tiktok`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        api_key: localStorage.getItem('api_key'),
        TiktokAccountUser: newAccountUsername,
        TiktokAccountCookies: cookieInput
      }),
    })
      .then(() => refreshAccounts())
      .finally(() => setShowTikTokModal(false));
  };

  // Funções para Instagram
  const handleAddInstagram = () => {
    fetch(`${apiUrl}/api/new-account/instagram`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        api_key: localStorage.getItem('api_key'),
        ig_username: newIgUsername,
        ig_password: newIgPassword
      }),
    })
      .then(res => {
        if (!res.ok) throw new Error('Erro ao adicionar conta Instagram');
        return res.json();
      })
      .then(() => {
        setNewIgUsername('');
        setNewIgPassword('');
        refreshAccounts();
      })
      .catch(err => console.error(err));
  };

  // Atualiza lista de contas
  const refreshAccounts = () => {
    fetch(`${apiUrl}/api/accounts/active`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ api_key: localStorage.getItem('api_key') }),
    })
      .then(res => res.json())
      .then(setAccounts)
      .catch(console.error);
  };

  return (
    <div className="p-6 bg-gray-50 dark:bg-gray-900 min-h-screen text-gray-900 dark:text-gray-100 transition-colors duration-300">
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Card: Adicionar TikTok */}
        <Card className="bg-white dark:bg-gray-800 border dark:border-gray-700 shadow-sm">
          <CardHeader>
            <CardTitle className="text-gray-900 dark:text-gray-100">Adicionar conta TikTok</CardTitle>
          </CardHeader>
          <CardContent>
            <Input
              placeholder="Username TikTok"
              value={newAccountUsername}
              onChange={e => setNewAccountUsername(e.target.value)}
              className="mb-4"
            />
            <Button onClick={handleOpenTikTokModal} className="w-full">
              Add TikTok Account
            </Button>
          </CardContent>
        </Card>

        {/* Card: Adicionar Instagram */}
        {/* <Card className="bg-white dark:bg-gray-800 border dark:border-gray-700 shadow-sm">
          <CardHeader>
            <CardTitle className="text-gray-900 dark:text-gray-100">Adicionar conta Instagram</CardTitle>
          </CardHeader>
          <CardContent>
            <Input
              placeholder="Telefone, Username ou email Instagram"
              value={newIgUsername}
              onChange={e => setNewIgUsername(e.target.value)}
              className="mb-4"
            />
            <Input
              placeholder="Senha Instagram"
              type="password"
              value={newIgPassword}
              onChange={e => setNewIgPassword(e.target.value)}
              className="mb-4"
            />
            <Button
              onClick={handleAddInstagram}
              disabled={!newIgUsername || !newIgPassword}
              className="w-full"
            >
              Adicionar conta Instagram
            </Button>
          </CardContent>
        </Card> */}

        {/* Card: Contas Ativas */}
        <Card className="bg-white dark:bg-gray-800 border dark:border-gray-700 shadow-sm lg:col-span-2">
          <CardHeader>
            <CardTitle className="text-gray-900 dark:text-gray-100">Contas Ativas</CardTitle>
          </CardHeader>
          <CardContent>
            {accounts.map(acc => (
              <div
                key={acc.id}
                className="flex justify-between items-center p-3 rounded-lg mb-2 bg-gray-50 dark:bg-gray-700 border border-gray-200 dark:border-gray-600"
              >
                <div>
                  <p className="font-medium text-gray-900 dark:text-gray-100">{acc.platform}</p>
                  <p className="text-sm text-gray-600 dark:text-gray-400">{acc.username}</p>
                </div>
                <Badge variant={acc.status === 'active' ? 'default' : 'secondary'}>{acc.status}</Badge>
              </div>
            ))}
          </CardContent>
        </Card>
      </div>

      {/* Modal para TikTok */}
      <Dialog open={showTikTokModal} onOpenChange={setShowTikTokModal}>
        <DialogContent className="bg-white dark:bg-gray-800 border dark:border-gray-700">
          <DialogHeader>
            <DialogTitle className="text-gray-900 dark:text-gray-100">Inserir Cookie TikTok</DialogTitle>
          </DialogHeader>
          <p className="mb-4 text-sm text-gray-700 dark:text-gray-300">
            Após fazer login no TikTok em outra aba, copie o cookie <code className="bg-gray-100 dark:bg-gray-900 px-1 py-0.5 rounded text-gray-800 dark:text-gray-200">sessionid</code> e cole aqui:
          </p>
          <Textarea
            placeholder="sessionid=...;"
            value={cookieInput}
            onChange={e => setCookieInput(e.target.value)}
            rows={4}
            className="bg-gray-100 dark:bg-gray-900 text-gray-800 dark:text-gray-200 border border-gray-200 dark:border-gray-700"
          />
          <DialogFooter>
            <Button onClick={handleSaveTikTok} disabled={!cookieInput || !newAccountUsername} className="w-full">OK</Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>
    </div>
  );
};

export default AccountsPage;
