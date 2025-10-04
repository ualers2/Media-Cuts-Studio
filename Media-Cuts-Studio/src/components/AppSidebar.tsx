import React, { useState, useEffect } from 'react';
import { NavLink, useLocation } from 'react-router-dom';
import {
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarTrigger,
  useSidebar,
} from '@/components/ui/sidebar';
import {
  Settings,
  BarChart3,
  CheckSquare,
  Users,
  Cog,
  FileText,
  User,
  Folder,
  Plus, 
  Upload, 
  List, 
  KeyIcon,
  LogOut,
  Home, 
  Calendar,
  Menu,
  X
} from 'lucide-react';

const sidebarItems = [
  { title: 'Dashboard', url: '/dashboard', icon: BarChart3, category: 'main' },
  { title: 'Studio', url: '/shortify', icon: CheckSquare, category: 'main' },
  { title: 'Projetos', url: '/projects', icon: Folder, category: 'main' },
  { title: "Novo Post", url: "/new-post", icon: Plus, category: 'content' },
  // { title: "Agendamento em Massa", url: "/bulk-schedule", icon: Upload, category: 'content' },
  { title: "Calendário", url: "/calendar", icon: Calendar, category: 'content' },
  { title: "Lista de Posts", url: "/posts", icon: List, category: 'content' },
  { title: "Autenticar Conta", url: "/authenticate-account", icon: KeyIcon, category: 'settings' },
  { title: 'Minha conta', url: '/my-account', icon: User, category: 'settings' },
];

const legalItems = [
  { title: 'Política de Privacidade', url: '/privacy-policy', icon: FileText },
  { title: 'Termos de Uso', url: '/terms-of-use', icon: FileText },
];

const categories = {
  main: 'Principal',
  content: 'Conteúdo',
  settings: 'Configurações'
};

export function AppSidebar() {
  const { state, open, setOpen } = useSidebar();
  const location = useLocation();
  const [isMobile, setIsMobile] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  
  const collapsed = state === 'collapsed';
  
  // Detectar se é mobile
  useEffect(() => {
    const checkMobile = () => {
      setIsMobile(window.innerWidth < 768);
    };
    
    checkMobile();
    window.addEventListener('resize', checkMobile);
    return () => window.removeEventListener('resize', checkMobile);
  }, []);

  // Fechar menu mobile quando mudar de rota
  useEffect(() => {
    setMobileMenuOpen(false);
  }, [location.pathname]);

  // Agrupar itens por categoria
  const groupedItems = sidebarItems.reduce((acc, item) => {
    if (!acc[item.category]) {
      acc[item.category] = [];
    }
    acc[item.category].push(item);
    return acc;
  }, {});

  const getNavCls = ({ isActive }: { isActive: boolean }) =>
    isActive
      ? 'bg-primary-purple/10 text-primary-purple font-medium border-r-2 border-primary-purple dark:bg-primary-purple/30 dark:text-primary-purple-light dark:border-primary-purple shadow-sm'
      : 'hover:bg-deep-purple/20 text-gray-text dark:text-white dark:hover:bg-deep-purple/50 hover:shadow-sm transition-all duration-200';
      
  // Mobile Menu Button
  const MobileMenuButton = () => (
    <button
      onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
      className="md:hidden fixed top-4 left-4 z-50 p-2 bg-background-light dark:bg-deep-purple rounded-lg shadow-lg border dark:border-border-dark hover:shadow-xl transition-all duration-200"
      aria-label="Toggle menu"
    >
      {mobileMenuOpen ? (
        <X className="h-5 w-5 text-gray-dark dark:text-white" />
      ) : (
        <Menu className="h-5 w-5 text-gray-dark dark:text-white" />
      )}
    </button>
  );

  // Mobile Overlay
  const MobileOverlay = () => (
    mobileMenuOpen && (
      <div
        className="md:hidden fixed inset-0 bg-black bg-opacity-50 z-30 transition-opacity duration-200"
        onClick={() => setMobileMenuOpen(false)}
      />
    )
  );

  // Sidebar Content Component
  const SidebarContentComponent = () => (
    <div className="flex flex-col h-full">
      {/* Header do sidebar */}
      <div className="flex items-center justify-between p-4 border-b dark:border-gray-800">
        {(!collapsed || isMobile) && (
          <h2 className="text-lg font-semibold text-gray-dark dark:text-white">
            Menu
          </h2>
        )}
        {!isMobile && (
          <SidebarTrigger className="text-gray-dark dark:text-white hover:text-primary-purple dark:hover:text-primary-purple-light hover:bg-background-light dark:hover:bg-deep-purple/50 rounded-md p-1 transition-colors duration-200" />
        )}
        {isMobile && (
          <button
            onClick={() => setMobileMenuOpen(false)}
            className="text-gray-dark dark:text-white hover:text-primary-purple dark:hover:text-primary-purple-light hover:bg-background-light dark:hover:bg-deep-purple/50 rounded-md p-1 transition-colors duration-200"
          >
            <X className="h-4 w-4" />
          </button>
        )}
      </div>

      {/* Menu principal */}
      <div className="flex-1 overflow-y-auto py-4">
        {Object.entries(groupedItems).map(([category, items]) => (
          <SidebarGroup key={category}>
            {(!collapsed || isMobile) && (
              <SidebarGroupLabel className="text-gray-text dark:text-white font-medium px-4 py-2 text-xs uppercase tracking-wider">
                {categories[category]}
              </SidebarGroupLabel>
            )}
            <SidebarGroupContent>
              <SidebarMenu className="space-y-1 px-2">
                {items.map((item) => (
                  <SidebarMenuItem key={item.title}>
                    <SidebarMenuButton asChild>
                      <NavLink
                        to={item.url}
                        end
                        className={({ isActive }) =>
                          `flex items-center px-3 py-3 rounded-lg ${getNavCls({ isActive })} ${
                            collapsed && !isMobile ? 'justify-center' : ''
                          }`
                        }
                        title={collapsed && !isMobile ? item.title : undefined}
                      >
                        <item.icon className="h-5 w-5 flex-shrink-0" />
                        {(!collapsed || isMobile) && (
                          <span className="ml-3 font-medium">{item.title}</span>
                        )}
                      </NavLink>
                    </SidebarMenuButton>
                  </SidebarMenuItem>
                ))}
              </SidebarMenu>
            </SidebarGroupContent>
          </SidebarGroup>
        ))}

        {/* Seção Legal */}
        <SidebarGroup className="mt-8">
          {(!collapsed || isMobile) && (
            <SidebarGroupLabel className="text-gray-text dark:text-gray-text font-medium px-4 py-2 text-xs uppercase tracking-wider">
              Legal
            </SidebarGroupLabel>
          )}
          <SidebarGroupContent>
            <SidebarMenu className="space-y-1 px-2">
              {legalItems.map((item) => (
                <SidebarMenuItem key={item.title}>
                  <SidebarMenuButton asChild>
                    <NavLink
                      to={item.url}
                      end
                      className={({ isActive }) =>
                        `flex items-center px-3 py-2 rounded-lg text-sm ${getNavCls({ isActive })} ${
                          collapsed && !isMobile ? 'justify-center' : ''
                        }`
                      }
                      title={collapsed && !isMobile ? item.title : undefined}
                    >
                      <item.icon className="h-4 w-4 flex-shrink-0 text-gray-text dark:text-white opacity-70" />
                      {(!collapsed || isMobile) && (
                        <span className="ml-3 font-medium text-gray-text dark:text-white opacity-80">{item.title}</span>
                      )}
                    </NavLink>
                  </SidebarMenuButton>
                </SidebarMenuItem>
              ))}
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>
      </div>

      {/* Footer do sidebar */}
      <div className="border-t dark:border-gray-800 p-4">
        {(!collapsed || isMobile) && (
          <div className="text-xs text-gray-400 dark:text-gray-500 text-center">
            © 2025 Sua Empresa
          </div>
        )}
      </div>
    </div>
  );

  return (
    <>
      {/* Mobile Menu Button */}
      <MobileMenuButton />
      
      {/* Mobile Overlay */}
      <MobileOverlay />

      {/* Desktop Sidebar */}
      {!isMobile && (
        <Sidebar 
          className={`transition-all duration-300 ${collapsed ? 'w-16' : 'w-64'} border-r-0`} 
          collapsible="icon"
        >
          <SidebarContent className="bg-background-light dark:bg-deep-purple border-r dark:border-border-dark shadow-sm">
            <SidebarContentComponent />
          </SidebarContent>
        </Sidebar>
      )}

      {/* Mobile Sidebar */}
      {isMobile && (
        <div
          className={`fixed top-0 left-0 h-full w-80 bg-white dark:bg-gray-900 border-r dark:border-gray-800 shadow-2xl z-40 transform transition-transform duration-300 ${
            mobileMenuOpen ? 'translate-x-0' : '-translate-x-full'
          }`}
        >
          <SidebarContentComponent />
        </div>
      )}
    </>
  );
}