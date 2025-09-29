import React, { useState } from 'react';
import { Dialog, DialogContent, DialogClose } from '@radix-ui/react-dialog';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { toast } from '@/hooks/use-toast';
import { Youtube, Music, X, AlertCircle, Check } from 'lucide-react';
import Layout from '@/components/Layout';

export default function AuthenticateAccount() {
  const [activeTab, setActiveTab] = useState('youtube');
  const [channelName, setChannelName] = useState('');
  const [error, setError] = useState('');
  const [showTikTokModal, setShowTikTokModal] = useState(false);
  const [tiktokCookies, setTiktokCookies] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const API_BASE_URL = import.meta.env.VITE_SHEDULER_URL || 'http://localhost:5000/api';

  const handleAuthenticateYouTube = () => {
    if (!channelName.trim()) {
      setError('Por favor, insira o nome do canal para autenticar.');
      return;
    }
    setError('');
    setIsLoading(true);
    window.location.href = `${API_BASE_URL}/authenticate-google?canal_id=${encodeURIComponent(channelName.trim())}`;
  };

  const handleSaveTikTokCookies = async () => {
    if (!channelName.trim()) {
      setError('Por favor, insira o identificador da sua conta TikTok.');
      return;
    }
    if (!tiktokCookies.trim()) {
      setError('Por favor, cole os cookies da sua conta TikTok.');
      return;
    }

    setIsLoading(true);
    try {
      const resp = await fetch(`${API_BASE_URL}/api/canais`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          nome: channelName.trim(),
          socialNetwork: 'tiktok',
          token_content: tiktokCookies
        })
      });
      const json = await resp.json();
      if (!resp.ok) {
        throw new Error(json.error || 'Erro ao criar canal TikTok');
      }
      
      toast({
        title: 'Canal TikTok criado com sucesso!',
        description: `ID do canal: ${json.canal_id}`,
      });
      
      setShowTikTokModal(false);
      setChannelName('');
      setTiktokCookies('');
      setError('');
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Layout>
      <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-slate-50 to-blue-50 p-6">
        <div className="bg-white/80 backdrop-blur-sm p-8 rounded-3xl shadow-2xl w-full max-w-lg border border-white/20">
          {/* Header */}
          <div className="text-center mb-8">
            <div className="w-16 h-16 bg-gradient-to-r from-blue-500 to-purple-600 rounded-2xl flex items-center justify-center mx-auto mb-4">
              <div className="w-8 h-8 bg-white rounded-lg flex items-center justify-center">
                <div className="w-4 h-4 bg-gradient-to-r from-blue-500 to-purple-600 rounded"></div>
              </div>
            </div>
            <h1 className="text-3xl font-bold bg-gradient-to-r from-gray-800 to-gray-600 bg-clip-text text-transparent">
              Conectar Conta
            </h1>
            <p className="text-gray-500 mt-2">Autentique sua conta para começar</p>
          </div>

          {/* Abas modernas */}
          <div className="flex bg-gray-100/80 rounded-2xl p-1 mb-8">
            {[
              { key: 'youtube', label: 'YouTube', icon: Youtube, color: 'from-red-500 to-red-600' },
              { key: 'tiktok', label: 'TikTok', icon: Music, color: 'from-pink-500 to-purple-600' }
            ].map(tab => (
              <button
                key={tab.key}
                onClick={() => {
                  setActiveTab(tab.key);
                  setError('');
                  setChannelName('');
                }}
                className={`flex-1 flex items-center justify-center gap-2 px-6 py-3 rounded-xl font-semibold transition-all duration-300 ${
                  activeTab === tab.key
                    ? `bg-white shadow-lg text-gray-800 transform scale-105`
                    : 'text-gray-500 hover:text-gray-700 hover:bg-white/50'
                }`}
              >
                <tab.icon className={`w-5 h-5 ${activeTab === tab.key ? `bg-gradient-to-r ${tab.color} bg-clip-text text-transparent` : ''}`} />
                {tab.label}
              </button>
            ))}
          </div>

          {/* Conteúdo das abas */}
          <div className="space-y-6">
            {activeTab === 'youtube' && (
              <div className="space-y-6">
                <div className="text-center">
                  <div className="w-12 h-12 bg-gradient-to-r from-red-500 to-red-600 rounded-xl flex items-center justify-center mx-auto mb-4">
                    <Youtube className="w-6 h-6 text-white" />
                  </div>
                  <h2 className="text-xl font-bold text-gray-800 mb-2">
                    Conectar YouTube
                  </h2>
                  <p className="text-gray-600 text-sm">
                    Insira o nome do seu canal do YouTube
                  </p>
                </div>

                <div className="space-y-4">
                  <div className="relative">
                    <Input
                      type="text"
                      placeholder="Ex: MeuCanalLegal"
                      value={channelName}
                      onChange={e => {
                        setChannelName(e.target.value);
                        if (error) setError('');
                      }}
                      className="pl-12 pr-4 py-3 text-lg border-2 border-gray-200 rounded-xl focus:border-red-500 focus:ring-0 transition-colors"
                    />
                    <Youtube className="absolute left-4 top-1/2 transform -translate-y-1/2 w-5 h-5 text-gray-400" />
                  </div>

                  {error && (
                    <div className="flex items-center gap-2 p-3 bg-red-50 border border-red-200 rounded-xl">
                      <AlertCircle className="w-4 h-4 text-red-500 flex-shrink-0" />
                      <span className="text-sm text-red-600">{error}</span>
                    </div>
                  )}

                  <Button
                    onClick={handleAuthenticateYouTube}
                    disabled={isLoading}
                    className="w-full bg-gradient-to-r from-red-500 to-red-600 hover:from-red-600 hover:to-red-700 text-white font-bold py-4 px-6 rounded-xl shadow-lg hover:shadow-xl transform hover:-translate-y-0.5 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none"
                  >
                    {isLoading ? (
                      <div className="flex items-center gap-2">
                        <div className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin"></div>
                        Conectando...
                      </div>
                    ) : (
                      <div className="flex items-center gap-2">
                        <Youtube className="w-5 h-5" />
                        Autenticar com Google
                      </div>
                    )}
                  </Button>
                </div>

                <div className="text-center">
                  <p className="text-xs text-gray-500">
                    🔒 Você será redirecionado para o Google de forma segura
                  </p>
                </div>
              </div>
            )}

            {activeTab === 'tiktok' && (
              <div className="space-y-6">
                <div className="text-center">
                  <div className="w-12 h-12 bg-gradient-to-r from-pink-500 to-purple-600 rounded-xl flex items-center justify-center mx-auto mb-4">
                    <Music className="w-6 h-6 text-white" />
                  </div>
                  <h2 className="text-xl font-bold text-gray-800 mb-2">
                    Conectar TikTok
                  </h2>
                  <p className="text-gray-600 text-sm">
                    Adicione sua conta TikTok usando cookies
                  </p>
                </div>

                <div className="space-y-4">
                  <div className="relative">
                    <Input
                      type="text"
                      placeholder="Ex: @MeuPerfilTikTok"
                      value={channelName}
                      onChange={e => {
                        setChannelName(e.target.value);
                        if (error) setError('');
                      }}
                      className="pl-12 pr-4 py-3 text-lg border-2 border-gray-200 rounded-xl focus:border-pink-500 focus:ring-0 transition-colors"
                    />
                    <Music className="absolute left-4 top-1/2 transform -translate-y-1/2 w-5 h-5 text-gray-400" />
                  </div>

                  {error && (
                    <div className="flex items-center gap-2 p-3 bg-red-50 border border-red-200 rounded-xl">
                      <AlertCircle className="w-4 h-4 text-red-500 flex-shrink-0" />
                      <span className="text-sm text-red-600">{error}</span>
                    </div>
                  )}

                  <Button
                    onClick={() => setShowTikTokModal(true)}
                    disabled={!channelName.trim()}
                    className="w-full bg-gradient-to-r from-pink-500 to-purple-600 hover:from-pink-600 hover:to-purple-700 text-white font-bold py-4 px-6 rounded-xl shadow-lg hover:shadow-xl transform hover:-translate-y-0.5 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none"
                  >
                    <div className="flex items-center gap-2">
                      <Music className="w-5 h-5" />
                      Adicionar Cookies
                    </div>
                  </Button>
                </div>

                <div className="bg-blue-50 border border-blue-200 rounded-xl p-4">
                  <h3 className="font-semibold text-blue-800 text-sm mb-2">💡 Como obter os cookies:</h3>
                  <ol className="text-xs text-blue-700 space-y-1">
                    <li>1. Faça login no TikTok no navegador</li>
                    <li>2. Instale e Abra a ferramenta Cookies editor</li>
                    <li>3. Aceite o Cookies editor ler os cookies da pagina</li>
                    <li>4. Clicke em Export e depois em Json</li>
                  </ol>
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Modal TikTok aprimorado */}
        <Dialog open={showTikTokModal} onOpenChange={setShowTikTokModal}>
          <DialogContent className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm">
            <div className="bg-white rounded-2xl shadow-2xl w-full max-w-md p-6 animate-in fade-in-0 zoom-in-95 duration-300">
              <div className="flex justify-between items-center mb-6">
                <div>
                  <h2 className="text-xl font-bold text-gray-800">Cookies do TikTok</h2>
                  <p className="text-sm text-gray-500">Cole os cookies da sua conta</p>
                </div>
                <DialogClose asChild>
                  <Button 
                    variant="ghost" 
                    className="p-2 rounded-full hover:bg-gray-100 transition-colors" 
                    aria-label="Fechar"
                  >
                    <X className="h-5 w-5" />
                  </Button>
                </DialogClose>
              </div>

              <div className="space-y-4">
                <div className="relative">
                  <textarea
                    className="w-full h-40 px-4 py-3 border-2 border-gray-200 rounded-xl focus:border-pink-500 focus:ring-0 resize-none transition-colors text-sm"
                    placeholder="Cole aqui todos os cookies do TikTok...
  Exemplo: sessionid=abc123; csrftoken=xyz789; ..."
                    value={tiktokCookies}
                    onChange={e => setTiktokCookies(e.target.value)}
                  />
                  {tiktokCookies && (
                    <div className="absolute top-2 right-2">
                      <div className="w-6 h-6 bg-green-100 rounded-full flex items-center justify-center">
                        <Check className="w-4 h-4 text-green-600" />
                      </div>
                    </div>
                  )}
                </div>

                <div className="flex gap-3">
                  <Button
                    variant="outline"
                    className="flex-1 py-3 border-2 border-gray-200 hover:bg-gray-50 font-semibold rounded-xl transition-colors"
                    onClick={() => {
                      setShowTikTokModal(false);
                      setTiktokCookies('');
                    }}
                  >
                    Cancelar
                  </Button>
                  <Button
                    className="flex-1 bg-gradient-to-r from-pink-500 to-purple-600 hover:from-pink-600 hover:to-purple-700 text-white font-bold py-3 rounded-xl shadow-lg hover:shadow-xl transform hover:-translate-y-0.5 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none"
                    onClick={handleSaveTikTokCookies}
                    disabled={!tiktokCookies.trim() || isLoading}
                  >
                    {isLoading ? (
                      <div className="flex items-center gap-2">
                        <div className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin"></div>
                        Salvando...
                      </div>
                    ) : (
                      'Salvar Cookies'
                    )}
                  </Button>
                </div>
              </div>
            </div>
          </DialogContent>
        </Dialog>
      </div>
    </Layout>
  );
}