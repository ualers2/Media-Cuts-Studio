import os
import re
import requests
from bs4 import BeautifulSoup
import yt_dlp

COOKIES_FILE = os.path.join(os.path.dirname(__file__), '../', 'Cookies', 'yt.json')
TIMEOUT = 7

class _QuietLogger:
    # yt_dlp espera um objeto com debug/info/warning/error
    def debug(self, *args, **kwargs): pass
    def info(self, *args, **kwargs): pass
    def warning(self, *args, **kwargs): pass
    def error(self, *args, **kwargs): pass

def extract_youtube_id(url_or_id):
    if not url_or_id:
        return None
    if re.fullmatch(r'[0-9A-Za-z_-]{11}', url_or_id):
        return url_or_id
    patterns = [
        r'(?:v=|vi=)([0-9A-Za-z_-]{11})',
        r'youtu\.be\/([0-9A-Za-z_-]{11})',
        r'\/shorts\/([0-9A-Za-z_-]{11})',
        r'\/embed\/([0-9A-Za-z_-]{11})',
        r'([0-9A-Za-z_-]{11})'
    ]
    for p in patterns:
        m = re.search(p, url_or_id)
        if m:
            return m.group(1)
    return None

def scrape_youtube_title(url):
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=TIMEOUT)
        if r.status_code != 200:
            return None
        soup = BeautifulSoup(r.text, "html.parser")
        tag = soup.find("meta", property="og:title")
        if tag and tag.get("content"):
            return tag["content"].strip()
        if soup.title and soup.title.string:
            return soup.title.string.strip()
    except Exception:
        return None
    return None

def _yt_dlp_title(url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'noplaylist': True,
        'ignoreerrors': True,
        'no_warnings': True,
        'logger': _QuietLogger(),
    }
    if os.path.exists(COOKIES_FILE):
        ydl_opts['cookiefile'] = COOKIES_FILE

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            if isinstance(info, dict):
                return info.get("title")
    except Exception:
        # silencia totalmente: yt-dlp já registra internamente via logger
        return None
    return None

def _oembed_title(url):
    try:
        oembed_url = f"https://www.youtube.com/oembed?url={requests.utils.requote_uri(url)}&format=json"
        r = requests.get(oembed_url, timeout=TIMEOUT)
        if r.status_code == 200:
            j = r.json()
            return j.get("title")
    except Exception:
        return None
    return None

def get_video_title(video_id_or_url):
    if not video_id_or_url:
        return "VideoSemTitulo"

    video_id = extract_youtube_id(video_id_or_url)
    if video_id:
        url = f"https://www.youtube.com/watch?v={video_id}"
    else:
        url = video_id_or_url

    # tentativa 1: yt-dlp (silencioso)
    title = _yt_dlp_title(url)
    if title:
        return title.strip()

    # tentativa 2: oEmbed
    title = _oembed_title(url)
    if title:
        return title.strip()

    # tentativa 3: scraping simples
    title = scrape_youtube_title(url)
    if title:
        return title.strip()

    return "VideoSemTitulo"

def get_video_title_by_url(pasted_url):
    return get_video_title(pasted_url)

if __name__ == '__main__':
    tests = [
        "szSGnn3FIVA",
        "https://www.youtube.com/watch?v=szSGnn3FIVA",
        "https://youtu.be/szSGnn3FIVA",
        "https://www.youtube.com/shorts/szSGnn3FIVA"
    ]
    for t in tests:
        print(get_video_title(t))
