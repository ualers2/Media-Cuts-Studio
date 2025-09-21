

# import os
# PRODUCTION_ENV = os.getenv("PRODUCTION_ENV", "True")

# if PRODUCTION_ENV == "True":
#     # Production
#     from Studio.Modules.__init_libs__ import *

# if PRODUCTION_ENV == "False":
#     # Local test
#     from Modules.__init_libs__ import *

import os
import requests
from bs4 import BeautifulSoup
import yt_dlp

COOKIES_FILE = os.path.join(os.path.dirname(__file__), '../', 'Cookies', 'yt.json')
TIMEOUT = 7


def _check_i_ytimg(video_id):
    base = f"https://i.ytimg.com/vi/{video_id}/"
    candidates = [
        "maxresdefault.jpg",
        "sddefault.jpg",
        "hqdefault.jpg",
        "mqdefault.jpg",
        "default.jpg"
    ]
    for name in candidates:
        url = base + name
        try:
            # HEAD é mais rápido; se HEAD falhar por algum motivo, tenta GET
            r = requests.head(url, timeout=TIMEOUT, allow_redirects=True)
            if r.status_code == 200 and r.headers.get("Content-Type", "").startswith("image"):
                return url
            # fallback GET (alguns hosts não respondem corretamente ao HEAD)
            r = requests.get(url, timeout=TIMEOUT)
            if r.status_code == 200 and r.headers.get("Content-Type", "").startswith("image"):
                return url
        except Exception:
            continue
    return None

def _oembed_thumbnail(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    oembed_url = f"https://www.youtube.com/oembed?url={requests.utils.requote_uri(url)}&format=json"
    try:
        r = requests.get(oembed_url, timeout=TIMEOUT)
        if r.status_code == 200:
            j = r.json()
            return j.get("thumbnail_url")
    except Exception:
        return None

def _scrape_thumbnail(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=TIMEOUT)
        if r.status_code != 200:
            return None
        soup = BeautifulSoup(r.text, "html.parser")
        tag = soup.find("meta", property="og:image")
        if tag and tag.get("content"):
            return tag["content"]
    except Exception:
        return None

def _yt_dlp_thumbnail(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    ydl_opts = {
        'cookiefile': COOKIES_FILE if os.path.exists(COOKIES_FILE) else None,
        'quiet': True,
        'skip_download': True,
        'ignoreerrors': True,
        'no_warnings': True,
        # não forçar formatos aqui — só metadata
        'noplaylist': True,
    }
    # remove None entries
    ydl_opts = {k: v for k, v in ydl_opts.items() if v is not None}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            if isinstance(info, dict):
                return info.get("thumbnail")
    except Exception as e:
        # não interrompe; retorna None para permitir fallback seguintes
        print(f"[yt_dlp] falhou para {video_id}: {e}")
    return None

def get_video_thumbnail(video_id):
    # 1) i.ytimg direto (mais rápido e simples)
    t = _check_i_ytimg(video_id)
    if t:
        return t

    # 2) oEmbed
    t = _oembed_thumbnail(video_id)
    if t:
        return t

    # 3) yt-dlp (usa cookies se existir)
    t = _yt_dlp_thumbnail(video_id)
    if t:
        return t

    # 4) scraping da página (último recurso)
    t = _scrape_thumbnail(video_id)
    if t:
        return t

    return None

if __name__ == '__main__':
    video_id = "O5amJDSfaWE"
    T = get_video_thumbnail(video_id)
    print(T)