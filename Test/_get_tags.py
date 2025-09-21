import yt_dlp

def obter_tags(video_url: str) -> list[str]:
    """
    Retorna a lista de tags (palavras-chave) associadas ao vídeo.
    Se não houver tags, retorna lista vazia.
    """
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        # 'tags' normalmente é uma lista de strings
        return info.get('tags', [])
url = 'https://www.youtube.com/watch?v=UcBuI3yUHtc'
tags = obter_tags(url)
print("Tags encontradas:", tags)