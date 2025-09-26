# Studio\Shortify.py
import os
import sys
import json
import time
import asyncio
import re
import subprocess
import platform
from datetime import datetime, timedelta
from queue import Queue, Empty
import unicodedata
import requests
import yt_dlp
from firebase_admin import credentials, initialize_app, storage, db, delete_app
from termcolor import cprint
from dotenv import dotenv_values
from pathlib import Path
import unicodedata
from queue import Queue, Empty
import unicodedata
from pathlib import Path
import threading
import shutil
import whisper
import math
from concurrent.futures import ThreadPoolExecutor
# import wave
import srt
import yt_dlp
import psutil
from firebase_admin import credentials, initialize_app, storage, db, delete_app
from pathlib import Path
from termcolor import cprint
import cv2
from difflib import SequenceMatcher
import base64
import os
import requests
import zipfile
import logging
from dotenv import load_dotenv

import unicodedata
# from googletrans import Translator


########################################################################
# IMPORT CoreApp

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "Keys", "env.env"))

PRODUCTION_ENV = os.getenv("PRODUCTION_ENV", "True")

if PRODUCTION_ENV == "True":
    # Production
    from Studio.Studio import MediaCutsStudio
    from Studio.AICuration import AI_Curation

    from Studio.Modules.__init__ import *


if PRODUCTION_ENV == "False":
    # Local test
    from .Studio import MediaCutsStudio
    from .AICuration import AI_Curation

    from .Modules.__init__ import *

########################################################################

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Shortify_logger")

class ShortifyAlgo:
    """
    Automatiza a criação de cortes de vídeos do YouTube e o agendamento para o TikTok.

    Este algoritmo estático, sem aprendizado de máquina, foi projetado para
    otimizar e automatizar o processo de transformar vídeos longos do YouTube
    em clipes curtos e dinâmicos para plataformas como o TikTok. Ele gerencia
    desde o download do conteúdo original até a aplicação de legendas,
    configurações de vídeo e upload agendado.


    """
    def __init__(self,
                user_Control_Panel_ref,
                includeHorizontal,
                includeVertical,
                app1,
                appdocs,
                user_email,
                TiktokAccount,
                TiktokAccountCookies,
                canal_do_yt,
                current_date,
                date_time,
                Cutting_seconds,
                secondsScheduleTiktokVideo,
                StudioMode,
                downloadToPanelEnabled,
                task_id,
                hash_id,
                title_origin,
                pastedUrl,

                UPLOAD_URL,
                api_key,
                WEBHOOK_URL,
                WEBHOOK_ZIP_URL,
                text_edit_download,

                SubtitleColor,
                SubtitleAnimation, 
                SubtitleFontName,
                SubtitleEffects,
                SubtitleFontsize,
                SubtitleVerticalReference, 


                CaptionsColor,
                CaptionsFontName,
                CaptionsAlignment,
                CaptionsFontsize, 
                CaptionsPrimaryColour, 
                CaptionsSecondaryColour, 
                CaptionsOutlineColour, 
                CaptionsBackColour, 
                CaptionsBold, 
                CaptionsItalic, 
                CaptionsUnderline, 
                CaptionsOutline, 
                CaptionsShadow, 
                CaptionsRevealEffectInitialColor, 
                CaptionsRevealEffectFinalColor, 

                legendstheme,
                editiontheme,
                hwaccel="cuda",
                hwaccel_encode_device="0",
                vcodec="h264_nvenc",
                vcodec_audio="copy",
                preset="medium",
                gpu_="0",
                profile="high",
                bitrate="100M",
                maxrate="100M",
                bufsize="400M",
                
                webhook = True,
                dockerffmpegGPU=True,
                dockerffmpegCPU=False,

                production=True,
                lastlongvideo=True,
                videoTitleForLatestVideo=None,
                lastlongvideotitle=None,
                titleForTiktokCutsEnabled=False,
                titleForTiktokCuts=None,
                hashtagsForTiktokCutsEnabled=False,
                hashtagsForTiktokCuts=None

                ):
        super().__init__() 
        self.user_Control_Panel_ref = user_Control_Panel_ref
        self.includeHorizontal = includeHorizontal
        self.includeVertical = includeVertical
        self.UPLOAD_URL = UPLOAD_URL
        self.videoTitleForLatestVideo = videoTitleForLatestVideo
        self.production = production
        self.StudioMode = StudioMode
        self.downloadToPanelEnabled = downloadToPanelEnabled
        self.hashtagsForTiktokCutsEnabled = hashtagsForTiktokCutsEnabled
        self.hashtagsForTiktokCuts = hashtagsForTiktokCuts
        self.titleForTiktokCuts = titleForTiktokCuts
        self.titleForTiktokCutsEnabled = titleForTiktokCutsEnabled
        self.lastlongvideo = lastlongvideo
        self.lastlongvideotitle = lastlongvideotitle
        self.app1 = app1
        self.appdocs = appdocs
        self.user_email = user_email.replace(".", "_")
        self.user_email_origin = user_email
        self.TiktokAccount = TiktokAccount
        self.TiktokAccountCookies = TiktokAccountCookies
        self.api_key = api_key
        self.current_date = current_date
        self.date_time = date_time
        self.task_id = task_id
        self.hash_id= hash_id
        self.title_origin = title_origin
        self.pastedUrl = pastedUrl

        self.webhook = webhook
        self.WEBHOOK_URL = WEBHOOK_URL
        self.WEBHOOK_ZIP_URL = WEBHOOK_ZIP_URL
        self.text_edit_download = text_edit_download 
        self.Cutting_seconds = Cutting_seconds
        self.secondsScheduleTiktokVideo = secondsScheduleTiktokVideo
        self.SubtitleColor = SubtitleColor 
        self.SubtitleAnimation = SubtitleAnimation
        self.SubtitleFontName = SubtitleFontName 
        self.SubtitleEffects = SubtitleEffects 
        self.SubtitleFontsize = SubtitleFontsize 
        self.SubtitleVerticalReference = SubtitleVerticalReference 
        self.CaptionsColor = CaptionsColor 
        self.CaptionsFontName = CaptionsFontName 
        self.CaptionsAlignment = CaptionsAlignment 
        self.CaptionsFontsize = CaptionsFontsize 
        self.CaptionsPrimaryColour = CaptionsPrimaryColour 
        self.CaptionsSecondaryColour = CaptionsSecondaryColour 
        self.CaptionsOutlineColour = CaptionsOutlineColour 
        self.CaptionsBackColour = CaptionsBackColour 
        self.CaptionsBold = CaptionsBold 
        self.CaptionsItalic = CaptionsItalic 
        self.CaptionsUnderline = CaptionsUnderline 
        self.CaptionsOutline = CaptionsOutline 
        self.CaptionsShadow = CaptionsShadow 
        self.CaptionsRevealEffectInitialColor = CaptionsRevealEffectInitialColor 
        self.CaptionsRevealEffectFinalColor = CaptionsRevealEffectFinalColor 

        self.hwaccel = hwaccel
        self.hwaccel_encode_device = hwaccel_encode_device
        self.vcodec = vcodec
        self.vcodec_audio = vcodec_audio
        self.preset = preset
        self.gpu_ = gpu_
        self.profile = profile
        self.bitrate = bitrate
        self.maxrate = maxrate
        self.bufsize = bufsize
        self.canal_do_yt = canal_do_yt

        self.dockerffmpegGPU = dockerffmpegGPU
        self.dockerffmpegCPU = dockerffmpegCPU

        self.editiontheme = editiontheme
        self.legendstheme = legendstheme
        self.diretorio_script = os.path.dirname(os.path.abspath(__file__))
        self.log_file = os.path.join(self.diretorio_script, "WorkEnvironment", 'task_log.log') 
        self.downloadted_file = os.path.join(self.diretorio_script, "WorkEnvironment", 'task_log.json') 

        # path_ffmpeg = os.path.join(diretorio_script, 'Utils', 'ffmpeg', 'ffmpeg.exe')
        self.path_ffmpegnotexe = os.path.join(self.diretorio_script, 'Utils', 'ffmpeg')
        # os.environ['PATH'] = path_ffmpegnotexe + os.pathsep + os.environ['PATH']


    async def Shortify(self,
              

        ):
        inicio = time.time() 

        file_tasks_video_base = os.path.join(self.diretorio_script, "WorkEnvironment", f'task_log.json')
        path_process = os.path.join(self.diretorio_script, "WorkEnvironment", "Process")
        path_tiktok_video_upload = os.path.join(self.diretorio_script, "TiktokAutoUploader_TESTE", "VideosDirPath")
        path_AICuration = os.path.join(self.diretorio_script, "WorkEnvironment", "Process", "AICuration", "Transcript")
        
        if self.production == True:
            pass
        elif self.production == False:
            try:
                shutil.rmtree(path_process)
            except:
                pass

            try:
                shutil.rmtree(path_tiktok_video_upload)
            except:
                pass

            try:
                os.remove(file_tasks_video_base)
            except:
                pass

            with open(file_tasks_video_base, "x") as file:
                file.write("""[]""")

            try:
                shutil.rmtree(path_AICuration)
            except:
                pass

            os.makedirs(path_process, exist_ok=True)
            os.makedirs(path_AICuration, exist_ok=True)

        base_dir = os.path.abspath(
            os.path.join(self.diretorio_script, "WorkEnvironment", "Process", "MediaBase",  f'{self.canal_do_yt}')
        )

        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        canal_do_yt_replace =  self.canal_do_yt.replace('- Videos', '')
        if self.webhook == True:
            self.send_to_webhook(self.api_key, "Mode", f"Shortify - Date", "yellow")
            self.send_to_webhook(self.api_key, "cuts_duration", f"{self.Cutting_seconds}", "green")
            self.send_to_webhook(self.api_key, "Status", f"Running", "yellow")
            self.send_to_webhook(self.api_key, "TiktokAccount", f"{self.TiktokAccount}", "green")
            self.send_to_webhook(self.api_key, "YtChannel", f"@{canal_do_yt_replace}", "green")
            self.send_to_webhook(self.api_key, "Createdat", f"{created_at}", "yellow")
            self.send_to_webhook(self.api_key, "mediabase", f"in download...", "yellow")
            self.send_to_webhook(self.api_key, "target", f"0/0", "yellow")
            self.send_to_webhook(self.api_key, "Thread", f"In progres...", "yellow")


        self.send_to_webhook(self.api_key, "info", "🔑 Studio - Fetch sha256 Hash", "yellow")

        hash_do_dia = self.hash_id[:15]
        self.send_to_webhook(self.api_key, "Thread", f"{hash_do_dia}", "yellow")
        

        if self.webhook == True:
            self.send_to_webhook(self.api_key, "notification", f"🚀 Shortify is Initializing, open the process control panel to observe the work", "yellow")

        cprint("🚀 Shortify Algo V1 – Initializing Shortify", "blue")
        if self.webhook == True:
            self.send_to_webhook(self.api_key, "info", "🚀 Shortify Algo V1 – Initializing Shortify", "blue")
            self.send_to_webhook(self.api_key, "progress", 0, "yellow")


        cprint(f"🚀 title_origin {self.title_origin}")
        cprint("🚀 Shortify Algo V1 - Algorithm starting checking for new videos...")
        if self.webhook == True:
            self.send_to_webhook(self.api_key, "info", "🚀 Shortify Algo V1 - Algorithm starting checking for new videos...", "blue")
            self.send_to_webhook(self.api_key, "progress", 0, "yellow")

        try:
            user_control_data = self.user_Control_Panel_ref.get()
            if not user_control_data or 'project_simultaneo' not in user_control_data:
                logger.error(f"Dados de controle de usuário ou 'project_simultaneo' não encontrados para a api_key. Pulando...")
            
            limite_simultaneo = user_control_data['project_simultaneo']
            projects_videos_base_completed_count = user_control_data.get('projects_videos_base_completed', 0) # Novo campo para controle
            projects_running_count = user_control_data.get('projects_running', 0) # Novo campo para controle
        except Exception as e:
            logger.error(f"Erro ao buscar dados de controle para  {e}")
            
        novo_valor = min(limite_simultaneo, projects_running_count + 1)
        self.user_Control_Panel_ref.update({
            'projects_running': novo_valor,
            'projects_videos_base_completed': projects_videos_base_completed_count + 1
            })
        if str(self.editiontheme) == "AI Vertical Fusion":

            AI_Curation_instance = AI_Curation(
                
                includeHorizontal=self.includeHorizontal,
                includeVertical=self.includeVertical,
                StudioMode=self.StudioMode,
                linux_env=True,
                downloadToPanelEnabled=self.downloadToPanelEnabled,
                secondsScheduleTiktokVideo=self.secondsScheduleTiktokVideo,
                TiktokAccount=self.TiktokAccount,
                TiktokAccountCookies=self.TiktokAccountCookies,
                user_email=self.user_email,
                user_email_origin=self.user_email_origin,
                canal_do_yt=canal_do_yt_replace, 
                lastlongvideotitle=self.title_origin,
                app_instance=self.app1,
                appdocs=self.appdocs,
                task_id=self.task_id,
                title_origin=self.title_origin,
                pastedUrl=self.pastedUrl,
                Cutting_seconds=self.Cutting_seconds,

                SubtitleColor=self.SubtitleColor,
                SubtitleAnimation=self.SubtitleAnimation, 
                SubtitleFontName=self.SubtitleFontName,
                SubtitleEffects=self.SubtitleEffects,
                SubtitleFontsize=self.SubtitleFontsize,
                SubtitleVerticalReference=self.SubtitleVerticalReference, 

                CaptionsColor=self.CaptionsColor,
                CaptionsFontName=self.CaptionsFontName,
                CaptionsAlignment=self.CaptionsAlignment,
                CaptionsFontsize=self.CaptionsFontsize, 
                CaptionsPrimaryColour=self.CaptionsPrimaryColour, 
                CaptionsSecondaryColour=self.CaptionsSecondaryColour, 
                CaptionsOutlineColour=self.CaptionsOutlineColour, 
                CaptionsBackColour=self.CaptionsBackColour, 
                CaptionsBold=self.CaptionsBold, 
                CaptionsItalic=self.CaptionsItalic, 
                CaptionsUnderline=self.CaptionsUnderline, 
                CaptionsOutline=self.CaptionsOutline, 
                CaptionsShadow=self.CaptionsShadow, 
                CaptionsRevealEffectInitialColor=self.CaptionsRevealEffectInitialColor, 
                CaptionsRevealEffectFinalColor=self.CaptionsRevealEffectFinalColor, 
                legendstheme=self.legendstheme,
                editiontheme=self.editiontheme,

                webhook=True,
                api_key=self.api_key

                


                    
            )
            await AI_Curation_instance.main()


        elif str(self.editiontheme) == "Thumbnail Vertical Fusion":



            cprint(f"🚀 editiontheme {self.editiontheme}")
            if self.lastlongvideo == True or self.lastlongvideo == "true" or self.lastlongvideo == "True": 
                canal_url = f"https://www.youtube.com/@{self.canal_do_yt}"  
                downloaded_videos = self.load_downloaded_videos()
                canal_nome, videos = get_channel_info(canal_url)
                if not videos:
                    cprint("Shortify Algo V1 - Nenhum vídeo encontrado no canal")
                    if self.webhook == True:
                        self.send_to_webhook(self.api_key, "info", "🚀 Shortify Algo V1 - Nenhum vídeo encontrado no canal", "blue")
                        self.send_to_webhook(self.api_key, "progress", 0, "yellow")
                        self.send_to_webhook(self.api_key, "notification", f"Shortify did not find any new videos on the channel", "yellow")

                    return
                    
            elif self.lastlongvideo == False or self.lastlongvideo == "false" or self.lastlongvideo == "False":
                if self.webhook == True:    
                    self.send_to_webhook(self.api_key, "info", f"🚀 Shortify Algo V1 - Download {self.lastlongvideotitle}", "blue")
                downloaded_videos = self.load_downloaded_videos()
                canal_nome, videos = await get_video_by_title(
                    canal_url=f"https://www.youtube.com/@{self.canal_do_yt}", 
                    title_target=self.lastlongvideotitle,
                    path_ffmpegnotexe=self.path_ffmpegnotexe,
                    linux_env=self.dockerffmpegGPU,
                    logger=logger
                                
                    )
                if not videos:
                    cprint("Shortify Algo V1 - Nenhum vídeo encontrado no canal")
                    if self.webhook == True:
                        self.send_to_webhook(self.api_key, "info", "🚀 Shortify Algo V1 - Nenhum vídeo encontrado no canal", "blue")
                        self.send_to_webhook(self.api_key, "progress", 0, "yellow")
                        self.send_to_webhook(self.api_key, "notification", f"Shortify did not find any new videos on the channel", "yellow")
                    return
                



            cprint(f"Shortify Algo V1 - Canal: {canal_nome}")

            if self.webhook == True:
                self.send_to_webhook(self.api_key, "info", f"🚀 Shortify Algo V1 - Canal: {canal_nome}", "yellow")


            output_dir = self.create_download_directory(base_dir)

            canal_nome_str = f"{canal_nome}"
            canal_nome = canal_nome_str.replace("- Videos", "").replace(" ", "")

            new_downloads, new_video_ids, downloaded_filenames, output_miniatura, thumbnail_url = download_new_videos(
                                                videos=videos, 
                                                output_dir=base_dir, 
                                                channel=self.canal_do_yt, 
                                                linux_env=True, 
                                                path_ffmpegnotexe=self.path_ffmpegnotexe,
                                                output_path_ = os.path.join(os.path.dirname(__file__), 
                                               "WorkEnvironment",  
                                               "Process", 
                                               "MediaBase"),
                                               downloaded_videos=downloaded_videos
                                               )
            


            logger.info(f"old {downloaded_filenames}")

            # downloaded_filenames = self.clean_name_to_ytdl_filename_compatible(downloaded_filenames)

            # logger.info(f"new {downloaded_filenames}")

            downloaded_videos.update(new_video_ids)

            self.save_downloaded_videos(downloaded_videos)
            
            logger.info(f"Shortify Algo V1 - New videos downloaded: {new_downloads}")

            if self.webhook == True:
                self.send_to_webhook(self.api_key, "info", f"Shortify Algo V1 - New videos downloaded: {new_downloads}", "yellow")
            
            nome_rename_final = self.rename_file_mp4(self.canal_do_yt, downloaded_filenames)
            
            if nome_rename_final:
                logger.info(f"nome_rename_final? {nome_rename_final}")
            
                    
                MediaCutsStudio_class = MediaCutsStudio(
                    app1=self.app1,
                    user_email=self.user_email,
                    yt_channel=self.canal_do_yt,
                    TiktokAccount=self.TiktokAccount,
                    TiktokAccountCookies=self.TiktokAccountCookies,
                    video_path=nome_rename_final,
                    current_date=self.current_date,
                    date_time=self.date_time,
                    Cutting_seconds=self.Cutting_seconds,
                    secondsScheduleTiktokVideo=self.secondsScheduleTiktokVideo,
                    titleForTiktokCutsEnabled=self.titleForTiktokCutsEnabled,
                    titleForTiktokCuts=self.titleForTiktokCuts,
                    hashtagsForTiktokCutsEnabled=self.hashtagsForTiktokCutsEnabled,
                    hashtagsForTiktokCuts=self.hashtagsForTiktokCuts,


                    api_key=self.api_key,
                    WEBHOOK_URL=self.WEBHOOK_URL,
                    WEBHOOK_ZIP_URL=self.WEBHOOK_ZIP_URL,
                    text_edit_download=None,

                    SubtitleColor=self.SubtitleColor,
                    SubtitleAnimation=self.SubtitleAnimation, 
                    SubtitleFontName=self.SubtitleFontName,
                    SubtitleEffects=self.SubtitleEffects,
                    SubtitleFontsize=self.SubtitleFontsize,
                    SubtitleVerticalReference=self.SubtitleVerticalReference, 

                    CaptionsColor=self.CaptionsColor,
                    CaptionsFontName=self.CaptionsFontName,
                    CaptionsAlignment=self.CaptionsAlignment,
                    CaptionsFontsize=self.CaptionsFontsize, 
                    CaptionsPrimaryColour=self.CaptionsPrimaryColour, 
                    CaptionsSecondaryColour=self.CaptionsSecondaryColour, 
                    CaptionsOutlineColour=self.CaptionsOutlineColour, 
                    CaptionsBackColour=self.CaptionsBackColour, 
                    CaptionsBold=self.CaptionsBold, 
                    CaptionsItalic=self.CaptionsItalic, 
                    CaptionsUnderline=self.CaptionsUnderline, 
                    CaptionsOutline=self.CaptionsOutline, 
                    CaptionsShadow=self.CaptionsShadow, 
                    CaptionsRevealEffectInitialColor=self.CaptionsRevealEffectInitialColor, 
                    CaptionsRevealEffectFinalColor=self.CaptionsRevealEffectFinalColor, 

                    path_ffmpeg="self.path_ffmpeg",
                    path_ffprobe="self.path_ffprobe",
                    path_ffmpegnotexe="self.path_ffmpegnotexe",
                    legendstheme=self.legendstheme,
                    theme=self.editiontheme,
                    hwaccel=self.hwaccel,
                    hwaccel_encode_device=self.hwaccel_encode_device,
                    vcodec=self.vcodec,
                    vcodec_audio=self.vcodec_audio,
                    preset=self.preset,
                    gpu_=self.gpu_,
                    profile=self.profile,
                    bitrate=self.bitrate,
                    maxrate=self.maxrate,
                    bufsize=self.bufsize,
                    
                    webhook=self.webhook,
                    dockerffmpegGPU = self.dockerffmpegGPU,
                    dockerffmpegCPU = self.dockerffmpegCPU,

                    output_miniatura=output_miniatura
                )
                MediaCutsStudio_class.main()

                fim = time.time()  
                processing_time = fim - inicio
                horas, resto = divmod(processing_time, 3600)
                minutos, segundos = divmod(resto, 60)
                tempo_formatado = f"{int(horas):02}:{int(minutos):02}:{int(segundos):02}"
                logger.info(f"Tempo de execução: {tempo_formatado}")
                if self.webhook == True:
                    self.send_to_webhook(self.api_key, "timestamp", f"{tempo_formatado}", "yellow")

        else:
            cprint("Failed")


    def send_to_webhook(self, user, type, message, cor):
        """Envia uma mensagem para o webhook."""
        # Envia o conteúdo da mensagem como JSON
        requests.post(self.WEBHOOK_URL, json={str(user): {"type": type, "message": message}})


        
    def clean_name_to_ytdl_filename_compatible(self, filename:str):

        substitutions = {
            "z'": "z",
            "ft.": "ft",
            "À": "A",
            "Á": "A",
            "Ó": "O",
            "Ç": "C",
            "Í": "I",
            "É": "E",
            "é": "e",
            "Ã": "A",
            "Ô": "O",
            "Õ": "O",
            "｜": "",
            ",": "",
            "...": "",
            "'": "",
            "?": "",
            "!": "",
            " ": "_",
            "z'": "",
            "(+": "+", 
            ")": "_", 
            "  ": "_", 
            " ": "_", 
            "'": "", 
            "!": "", 
            "'": "", 
            "O G": "_", 


        }
        for key, value in substitutions.items():
            stem = filename.replace(key, value)

        logger.info(f"stem? {stem}")

        # # stem = unicodedata.normalize('NFKD', stem).encode('ASCII', 'ignore').decode('ASCII')

        # stem = re.sub(r'[<>:"/\\|?*]', '', stem)

        # stem = stem.replace("'", '').replace("!", '')

        # stem = stem.replace("", '_').replace("O G", '_')
        # stem = stem.replace("  ", '_').replace("O G", '_')


        return stem


    def clear_file_name_to_rename(self, filename):
        """
        Limpa o nome do arquivo para buscar corretamente, na pasta mediabase
        """
        p = Path(filename)
        stem = p.stem   # parte sem a extensão
        extension = p.suffix  # inclui o ponto, ex.: ".mp4"

        # 1. Substituições explícitas para tratar casos específicos
        substitutions = {
            "z'": "z",
            "ft.": "ft",
            "À": "A",
            "Á": "A",
            "Ó": "O",
            "Ç": "C",
            "Í": "I",
            "É": "E",
            "é": "e",
            "Ã": "A",
            "Ô": "O",
            "Õ": "O",
            "｜": "",
            ",": "",
            "...": "",
            "'": "",
            "?": "",
            "!": "",
            " - ": " ",
            "(+": "_", 
            ")": "_", 
        }
        for key, value in substitutions.items():
            stem = stem.replace(key, value)

        # 2. Normaliza o texto (remove acentos e converte para ASCII)
        stem = unicodedata.normalize('NFKD', stem).encode('ASCII', 'ignore').decode('ASCII')

        # 3. Remove caracteres ilegais para nomes de arquivo no Windows: < > : " / \ | ? *
        stem = re.sub(r'[<>:"/\\|?*]', '', stem)

        # 4. Remove qualquer outro caractere indesejado, mantendo apenas letras, números, espaços, hífens e underscores
        stem = re.sub(r'[^\w\s-]', '', stem)

        # 5. Consolida múltiplos espaços ou hífens e aparar os extremos
        stem = re.sub(r'[-\s]+', ' ', stem).strip()

        # 6. (Opcional) Se o ffmpeg preferir nomes sem espaços, converte para underscore
        stem = stem.replace(' ', '_')

        # 7. Verifica se o 'stem' já termina com o nome da extensão (sem o ponto) e remove se necessário
        ext_without_dot = extension.lower()[1:]
        if stem.lower().endswith(ext_without_dot):
            stem = stem[:-len(ext_without_dot)]
            stem = stem.rstrip('_')  # remove underscore final se existir

        stem = stem.replace(' ', '_')

        stem = stem.replace('-', '')

        return f"{stem}{extension}"


    def clear_file_name_to_search_correctly(self, filename):
        """
        Limpa o nome do arquivo para buscar corretamente, na pasta mediabase
        """
        p = Path(filename)
        stem = p.stem   # parte sem a extensão
        extension = p.suffix  # inclui o ponto, ex.: ".mp4"

        # 1. Substituições explícitas para tratar casos específicos
        substitutions = {
            "z'": "z",
            "ft.": "ft",
            "À": "A",
            "Á": "A",
            "Ó": "O",
            "Ç": "C",
            "Í": "I",
            "É": "E",
            "é": "e",
            "Ã": "A",
            "Ô": "O",
            "Õ": "O",
            "｜": "",
            ",": "",
            "...": "",
            "'": "",
            "?": "",
            "!": "",
            " - ": " ",
            "(+": "+", 
            ")": "_", 
        }
        for key, value in substitutions.items():
            stem = stem.replace(key, value)

        # 2. Normaliza o texto (remove acentos e converte para ASCII)
        stem = unicodedata.normalize('NFKD', stem).encode('ASCII', 'ignore').decode('ASCII')

        # 3. Remove caracteres ilegais para nomes de arquivo no Windows: < > : " / \ | ? *
        stem = re.sub(r'[<>:"/\\|?*]', '', stem)

        # 4. Remove qualquer outro caractere indesejado, mantendo apenas letras, números, espaços, hífens e underscores
        stem = re.sub(r'[^\w\s-]', '', stem)

        # 5. Consolida múltiplos espaços ou hífens e aparar os extremos
        stem = re.sub(r'[-\s]+', ' ', stem).strip()

        # 6. (Opcional) Se o ffmpeg preferir nomes sem espaços, converte para underscore
        stem = stem.replace(' ', '_')

        # 7. Verifica se o 'stem' já termina com o nome da extensão (sem o ponto) e remove se necessário
        ext_without_dot = extension.lower()[1:]
        if stem.lower().endswith(ext_without_dot):
            stem = stem[:-len(ext_without_dot)]
            stem = stem.rstrip('_')  # remove underscore final se existir

        stem = stem.replace(' ', '_')

        stem = stem.replace('-', '')

        return f"{stem}{extension}"


    def safe_rename(self, original, new):
        short_path = original
        os.rename(short_path, new)

    def normalize_find_and_rename_mp4(self, name: str) -> str:
        # Remove acentos
        nfkd = unicodedata.normalize('NFKD', name)
        only_ascii = nfkd.encode('ASCII', 'ignore').decode('ASCII')
        # Remove pontuação e unifica espaços/underscores
        cleaned = re.sub(r'[\W]+', '_', only_ascii)
        return cleaned.strip('_').upper()

    def find_and_rename_mp4(
        self,
        base_dir: str,
        original_name: str,
        new_name: str,
        threshold: float = 0.8
    ) -> str:
        """
        Percorre base_dir procurando arquivos .mp4 cuja similaridade com original_name seja >= threshold.
        Se encontrar, renomeia para new_name e retorna o caminho final.
        """
        original_norm = self.normalize_find_and_rename_mp4(original_name)
        for root, _, files in os.walk(base_dir):
            for fname in files:
                if not fname.lower().endswith('.mp4'):
                    continue

                orig_path = os.path.join(root, fname)
                fname_norm = self.normalize_find_and_rename_mp4(fname)

                # Calcula similaridade entre fname_norm e original_norm
                sim = SequenceMatcher(None, fname_norm, original_norm).ratio()
                print(f"similaridade?: {sim}")
                if sim >= threshold:
                    final_path = os.path.join(root, new_name)
                    os.rename(orig_path, final_path)
                    return final_path

        return None

    def rename_file_mp4(
        self, 
        canal_do_yt = "BisteconeLive",
        downloaded_filenames = "O QUE ESTÁ ACONTECENDO NESSA LANCHONETE À NOITE？ - BurgerPiz'",

        ):

        base_dir = os.path.abspath(
            os.path.join(self.diretorio_script, "WorkEnvironment", "Process", "MediaBase",  f'{canal_do_yt}')
        )

        nome_original = Path(base_dir) / f"{downloaded_filenames}.mp4"
        # remove_accents_nome = self.clear_file_name_to_search_correctly(nome_original.name) #remove_accents()
        # logger.info(f"remove_accents_nome: {remove_accents_nome}")

        novo_nome = self.clear_file_name_to_rename(nome_original.name)
        logger.info(f"novo_nome: {novo_nome}")
        nome_rename_final = nome_original.parent / novo_nome
        rename_final = nome_original.parent / novo_nome
        logger.info(f"nome_rename_final: {nome_rename_final}")

        try:
            self.safe_rename(nome_original, nome_rename_final)
        except Exception as fallback:
            logger.info(f"fallback: {fallback}")
            nome_rename_final = self.find_and_rename_mp4(base_dir, str(nome_original), novo_nome, threshold=0.8)
            if nome_rename_final == None:
                logger.info(f"?")
                nome_rename_final = self.find_and_rename_mp4(base_dir, str(nome_original), novo_nome, threshold=0.6)
                if nome_rename_final == None:
                    logger.info(f"??")
                    nome_rename_final = self.find_and_rename_mp4(base_dir, str(nome_original), novo_nome, threshold=0.4)
                    if nome_rename_final == None:
                        logger.info(f"???")
                        nome_rename_final = rename_final

        logger.info(f"Arquivo renomeado para: {nome_rename_final}")
        return nome_rename_final


    def remove_accents(self, input_str):
        # Normaliza a string para decompor caracteres acentuados
        nfkd_form = unicodedata.normalize('NFKD', input_str)
        # Remove os acentos (caracteres de combinação)
        return "".join([c for c in nfkd_form if not unicodedata.combining(c)])

    def load_downloaded_videos(self):
        """Carrega a lista de vídeos já baixados"""
        if os.path.exists(self.downloadted_file):
            with open(self.downloadted_file, 'r') as f:
                return set(json.load(f))
        return set()

    def save_downloaded_videos(self, video_ids):
        """Salva a lista de vídeos baixados"""
        with open(self.downloadted_file, 'w') as f:
            json.dump(list(video_ids), f)

    def convert_time_to_seconds(self,time_str):
        hours, minutes, seconds = map(int, time_str.split(':'))
        return hours * 3600 + minutes * 60 + seconds
    
    def create_download_directory(self, base_dir):
        """Cria um diretório para os downloads com base no nome do canal"""
        channel_dir = os.path.join(base_dir)
        if not os.path.exists(channel_dir):
            cprint(f"Shortify Algo V1 - Criando diretório: {channel_dir}")
            os.makedirs(channel_dir)
        return channel_dir

    def bytes_to_human_readable(self, size_in_bytes):
        """
        Converte bytes para um formato legível (KB, MB, GB, etc.)
        """
        if size_in_bytes < 1024:
            return f"{size_in_bytes} B"
        elif size_in_bytes < 1024 ** 2:
            return f"{size_in_bytes / 1024:.2f} KB"
        elif size_in_bytes < 1024 ** 3:
            return f"{size_in_bytes / (1024 ** 2):.2f} MB"
        else:
            return f"{size_in_bytes / (1024 ** 3):.2f} GB"
        

    def normalize_title(self, s: str) -> str:
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

    # def translate_to_pt(self, text):
    #     try:
    #         translated = self.translator.translate(text, dest='pt').text
    #         return translated
    #     except Exception as e:
    #         cprint(f"Erro ao traduzir texto: {e}", 'yellow')
    #         return text




            
    def get_video_title(self, video_id):
        url = f"https://www.youtube.com/watch?v={video_id}"
        ydl_opts = {
            'quiet': True,
            'skip_download': True  # Garante que o vídeo não será baixado
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return info.get("title", "Desconhecido")

    def get_video_thumbnail(self, video_id):
        url = f"https://www.youtube.com/watch?v={video_id}"
        ydl_opts = {
            'quiet': True,
            'skip_download': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return info.get("thumbnail", "Thumbnail não encontrada")

    def download_thumbnail(self, thumbnail_url, output_path):
        response = requests.get(thumbnail_url)
        if response.status_code == 200:
            with open(output_path, 'wb') as file:
                file.write(response.content)
            print(f"Thumbnail baixada com sucesso: {output_path}")
            return True
        else:
            print(f"Falha ao baixar a thumbnail. Status code: {response.status_code}")
            return False




    def get_cpu_name(self):
        """Obtém a nomenclatura do processador."""
        if platform.system() == "Windows":
            command = "wmic cpu get name"
            cpu_name = subprocess.check_output(command, shell=True).decode().strip().split('\n')[1]
        elif platform.system() == "Linux":
            command = "cat /proc/cpuinfo | grep 'model name' | uniq"
            cpu_name = subprocess.check_output(command, shell=True).decode().strip().split(': ')[1]
        elif platform.system() == "Darwin":
            command = "sysctl -n machdep.cpu.brand_string"
            cpu_name = subprocess.check_output(command, shell=True).decode().strip()
        else:
            cpu_name = "Sistema não suportado."
        
        return cpu_name
    
    def get_machine_info(self):
        system_info = platform.uname()
        machine = system_info.node
        return machine
    