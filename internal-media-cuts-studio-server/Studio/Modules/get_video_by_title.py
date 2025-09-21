

import os
PRODUCTION_ENV = os.getenv("PRODUCTION_ENV", "True")

if PRODUCTION_ENV == "True":
    # Production
    from Studio.Modules.__init_libs__ import *
    from Studio.Modules.normalize_title import normalize_title
    from Studio.Modules.get_video_title import get_video_title
    from Studio.Modules.DetectEnglish import DetectEnglish
    from Studio.Modules.TranslateEnglishtoPortuguese import TranslateEnglishtoPortuguese
    from Studio.Modules.loop_threshold_norm_target import loop_threshold_norm_target
 
elif PRODUCTION_ENV == "False":
    # Local test
    from Modules.__init_libs__ import *
    from Modules.normalize_title import normalize_title
    from Modules.get_video_title import get_video_title
    from Modules.DetectEnglish import DetectEnglish
    from Modules.TranslateEnglishtoPortuguese import TranslateEnglishtoPortuguese
    from Modules.loop_threshold_norm_target import loop_threshold_norm_target
    
async def get_video_by_title(
    canal_url: str = "",
    title_target: str = "",
    max_checks: int = 20,
    max_checks_to_translate: int = 10,
    path_ffmpegnotexe: str = "",
    linux_env: bool = False,
    logger= "",

    ):
    """
    Percorre vídeos de um canal YouTube (yt-dlp), traduz e normaliza títulos,
    e retorna o primeiro vídeo cuja similaridade com `title_target` ultrapasse
    `threshold` (%) ou seja EXATAMENTE igual.
    Retorna: (channel_title_pt, video_entry, sim_score) ou (channel_title_pt, None, None).
    """
    videos_url = f"{canal_url}/videos"
    if linux_env == True:
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'ignoreerrors': True,
            'skip_download': True,
            'extract_flat': 'in_playlist',
            'timeout': 30,
        }
        ydl_opts['playlist_items'] = f"1-{max_checks}"

    elif linux_env == False:
        ydl_opts = {
            'ffmpeg_location': path_ffmpegnotexe,  
            'quiet': True,
            'no_warnings': True,
            'ignoreerrors': True,
            'skip_download': True,
            'extract_flat': 'in_playlist',
            'timeout': 30,
        }
        ydl_opts['playlist_items'] = f"1-{max_checks}"

    print(f"get_video_by_title ")
    target_norm = normalize_title(s=title_target)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        
        try:
            info = ydl.extract_info(canal_url, download=False)
            print(f"info ")
            channel_title = info.get('title', canal_url)
            # channel_title_pt = translate_to_pt(channel_title)
        except Exception as e:
            cprint(f"❌ Erro ao obter título do canal: {e}", 'red')
            raise

        contador_ = 0        
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

            id_video = video.get('id', '')
            video_title = get_video_title(video_id=f"{id_video}")
            norm = normalize_title(s=video_title)
            cprint(f"[{idx}] norm: {norm!r}", 'magenta')
            cprint(f" target: {target_norm!r}", 'magenta')
            contador_ += 1
            if contador_ == max_checks_to_translate:
                break

            if norm == target_norm:
                return channel_title, video


        English_flag = await DetectEnglish(
            text=target_norm,
            logger=logger
        )
        logger.info(f"English_flag? {English_flag}")
        if English_flag == True:
            target_norm = await TranslateEnglishtoPortuguese(
                text=target_norm,
                logger=logger
            )
            logger.info(f"target_norm? {target_norm}")
            
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

            id_video = video.get('id', '')
            video_title = get_video_title(video_id=f"{id_video}")
            norm = normalize_title(s=video_title)
            cprint(f"[{idx}] norm: {norm!r}", 'magenta')
            cprint(f" target: {target_norm!r}", 'magenta')
            flag = loop_threshold_norm_target(norm, target_norm)
            if flag == True:
                return channel_title, video

            if norm == target_norm:
                return channel_title, video
            
    return channel_title, None

