import React, { useEffect, useState } from "react";
import { CtaProperty1DarkProperty2M } from "./CtaProperty1DarkProperty2M";
import { CtaProperty1PurpleProperty2M } from "./CtaProperty1PurpleProperty2M";
import { FeatureCard } from "./FeatureCard"; // Importe o novo componente
import { PricingCard } from "./PricingCard"; // Importe o novo componente
import { useAuth } from '@/contexts/AuthContext';
import { useNavigate } from 'react-router-dom';
import { Play, Sparkles } from "lucide-react";
import ChatWidget from "./ChatWidget"; // <--- adicione essa linha

export const HeroLanding: React.FC = () => {
  const [videoUrl, setVideoUrl] = useState('');
  const { isAuthenticated } = useAuth();
  const navigate = useNavigate();
  const [channelsKey, setChannelsKey] = useState(Date.now()); // <--- Adicione esta linha
  // Adicione este bloco
  useEffect(() => {
    const handleFocus = () => {
      setChannelsKey(Date.now());
    };

    window.addEventListener('focus', handleFocus);

    return () => {
      window.removeEventListener('focus', handleFocus);
    };
  }, []);
    // "Publique em TikTok, Reels e Shorts sem editar nada!",
    // "Do Vídeo inteiro pro feed em segundos usando IA.",
  const slogans = [
    "Poste Todo Dia Sem Editar Nada!",
    "1 vídeo Longo, 10 Clipes Virais.",
    "Crie 10x Mais Rápido Usando IA.",
    "Posts diários sem dor de cabeça!",
    "Seu conteúdo viralizado sem custo de edição!",
    "Transforme vídeos longos em cortes virais com nossa IA.",
    "Automatize Seus Cortes Agora Mesmo"
  ];
  const Startupfeatures = [
    "30 vídeos por mes de Cortes de IA",
    "Cortes em 1080p (FULL HD)",
    "1 Projetos em Simultaneo",
    "Auto importar com limite de 1 canal (em breve)",
    "10/p.dia Cortes de IA em tempo Real com base em uma url de Live twitch ou youtube (em breve)",
    "2 Temas de Legendas revelacao de efeito e tipo escrevendo ",
    "2 Temas de Autoreframe podcast e game ",
    "Modelo de IA: Studio Startup",
    "Analise de Sentimento",
    "Analise de Justificativa do porque o corte é relevante",
    "Analise de Potencial de viralizacao",
    "Analise de Hashtags de viralizacao",
    "Area de Analise de Engajamento das tarefas criadas (em breve)",
    "Area de controle de tarefas",
    "Area de Visualizacao de progresso de criacao de cortes do projeto",
    "Area de dashboard para visualizar a quantidade de tarefas totais, criadas, processando e com erros",
    "Suporte e Grupos De Comunidade via WhatsApp, Discord, Telegram",
    "Marca d´agua nos cortes",
    "Acesso Instantaneo (1 a 10 minutos)",
  ];
  const ContentCreatorfeatures = [
    "Tudo do plano Startup +",
    "60 vídeos por mes de Cortes de IA (Totalizando 90 por mes)",
    "Cortes em 2K (Quad HD)",
    "+ 1 projetos em simultaneo (Totalizando 2 em simultaneo)",
    "Remoção de marca d´agua nos cortes",
  ];

  function useTypewriter(words: string[], speed = 100, pause = 1500) {
    const [index, setIndex] = useState(0); // slogan atual
    const [subIndex, setSubIndex] = useState(0); // posição da letra
    const [direction, setDirection] = useState(1); // 1 digitando, -1 apagando

    useEffect(() => {
      const currentWord = words[index];

      // Se terminou de digitar e vai pausar antes de apagar
      if (direction === 1 && subIndex === currentWord.length) {
        const timeout = setTimeout(() => setDirection(-1), pause);
        return () => clearTimeout(timeout);
      }

      // Se terminou de apagar e vai para o próximo
      if (direction === -1 && subIndex === 0) {
        setDirection(1);
        setIndex((prev) => (prev + 1) % words.length);
        return;
      }

      const timeout = setTimeout(() => {
        setSubIndex((prev) => prev + direction);
      }, speed);

      return () => clearTimeout(timeout);
    }, [subIndex, direction, index, words, speed, pause]);

    return words[index].substring(0, subIndex);
  }

  const channels = [
    {
      id: 'flow-podpah-cortes',
      plataform: "YouTube",
      name: 'Flow & Podpah Cortes',
      thumbnail: '/channels/channels4_profile.jpg', 
      viewsLast90Days: 711454,
      postsPerDay: '30 shorts + 1 vídeo longo por dia',
      subscribersDiff: 343,
      subscribersTotal: 435,
      channelUrl: 'https://www.youtube.com/channel/UCPQFK99DMteVOJQLtLYaU9A'
    },
    {
      id: 'cortes-do-flow07',
      plataform: "Instagram",
      name: 'Cortes Do Flow07',
      thumbnail: '/channels/516593479_17845991175519318_2630081272201720715_n.jpg', 
      viewsLast90Days: 452648,
      postsPerDay: '30 Reels por dia',
      subscribersDiff: 87,
      subscribersTotal: 87,
      channelUrl: 'https://www.instagram.com/cortesdoflow07'
    },
    {
      id: 'react-do-felca',
      plataform: "YouTube",
      name: 'React Do Felca',
      thumbnail: '/channels/channels4_profile (1).jpg', 
      viewsLast90Days: 61589,
      postsPerDay: '5 shorts + 1 vídeo longo por dia',
      subscribersDiff: 44,
      subscribersTotal: 78,
      channelUrl: 'https://www.youtube.com/channel/UChsl0cAeFcaeBc_X0dgeT8Q'
    },
    {
      id: 'cortes-do-felquinhasss',
      plataform: "TikTok",
      name: 'Cortes Do Felquinhasss',
      thumbnail: '/channels/cortesdofelquinhasss.jpeg', 
      viewsLast90Days: 17686,
      postsPerDay: '5 posts por dia',
      subscribersDiff: 15,
      subscribersTotal: 44,
      channelUrl: 'https://www.tiktok.com/@cortesdofelquinhasss'
    },    
    {
      id: 'cortes-do-bruniim',
      plataform: "TikTok",
      name: 'Cortes Do Bruniim',
      thumbnail: '/channels/cortesdobruniim.jpeg', 
      viewsLast90Days: 8191,
      postsPerDay: '5 posts por dia',
      subscribersDiff: 20,
      subscribersTotal: 30,
      channelUrl: 'https://www.tiktok.com/@cortesdobruniim'
    },    
    {
      id: 'cortes-do-bruniim',
      plataform: "YouTube",
      name: 'Cortes Do Bruniim',
      thumbnail: '/channels/channels4_profile_brunnim.jpg', 
      viewsLast90Days: 2140,
      postsPerDay: '5 posts por dia',
      subscribersDiff: 20,
      subscribersTotal: 30,
      channelUrl: 'https://www.tiktok.com/@cortesdobruniim'
    },
  ];

  const formattedNumber = (n: number) => {
    return n.toLocaleString('pt-BR');
  }
  const ChannelCard: React.FC<any> = ({ channel }) => {
    const openExternal = (e: React.MouseEvent) => {
      // evita que pais capturem/consumam o clique
      e.stopPropagation();
      // evita comportamento padrão do <a> (por segurança) e abre em nova janela
      e.preventDefault();
      window.open(channel.channelUrl, '_blank', 'noopener,noreferrer');
    };

  return (
    <div
      className="bg-[rgba(255,255,255,0.03)] border border-[rgba(255,255,255,0.06)] rounded-xl p-4 flex gap-4 items-center shadow-md"
      // opcional: garante que o cartão não capture cliques se houver listener global
      onClick={(e) => e.stopPropagation()}
    >
      <div className="w-20 h-20 rounded-lg overflow-hidden flex-shrink-0">
        <img src={channel.thumbnail} alt={channel.name} className="w-full h-full object-cover" />
      </div>

      <div className="flex-1">
        <div className="flex items-center justify-between">
          <h3 className="font-semibold text-white">{channel.name}</h3>

          <a
            href={channel.channelUrl}
            target="_blank"
            rel="noopener noreferrer"
            onClick={openExternal}
            className="text-sm text-purple-400 hover:underline cursor-pointer"
            aria-label={`Abrir ${channel.name} no ${channel.plataform}`}
          >
            Ver no {channel.plataform}
          </a>
        </div>

        <p className="text-sm text-gray-300 mt-1">{channel.postsPerDay}</p>

        <div className="mt-3 flex gap-3 items-center">
          <div className="flex items-center gap-2">
            <div className="w-3 h-3 rounded-full bg-emerald-400" />
            <div className="text-xs text-gray-300">{formattedNumber(channel.viewsLast90Days)} visualizações (últimos 90 dias)</div>
          </div>

          <div className="h-6 border-l border-[rgba(255,255,255,0.06)]" />

          <div>
            <div className="text-xs text-gray-300">Inscritos (crescimento)</div>
            <div className="text-sm font-medium text-white">+{formattedNumber(channel.subscribersDiff)} (total {formattedNumber(channel.subscribersTotal)})</div>
          </div>
        </div>
      </div>
    </div>
  );
};
  return (
    <section className="bg-black text-white py-20 px-6 flex flex-col items-center">
      <div className="w-full max-w-6xl flex justify-between items-center mb-6 self-start px-6">
        <div className="flex items-center gap-2 h-full">
          <div className="flex items-center justify-center w-9 h-9 rounded-full">
            <img src="/logo-branco.png" alt="Logo" className="h-3.5 w-3.5 object-contain" />
          </div>
          <span className="text-base md:text-lg font-bold text-white leading-none">
            MediaCuts Studio
          </span>
          <Sparkles className="h-4 w-4 text-purple-400 animate-pulse relative top-[0.5px]" />
        </div>
        <button
          onClick={() => navigate(isAuthenticated ? '/shortify' : '/login')}
          className="px-4 py-2 bg-purple-600 hover:bg-purple-500 rounded-md text-sm"
          aria-label={isAuthenticated ? "Abrir perfil" : "Entrar"}
        >
          {isAuthenticated ? 'Perfil' : 'Login'}
        </button>
      </div>
      {/* Seção Principal (já existente) */}
      <h1 className="text-center text-4xl md:text-5xl font-bold mb-4 h-24">
        1 vídeo Longo, 10 Clipes Virais. {/* {useTypewriter(slogans, 50, 1000)} */}
        <span className="border-r-2 border-purple-500 animate-pulse ml-1"></span>
      </h1>
      <p className="text-center text-lg text-gray-300 mb-8 max-w-xl">
        O MediaCuts transforma vídeos longos em videos curtos virais prontos para ser publicado no Tiktok, Reels, Youtube Shorts com um clique.
      </p>

      {/* Input estilizado (já existente) */}
      <div className="w-full max-w-lg mb-6">
        <label className="block relative">
          <input
            type="text"
            value={videoUrl}
            onChange={e => setVideoUrl(e.target.value)}
            placeholder="Cole algum link de um video do YouTube"
            className="w-full bg-[rgba(255,255,255,0.05)] border border-[rgba(255,255,255,0.15)] rounded-lg py-3 px-4 placeholder-gray-400 text-white focus:outline-none focus:ring-2 focus:ring-purple-500"
          />
          <span className="absolute right-4 top-1/2 transform -translate-y-1/2 text-gray-400">
            {/* opcional: ícone */}
          </span>
        </label>
        <p className="text-center text-xs text-gray-500 mt-2">
          Ou insira após registrar-se
        </p>
      </div>



      {/* CTAs lado a lado em mobile e desktop (já existente) */}
      <div className="flex flex-col sm:flex-row gap-4 mb-20"> {/* Adicionei mb-20 para espaçamento */}
        <button
          type="button"
          onClick={() => {
            if (!videoUrl) return;
            const target = isAuthenticated ? '/shortify' : '/login';
            navigate(`${target}?video_url=${encodeURIComponent(videoUrl)}`);
          }}
          className="p-0 border-0 bg-transparent"
        >
          <CtaProperty1DarkProperty2M
            text="Obtenha clips grátis"
            property1="dark"
            property2="m"
          />
        </button>
      </div>
      {/* Vídeo Demonstração em Loop */}
      <div className="w-full max-w-4xl mb-16">
        <video 
          src="/videos/VIDEO-MARKETING-1.mp4" 
          autoPlay 
          muted 
          loop 
          playsInline
          className="w-full rounded-2xl shadow-lg"
        />
      </div>
      
      <div className="w-full max-w-6xl mb-20" key={channelsKey}> 
        <h2 className="text-center text-3xl md:text-4xl font-bold mb-6">Canais que usam o Media Cuts Studio</h2>
        <p className="text-center text-gray-400 mb-8 max-w-3xl mx-auto">Exemplos reais de canais que usam nosso studio para criar cortes e impulsionar o alcance — métricas dos últimos 90 dias.</p>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {channels.map((ch) => (
            <ChannelCard key={ch.id} channel={ch} />
          ))}
        </div>

        <p className="text-xs text-gray-500 mt-4">Quer exibir seus resultados aqui? Entre em contato com nossa equipe de parcerias para ser destaque.</p>
      </div>

      <h2 className="text-center text-3xl md:text-4xl font-bold mb-12">
        Automatize sua presença, escale seu conteúdo.
      </h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl w-full mb-20">
        <FeatureCard
          icon={<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-12 h-12"><path strokeLinecap="round" strokeLinejoin="round" d="M3 16.5v2.25A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75V16.5M16.5 12 12 16.5m0 0L7.5 12m4.5 4.5V3" /></svg>}
          title="Shortify"
          description="Criação de cortes automáticos com base em um link ou nome de canal do Youtube"
          learnMoreLink="#"
        />
        <FeatureCard
          icon={<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-12 h-12"><path strokeLinecap="round" strokeLinejoin="round" d="M16.5 7.5A.75.75 0 0 1 17.25 8.25v1.066a2.25 2.25 0 0 1-.659 1.591L15 14.25m6-4.5c0 3.866-3.414 7-7.625 7-1.761 0-3.374-.431-4.747-1.109L2 21l1.631-4.757A9.126 9.126 0 0 1 12.375 1.5c4.211 0 7.625 3.134 7.625 7z" /></svg>}
          title="Inteligência Artificial"
          description={"Deixe nossa inteligência artificial identificar automaticamente os melhores momentos do seu vídeo base, poupando seu tempo e garantindo conteúdo de alta qualidade."}
          learnMoreLink="#"
        />
        <FeatureCard
          icon={<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-12 h-12"><path strokeLinecap="round" strokeLinejoin="round" d="M12 16.5V9.75m0 0 3 3m-3-3-3 3M6.75 19.5a4.5 4.5 0 0 1-1.41-8.775 5.25 5.25 0 0 1 10.233-2.33 3 3 0 0 1 3.758 3.848A3.75 3.75 0 0 1 18 19.5H6.75Z" /></svg>}
          title="Edição Inteligente de Faces"
          description="Nossa inteligência artificial detecta automaticamente rostos no seu vídeo e edita o conteúdo no formato 9:16, ideal para Podcasts."
          learnMoreLink="#"
        />
      </div>

      <h2 className="text-center text-3xl md:text-4xl font-bold mb-12">Planos</h2>
      <div className="flex flex-col md:flex-row gap-8 max-w-4xl w-full justify-center">
        <PricingCard
          planName="Startup"
          price="$0.00/mo"
          features={Startupfeatures}
          buttonText="Join New Startup"
          buttonVariant="dark"
          onClick={() => navigate("/login")}  
        />
        <PricingCard
          planName="Content Creator"
          price="$8/mo"
          features={ContentCreatorfeatures}
          buttonText="Start creating content"
          buttonVariant="purple"
          onClick={() => navigate("/checkout")}  
        />
      </div>

      {/* Chat do Cliente */}
      <ChatWidget />
    </section>


    );
  };
