import yt_dlp

def obter_descricao(video_url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        return info.get('description', '')

# Exemplo de uso
url = 'https://www.youtube.com/watch?v=kh-CGdrTLFw'
descricao = obter_descricao(url)
print(descricao)
