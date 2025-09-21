

import os
PRODUCTION_ENV = os.getenv("PRODUCTION_ENV", "False")

if PRODUCTION_ENV == "True":
    # Production
    from Studio.Modules.__init_libs__ import *

    from Studio.Modules.get_video_thumbnail import get_video_thumbnail
    from Studio.Modules.get_video_title import get_video_title
    
elif PRODUCTION_ENV == "False":
    # Local test
    from __init_libs__ import *

    from get_video_thumbnail import get_video_thumbnail
    from get_video_title import get_video_title
    

def download_new_videos(videos, 
                        output_dir, 
                        channel, 
                        linux_env, 
                        output_path_,
                        downloaded_videos=[],
                        path_ffmpegnotexe="", 
                        ):
    """Faz o download apenas dos novos vídeos que estão disponíveis"""
    COOKIES_FILE = os.path.join(os.path.dirname(__file__), '../', 'Cookies', 'yt.json')
    use_cookies = os.path.isfile(COOKIES_FILE) and os.path.getsize(COOKIES_FILE) > 0

    progress_msg = ""
    downloaded_filenames = []  # Lista para armazenar os nomes dos vídeos finais baixados
    def download_thumbnail(thumbnail_url, output_path):
        response = requests.get(thumbnail_url)
        if response.status_code == 200:
            with open(output_path, 'wb') as file:
                file.write(response.content)
            print(f"Thumbnail baixada com sucesso: {output_path}")
            return True
        else:
            print(f"Falha ao baixar a thumbnail. Status code: {response.status_code}")
            return False

    def progress_hook(d):
        if d.get('status') == 'postprocessed':
            outfile = d.get('outfile')
            if outfile:
                # Adiciona o arquivo final, se ainda não estiver na lista
                if outfile not in downloaded_filenames:
                    downloaded_filenames.append(outfile)


    # if linux_env == True:
    #     # 'format': ( 'bestvideo[height=1080]+bestaudio/' 'bestvideo[height=720]+bestaudio/' 'bestvideo[height=480]+bestaudio/' 'bestvideo[height=360]+bestaudio/' 'best' ),

    #     ydl_opts = {
    #         'format': 'bv*[height<=1080]+ba/b[height<=1080]',
    #         'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s').replace('？','_').replace('á','a'),
    #         'quiet': False,
    #         'windowsfilenames': True,
    #         'overwrites': True,

    #         'ignoreerrors': True,
    #         'skip_download_errors': True,
    #         'user_agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    #                     'AppleWebKit/537.36 (KHTML, like Gecko) '
    #                     'Chrome/XX.0.0.0 Safari/537.36'),
    #         # 'merge_output_format': 'mp4',
    #         # 'postprocessors': [{'key': 'FFmpegMerger'}],
           
    #         'cookiefile': COOKIES_FILE,
    #         'progress_hooks': [progress_hook],
    #         # --- novas opções importantes ---
    #         # priorizar player android (frequentemente tem URLs estáveis) e depois web
    #         'extractor_args': {'youtube': {'player_client': 'android,web'}},
    #         # tenta extrair formatos mesmo que sejam "unplayable" (HLS/m3u8) — evita erro imediato
    #         'allow_unplayable_formats': True,
    #         # ignora erro de "no formats" (útil pra só coletar metadados sem falhar)
    #         'ignore_no_formats_error': True,
    #         # ajuda a debugar; remova se desejar menos verbosidade
    #         'verbose': True,
    #     }
    # elif linux_env == False:
    path_ffmpegexe = os.path.join(os.path.dirname(__file__),
                                    "../",
                                    "Utils",
                                    "ffmpeg",
                                    "ffmpeg.exe"
                                )
    print(path_ffmpegexe)
    ydl_opts = {
        # 'ffmpeg_location': path_ffmpegexe,  # Diretório onde está o ffmpeg.exe
        'format': 'bv*[vcodec^=avc1][height<=1080]+ba[ext=m4a]/b[vcodec^=avc1][height<=1080]',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s').replace('？','_').replace('á','a'),
        'quiet': False,
        'windowsfilenames': True,
        'overwrites': True,
        'allow_unplayable_formats': False,
        'ignore_no_formats_error': True,
        'ignoreerrors': True,
        'skip_download_errors': True,
        'geo_bypass': True,
        'nocheckcertificate': True,
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegMerger'

        }],
        'cookiefile': COOKIES_FILE,
        'progress_hooks': [progress_hook],
        'extractor_args': {'youtube': {'player_client': 'web' if use_cookies else 'android,web'}},

        'verbose': False,
    }

    new_downloads = 0
    titulo =None
    output_path_thumbnail = None
    hash_str = None
    thumbnail_url = None
    new_video_ids = set()
    if not isinstance(videos, list):
        videos = [videos]
    for video in videos:
        video_id = video['id']
        if video_id not in downloaded_videos:
            try:
                new_downloads += 1
                
                video_url = f"https://www.youtube.com/watch?v={video_id}"

                success = False

                # Estratégia 2: Se o progressivo falhar, tentar formato que requer merge
                if not success:
                    try:
              
                        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                            # ydl.add_post_processor(FFmpegNVEnc(ydl))
                            ydl.download([video_url])
                        success = True
                        print(f"[yt_dlp com merge] vídeo baixado com sucesso: {video_id}")
                    except KeyError as e:
                        if '__files_to_merge' in str(e):
                            print(f"[yt_dlp com merge] erro de merge, tentando fallback...")
                            # Se ocorrer erro de merge, tentar método alternativo
                            success = False
                        else:
                            raise e
                    except Exception as e:
                        print(f"[yt_dlp com merge] falhou: {e}")


                # # 3️⃣ Fallback real: pytube
                # if not success:
                #     try:
                #         yt = YouTube(video_url)
                #         stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
                       
                #         output_file = stream.download(output_path=output_dir)
                #         downloaded_filenames.append(output_file)
                #         success = True
                #         print(f"[pytube] vídeo baixado com sucesso: {output_file}")
                #     except Exception as e:
                #         print(f"[pytube] falhou para {video_id}: {e}")


                print("????????????????????????????")
                try:
                    titulo = get_video_title(video_id)

                    thumbnail_url = get_video_thumbnail(video_id)
                                
                    hash_str = hashlib.sha256(f"{time.time()}".encode()).hexdigest()[:10]
                    os.makedirs(os.path.join(output_path_, f"{channel}"), exist_ok=True)
                    output_path_thumbnail = os.path.join(output_path_, f"{channel}", f"{video_id}_{hash_str}.jpg")
                    download_thumbnail(thumbnail_url, output_path_thumbnail)
                    
                except Exception as e:
                    print(f"Erro inesperado ao baixar vídeo {video_url}: {str(e)}")
                    
                new_video_ids.add(video_id)
            except yt_dlp.utils.DownloadError as e:
                print(f"Erro ao baixar vídeo {video_url}: {str(e)}")
                continue  
            except Exception as e:
                print(f"Erro inesperado ao baixar vídeo {video_url}: {str(e)}")

    return new_downloads, new_video_ids, titulo, output_path_thumbnail, thumbnail_url
        
if __name__ == '__main__':
    base_dir = os.path.join(os.path.dirname(__file__),
                                    "MediaBase")
    os.makedirs(base_dir, exist_ok=True)
    canal_do_yt = "YmaGu"
    video_id = "ctm3B_qj4FA"
    path_ffmpegnotexe = os.path.join(os.path.dirname(__file__),
                                    "../",
                                    "Utils",
                                    "ffmpeg"
                                )
    os.environ['PATH'] = path_ffmpegnotexe + os.pathsep + os.environ['PATH']
   
    #"C:\Users\Media Cuts DeV\Downloads\HomeServer\HomeServer\internalserver\Studio\Utils\ffmpeg"
    videos = [{'id': video_id}]
    new_downloads, new_video_ids, titulo, output_miniatura, thumbnail_url = download_new_videos(
        videos=videos,
        output_dir=base_dir,
        channel=canal_do_yt,
        # path_ffmpegnotexe=path_ffmpegnotexe,
        linux_env=True,
        output_path_=base_dir,
        downloaded_videos=[] 
    )
