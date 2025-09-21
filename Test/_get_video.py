import re
import unicodedata
import yt_dlp
from termcolor import cprint
from deep_translator import GoogleTranslator
from difflib import SequenceMatcher

# Inicializa o tradutor do deep-translator
translator = GoogleTranslator(source='auto', target='pt')

def normalize_title(s: str) -> str:
    """
    - Remove espaços extras
    - Normaliza Unicode e casefold
    - Remove pontuação (tudo que não for letra, número ou espaço)
    """
    # colapsa múltiplos espaços
    s = " ".join(s.split())
    # normalização Unicode e lowercase
    s = unicodedata.normalize("NFC", s).casefold()
    # remove pontuação
    return re.sub(r"[^0-9a-zçáâãéêíóôõúü ]+", "", s)

def translate_to_pt(text: str) -> str:
    """
    Traduz texto para o português, retornando original em caso de erro.
    """
    try:
        return translator.translate(text)
    except Exception as e:
        cprint(f"⚠ Erro ao traduzir: {e}", 'yellow')
        return text

def similarity_percent(a: str, b: str) -> float:
    """Calcula similaridade (%) entre duas strings."""
    return SequenceMatcher(None, a, b).ratio() * 100

def get_video_by_title(
    canal_url: str = "",
    title_target: str = "",
    max_checks: int = 100,
):
    """
    Percorre vídeos de um canal YouTube (yt-dlp), traduz e normaliza títulos,
    e retorna o primeiro vídeo cuja similaridade com `title_target` ultrapasse
    `threshold` (%) ou seja EXATAMENTE igual.
    Retorna: (channel_title_pt, video_entry, sim_score) ou (channel_title_pt, None, None).
    """
    videos_url = f"{canal_url}/videos"
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'ignoreerrors': True,
        'skip_download': True,
        'extract_flat': 'in_playlist',
        'timeout': 30,
    }

    # normaliza o alvo uma única vez
    target_norm = normalize_title(title_target)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # pega título original do canal e traduz
        try:
            info = ydl.extract_info(canal_url, download=False)
            channel_title = info.get('title', canal_url)
            channel_title_pt = translate_to_pt(channel_title)
        except Exception as e:
            cprint(f"❌ Erro ao obter título do canal: {e}", 'red')
            raise

        # varre vídeo a vídeo
        for idx in range(1, max_checks + 1):
            ydl.params['playlist_items'] = str(idx)
            try:
                res = ydl.extract_info(videos_url, download=False)
                entries = res.get('entries') or []
                if not entries:
                    break
                video = entries[0]
            except Exception as e:
                cprint(f"⚠ Erro no vídeo #{idx}: {e}", 'yellow')
                continue

            # raw = video.get('title', '')
            id_video = video.get('id', '')
            video_title= get_video_title(f"{id_video}")
            # traduzido = translate_to_pt(raw)
            norm = normalize_title(video_title)
            sim = similarity_percent(norm, target_norm)

            cprint(f"[{idx}] norm: {norm!r}", 'magenta')
            cprint(f" target: {target_norm!r}", 'magenta')
            # cprint(f" similaridade: {sim:.2f}% (limiar = {threshold}%)", 'magenta')

            if norm == target_norm:
                # cprint(f"✔ Encontrou no #{idx}: {traduzido} (sim={sim:.2f}%)", 'green')
                # video['title'] = traduzido
                return channel_title_pt, video, sim

    return channel_title_pt, None, None

def get_video_title(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    ydl_opts = {
        'quiet': True,
        'skip_download': True  # Garante que o vídeo não será baixado
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info.get("title", "Desconhecido")
    

# video_title= get_video_title("kKfy0IAmhi8")
# print(video_title)
# Exemplo de uso
if __name__ == "__main__":
    canal = "https://www.youtube.com/@YmaGu"
    alvo = "O QUE ACONTECEU COM FORNITE? (2017-2025) - MINHA OPINIÃO SINCERA!"
    titulo_canal, video, score = get_video_by_title(
        canal_url=canal,
        title_target=alvo,
        max_checks=20,
        threshold=76  # ajuste para maior ou menor tolerância
    )
    if video:
        print(f"Vídeo encontrado com similaridade {score:.2f}%")
        print(video)
    else:
        print("Nenhum vídeo similar encontrado.")
