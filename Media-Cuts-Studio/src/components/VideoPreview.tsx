// src/components/VideoPreview.tsx
import { useEffect, useRef, useState } from 'react';
import { toast } from 'react-hot-toast';
import { runWithLimit } from '@/utils/previewQueue';
import { ProjectVideo } from '@/contexts/ProjectsContext';

interface VideoPreviewProps {
  video: ProjectVideo;
  previewEndpoint: string;
  isOpen: boolean;
  allowLoad?: boolean;
}

// Config
const FAILURE_STORAGE_KEY = 'failed_video_previews_v1';
const FAILURE_TTL_MS = 24 * 60 * 60 * 1000; // 24 horas, altere se quiser

// Cache em memória (dura enquanto a página está aberta)
const previewObjectUrlCache = new Map<string, string>();
const inFlightFetches = new Map<string, Promise<string>>();

function loadFailedMap(): Record<string, number> {
  try {
    const raw = localStorage.getItem(FAILURE_STORAGE_KEY);
    return raw ? JSON.parse(raw) : {};
  } catch {
    return {};
  }
}
function saveFailedMap(m: Record<string, number>) {
  try {
    localStorage.setItem(FAILURE_STORAGE_KEY, JSON.stringify(m));
  } catch {}
}
function markFailed(id: string) {
  const m = loadFailedMap();
  m[id] = Date.now();
  saveFailedMap(m);
}
function isFailed(id: string) {
  const m = loadFailedMap();
  const t = m[id];
  if (!t) return false;
  if (Date.now() - t > FAILURE_TTL_MS) {
    delete m[id];
    saveFailedMap(m);
    return false;
  }
  return true;
}


const VideoPreview: React.FC<VideoPreviewProps> = ({ video, previewEndpoint, isOpen, allowLoad = true }) => {
  const videoElRef = useRef<HTMLVideoElement | null>(null);
  const [mode, setMode] = useState<'loading' | 'video' | 'thumbnail' | 'placeholder'>('loading');
  const [src, setSrc] = useState<string | null>(null);

  useEffect(() => {
    // Se modal fechado, sempre mostra thumbnail/placeholder (sem tocar no cache)
    if (!isOpen) {
      if (video.urltumbnail) {
        setMode('thumbnail');
        setSrc(video.urltumbnail);
      } else {
        setMode('placeholder');
        setSrc(null);
      }
      return;
    }

    // Se carregamento global estiver desabilitado (ex: "baixando todos"),
    // NÃO substituímos um preview já carregado — mantemos o cached objectUrl.
    if (!allowLoad) {
      const videoId = video.id;
      if (previewObjectUrlCache.has(videoId)) {
        // já temos o preview em memória: mantém o vídeo
        setMode('video');
        setSrc(previewObjectUrlCache.get(videoId)!);
      } else if (video.urltumbnail) {
        // não temos cache: mostra thumbnail
        setMode('thumbnail');
        setSrc(video.urltumbnail);
      } else {
        setMode('placeholder');
        setSrc(null);
      }
      return;
    }

    // Se aqui, allowLoad === true e isOpen === true => permite carregar/recuperar preview
    let cancelled = false;
    const controller = new AbortController();
    const signal = controller.signal;

    const loadPreview = async () => {
      const videoId = video.id;
      console.log(`videoId ${videoId}`)
      if (isFailed(videoId)) {
        if (!cancelled) {
          if (video.urltumbnail) {
            setMode('thumbnail');
            setSrc(video.urltumbnail);
          } else {
            setMode('placeholder');
            setSrc(null);
          }
        }
        return;
      }

      // se já tiver cache, usa e sai (sem novos fetches)
      if (previewObjectUrlCache.has(videoId)) {
        if (!cancelled) {
          setMode('video');
          setSrc(previewObjectUrlCache.get(videoId)!);
        }
        return;
      }

      // se já existe uma fetch em andamento, aguarda-a
      if (inFlightFetches.has(videoId)) {
        try {
          const url = await inFlightFetches.get(videoId)!;
          if (!cancelled) {
            setMode('video');
            setSrc(url);
          }
          return;
        } catch (err) {
          // se falhar, continua e tentará refazer abaixo
        }
      }

      setMode('loading');

      const fetchPromise: Promise<string> = runWithLimit(async () => {
        try {
          const token = localStorage.getItem('api_key') || '';
          const userId = localStorage.getItem('user_email') || '';

          const metaRes = await fetch(previewEndpoint, {
            headers: { Authorization: `Bearer ${token}`, 'X-User-Id': userId },
            signal
          });

          if (signal.aborted) throw new Error('aborted');

          if (metaRes.status === 401) {
            toast.error('Não autorizado para ver preview.', { position: 'bottom-center' });
            throw new Error('401');
          }
          if (!metaRes.ok) throw new Error(`meta fetch failed: ${metaRes.status}`);

          const metaJson = await metaRes.json();
          const preview_url = metaJson.preview_url;
          if (!preview_url) throw new Error('preview_url ausente');

          // tenta Cache API primeiro (não passa signal para cache.match)
          try {
            const cache = await caches.open('video-previews');
            const cached = await cache.match(preview_url);
            if (cached) {
              const cachedBlob = await cached.blob();
              const cachedObjectUrl = URL.createObjectURL(cachedBlob);
              previewObjectUrlCache.set(videoId, cachedObjectUrl);
              return cachedObjectUrl;
            }
          } catch (e) {
            console.debug('Cache API indisponível ou falhou', e);
          }

          // busca o arquivo real (com signal para permitir abort)
          const fileRes = await fetch(preview_url, {
            headers: { Authorization: `Bearer ${token}`, 'X-User-Id': userId },
            signal
          });

          if (!fileRes.ok) throw new Error(`arquivo fetch failed: ${fileRes.status}`);
          const blob = await fileRes.blob();

          // tenta salvar no Cache API (não crítico)
          try {
            const cache = await caches.open('video-previews');
            cache.put(new Request(preview_url), new Response(blob)).catch(()=>{});
          } catch (e) { console.debug('Falha ao salvar no Cache API', e); }

          const objectUrl = URL.createObjectURL(blob);
          previewObjectUrlCache.set(videoId, objectUrl);

          return objectUrl;
        } catch (err) {
          throw err;
        }
      });

      inFlightFetches.set(videoId, fetchPromise);

      try {
        const objectUrl = await fetchPromise;
        inFlightFetches.delete(videoId);
        if (!cancelled) {
          setMode('video');
          setSrc(objectUrl);
        }
      } catch (err: any) {
        inFlightFetches.delete(videoId);
        if (err?.name === 'AbortError' || err?.message === 'aborted') {
          // fetch abortado: silenciosamente mostra thumbnail/placeholder
          if (!cancelled) {
            if (video.urltumbnail) {
              setMode('thumbnail');
              setSrc(video.urltumbnail);
            } else {
              setMode('placeholder');
              setSrc(null);
            }
          }
          return;
        }
        markFailed(videoId);
        if (!cancelled) {
          if (video.urltumbnail) {
            setMode('thumbnail');
            setSrc(video.urltumbnail);
          } else {
            setMode('placeholder');
            setSrc(null);
          }
          const message = err?.message || 'Erro desconhecido ao carregar preview';
          if (message !== '401') {
            toast.error(`Erro no preview: ${message}`, { position: 'bottom-center' });
          }
          console.error('Erro no preview do vídeo', videoId, err);
        }
      }
    };

    loadPreview();

    return () => {
      cancelled = true;
      controller.abort(); // cancela fetchs pendentes (somente relevantes para previews ainda não carregados)
    };
  }, [previewEndpoint, isOpen, allowLoad, video.id]);


  if (mode === 'video' && src) {
    return (
      <video
        ref={videoElRef}
        src={src}
        className="rounded-md object-contain w-full"
        style={{ maxHeight: '400px' }}
        playsInline
        controls={false}
      />
    );
  }

  if (mode === 'thumbnail' && src) {
    return (
      <img
        src={src}
        alt={`Thumbnail ${video.title}`}
        className="rounded-md object-cover w-full"
        style={{ maxHeight: '400px' }}
      />
    );
  }

  return (
    <div className="rounded-md flex items-center justify-center w-full h-40 bg-gray-200 dark:bg-gray-700 text-gray-600 dark:text-gray-300">
      {mode === 'loading' ? 'Carregando preview...' : 'Sem preview disponível'}
    </div>
  );
};

export default VideoPreview;