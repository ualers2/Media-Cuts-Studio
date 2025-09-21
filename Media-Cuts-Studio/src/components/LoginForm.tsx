// webproject\src\components\LoginForm.tsx
import React, { useState, useEffect } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Card, CardContent, CardHeader } from '@/components/ui/card';
import { Mail, Lock, LogIn, UserPlus, Sun, Moon } from 'lucide-react';
import { useNavigate, useLocation } from 'react-router-dom';
import { initSocket } from '@/utils/socket';
import { useAuth } from '@/contexts/AuthContext';

const LoginForm: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [isRegistering, setIsRegistering] = useState(false);
  const [isDarkMode, setIsDarkMode] = useState(true);
  const navigate = useNavigate();
  const { login } = useAuth();
  const location = useLocation();
  const params = new URLSearchParams(location.search);
  const videoUrl = params.get('video_url');
  console.log(`videoUrl ${videoUrl}`)
  // Aplica ou remove classe 'dark' no root
  useEffect(() => {
    const root = document.documentElement;
    if (isDarkMode) root.classList.add('dark');
    else root.classList.remove('dark');
  }, [isDarkMode]);

  const toggleTheme = () => setIsDarkMode(prev => !prev);

  const toggleMode = () => {
    setIsRegistering(prev => !prev);
    setEmail('');
    setPassword('');
    setConfirmPassword('');
  };

  const fromPath = videoUrl ? undefined : (location.state as { from?: Location })?.from?.pathname;

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    const LANDING_APIURL = import.meta.env.VITE_LANDING_API;
    if (email && password) {
      try {
        const response = await fetch(`${LANDING_APIURL}/login`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ username: email, password }),
        });
        const result = await response.json();
        if (!response.ok) {
          alert(result.message || 'Erro no login');
          return;
        }
        // Armazena dados de sessão
        localStorage.setItem('isAuthenticated', 'true');
        localStorage.setItem('user_email', email);
        localStorage.setItem('api_key', result.api_key);
        localStorage.setItem('expire_time_license', result.expire_time_license);
        // Formata horário do login
        const now = new Date();
        const horas24 = now.getHours();
        const horas12 = horas24 % 12 || 12;
        const minutos = now.getMinutes().toString().padStart(2, '0');
        const ampm = horas24 < 12 ? 'am' : 'pm';
        const dia = now.getDate().toString().padStart(2, '0');
        const meses = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
        const mesAbrev = meses[now.getMonth()];
        const ano = now.getFullYear();
        const formattedTime = `${horas12}:${minutos} ${ampm} ${dia} ${mesAbrev} ${ano}`;
        localStorage.setItem('login_time', formattedTime);
        // Busca configs e dados da conta
        const [configRes, accountRes] = await Promise.all([
          fetch(`${LANDING_APIURL}/api/user-config/${email}`),
          fetch(`${LANDING_APIURL}/api/account/${email}`),
        ]);
        const config = await configRes.json();
        const account = await accountRes.json();
        localStorage.setItem('user_config', JSON.stringify(config.config || {}));
        localStorage.setItem('account_data', JSON.stringify(account.account || {}));
        // Inicializa socket e fecha fluxo
        initSocket(result.api_key);
        login(result.api_key);
        console.log(videoUrl)
        if (videoUrl) {
          navigate(`/shortify?video_url=${encodeURIComponent(videoUrl)}`, { replace: true });
        } else {
          navigate(fromPath || '/dashboard', { replace: true });
        }
      } catch (err) {
        console.error('Erro ao fazer login:', err);
        alert('Erro ao tentar logar. Verifique sua conexão ou tente novamente.');
      }
    }
  };

  const handleRegister = async (e: React.FormEvent) => {
    e.preventDefault();
    const LANDING_APIURL = import.meta.env.VITE_LANDING_API;
    if (!email || !password || !confirmPassword) {
      alert('Preencha todos os campos.');
      return;
    }
    if (password !== confirmPassword) {
      alert('As senhas não coincidem.');
      return;
    }
    try {
      const response = await fetch(`${LANDING_APIURL}/proxy-create-login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: email, password: password,subscription_plan: 'startup', expiration: 'None' }),
      });
      const result = await response.json();
      if (!response.ok) {
        alert(result.message || 'Erro no registro');
        return;
      }
      alert('Registro realizado com sucesso! Você já pode fazer login.');
      toggleMode();
    } catch (err) {
      console.error('Erro ao registrar:', err);
      alert('Erro ao tentar registrar. Verifique sua conexão ou tente novamente.');
    }
  };

  return (
    <div className={`min-h-screen flex items-center justify-center ${isDarkMode ? 'bg-gray-900' : 'bg-gradient-to-br from-gray-50 to-gray-100'} p-4 transition-colors duration-300`}>
      <div className="absolute top-4 right-4">
        <Button onClick={toggleTheme} className="p-2">
          {isDarkMode ? <Sun size={20} /> : <Moon size={20} />}
        </Button>
      </div>
      <div className="w-full max-w-6xl grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
        <div className="w-full max-w-md mx-auto lg:mx-0">
          <div className="text-center mb-8">
            <h1 className={`text-2xl font-bold ${isDarkMode ? 'text-gray-100' : 'text-gray-900'} mb-2`}>Media Cuts Studio</h1>
          </div>
          <Card className={`border-0 shadow-xl transition-colors duration-300 ${isDarkMode ? 'bg-gray-800' : 'bg-white'}`}>
            <CardHeader className="text-center pb-2">
              {isRegistering ? (
                <>
                  <UserPlus size={24} className="mx-auto text-green-600" />
                  <h2 className={`text-2xl font-bold ${isDarkMode ? 'text-gray-100' : 'text-gray-900'}`}>Register</h2>
                </>
              ) : (
                <>
                  <LogIn size={24} className="mx-auto text-purple-600" />
                  <h2 className={`text-2xl font-bold ${isDarkMode ? 'text-gray-100' : 'text-gray-900'}`}>Login</h2>
                </>
              )}
            </CardHeader>
            <CardContent className="space-y-6">
              {isRegistering ? (
                <form onSubmit={handleRegister} className="space-y-4">
                  <div className="space-y-2">
                    <div className="flex items-center space-x-2">
                      <Mail size={20} className={`text-${isDarkMode ? 'gray-200' : 'gray-700'}`} />
                      <span className={`font-medium ${isDarkMode ? 'text-gray-200' : 'text-gray-700'}`}>Email</span>
                    </div>
                    <Input type="email" placeholder="Enter your email" value={email} onChange={e => setEmail(e.target.value)} className="h-12" required />
                  </div>
                  <div className="space-y-2">
                    <div className="flex items-center space-x-2">
                      <Lock size={20} className={`text-${isDarkMode ? 'gray-200' : 'gray-700'}`} />
                      <span className={`font-medium ${isDarkMode ? 'text-gray-200' : 'text-gray-700'}`}>Senha</span>
                    </div>
                    <Input type="password" placeholder="Enter your password" value={password} onChange={e => setPassword(e.target.value)} className="h-12" required />
                  </div>
                  <div className="space-y-2">
                    <div className="flex items-center space-x-2">
                      <Lock size={20} className={`text-${isDarkMode ? 'gray-200' : 'gray-700'}`} />
                      <span className={`font-medium ${isDarkMode ? 'text-gray-200' : 'text-gray-700'}`}>Confirmar Senha</span>
                    </div>
                    <Input type="password" placeholder="Confirm your password" value={confirmPassword} onChange={e => setConfirmPassword(e.target.value)} className="h-12" required />
                  </div>
                  <Button type="submit" className="w-full h-12 bg-gradient-to-r from-green-600 to-green-700 hover:from-green-700 hover:to-green-800 text-white font-medium rounded-lg transition-all duration-200">
                    <UserPlus size={20} className="mr-2" />
                    Register
                  </Button>
                  <p className={`text-center text-sm ${isDarkMode ? 'text-gray-400' : 'text-gray-600'}`}>Já tem conta?{' '}
                    <button type="button" onClick={toggleMode} className="text-purple-600 font-semibold hover:underline">Login</button>
                  </p>
                </form>
              ) : (
                <form onSubmit={handleLogin} className="space-y-4">
                  <div className="space-y-2">
                    <div className="flex items-center space-x-2">
                      <Mail size={20} className={`text-${isDarkMode ? 'gray-200' : 'gray-700'}`} />
                      <span className={`font-medium ${isDarkMode ? 'text-gray-200' : 'text-gray-700'}`}>Email</span>
                    </div>
                    <Input type="email" placeholder="Enter your Email" value={email} onChange={e => setEmail(e.target.value)} className="h-12" required />
                  </div>
                  <div className="space-y-2">
                    <div className="flex items-center space-x-2">
                      <Lock size={20} className={`text-${isDarkMode ? 'gray-200' : 'gray-700'}`} />
                      <span className={`font-medium ${isDarkMode ? 'text-gray-200' : 'text-gray-700'}`}>Password</span>
                    </div>
                    <Input type="password" placeholder="Enter your password" value={password} onChange={e => setPassword(e.target.value)} className="h-12" required />
                  </div>
                  <Button type="submit" className="w-full h-12 bg-gradient-to-r from-purple-600 to-purple-700 hover:from-purple-700 hover:to-purple-800 text-white font-medium rounded-lg transition-all duration-200">
                    <LogIn size={20} className="mr-2" />
                    Login
                  </Button>
                  <p className={`text-center text-sm ${isDarkMode ? 'text-gray-400' : 'text-gray-600'}`}>Não tem conta?{' '}
                    <button type="button" onClick={toggleMode} className="text-green-600 font-semibold hover:underline">Register</button>
                  </p>
                </form>
              )}
            </CardContent>
          </Card>
        </div>
        <div className="hidden lg:flex items-center justify-center">
          {/* Ilustração permanece inalterada */}
        </div>
      </div>
    </div>
  );
};

export default LoginForm;
