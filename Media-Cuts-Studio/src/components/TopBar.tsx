// webproject\src\components\TopBar.tsx
import React, { useState, useEffect } from 'react';
import { Button } from '@/components/ui/button';
import { SidebarTrigger } from '@/components/ui/sidebar';
import { LogOut, User, Sun, Moon } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

import { useTheme } from '@/contexts/ThemeContext';


const TopBar: React.FC = () => {
  const navigate = useNavigate();
  const { isDarkMode, toggleTheme } = useTheme();

  // Aplica/remover classe 'dark' no <html> e persiste
  useEffect(() => {
    const root = document.documentElement;
    if (isDarkMode) {
      root.classList.add('dark');
      localStorage.setItem('theme', 'dark');
    } else {
      root.classList.remove('dark');
      localStorage.setItem('theme', 'light');
    }
  }, [isDarkMode]);


  const handleLogout = () => {
    localStorage.removeItem('isAuthenticated');
    navigate('/login');
  };

  const handleMyaccount = () => {
    navigate('/my-account');
  };

  // Lê horário de login
  const loginTime = localStorage.getItem('login_time') || '';


  return (
    <header className="h-16 bg-white dark:bg-deep-purple border-b border-border-light dark:border-border-dark flex items-center justify-between px-6 transition-colors duration-300 shadow-sm">
      {/* Lado esquerdo */}
      <div className="flex items-center space-x-4">
        <SidebarTrigger className="lg:hidden text-gray-dark dark:text-white hover:text-primary-purple transition-colors duration-200" />

        <div className="flex items-center space-x-3">
          <img
            src="/logo-branco.png"
            alt="Logo do Aplicativo"
            className="w-8 h-8 rounded-xl"
          />
          <div>
            <h1 className="font-bold text-gray-900 dark:text-white text-lg">Media Cuts Studio</h1>
            <p className="text-xs text-gray-text dark:text-gray-400">{loginTime}</p>
          </div>
        </div>
      </div>

      {/* Lado direito */}
      <div className="flex items-center space-x-3">
        {/* Botão de alternância de tema */}
        {/* <Button
          variant="ghost"
          size="sm"
          onClick={toggleTheme}
          className="p-2 rounded-full hover:bg-primary-purple-light dark:hover:bg-primary-purple-dark transition-colors duration-200"
          aria-label="Alternar tema"
        >
          {isDarkMode ? <Sun size={20} className="text-yellow-400" /> : <Moon size={20} className="text-gray-700 dark:text-gray-200" />}
        </Button> */}

        <Button
          variant="ghost"
          size="sm"
          onClick={handleMyaccount}
          className="p-2 rounded-full hover:bg-accent-blue transition-colors duration-200"
          aria-label="Minha conta"
        >
          <User size={20} />
        </Button>

        <Button
          variant="ghost"
          size="sm"
          onClick={handleLogout}
          className="p-2 rounded-full hover:bg-red-500 hover:text-white transition-colors duration-200"
          aria-label="Sair"
        >
          <LogOut size={20} />
        </Button>
      </div>
    </header>
  );
};

export default TopBar;