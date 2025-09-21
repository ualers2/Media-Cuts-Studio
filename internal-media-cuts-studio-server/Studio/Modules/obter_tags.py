

import os
PRODUCTION_ENV = os.getenv("PRODUCTION_ENV", "True")

if PRODUCTION_ENV == "True":
    # Production
    from Studio.Modules.__init_libs__ import *

elif PRODUCTION_ENV == "False":
    # Local test
    from Modules.__init_libs__ import *
    
COOKIES_FILE = os.path.join(os.path.dirname(__file__), '../', 'Cookies', 'yt.json')

def obter_tags(video_url: str) -> List[str]:
    """
    Retorna a lista de tags (palavras-chave) associadas ao vídeo.
    Se não houver tags, retorna lista vazia.
    """
    ydl_opts = {
        'cookiefile': COOKIES_FILE,
        'quiet': True,
        'skip_download': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        # 'tags' normalmente é uma lista de strings
        return info.get('tags', [])
    