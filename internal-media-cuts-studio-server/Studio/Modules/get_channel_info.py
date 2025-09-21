

import os
PRODUCTION_ENV = os.getenv("PRODUCTION_ENV", "True")

if PRODUCTION_ENV == "True":
    # Production
    from Studio.Modules.__init_libs__ import *

elif PRODUCTION_ENV == "False":
    # Local test
    from Modules.__init_libs__ import *


def get_channel_info(channel_url):
    """Obtém o nome do canal e o vídeo mais recente"""
    videos_url = f"{channel_url}/videos"
    ydl_opts = {
        'quiet': False,
        'ignoreerrors': True,
        'force_generic_extractor': False,
        'skip_download_errors': True,
        'timeout': 30,
        'playlistend': 1  
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            result = ydl.extract_info(videos_url, download=False)
            entries = result.get('entries', [])
            

        except Exception as e:
            print(f"Erro ao obter informações do canal: {str(e)}")
            raise
    
    ydl.close()
    return result.get('title'), entries