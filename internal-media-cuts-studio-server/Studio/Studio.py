# Studio\Studio.py
########################################################################
## IMPORTAÇÃO DE BIBLIOTECAS
########################################################################
import os
import sys
import json
import time
import random
import re
import subprocess
import platform
import tempfile
from datetime import datetime, timedelta
from typing import Dict, Any
from collections import defaultdict
from queue import Queue, Empty
import threading
import requests
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
import logging
import base64
import os
import requests
import zipfile
import unicodedata
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "Keys", "env.env"))

PRODUCTION_ENV = os.getenv("PRODUCTION_ENV", "True")

if PRODUCTION_ENV == "True":
    # Production
    from Studio.AudioTranscriber import Audio_Transcriber
    from Studio.TiktokAutoUploader_TESTEE.tiktok_uploader import tiktok, Video


if PRODUCTION_ENV == "False":
    # Local Test
    from AudioTranscriber import Audio_Transcriber
    # from TiktokAutoUploader_TESTEE.tiktok_uploader import tiktok, Video


    # os.chdir(os.path.join(os.path.dirname(__file__)))        



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Studio_logger")


class MediaCutsStudio:
    """
    Processa e edita vídeos de canais do YouTube para criar cortes otimizados para o TikTok.

    Esta classe é responsável por todo o pipeline de pós-produção de vídeo,
    incluindo corte, aplicação de legendas dinâmicas, watermarks e outras
    configurações visuais, preparando o conteúdo para upload e agendamento
    em plataformas como o TikTok. Ela integra ferramentas como FFmpeg para
    manipulação de vídeo e webhooks para comunicação de status.

    ---
    Args:
        app1 (object, optional): Instância da aplicação, tipicamente para interação com um banco de dados (e.g., Firebase). Defaults to None.
        user_email (str, optional): Email do usuário, usado para identificar tarefas e logs. Será normalizado para um formato compatível com caminhos de arquivo. Defaults to None.
        yt_channel (str, optional): O identificador ou nome do canal do YouTube de onde o vídeo original foi obtido. Defaults to None.
        TiktokAccount (str, optional): O nome de usuário da conta do TikTok para a qual os cortes serão destinados. Defaults to None.
        TiktokAccountCookies (str, optional): Cookies de autenticação necessários para interagir com a API do TikTok. Defaults to None.
        video_path (str, optional): O caminho completo para o arquivo de vídeo original a ser processado. Defaults to None.
        current_date (str, optional): A data atual no formato 'YYYY-MM-DD', usada para log e agendamento. Defaults to None.
        date_time (str, optional): O horário atual no formato 'HH:MM:SS', usado para log e agendamento. Defaults to None.
        hash_task_list (list, optional): Uma lista de hashes de tarefas, usada para rastrear o progresso. Defaults to None.
        Cutting_seconds (int, optional): A duração desejada (em segundos) de cada corte de vídeo a ser gerado. Defaults to None.
        secondsScheduleTiktokVideo (int, optional): O atraso (em segundos) para agendar o upload do vídeo no TikTok após o processamento. Defaults to None.
        titleForTiktokCutsEnabled (bool, optional): Se True, permite definir um título personalizado para os cortes do TikTok. Defaults to None.
        titleForTiktokCuts (str, optional): O título personalizado a ser aplicado aos cortes do TikTok, se habilitado. Defaults to None.
        hashtagsForTiktokCutsEnabled (bool, optional): Se True, permite definir hashtags personalizadas para os cortes do TikTok. Defaults to None.
        hashtagsForTiktokCuts (str, optional): As hashtags personalizadas a serem aplicadas aos cortes do TikTok, se habilitado. Defaults to None.
        text_watermark (str, optional): Texto para ser usado como watermark no vídeo. Defaults to None.
        watermark_image (str, optional): Caminho para uma imagem de watermark a ser aplicada no vídeo. Defaults to None.
        api_key (str, optional): Chave de API para autenticação com serviços externos (ex: webhooks). Defaults to None.
        WEBHOOK_URL (str, optional): URL do webhook para envio de notificações gerais de status. Defaults to None.
        WEBHOOK_ZIP_URL (str, optional): URL do webhook para envio de arquivos ZIP ou notificações relacionadas a arquivos. Defaults to None.
        text_edit_download (str, optional): Um campo opcional para qualquer texto de edição ou instrução durante o download. Defaults to None.

        SubtitleColor (str, optional): Cor do texto das legendas geradas. Padrão é 'white'.
        SubtitleAnimation (str, optional): Tipo de animação aplicada às legendas. Padrão é 'Slow Fade-Out'.
        SubtitleFontName (str, optional): Nome da fonte a ser usada para as legendas. Padrão é 'Future'.
        SubtitleEffects (str, optional): Efeitos visuais adicionais para as legendas (e.g., 'Glow Effect'). Padrão é 'Glow Effect'.
        SubtitleFontsize (str, optional): Tamanho da fonte das legendas. Padrão é '30'.
        SubtitleVerticalReference (str, optional): Posição vertical das legendas (e.g., '+20' pixels do centro). Padrão é '+20'.

        CaptionsAlignment (str, optional): Alinhamento do texto das legendas automáticas. Padrão é "5" (provavelmente 'center' ou similar).
        CaptionsColor (str, optional): Cor principal do texto das legendas automáticas. Padrão é "aqua".
        CaptionsFontName (str, optional): Nome da fonte para as legendas automáticas. Padrão é "Future".
        CaptionsFontsize (int, optional): Tamanho da fonte das legendas automáticas. Padrão é 20.
        CaptionsPrimaryColour (str, optional): Cor primária (código hexadecimal) para elementos de destaque. Padrão é "&HC0C0C0".
        CaptionsSecondaryColour (str, optional): Cor secundária (código hexadecimal) para elementos de destaque. Padrão é "&H8080".
        CaptionsOutlineColour (str, optional): Cor do contorno (código hexadecimal) para as legendas automáticas. Padrão é "&H0" (preto).
        CaptionsBackColour (str, optional): Cor de fundo (código hexadecimal) para as legendas automáticas. Padrão é "&H0" (preto).
        CaptionsBold (int, optional): Define se o texto das legendas automáticas deve ser em negrito (1 para True, 0 para False). Padrão é 1.
        CaptionsItalic (int, optional): Define se o texto das legendas automáticas deve ser em itálico (1 para True, 0 para False). Padrão é 0.
        CaptionsUnderline (int, optional): Define se o texto das legendas automáticas deve ser sublinhado (1 para True, 0 para False). Padrão é 0.
        CaptionsOutline (int, optional): Espessura do contorno das legendas automáticas. Padrão é 3.
        CaptionsShadow (int, optional): Profundidade da sombra das legendas automáticas. Padrão é 1.
        CaptionsRevealEffectInitialColor (str, optional): Cor inicial (código hexadecimal) para efeitos de revelação de texto. Padrão é "&HCCCC33&".
        CaptionsRevealEffectFinalColor (str, optional): Cor final (código hexadecimal) para efeitos de revelação de texto. Padrão é "&H0099FF&".

        path_ffmpeg (str, optional): Caminho completo para o executável do FFmpeg. Defaults to None.
        path_ffprobe (str, optional): Caminho completo para o executável do FFprobe. Defaults to None.
        path_ffmpegnotexe (str, optional): Caminho para o diretório onde os executáveis do FFmpeg/FFprobe estão. Defaults to None.
        legendstheme (str, optional): Tema específico para a renderização de legendas. Padrão é "Revelation Effect".
        theme (str, optional): Tema geral para o processamento de vídeo. Padrão é "default".
        ad_marketing (bool, optional): Habilita ou desabilita funcionalidades de marketing/propaganda. Padrão é True.
        hwaccel (str, optional): Tipo de aceleração de hardware para FFmpeg (e.g., 'nvdec' para decodificação NVIDIA). Padrão é "nvdec".
        hwaccel_encode_device (str, optional): O ID do dispositivo de codificação de hardware. Padrão é "0".
        vcodec (str, optional): Codec de vídeo a ser usado para a codificação. Padrão é "h264_nvenc".
        vcodec_audio (str, optional): Codec de áudio a ser usado. Padrão é "copy" (copia o stream original).
        preset (str, optional): Preset de codificação do FFmpeg (controla velocidade vs. qualidade). Padrão é "medium".
        gpu_ (str, optional): O ID da GPU a ser utilizada para processamento. Padrão é "0".
        profile (str, optional): O perfil de codificação do vídeo (e.g., 'high', 'main'). Padrão é "high".
        bitrate (str, optional): Taxa de bits do vídeo de saída (e.g., "10M", "100M"). Padrão é "100M".
        maxrate (str, optional): Taxa de bits máxima para o vídeo de saída. Padrão é "100M".
        bufsize (str, optional): Tamanho do buffer para o codificador. Padrão é "400M".
        webhook (bool, optional): Se True, ativa o envio de notificações via webhook. Padrão é True.
        dockerffmpeg (bool, optional): Se True, indica que o FFmpeg está rodando em um ambiente Docker. Padrão é False.
        output_miniatura (str, optional): Caminho para a miniatura de saída gerada. Defaults to None.
    """
    def __init__(self,
                app1=None,
                user_email=None,
                yt_channel=None,
                TiktokAccount=None,
                TiktokAccountCookies=None,
                video_path=None,
                current_date=None,
                date_time=None,
                hash_task_list=None,
                Cutting_seconds=None,
                secondsScheduleTiktokVideo=None,
                titleForTiktokCutsEnabled=None,
                titleForTiktokCuts=None,
                hashtagsForTiktokCutsEnabled=None,
                hashtagsForTiktokCuts=None,
                text_watermark=None,
                watermark_image=None,
                api_key=None,
                WEBHOOK_URL=None,
                WEBHOOK_ZIP_URL=None,
                text_edit_download=None,
                SubtitleColor='white',
                SubtitleAnimation='Slow Fade-Out', 
                SubtitleFontName='Future',
                SubtitleEffects='Glow Effect',
                SubtitleFontsize='30',
                SubtitleVerticalReference='+20', 
                CaptionsAlignment = "5",
                CaptionsColor = "aqua",
                CaptionsFontName = "Future",
                CaptionsFontsize = 20,
                CaptionsPrimaryColour = "&HC0C0C0",
                CaptionsSecondaryColour = "&H8080",
                CaptionsOutlineColour = "&H0",
                CaptionsBackColour = "&H0",
                CaptionsBold = 1,
                CaptionsItalic = 0,
                CaptionsUnderline = 0,
                CaptionsOutline = 3,
                CaptionsShadow = 1,
                CaptionsRevealEffectInitialColor = "&HCCCC33&",
                CaptionsRevealEffectFinalColor = "&H0099FF&",
                path_ffmpeg=None,
                path_ffprobe=None,
                path_ffmpegnotexe=None,
                legendstheme="Revelation Effect",
                theme="default",
                hwaccel="nvdec",
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
                dockerffmpegGPU = True,
                dockerffmpegCPU = False,
                output_miniatura=None,
                ad_marketing=True,

                ):

        self.hashtagsForTiktokCutsEnabled = hashtagsForTiktokCutsEnabled
        self.hashtagsForTiktokCuts = hashtagsForTiktokCuts

        self.titleForTiktokCutsEnabled = titleForTiktokCutsEnabled
        self.titleForTiktokCuts = titleForTiktokCuts
        self.app1 = app1
        try:
            self.user_email = user_email.replace(".", "_")
        except:
            pass
        self.yt_channel = yt_channel
        self.TiktokAccount = TiktokAccount
        self.TiktokAccountCookies = TiktokAccountCookies
        self.api_key = api_key
        self.video_path = video_path
        self.video_path= rf"{self.video_path}"
        self.current_date = current_date
        self.date_time = date_time 

        self.hash_task_list = hash_task_list
        self.text_watermark = text_watermark
        self.watermark_image = watermark_image
        self.webhook = webhook
        self.dockerffmpegGPU = dockerffmpegGPU
        self.dockerffmpegCPU = dockerffmpegCPU

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
       
        self.path_ffmpeg = path_ffmpeg
        self.path_ffprobe = path_ffprobe
        self.path_ffmpegnotexe = path_ffmpegnotexe 
        self.legendstheme = legendstheme 
        self.theme = theme
        self.ad_marketing = ad_marketing


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

        self.output_miniatura = output_miniatura

        self.diretorio_script = os.path.dirname(os.path.abspath(__file__)) 
        self.init_cor_segundo_texto = os.path.join(self.diretorio_script, 'Utils', 'resources', 'subtitle_color', 'Subcolor.txt')
        self.init_alpha_for_animation = os.path.join(self.diretorio_script, 'Utils', 'resources', 'animations', 'animations.txt')
        self.init_effects = os.path.join(self.diretorio_script, 'Utils', 'resources', 'effects', 'effects.txt')
        self.init_color_for_caption = os.path.join(self.diretorio_script, 'Utils', 'resources', 'captions_color', 'colors.txt')

        # self.path_ffprobe = os.path.join(self.diretorio_script, 'Utils', "ffmpeg", 'ffprobe.exe')

        # self.path_ffmpeg = os.path.join(self.diretorio_script, 'Utils', "ffmpeg", 'ffmpeg.exe')

        # self.path_ffmpegnotexe = os.path.join(self.diretorio_script, 'Utils', 'ffmpeg')

        # os.environ['PATH'] = self.path_ffmpegnotexe + os.pathsep + os.environ['PATH']
                  
    def main(self):


        system_info = platform.uname()
        machine = system_info.node


        cprint("⏳ Studio - Initializing Counters", "yellow")
        if self.webhook == True:
            self.send_to_webhook(self.api_key, "info", "⏳ Studio - Initializing Counters", "yellow")
            self.send_to_webhook(self.api_key, "progress", 6, "yellow")

        start_time_seconds = 0
        contador_de_Cortes_criados = 0
        tempo_inicial = time.time()

        cprint("📏 Studio - Defining video dimensions", "blue")
        if self.webhook == True:
            self.send_to_webhook(self.api_key, "info", "📏 Studio - Defining video dimensions", "blue")
            self.send_to_webhook(self.api_key, "progress", 5, "yellow")

            
        largura_vertical = 1080
        altura_vertical = 1920


        if self.webhook == True:
            self.send_to_webhook(self.api_key, "Mode", f"Shortify - Date", "yellow")
            self.send_to_webhook(self.api_key, "cuts_duration", f"{self.Cutting_seconds}", "green")
            self.send_to_webhook(self.api_key, "Status", f"Running", "yellow")
            self.send_to_webhook(self.api_key, "TiktokAccount", f"{self.TiktokAccount}", "green")
            self.send_to_webhook(self.api_key, "YtChannel", f"{self.yt_channel}", "green")
                 
                 

        tempo_formatado, tempo_total_por_corte = self.get_total_current_time(tempo_inicial)
        if self.webhook == True:
            self.send_to_webhook(self.api_key, "timestamp", tempo_formatado, "green")

        print("""
        🔵 Blue for startup steps.
        🟢 Green for successes and confirmations.
        🟡 Yellow for ongoing processes.
        🔴 Red for possible failures (like flag == False).
        """)
        if self.webhook == True:
            self.send_to_webhook(self.api_key, "info", """
        🔵 Blue for startup steps.
        🟢 Green for successes and confirmations.
        🟡 Yellow for ongoing processes.
        🔴 Red for possible failures (like flag == False).
            """
            , "blue")
        VideoFile = os.path.basename(self.video_path)

        if self.webhook == True:
            if len(VideoFile) >= 25:
                self.send_to_webhook(self.api_key, "mediabase", f"{VideoFile[:25]}...", "yellow")
            else:
                self.send_to_webhook(self.api_key, "mediabase", f"{VideoFile}", "yellow")
            self.send_to_webhook(self.api_key, "progress", 1, "yellow")

        if not VideoFile:
            return {"error": "Nenhum vídeo enviado."}, 400

        tempo_formatado, tempo_total_por_corte = self.get_total_current_time(tempo_inicial)
        if self.webhook == True:
            self.send_to_webhook(self.api_key, "timestamp", tempo_formatado, "green")

        cprint("🚀 Studio - Initializing Media Cuts Studio", "blue")
        if self.webhook == True:
            self.send_to_webhook(self.api_key, "info", "🚀 Studio - Initializing Media Cuts Studio", "blue")
            self.send_to_webhook(self.api_key, "progress", 2, "yellow")

        tempo_formatado, tempo_total_por_corte = self.get_total_current_time(tempo_inicial)
        if self.webhook == True:
            self.send_to_webhook(self.api_key, "timestamp", tempo_formatado, "green")


        cprint("📜 Studio - Initializing Title Creation", "blue")
        if self.webhook == True:
            self.send_to_webhook(self.api_key, "info", "📜 Studio - Initializing Title Creation", "blue")
            self.send_to_webhook(self.api_key, "progress", 3, "yellow")

        tempo_formatado, tempo_total_por_corte = self.get_total_current_time(tempo_inicial)
        if self.webhook == True:
            self.send_to_webhook(self.api_key, "timestamp", tempo_formatado, "green")

        
        texto_sem_espacos = VideoFile.replace("?", "").replace(".mp4", "").replace(" ", "").replace("  ", "").replace("Ó", "O").replace("Ç", "C").replace("Í", "I").replace("É", "E").replace("ft.", "ft").replace("é", "e").replace("｜", "").replace(",", "").replace("...", "").replace("-", "").replace("Ã", "A").replace("Ô", "O").replace("Õ", "O").replace("!", "").replace("À", "A")
        
        if self.titleForTiktokCutsEnabled == True or self.titleForTiktokCutsEnabled == "true":
            texto_para_titulo = self.titleForTiktokCuts 
        elif self.titleForTiktokCutsEnabled == False or self.titleForTiktokCutsEnabled == "false":
            texto_para_titulo = VideoFile.replace(".mp4", "").replace("_", " ")

        cprint("📂 Studio - Creating folders in RealtimeCuts", "blue")
        if self.webhook == True:
            self.send_to_webhook(self.api_key, "info", "📂 Studio - Creating folders in RealtimeCuts", "blue")
            self.send_to_webhook(self.api_key, "progress", 4, "yellow")
            self.send_to_webhook(self.api_key, "notification", f"🚀 Studio - Initializing Create Cuts", "yellow")


        tempo_formatado, tempo_total_por_corte = self.get_total_current_time(tempo_inicial)
        if self.webhook == True:
            self.send_to_webhook(self.api_key, "timestamp", tempo_formatado, "green")


        path_create = os.path.abspath(os.path.join(self.diretorio_script, "WorkEnvironment", "Process", "Realtime_Cuts", 'Cuts', f'{texto_sem_espacos}'))
        path_create_2 = os.path.abspath(os.path.join(path_create, "CutsCreate"))
        VideosDirPath2 = os.path.abspath(os.path.join(path_create, "CutsDirPath"))
        output_video_converter = os.path.abspath(os.path.join(path_create, "CutsConverter"))
        output_folder = os.path.abspath(os.path.join(path_create, "CutsCreate"))
       

        os.makedirs(output_folder, exist_ok=True)
        os.makedirs(path_create, exist_ok=True)
        os.makedirs(path_create_2, exist_ok=True)
        os.makedirs(VideosDirPath2, exist_ok=True)
        os.makedirs(output_video_converter, exist_ok=True)

        tempo_formatado, tempo_total_por_corte = self.get_total_current_time(tempo_inicial)
        if self.webhook == True:
            self.send_to_webhook(self.api_key, "timestamp", tempo_formatado, "green")


        cprint("🔍 Studio - Checking number of possible cuts", "yellow")
        if self.webhook == True:
            self.send_to_webhook(self.api_key, "info", "🔍 Studio - Checking number of possible cuts", "yellow")
            self.send_to_webhook(self.api_key, "progress", 7, "yellow")
            
        tempo_formatado, tempo_total_por_corte = self.get_total_current_time(tempo_inicial)
        if self.webhook == True:
            self.send_to_webhook(self.api_key, "timestamp", tempo_formatado, "green")

        try:

            duracao_total = self.get_duration_video(video_path=self.video_path)
            num_videos = math.ceil(duracao_total / self.Cutting_seconds)

            cprint(f"🎞️ Studio - Number of possible cuts: {num_videos} - Video duration: {duracao_total}s", "yellow")
            if self.webhook == True:
                self.send_to_webhook(self.api_key, "info", f"🎞️ Studio - Number of possible cuts: {num_videos} - Video duration: {duracao_total}s", "yellow")
                self.send_to_webhook(self.api_key, "target", f"0/{num_videos}", "yellow")
                self.send_to_webhook(self.api_key, "progress", 8, "yellow")

        except Exception as e:
            print(f"e: {e}")

        tempo_formatado, tempo_total_por_corte = self.get_total_current_time(tempo_inicial)
        if self.webhook == True:
            self.send_to_webhook(self.api_key, "timestamp", tempo_formatado, "green")

        cprint("🔑 Studio - Inicialize loop for cuts", "yellow")
        if self.webhook == True:
            self.send_to_webhook(self.api_key, "info", "🔑 Studio - Inicialize loop for cuts", "yellow")
            self.send_to_webhook(self.api_key, "progress", 0, "yellow")

        for video in range(num_videos):
            tempo_formatado, tempo_total_por_corte = self.get_total_current_time(tempo_inicial)
            if self.webhook == True:
                self.send_to_webhook(self.api_key, "timestamp", tempo_formatado, "green")

            contador_de_Cortes_criados_para_o_Titulo = contador_de_Cortes_criados + 1

            if self.hashtagsForTiktokCutsEnabled == True or self.hashtagsForTiktokCutsEnabled == "true":
                texto_com_espacos = self.add_line_breaks(f"{texto_para_titulo} parte {contador_de_Cortes_criados_para_o_Titulo} {self.hashtagsForTiktokCuts}")

            elif self.hashtagsForTiktokCutsEnabled == False or self.hashtagsForTiktokCutsEnabled == "false":
                texto_com_espacos = self.add_line_breaks(f"{texto_para_titulo} parte {contador_de_Cortes_criados_para_o_Titulo}")

            cprint("🕒 Studio - Accounting for time", "yellow")
            if self.webhook == True:
                self.send_to_webhook(self.api_key, "info", "🕒 Studio - Accounting for time", "yellow")
                self.send_to_webhook(self.api_key, "progress", 10, "yellow")

            tempo_formatado, tempo_total_por_corte = self.get_total_current_time(tempo_inicial)
            if self.webhook == True:
                self.send_to_webhook(self.api_key, "timestamp", tempo_formatado, "green")

            cprint(f"🎬 Studio - Creating cut number {contador_de_Cortes_criados + 1}", "yellow")
            if self.webhook == True:
                self.send_to_webhook(self.api_key, "info", f"🎬 Studio - Creating cut number {contador_de_Cortes_criados + 1}", "yellow")
                self.send_to_webhook(self.api_key, "target", f"{contador_de_Cortes_criados + 1}/{num_videos}", "yellow")
                self.send_to_webhook(self.api_key, "progress", 20, "yellow")

            tempo_formatado, tempo_total_por_corte = self.get_total_current_time(tempo_inicial)
            if self.webhook == True:
                self.send_to_webhook(self.api_key, "timestamp", tempo_formatado, "green")


            cprint("📝 Studio - Creating names for cuts", "yellow")
            if self.webhook == True:
                self.send_to_webhook(self.api_key, "info", "📝 Studio - Creating names for cuts", "yellow")
                self.send_to_webhook(self.api_key, "progress", 30, "yellow")

            audio_output = os.path.join(output_folder, f"audio_video_vertical_{contador_de_Cortes_criados + 1}.wav")

            audio_srt = os.path.join(output_folder, f"audio_video_vertical_{contador_de_Cortes_criados + 1}.srt")
            audio_ass = f"/app/Studio/WorkEnvironment/Process/Realtime_Cuts/Cuts/{texto_sem_espacos}/CutsCreate/audio_video_vertical_{contador_de_Cortes_criados + 1}.ass"
            output_processar_video = os.path.join(output_folder, f"video_vertical_{contador_de_Cortes_criados + 1}.mp4")
            output_video_subtittle = os.path.join(output_folder, f"video_vertical_{contador_de_Cortes_criados + 1}_subtitle.mp4")
            output_video_subtittle_watermask = os.path.join(output_folder, f"video_vertical_{contador_de_Cortes_criados + 1}_subtitle_and_watermask.mp4")
            output_video_subtittle_ad = os.path.join(output_folder, f"video_vertical_{contador_de_Cortes_criados + 1}_subtitle_ad.mp4")
            output_video_convert = os.path.abspath(os.path.join(self.diretorio_script, "WorkEnvironment", "Process", "Realtime_Cuts", 'Cuts', f'{texto_sem_espacos}' ,  f"video_vertical_{contador_de_Cortes_criados + 1}_subtitles.mp4"))
            output_filename = os.path.join(output_folder, f"subclip_vertical_{contador_de_Cortes_criados + 1}.mp4")

            cprint("📝 Studio - Get start time", "yellow")
            if self.webhook == True:
                self.send_to_webhook(self.api_key, "info", "📝 Studio - Creating names for cuts", "yellow")
                self.send_to_webhook(self.api_key, "progress", 30, "yellow")

            start_time = self.seconds_to_hhmmss(segundos=start_time_seconds)

            cprint("✂️ Studio - Creating Subclip", "yellow")
            if self.webhook == True:
                self.send_to_webhook(self.api_key, "info", "✂️ Studio - Creating Subclip", "yellow")
                self.send_to_webhook(self.api_key, "progress", 35, "yellow")

            tempo_formatado, tempo_total_por_corte = self.get_total_current_time(tempo_inicial)
            if self.webhook == True:
                self.send_to_webhook(self.api_key, "timestamp", tempo_formatado, "green")

            subclip_filename = self.generate_subclip_with_ffmpeg(video_input=self.video_path,
                                                                start_time=start_time,
                                                                duration=self.Cutting_seconds,
                                                                output_filename=output_filename
                                                                )

            tempo_formatado, tempo_total_por_corte = self.get_total_current_time(tempo_inicial)
            if self.webhook == True:
                self.send_to_webhook(self.api_key, "timestamp", tempo_formatado, "green")

            if self.theme == "default":

                cprint("\n📐 Studio - Creating Vertical Section", "yellow")
                if self.webhook == True:
                    self.send_to_webhook(self.api_key, "info", "\n📐 Studio - Creating Vertical Section", "yellow")
                    self.send_to_webhook(self.api_key, "progress", 40, "yellow")

                self.process_video_with_ffmpeg(
                    video_input=subclip_filename,
                    largura_vertical=largura_vertical,
                    altura_vertical=altura_vertical,
                    output_filename=output_processar_video,
    
                )

            elif self.theme == "Vertical Fusion":
                output_processar_video = subclip_filename

            else:
                output_processar_video = subclip_filename

            transcriber = Audio_Transcriber(
                                            api_key=self.api_key,
                                            WEBHOOK_URL=self.WEBHOOK_URL,
                                            model_type="medium", 
                                            webhook=self.webhook
                                        )
            for i in range(5):
                try:
                    audio_2 = f"/app/Studio/WorkEnvironment/Process/Realtime_Cuts/Cuts/{texto_sem_espacos}/CutsCreate/audio_video_vertical_{contador_de_Cortes_criados + 1}.wav"
                    logger.info(f"audio_2 {audio_2}")
                    cprint("\n🎵 Studio - Extracting Audio", "yellow")
                    if self.webhook == True:
                        self.send_to_webhook(self.api_key, "info", "\n🎵 Studio - Extracting Audio", "yellow")
                        self.send_to_webhook(self.api_key, "progress", 45, "yellow")

                    tempo_formatado, tempo_total_por_corte = self.get_total_current_time(tempo_inicial)
                    if self.webhook == True:
                        self.send_to_webhook(self.api_key, "timestamp", tempo_formatado, "green")

                    transcriber.extract_audio_with_ffmpeg(video_input=output_processar_video,
                                                                    audio_output=audio_2)

                    cprint("\n🗣️ Studio - Transcribing Audio", "yellow")
                    if self.webhook == True:
                        self.send_to_webhook(self.api_key, "info", "\n🗣️ Studio - Transcribing Audio", "yellow")
                        self.send_to_webhook(self.api_key, "progress", 55, "yellow")

                    tempo_formatado, tempo_total_por_corte = self.get_total_current_time(tempo_inicial)
                    if self.webhook == True:
                        self.send_to_webhook(self.api_key, "timestamp", tempo_formatado, "green")


                    resultado, total_time_str = transcriber.transcrever_audio(
                        arquivo_audio=audio_2, 
                        audio_sliced_path=path_create_2,
                        vertical_id="hash_do_dia"
                    )
                    break
                except Exception as err:
                    audio_2 = audio_output
                    continue



            cprint("\n📜 Studio - Converting Subtitles", "yellow")
            if self.webhook == True:
                self.send_to_webhook(self.api_key, "info", "\n📜 Studio - Converting Subtitles", "yellow")
                self.send_to_webhook(self.api_key, "progress", 65, "yellow")

            tempo_formatado, tempo_total_por_corte = self.get_total_current_time(tempo_inicial)
            if self.webhook == True:
                self.send_to_webhook(self.api_key, "timestamp", tempo_formatado, "green")

            self.adpte_srt_file(audio_srt)
            
            flag = transcriber.convert_to_ass(self.path_ffmpeg, audio_srt, audio_ass)
            cprint(flag, "green" if flag else "red")

            novo_estilo = {
                'Fontname': self.CaptionsFontName,
                'Fontsize': self.CaptionsFontsize,
                'PrimaryColour': self.CaptionsPrimaryColour, 
                'SecondaryColour': self.CaptionsSecondaryColour, 
                'OutlineColour': self.CaptionsOutlineColour,  
                'BackColour': self.CaptionsBackColour, 
                'Bold': self.CaptionsBold, 
                'Italic': self.CaptionsItalic, 
                'Underline': self.CaptionsUnderline, 
                'Outline': self.CaptionsOutline,  
                'Shadow': self.CaptionsShadow, 
                'Alignment': self.CaptionsAlignment  
            }

            cprint("\n💾 Studio - Saving new subtitles", "yellow")
            if self.webhook == True:
                self.send_to_webhook(self.api_key, "info", "\n💾 Studio - Saving new subtitles", "yellow")
                self.send_to_webhook(self.api_key, "progress", 75, "yellow")

            tempo_formatado, tempo_total_por_corte = self.get_total_current_time(tempo_inicial)
            if self.webhook == True:
                self.send_to_webhook(self.api_key, "timestamp", tempo_formatado, "green")

            transcriber.modify_ass_styles(audio_ass, novo_estilo)

            cprint("\n✨ Studio - Applying reveal effect", "yellow")
            if self.webhook == True:
                self.send_to_webhook(self.api_key, "info", "\n✨ Studio - Applying reveal effect", "yellow")
                self.send_to_webhook(self.api_key, "progress", 79, "yellow")

            tempo_formatado, tempo_total_por_corte = self.get_total_current_time(tempo_inicial)
            if self.webhook == True:
                self.send_to_webhook(self.api_key, "timestamp", tempo_formatado, "green")

            if self.legendstheme == "Revelation Effect":
                
                self.apply_reveal_effect(
                    ass_file_path=audio_ass,
                    initial_color=self.CaptionsRevealEffectInitialColor,
                    final_color=self.CaptionsRevealEffectFinalColor
                )

            elif self.legendstheme == "Typewriter Effect":
                self.apply_typewriter_effect_fixed(
                    audio_ass, 
                    char_reveal_time=37
                    )



            cprint("\n🎥 Studio - Grouping Subtitles in Video", "yellow")
            if self.webhook == True:
                self.send_to_webhook(self.api_key, "info", "\n🎥 Studio - Grouping Subtitles in Video", "yellow")
                self.send_to_webhook(self.api_key, "progress", 80, "yellow")

            tempo_formatado, tempo_total_por_corte = self.get_total_current_time(tempo_inicial)
            if self.webhook == True:
                self.send_to_webhook(self.api_key, "timestamp", tempo_formatado, "green")

            if self.theme == "default":

                flag = self.theme_default(
                    nome_do_video=output_processar_video,
                    name_srt=audio_ass,
                    output_video_name=output_video_subtittle,
                    basenamefolder_arg=texto_com_espacos
                )

            elif self.theme == "Vertical Fusion":

                self.theme_VerticalFusion(
                    video_cima=output_processar_video,
                    imagem_baixo=self.output_miniatura,
                    fonte=self.SubtitleFontName,
                    texto_drawtext=texto_com_espacos,
                    ass_file=audio_ass,
                    saida=output_video_subtittle
                )


            cprint("\n✅ Caption applied successfully!", "green")
            if self.webhook == True:
                self.send_to_webhook(self.api_key, "info", "\n✅ Caption applied successfully!", "green")
                self.send_to_webhook(self.api_key, "progress", 83, "yellow")

            tempo_formatado, tempo_total_por_corte = self.get_total_current_time(tempo_inicial)
            if self.webhook == True:
                self.send_to_webhook(self.api_key, "timestamp", tempo_formatado, "green")


            # cprint("\n💦 Adding Watermark", "yellow")
            # if self.webhook == True:
            #     self.send_to_webhook(self.api_key, "info", "\n💦 Adding Watermark", "yellow")
            #     self.send_to_webhook(self.api_key, "progress", 85, "yellow")

            # self.add_watermark(output_video_subtittle, output_video_subtittle_watermask, self.text_watermark, self.watermark_image)

            # AD Markteting
            # if self.user_email == "freitasalexandre810gmailcom":
            #     print("is adm")
            #     if self.ad_marketing == True:
            #         print("ad marketing ")
            #         ad_video = os.path.join(os.path.dirname(__file__), "Ad_Marketing", "ad_1_resized.mp4")
            #         self.add_ad_marketing(output_video_subtittle, ad_video, output_video_subtittle_ad)
            #     else:
            #         output_video_subtittle_ad = output_video_subtittle
            # else:
            #     output_video_subtittle_ad = output_video_subtittle


            output_video_subtittle_ad = output_video_subtittle

            cprint("\n🔄 Converting video to MP4", "yellow")
            if self.webhook == True:
                self.send_to_webhook(self.api_key, "info", "\n🔄 Converting video to MP4", "yellow")
                self.send_to_webhook(self.api_key, "progress", 89, "yellow")

            tempo_formatado, tempo_total_por_corte = self.get_total_current_time(tempo_inicial)
            if self.webhook == True:
                self.send_to_webhook(self.api_key, "timestamp", tempo_formatado, "green")


            flag = self.convert_to_mp4_codec_with_ffmpeg(input_video=output_video_subtittle_ad,
                                                                        output_video_mkv=output_video_convert)

            cprint("\n🎉 Conversion Complete!", "green")
            if self.webhook == True:
                self.send_to_webhook(self.api_key, "info", "\n🎉 Conversion Complete!", "green")
                self.send_to_webhook(self.api_key, "progress", 90, "yellow")

            tempo_formatado, tempo_total_por_corte = self.get_total_current_time(tempo_inicial)
            if self.webhook == True:
                self.send_to_webhook(self.api_key, "timestamp", tempo_formatado, "green")

            tempo_final = time.time()
            minutos, segundos = divmod(int(tempo_final - tempo_inicial), 60)
            cprint(f"\n ⏳ Time taken to create vertical video: {minutos}m {segundos}", "yellow")
            if self.webhook == True:
                self.send_to_webhook(self.api_key, "info", f"\n ⏳ Time taken to create vertical video: {minutos}m {segundos}", "green")
                self.send_to_webhook(self.api_key, "progress", 95, "yellow")

            tempo_formatado, tempo_total_por_corte = self.get_total_current_time(tempo_inicial)
            if self.webhook == True:
                self.send_to_webhook(self.api_key, "timestamp", tempo_formatado, "green")

            for i in range(10):
                try: 
                    tempo_formatado, tempo_total_por_corte = self.get_total_current_time(tempo_inicial)
                    if self.webhook == True:
                        self.send_to_webhook(self.api_key, "timestamp", tempo_formatado, "green")

                    # os.chdir(os.path.join(os.path.dirname(__file__), "TiktokAutoUploader_TESTEE"))        
                    logger.info(f"secondsScheduleTiktokVideo? {self.secondsScheduleTiktokVideo}")
                    schedule_time_tiktok = int(self.secondsScheduleTiktokVideo)
                    logger.info(f"schedule_time_tiktok? {schedule_time_tiktok}")
                    flag = tiktok.upload_video(WEBHOOK_URL=self.WEBHOOK_URL, 
                                        api_key=self.api_key, 
                                        session_user_cookie=self.TiktokAccountCookies, 
                                        video=output_video_convert, 
                                        title=texto_com_espacos, 
                                        schedule_time=schedule_time_tiktok, 
                                        webhook=True
                                    )
                    if flag == True:
                        tempo_formatado, tempo_total_por_corte = self.get_total_current_time(tempo_inicial)
                        if self.webhook == True:
                            self.send_to_webhook(self.api_key, "timestamp", tempo_formatado, "green")
                        break

                    tempo_formatado, tempo_total_por_corte = self.get_total_current_time(tempo_inicial)
                    if self.webhook == True:
                        self.send_to_webhook(self.api_key, "timestamp", tempo_formatado, "green")

                    # time.sleep(3)  

                except Exception as errupload1:
                    logger.info(f"errupload1 {errupload1}")



            # try:
            #     shutil.rmtree(os.path.join(os.path.dirname(__file__), "TiktokAutoUploader_TESTEE", "VideosDirPath"))
            # except Exception as er1:
            #     logger.info(er1)

            # os.makedirs(os.path.join(os.path.dirname(__file__), "TiktokAutoUploader_TESTEE", "VideosDirPath"), exist_ok=True)
            

            # tempo_final_upload = time.time()
            #tempo_gasto_upload = tempo_final_upload - tempo_inicial_upload

            tempo_formatado, tempo_total_por_corte = self.get_total_current_time(tempo_inicial)
 
            logger.info(f"Total time for cutting {contador_de_Cortes_criados + 1}: {tempo_formatado}")
            if self.webhook == True:
                self.send_to_webhook(self.api_key, "info", f"Total time for cutting {contador_de_Cortes_criados + 1}: {tempo_formatado}", "green")
                self.send_to_webhook(self.api_key, "progress", 100, "yellow")
                self.send_to_webhook(self.api_key, "timestamp", tempo_formatado, "green")

                
            # Previsão do tempo total com base no tempo por corte
            tempo_estimado_total = tempo_total_por_corte * num_videos
            horas_estimadas = int(tempo_estimado_total // 3600)
            minutos_estimados = int((tempo_estimado_total % 3600) // 60)
            segundos_estimados = int(tempo_estimado_total % 60)

            if horas_estimadas > 0:
                logger.info( 
                    f"Weather Forecast: {str(horas_estimadas).zfill(2)}h {str(minutos_estimados).zfill(2)}m {str(segundos_estimados).zfill(2)}s"
                )
                if self.webhook == True:
                    self.send_to_webhook(self.api_key, "weather_forecast", f"{str(horas_estimadas).zfill(2)}h {str(minutos_estimados).zfill(2)}m {str(segundos_estimados).zfill(2)}s", "green")
                    self.send_to_webhook(self.api_key, "progress", 100, "yellow")
                
            else:
                logger.info(
                    f"Weather Forecast: 0h {str(minutos_estimados).zfill(2)}m {str(segundos_estimados).zfill(2)}s"
                )
                if self.webhook == True:
                    self.send_to_webhook(self.api_key, "weather_forecast", f"0h {str(minutos_estimados).zfill(2)}m {str(segundos_estimados).zfill(2)}s", "green")
                    self.send_to_webhook(self.api_key, "progress", 100, "yellow")
            
            start_time_seconds += self.Cutting_seconds
            contador_de_Cortes_criados += 1


        time.sleep(5)  

        diretorio_cutscreate = os.path.abspath(
            os.path.join(self.diretorio_script, "WorkEnvironment", "Process", "Realtime_Cuts", "Cuts", f'{texto_sem_espacos}', 'CutsCreate')
        )
        self.remover_todos_arquivos(diretorio_cutscreate)
        self.remover_todos_arquivos(diretorio_cutscreate)
        diretorio_cutscreate = os.path.abspath(
            os.path.join(self.diretorio_script, "WorkEnvironment", "Process", "Realtime_Cuts", "Cuts", f'{texto_sem_espacos}', 'CutsDirPath')
        )
        self.remover_todos_arquivos(diretorio_cutscreate)
        self.remover_todos_arquivos(diretorio_cutscreate)

        # diretorio_cutscreate = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "WorkEnvironment", 'Process', 'Realtime_Cuts', 'Cuts', f'{texto_sem_espacos}', 'CutsCreate'))#os.path.join(diretorio_script,  'src_', 'CoreApp', 'Process', 'Realtime_Cuts', 'Cuts', f'{texto_sem_espacos}', 'CutsCreate')
        # MediaCutsStudio_class.remover_todos_arquivos(diretorio_cutscreate)
        # MediaCutsStudio_class.remover_todos_arquivos(diretorio_cutscreate)
        # diretorio_cutscreate = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "WorkEnvironment", 'Process', 'Realtime_Cuts', 'Cuts', f'{texto_sem_espacos}', 'CutsDirPath')) #os.path.join(diretorio_script,  'src_', 'CoreApp', 'Process', 'Realtime_Cuts',  'Cuts', f'{texto_sem_espacos}', 'CutsDirPath')
        # MediaCutsStudio_class.remover_todos_arquivos(diretorio_cutscreate)
        try:
            os.remove(self.video_path)
        except:
            shutil.rmtree(self.video_path)
            
        # #remover_todos_arquivos(VideoFile)
        
        # diretorio_cutscreate = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "WorkEnvironment", 'Process', 'Realtime_Cuts', 'Cuts', f'{texto_sem_espacos}', 'CutsDirPath')) #os.path.join(diretorio_script, 'src_', 'CoreApp', 'Process', 'Realtime_Cuts',  'Cuts', f'{texto_sem_espacos}',  'CutsDirPath')
        # MediaCutsStudio_class.remover_todos_arquivos(diretorio_cutscreate)
        flag = self.close_ffmpeg_win64()
        logger.info(F"{flag} ")
        #return os.path.join(diretorio_script, 'src_', 'CoreApp', 'Process', 'Realtime_Cuts', 'Cuts', f'{texto_sem_espacos}')
                

        # # Caminho da pasta contendo os vídeos
        # video_folder = os.path.abspath(
        #     os.path.join(self.diretorio_script,
        #                 "WorkEnvironment",
        #                 "Process",
        #                 "Realtime_Cuts",
        #                 "Cuts",
        #                 f'{texto_sem_espacos}'
        #                 )
        #     )
        
        # zip_filename = os.path.abspath(
        #     os.path.join(self.diretorio_script,
        #                 "WorkEnvironment",
        #                 "Process",
        #                 "Realtime_Cuts",
        #                 "Cuts",
        #                 f'{texto_sem_espacos}.zip'
        #                 )
        #     )

        # # Cria um buffer de memória para o ZIP
        # zip_buffer = io.BytesIO()

        # # Compacta os arquivos no buffer
        # with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
        #     for video_file in os.listdir(video_folder):
        #         video_path = os.path.join(video_folder, video_file)
        #         if os.path.isfile(video_path) and video_file.endswith(".mp4"):
        #             zipf.write(video_path, arcname=video_file)  # Adiciona ao ZIP

        # # Move o ponteiro para o início do buffer
        # zip_buffer.seek(0)

        # # Codifica o ZIP em Base64
        # zip_encoded = base64.b64encode(zip_buffer.getvalue()).decode("utf-8")

        # # Monta o payload JSON
        # payload = {
        #     "arquivo_zip": zip_encoded,
        #     "api_key": self.api_key,
        #     "filename": zip_filename
        # }

        # # Envia a requisição POST com o JSON
        # response = requests.post(self.WEBHOOK_ZIP_URL, json=payload)

        # # Exibe a resposta do servidor
        # print("Status Code:", response.status_code)
        # print("Response:", response.json())



        try:
            ref_tasks = db.reference(f'user_tasks/{self.user_email}', app=self.app1)
            tasks = ref_tasks.get()  
            if tasks:
                for task_id, task_data in tasks.items():
                    scheduled_time = task_data.get("scheduled_time")
                    cprint(scheduled_time)
                    if str(scheduled_time) == str(self.current_date):
                        ref_tasks.child(task_id).update({"status": "Completed"})
                        if self.webhook == True:
                            self.send_to_webhook(self.api_key, "status", f"Completed", "yellow")

                        # ref_tasks.child(task_id).update({"download_path": zip_filename})
        except Exception as erro_:
            cprint(f"erro_{erro_}")

        cprint(f"All Cuts created for {os.path.basename(self.video_path)}")
        if self.webhook == True:

            self.send_to_webhook(self.api_key, "notification", f"🚀 All Cuts created for {os.path.basename(self.video_path)}", "yellow")

            self.send_to_webhook(self.api_key, "info", f"All Cuts created for {os.path.basename(self.video_path)}", "green")
            self.send_to_webhook(self.api_key, "progress", 100, "yellow")

        tempo_formatado, tempo_total_por_corte = self.get_total_current_time(tempo_inicial)
        if self.webhook == True:
            self.send_to_webhook(self.api_key, "timestamp", tempo_formatado, "green")

    def modify_ass_styles(self, ass_file_path, new_style):
        """
        Modifies the default subtitle style in an ASS (Advanced SubStation Alpha) file.

        This function updates the `[V4+ Styles]` section of the ASS file, specifically modifying the default style 
        with the properties provided in the `new_style` dictionary.

        Args:
            ass_file_path (str): Path to the ASS file to modify.
            new_style (dict): A dictionary containing the new style properties to apply.

        Returns:
            None

        Raises:
            Exception: If an error occurs while reading, modifying, or saving the ASS file.
        """
        try:
            # Read the content of the .ass file
            with open(ass_file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            # Control variables
            inside_styles = False
            new_lines = []
            for line in lines:
                line = line.strip()

                # Detect the start of the styles section
                if line.startswith('[V4+ Styles]'):
                    inside_styles = True
                    new_lines.append(line)
                    continue

                # Detect the end of the styles section
                if inside_styles and line.startswith('[Events]'):
                    inside_styles = False
                    new_lines.append(line)
                    continue

                # Modify the default style if found
                if inside_styles and line.startswith('Style: Default'):
                    # Split the components of the default style
                    style_values = line.split(',')

                    # Map new values to the correct positions
                    for key, value in new_style.items():
                        if key == 'Fontname':
                            style_values[1] = value
                        elif key == 'Fontsize':
                            style_values[2] = str(value)
                        elif key == 'PrimaryColour':
                            style_values[3] = value
                        elif key == 'SecondaryColour':
                            style_values[4] = value
                        elif key == 'OutlineColour':
                            style_values[5] = value
                        elif key == 'BackColour':
                            style_values[6] = value
                        elif key == 'Bold':
                            style_values[7] = str(value)
                        elif key == 'Italic':
                            style_values[8] = str(value)
                        elif key == 'Underline':
                            style_values[9] = str(value)
                        elif key == 'StrikeOut':
                            style_values[10] = str(value)
                        elif key == 'ScaleX':
                            style_values[11] = str(value)
                        elif key == 'ScaleY':
                            style_values[12] = str(value)
                        elif key == 'Spacing':
                            style_values[13] = str(value)
                        elif key == 'Angle':
                            style_values[14] = str(value)
                        elif key == 'BorderStyle':
                            style_values[15] = str(value)
                        elif key == 'Outline':
                            style_values[16] = str(value)
                        elif key == 'Shadow':
                            style_values[17] = str(value)
                        elif key == 'Alignment':
                            style_values[18] = str(value)
                        elif key == 'MarginL':
                            style_values[19] = str(value)
                        elif key == 'MarginR':
                            style_values[20] = str(value)
                        elif key == 'MarginV':
                            style_values[21] = str(value)
                        elif key == 'Encoding':
                            style_values[22] = str(value)

                    # Recreate the style line with the modified values
                    new_lines.append(','.join(style_values))
                else:
                    new_lines.append(line)

            # Save the modified content back to the .ass file
            with open(ass_file_path, 'w', encoding='utf-8') as file:
                file.writelines("\n".join(new_lines))

            print(f"Styles in the file {ass_file_path} were successfully modified!")

        except Exception as e:
            print(f"An error occurred while modifying the ASS file: {e}")

        # def write_captions(self, segments, filename):
        #     captions = []  # Lista de objetos Subtitle

        #     # Cabeçalho do arquivo .ass (Script Info)
        #     script_info_header = """
        #     [Script Info]
        #     Title: Example Subtitle File
        #     Original Script: Generated
        #     ScriptType: v4.00
        #     Collisions: Normal
        #     PlayDepth: 0
        #     """
            
        #     # Cabeçalho de estilo (V4+ Styles)
        #     styles_header = """
        #     [V4+ Styles]
        #     Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, BackColour, Bold, Italic, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
        #     Style: Default,Arial,24,&HFFFFFF,&H0000FF,&H000000,-1,0,1,1.0,0,2,10,10,10,1
        #     """
            
        #     # Adicionando o cabeçalho de script e estilos
        #     captions.append(script_info_header)
        #     captions.append(styles_header)
            
        #     # Adicionando as legendas
        #     for segment in segments['segments']:
        #         start = timedelta(seconds=segment['start'])
        #         end = timedelta(seconds=segment['end'])
        #         text = segment['text']

        #         # Convertendo os tempos para o formato ASS
        #         start_time = str(start).split('.')[0]  # Remover milissegundos
        #         end_time = str(end).split('.')[0]  # Remover milissegundos

        #         # Formatando a legenda no padrão ASS
        #         ass_subtitle = f"Dialogue: 0,{start_time},{end_time},Default,,0,0,0,,{text}"

        #         # Adicionando a legenda ao arquivo
        #         captions.append(ass_subtitle)

        #     # Salvando o conteúdo no arquivo .ass
        #     ass_file = f"{filename}.ass"
        #     with open(ass_file, "w", encoding="UTF-8") as file:
        #         file.writelines(captions)

        #     return ass_file

        def _format_timestamp(self, seconds):
            """Converte um timestamp em segundos para o formato SRT (hh:mm:ss,ms)."""
            hours = int(seconds // 3600)
            minutes = int((seconds % 3600) // 60)
            seconds = int(seconds % 60)
            milliseconds = int((seconds - int(seconds)) * 1000)
            return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"


    def timestamp_to_seconds(self, ts: str) -> int:
        h, m, s = map(int, ts.split(":"))
        return h*3600 + m*60 + s

    def normalize_find_mp4(self, name: str) -> str:
        # Remove acentos
        nfkd = unicodedata.normalize('NFKD', name)
        only_ascii = nfkd.encode('ASCII', 'ignore').decode('ASCII')
        # Remove pontuação e unifica espaços/underscores
        cleaned = re.sub(r'[\W]+', '_', only_ascii)
        return cleaned.strip('_').replace("?", "").replace(".mp4", "").replace(" ", "").replace("  ", "").replace("Ó", "O").replace("Ç", "C").replace("Í", "I").replace("É", "E").replace("ft.", "ft").replace("é", "e").replace("｜", "").replace(",", "").replace("...", "").replace("-", "").replace("Ã", "A").replace("Ô", "O").replace("Õ", "O").replace("!", "").replace("À", "A")
    
    def formatar_hashtags(self, hashtags_list: list[str], formato: str = "hash") -> str:
        """
        Recebe uma lista de hashtags e retorna formatado de acordo com o formato escolhido.

        formatos disponíveis:
        - "hash" : "#python #chatgpt #ia"
        - "virgula" : "python, chatgpt, ia"
        """
        # Limpa espaços e remove possíveis '#' existentes
        tags_limpas = [tag.strip().lstrip("#") for tag in hashtags_list if tag.strip()]

        if formato == "virgula":
            return ", ".join(tags_limpas)
        else:  # padrão é "hash"
            return " ".join(f"#{tag}" for tag in tags_limpas)


    def formatar_hashtags_legacy(self, hashtags_str: str) -> str:
        """
        Recebe uma string de hashtags separadas por vírgula (ex: "python,chatgpt,ia")
        e retorna uma lista de hashtags no formato "#python", "#chatgpt", "#ia".
        """
        # 1) Separa pelos ','  
        partes = hashtags_str.split(',')
        # 2) Para cada parte: remove espaços e eventuais '#' duplicados, e acrescenta o '#'
        resultado = ['#' + parte.strip().lstrip('#') for parte in partes if parte.strip()]
        return ' '.join(resultado)

    def get_total_current_time(self, tempo_inicial):
        tempo_final = time.time()
        tempo_gasto = tempo_final - tempo_inicial
        
        tempo_total_por_corte = tempo_gasto
        horas_corte = int(tempo_total_por_corte // 3600)
        minutos_corte = int((tempo_total_por_corte % 3600) // 60)
        segundos_corte = int(tempo_total_por_corte % 60)
        tempo_formatado = f"{horas_corte:02d}:{minutos_corte:02d}:{segundos_corte:02d}"
        return tempo_formatado, tempo_total_por_corte

    def fetch_hash_current_day(self):
        agora = datetime.now()
        indice_encontrado = None

        # Se date_time for uma lista, percorremos cada elemento
        if isinstance(self.date_time, list):
            for i, dt in enumerate(self.date_time):
                # Se o elemento não for um objeto datetime, tenta convertê-lo (supondo formato ISO)
                if not isinstance(dt, datetime):
                    try:
                        dt = datetime.fromisoformat(dt)
                    except Exception as e:
                        print(f"Erro ao converter '{dt}': {e}")
                        continue  # Pula esse elemento se não conseguir converter
                # Verifica se a data é igual ou alguns segundos depois de 'agora'
                if dt >= agora:
                    indice_encontrado = i
                    break
        else:
            # Se não for lista (ex.: string), tenta converter para datetime
            try:
                dt = datetime.fromisoformat(self.date_time)
            except Exception as e:
                print(f"Erro ao converter '{self.date_time}': {e}")
                dt = None
            if dt and dt >= agora:
                indice_encontrado = 0  # Se for apenas um valor, o índice é 0

        # Se encontramos um índice válido e ele está dentro do tamanho da lista hash_task_list,
        # retornamos o hash correspondente.
        if indice_encontrado is not None and indice_encontrado < len(self.hash_task_list):
            return self.hash_task_list[indice_encontrado]
        return None
    
    def generate_drawtext_commands(self, text, x_position, y_position, line_spacing, fontsize, fontcolor, font, animation="", effects=""):
        """
        Gera múltiplos comandos `drawtext` para exibir texto em várias linhas.

        Args:
            text (str): Texto com múltiplas linhas separadas por `\n`.
            x_position (str): Posição X para centralização.
            y_position (int): Posição Y inicial.
            line_spacing (int): Espaçamento entre as linhas.
            fontsize (int): Tamanho da fonte.
            fontcolor (str): Cor da fonte.
            font (str): Nome da fonte.
            animation (str): Animação do texto.
            effects (str): Efeitos adicionais.

        Returns:
            str: Comandos `drawtext` concatenados.
        """
        lines = text.split("\n")  # Dividir o texto em linhas
        drawtext_commands = []

        for i, line in enumerate(lines):
            y_position = y_position + i * line_spacing  # Ajusta a posição vertical para cada linha
            drawtext = (
                rf"""drawtext=text='{line}':x={x_position}:y={y_position}:"""
                rf"""fontsize={fontsize}:fontcolor={fontcolor}:font={font}"""
                rf"""{animation}{effects}"""
            )
            drawtext_commands.append(drawtext)

        return ",".join(drawtext_commands)  # Combina todos os comandos `drawtext`

    def add_dynamic_color_effects(self):
        # Transição de cores baseada em tempo para cada caractere
        effect = (
            "drawtext="
            "text='%{eif\\:n}':"
            "x=(w-text_w)/2:"
            "y=(h-text_h)/2:"
            "fontcolor_expr='r=255:g=if(mod(t*10\,2)\,255\,0):b=0':"
            "fontsize=36:"
            "font=Arial,"
        )
        return effect

    def add_ad_marketing(self, input_video, ad_video, output_video):

        command= [
            "ffmpeg",
            "-i", input_video,
            "-y",
            "-i", ad_video,
            "-filter_complex", "[0:v]setsar=1[v0]; [1:v]setsar=1[v1]; [v0][0:a][v1][1:a]concat=n=2:v=1:a=1 [v][a]",
            '-vsync', '2',  # Sincroniza os quadros
            "-map", "[v]",
            "-map", "[a]",
            output_video
        ]
        subprocess.run(command, check=True)




    def theme_default(self, 
                                            nome_do_video, 
                                            name_srt,
                                            output_video_name,
                                            basenamefolder_arg):
        #caminho_ffmpeg = self.path_ffmpeg #os.path.join(self.diretorio_script, 'CoreApp', "ffmpeg", 'ffmpeg.exe')
        cor_legenda = self.get_color_for_caption(color_name=self.CaptionsColor)
        
        cor_segundo_texto = self.get_cor_segundo_texto(color_title=self.SubtitleColor)

        animation = self.get_alpha_for_animation(subtitle_animation=self.SubtitleAnimation)

        efeitos = self.get_effect_for_subtitle(subtitle_effect=self.SubtitleEffects)

        name_ass = name_srt
        # PrimaryColour=&H007FFF&,
        # captions_filter = (
        #     f'subtitles="{name_srt}":force_style="FontName={self.CaptionsFontName_},Alignment={self.Alignment},Fontsize={self.Fontsize}"'
        # )
        
        # subtitle_filter = (
        # f"drawtext=text='{second_text}':x=(w-text_w)/2:y=(h-text_h)/{self.Subtitle_vertical_reference}:"
        # f"fontsize={self.Fontsize_title}:fontcolor={cor_segundo_texto}:font='{self.SubtitleFontName_}':"
 
        # f"{animation}"  
        # f"{efeitos}"
        # )
        # print(subtitle_filter)
        #combined_filter = f"{captions_filter},{subtitle_filter}"
        
        fontconfig_path = r'C:\Program Files (x86)\GnuWin32\share\fontconfig'
        os.environ['FONTCONFIG_PATH'] = fontconfig_path

        #testettf = "CoreApp/ttf/PlaywriteGBS-ExtraLight.ttf"
            
        vf_filter = (
            rf"""ass='{name_ass}',"""
            + self.generate_drawtext_commands(
                text=basenamefolder_arg,
                x_position="(w-text_w)/2",  # Centraliza horizontalmente
                y_position=100,#f"(h-text_h)/{self.SubtitleVerticalReference}",  # Posição Y inicial
                line_spacing=70,  # Espaçamento entre linhas
                fontsize=self.SubtitleFontsize,
                fontcolor=cor_segundo_texto,
                font=self.SubtitleFontName,
                animation=animation,
                effects=efeitos,
            )
            
        )


        # vf_filter = (
        #     rf"""subtitles={name_srt}:force_style='FontName={self.CaptionsFontName_},Alignment={self.Alignment},Fontsize={self.Fontsize}',"""
        #     rf"""drawtext=text='input\\n_video':x=(w-text_w)/2:y=(h-text_h)/{self.Subtitle_vertical_reference}:"""
        #     rf"""fontsize={self.Fontsize_title}:fontcolor={cor_segundo_texto}:font={self.SubtitleFontName_}{animation}{efeitos}"""
        # )

        #vf_filter = rf"""subtitles={name_srt}:force_style='FontName={self.CaptionsFontName_},Alignment={self.Alignment},Fontsize={self.Fontsize}',drawtext=text='input\n_video':x=(w-text_w)/2:y=(h-text_h)/{self.Subtitle_vertical_reference}:fontsize={self.Fontsize_title}:fontcolor={cor_segundo_texto}:font={self.SubtitleFontName_}{animation}{efeitos}"""
        
        
        for i  in range(5):
                
            time_pattern = re.compile(r'time=(\d+:\d+:\d+\.\d+)')
            size_pattern = re.compile(r'size=\s*(\d+(\.\d+)?[A-Za-z]+)')
            try:


                if self.dockerffmpegCPU == True:
                    comando = [
                        "ffmpeg",
                        '-y',
                        '-i', f"{nome_do_video}",
                        '-vf', vf_filter.strip(),  # Remove espaços extras
                        "-c:v", "libx264",
                        "-preset", "fast",   
                        "-threads", "0", 
                        "-c:a", "aac", 
                        "-b:a", "128k",  
                        output_video_name
                    ]

                elif self.dockerffmpegGPU == True:
                    comando = [
                        "ffmpeg", '-y',
                        '-hwaccel', "cuda",
                        '-hwaccel_output_format', 'cuda',
                        '-i', f"{nome_do_video}",
                        '-vf', vf_filter.strip(),  # Remove espaços extras
                        '-c:v', 'h264_nvenc', 
                        '-preset', 'p5', 
                        '-c:a', 'copy', 
                        output_video_name
                    ]
     
                #print(comando)
                # subprocess.run(comando, shell=True)
                # return True
                counter = 0
                process = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True,  encoding="utf-8")
                while True:
                    output = process.stderr.readline()
                    if output == "" and process.poll() is not None:
                        break
                    if output:
                        time_match = time_pattern.search(output)
                        size_match = size_pattern.search(output)
                            
                        if time_match and size_match:
                            time_value = time_match.group(1)
                            size_value = size_match.group(1)

                            log_message = f"⏳ Create captions in video... | Time: {time_value} | Size: {size_value}"

                            # if self.text_edit_download is not None:
                            #     self.text_edit_download.emit(f"Time: {time_value}, Size: {size_value}")
                            # else:
                            cprint(log_message, "yellow")
                            # # counter += 1
                            # if counter == 8:
                            if self.webhook == True:

                                self.send_to_webhook(self.api_key, "info",  log_message, "yellow")
                                # counter = 0


                        
                process.wait() 
                
                process.terminate() 
                return True
            except subprocess.CalledProcessError as e:
                print(f"Erro ao adicionar legendas ao vídeo: {e}")
            except FileNotFoundError as e:
                print(f"Arquivo não encontrado: {e}")
            except PermissionError as e:
                print(f"Permissões negadas: {e}")

    def embutir_legenda_ass(self, input_video: str, subtitle_ass: str, output_video: str):
        """
        Insere (queima) a legenda ASS no vídeo, copiando o áudio sem recodificar.
        """

        if self.dockerffmpegCPU == True:
            cmd = [
                'ffmpeg',
                "-y",
                '-i', input_video,
                '-vf', f"ass={subtitle_ass}",   # filtro que aplica a legenda ASS
                '-c:v', 'libx264',  # necessário para renderizar legenda
                '-c:a', 'aac',  # recodifica o áudio
                '-b:a', '192k', # opcional: define bitrate
                '-async', '1',  # corrige desalinhamentos
                output_video
            ]

        elif self.dockerffmpegGPU == True:
            cmd = [
                'ffmpeg',
                "-y",
                '-i', input_video,
                '-vf', f"ass={subtitle_ass}",   # filtro que aplica a legenda ASS
                '-c:v', 'h264_nvenc', 
                '-preset', 'p5', 
                '-c:a', 'aac',  # recodifica o áudio
                '-b:a', '192k', # opcional: define bitrate
                '-async', '1',  # corrige desalinhamentos
                output_video
            ]
        subprocess.run(cmd, check=True)

    def theme_VerticalFusion(
        self,
        video_cima: str,
        imagem_baixo: str,
        fonte: str,
        texto_drawtext: str,
        ass_file: str,
        saida: str,
        CaptionsAlignment,
        SubtitleFontsize,
        SubtitleColor,
        SubtitleVerticalReference

        ):
        """
        Combina:
        - O vídeo de cima (video_cima) com os subtitles do arquivo ASS queimados
        (usando force_style para centralização e margem vertical de 20px);
        - Empilha verticalmente com a imagem fixa da parte inferior;
        - Aplica o drawtext sobre o resultado empilhado, centralizando o texto
        em relação ao frame final, independentemente das dimensões individuais.
        """
        filter_chain = (
            # Processa o vídeo de cima: escala, queima os subtitles
            "[0:v]scale=1080:-1:force_original_aspect_ratio=decrease,setsar=1,format=yuv420p,"
            "subtitles={ass}:force_style='Alignment={CaptionsAlignment},MarginV=20'[top];"
            # Processa a imagem da parte inferior: escala
            "[1:v]scale=1080:-1:force_original_aspect_ratio=decrease,setsar=1,format=yuv420p[bottom];"
            # Empilha verticalmente os dois inputs
            "[top][bottom]vstack=inputs=2[stacked];"
            # Aplica o drawtext sobre o resultado empilhado,
            # centralizando-o em relação à largura e à altura total
            "[stacked]drawtext=fontfile={fonte}:text='{texto}':"
            "x=(w-text_w)/2:y=(h-text_h)/2{SubtitleVerticalReference}:fontsize={SubtitleFontsize}:fontcolor={SubtitleColor}:"
            "shadowcolor=black:shadowx=2:shadowy=2[out]"
        ).format(ass=ass_file,
                CaptionsAlignment=CaptionsAlignment,
                fonte=fonte,
                texto=texto_drawtext,
                SubtitleFontsize=SubtitleFontsize,
                SubtitleColor=SubtitleColor,
                SubtitleVerticalReference=SubtitleVerticalReference
                          
                )



        if self.dockerffmpegCPU == True:
            command = [
                "ffmpeg",
                '-y',
                "-i", video_cima,   # entrada 0: vídeo de cima
                "-loop", "1",
                "-framerate", "30",  # define o frame rate para a imagem
                "-i", imagem_baixo,  # entrada 1: imagem para a parte inferior
                "-filter_complex", filter_chain,
                '-vsync', '2',  # Sincroniza os quadros
                "-map", "[out]",
                "-map", "0:a?",  # mapeia o áudio (se houver) do vídeo de cima
                "-c:v", "libx264",  # ou libx264, conforme sua preferência
                "-pix_fmt", "yuv420p",
                "-c:a", "copy",
                "-shortest",
                saida
            ]


        elif self.dockerffmpegGPU == True:

            command = [
                "ffmpeg", 
                "-y",
                "-i", video_cima,
                "-loop", "1", "-i", imagem_baixo,
                "-filter_complex", filter_chain,
                '-vsync', '2',  
                "-map", "[out]", "-map", "0:a?",
                '-c:v', 'h264_nvenc',
                '-preset', 'p5',
                "-pix_fmt", "yuv420p", 
                "-c:a", "copy",
                "-shortest", saida
            ]

            # Opcional: imprimir pra você ver exatamente o que está chegando  
            print("FFMPEG FILTER_CHAIN:\n", filter_chain)

        subprocess.run(command, check=True)
        # subprocess.run(command, check=True)

        # time_pattern = re.compile(r'time=(\d+:\d+:\d+\.\d+)')
        # size_pattern = re.compile(r'size=\s*(\d+(\.\d+)?[A-Za-z]+)')
        # counter = 0
        # process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True,  encoding="utf-8")
        # while True:
        #     output = process.stderr.readline()
        #     if output == "" and process.poll() is not None:
        #         break
        #     if output:
        #         time_match = time_pattern.search(output)
        #         size_match = size_pattern.search(output)
                    
        #         if time_match and size_match:
        #             time_value = time_match.group(1)
        #             size_value = size_match.group(1)
        #             log_message = f"⏳ Create Theme... | Time: {time_value} | Size: {size_value}"
        #             cprint(log_message, "yellow")
        #             if self.webhook == True:
        #                 self.send_to_webhook(self.api_key, "info",  log_message, "yellow")


                
        # process.wait() 
        
        # process.terminate() 
        return True


    def generate_subclip_with_ffmpeg_ai_curation(self, 
        video_input, 
        start_time, 
        end_time, 
        output_filename
        ):
        start_sec = self.timestamp_to_seconds(start_time)
        end_sec   = self.timestamp_to_seconds(end_time)
        duration  = end_sec - start_sec
        logger.debug(f"start_sec={start_sec}, end_sec={end_sec}, duration={duration}")

        if duration <= 0:
            raise ValueError("end_time deve ser maior que start_time")


        if self.dockerffmpegCPU == True:
        
            command = [
                "ffmpeg", '-y',
                '-ss', start_time,
                '-i', video_input,
                '-t', str(duration),
                '-c:v', 'libx264', '-preset', 'fast',
                '-c:a', 'aac', '-b:a', '128k',
                output_filename
            ]

        elif self.dockerffmpegGPU == True:

            command = [
                "ffmpeg", '-y',
                '-ss', start_time,
                '-hwaccel', "cuda",
                '-hwaccel_output_format', 'cuda',
                '-i', video_input,
                '-t', str(duration),
                "-c", "copy",
                output_filename
            ]
        proc = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if proc.returncode != 0:
            logger.error(f"FFmpeg error:\n{proc.stderr}")
            raise RuntimeError(f"FFmpeg failed (code {proc.returncode})")
        return output_filename


    def generate_subclip_with_ffmpeg(self, video_input, start_time, duration, output_filename):
        """
        Gera um subclip de um vídeo com FFmpeg.
        
        Args:
            video_input (str): Caminho do vídeo original.
            start_time (str): Tempo de início do subclip (em formato HH:MM:SS).
            duration (int): Duração do subclip em segundos.
            output_filename (str): Nome do arquivo de saída do subclip.
            
        Returns:
            str: Caminho do arquivo do subclip gerado.
        """

        if isinstance(duration, str):
            duration = self.timestamp_to_seconds(duration)
            
        print(start_time)
        print(duration)

        if self.dockerffmpegCPU == True:
            command = [
                "ffmpeg",
                '-y',
                "-ss", start_time,  # ponto de início
                "-i", video_input,  # arquivo de entrada
                "-t", str(duration),  # duração
                "-c:v", "libx264", 
                "-preset", "fast",   
                "-c:a", "aac",  # codec de áudio
                "-b:a", "128k",  
                output_filename
            ]

        elif self.dockerffmpegGPU == True:

            command = [
                "ffmpeg", '-y',
                '-hwaccel', 'cuda',
                '-hwaccel_output_format', 'cuda',
                "-i", video_input,  # arquivo de entrada
                "-ss", start_time,  # ponto de início
                "-t", str(duration),  # duração
                "-c:v", "h264_nvenc",  # Força o codec de vídeo para `mp4v-20` (MPEG-4 Parte 2)
                "-preset", 'p5',
                "-c:a", "aac",  # codec de áudio
                "-profile:v", "high", 
                '-gpu', "0",
                output_filename

            ]


        subprocess.run(command, check=True)
        # subprocess.run(command, shell=True)

        # time_pattern = re.compile(r'time=(\d+:\d+:\d+\.\d+)')   
        # size_pattern = re.compile(r'size=\s*(\d+(\.\d+)?[A-Za-z]+)')
        # counter = 0
        # process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, encoding="utf-8", errors="replace")
        # while True:
        #     output = process.stderr.readline()
        #     if output == "" and process.poll() is not None:
        #         break
        #     if output:
                
        #         time_match = time_pattern.search(output)
        #         size_match = size_pattern.search(output)
                    
        #         if time_match and size_match:
        #             time_value = time_match.group(1)
        #             size_value = size_match.group(1)

        #             log_message = f"⏳ Create subclip... | Time: {time_value} | Size: {size_value}"

        #             # if self.text_edit_download:
        #             #     self.text_edit_download.emit(log_message)
                
        #             # else:
        #             cprint(log_message, "yellow")
        #             # counter += 1
        #             if self.webhook == True:
        #                 self.send_to_webhook(self.api_key, "info",  log_message, "yellow")
        

        #         else:
        #             pass

        # process.wait() 
        
        # process.terminate() 
        return output_filename


    def process_video_with_ffmpeg(
                self,
                video_input,
                largura_vertical,
                altura_vertical,
                output_filename,
            
                fps=30,

                ):

        largura_vertical = 1080
        altura_vertical = 1980

        #"scale=520:940,setsar=1,crop=420:940", # #scale=largura:altura   
        # pad_formula_original = f"pad={largura_vertical}:{altura_vertical}:(ow-iw)/2:(oh-ih)/2"
        # centralizar_opcao = "normal"
        # if centralizar_opcao == "normal":
        #     pad_formula = f"pad=1080:1980:(ow-iw)/2:(oh-ih)/2,setsar=1"#f"pad={largura_vertical}:{altura_vertical}:(ow-iw)/2:(oh-ih)/2"
        # elif centralizar_opcao == "cima":
        #     pad_formula = f"pad={largura_vertical}:{altura_vertical}:(ow-iw)/2:(oh-ih)/2"
        #    f"pad={largura_vertical}:{altura_vertical}:(ow-iw)/2:(oh-ih)/2 - (oh-ih)*0.2"
        # elif centralizar_opcao == "teste":
        #     pad_formula = "pad=iw+5:ih:0:0"


        # if self.mode_scale == "1":
        #     scale_formula=f"scale=iw*min({largura_vertical}/iw\,{altura_vertical}/ih):ih*min({largura_vertical}/iw\,{altura_vertical}/ih),pad={largura_vertical}:{altura_vertical}:({largura_vertical}-iw*min({largura_vertical}/iw\,{altura_vertical}/ih))/2:({altura_vertical}-ih*min({largura_vertical}/iw\,{altura_vertical}/ih))/2,setsar=1"  # mode 1   
        # elif self.mode_scale == "2":
        scale_formula=f"scale=iw*min(1080/iw\,1920/ih):ih*min(1080/iw\,1920/ih)" # mode 2
        # elif self.mode_scale == "3":
        #     scale_formula=f"scale=1080:1800,setsar=1" # mode 3
        # elif self.mode_scale == "4":
        #     scale_formula=f"scale={largura_vertical}:{altura_vertical},pad={largura_vertical}:{altura_vertical}:(ow-iw)/2:(oh-ih)/2 - (oh-ih)*0.2"     # mode 4   
        # elif self.mode_scale == "5":

            # scale_formula=f"scale=1280:1800,setsar=1,crop=1280:1800"     # mode 5   

        if self.dockerffmpegCPU == True:
            command = [
                "ffmpeg",
                '-y',
                "-i", video_input,                              
                "-vf", scale_formula,
                "-r", f"{fps}",
                "-c:v", "libx264", 
                "-preset", "fast",   
                "-threads", "0", 
                "-c:a", "aac", 
                "-b:a", "128k",  
            ]

        elif self.dockerffmpegGPU == True:
            command = [
                "ffmpeg",
                '-y',
                '-hwaccel', 'cuda',
                '-hwaccel_output_format', 'cuda',
                "-i", video_input,                              
                "-vf", scale_formula,
                "-r", f"{fps}",
                "-c:v", "h264_nvenc", 
                "-preset", 'p5',
                "-c:a", "aac", 
                "-b:a", "128k",  
            ]
        # subprocess.run(command, shell=True)
        # # print(command)
        # return output_filename
        try:
                
            time_pattern = re.compile(r'time=(\d+:\d+:\d+\.\d+)')   
            size_pattern = re.compile(r'size=\s*(\d+(\.\d+)?[A-Za-z]+)')
            counter = 0
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, encoding='utf-8')
            while True:
                output = process.stderr.readline()
                if output == "" and process.poll() is not None:
                    break
                if output:
                    try:
                        time_match = time_pattern.search(output)
                        size_match = size_pattern.search(output)
                    except Exception as erro2:
                        print(f"e2 {erro2}")
                        output_decoded = output.decode('utf-8')  
                        time_match = time_pattern.search(output_decoded)
                        size_match = size_pattern.search(output_decoded)

                    if time_match and size_match:
                        
                        time_value = time_match.group(1)
                        size_value = size_match.group(1)

                        log_message = f"⏳ Creating Vertical Cuts... | Time: {time_value} | Size: {size_value}"

                        cprint(log_message, "yellow")
                        # counter += 1
                        if self.webhook == True:
                            self.send_to_webhook(self.api_key, "info",  log_message, "yellow")
            


                    else:
                        pass

            process.wait() 
            process.terminate() 

            return output_filename

        except Exception as erro1:
            print(f"e1 {erro1}")
        try:
            subprocess.run(command, shell=True)
        except subprocess.CalledProcessError as e:
            print(f"Erro ao extrair áudio: {e.stderr.decode()}")

    def convert_to_mp4_codec_with_ffmpeg(self, input_video, output_video_mkv):
        try:
            command = [
                "ffmpeg",
                '-y',
                '-i', input_video, 
                '-c:v', "libx264", # 'mpeg4'
                "-threads", "0", 
                '-crf', '23',  # Menor valor = maior qualidade (padrão é 23, 18 é quase sem perdas)
                '-preset', 'slow',  # Melhor compressão sem perder muita velocidade
                "-c:a", "copy", 
                "-b:a", "192k",  

                output_video_mkv
            ]

            # try:
            #     subprocess.run(command, shell=True)
            # except subprocess.CalledProcessError as e:
            #     print(f"Erro ao extrair áudio: {e.stderr.decode()}")

            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True,  encoding="utf-8")
            time_pattern = re.compile(r'time=(\d+:\d+:\d+\.\d+)')
            size_pattern = re.compile(r'size=\s*(\d+(\.\d+)?[A-Za-z]+)')
            counter = 0
            while True:
                output = process.stderr.readline()
                if output == "" and process.poll() is not None:
                    break
                if output:
                    time_match = time_pattern.search(output)
                    size_match = size_pattern.search(output)
                    

                    if time_match and size_match:
                        time_value = time_match.group(1)
                        size_value = size_match.group(1)

                        log_message = f"⏳ Convert to mp4 codec... | Time: {time_value} | Size: {size_value}"

                        cprint(log_message, "yellow")
                        # counter += 1
                        if self.webhook == True:
                            self.send_to_webhook(self.api_key, "info",  log_message, "yellow")
            


                    

                    
                    else:
                        pass

            process.wait() 
            process.terminate() 
            return output_video_mkv
        except subprocess.CalledProcessError as e:
            print(f"Erro ao adicionar legendas ao vídeo: {e}")
        except FileNotFoundError as e:
            print(f"Arquivo não encontrado: {e}")
        except PermissionError as e:
            print(f"Permissões negadas: {e}")

    def add_watermark(
                    self, input_video,
                    output_video, text_watermark,
                    watermark_image=None, fontsize_text_watermark=39,
                    fontcolor="fontcolor=white@0.4", overlay="overlay=W-w-10:10",
                    watermark_width=100, watermark_height=43,
                    fontfile="fontfile=Studio/Utils/ttf/PlaywriteGBS-ExtraLight.ttf"
                ):
        """
        Adiciona uma marca d'água ao vídeo, incluindo uma imagem e um texto personalizado.

        :param input_video: str - Caminho para o vídeo de entrada.
        :param output_video: str - Caminho para salvar o vídeo de saída com a marca d'água.
        :param text_watermark: str - Texto a ser exibido como marca d'água no vídeo.
        :param watermark_image: str - Caminho para a imagem de marca d'água a ser sobreposta no vídeo.
        :param fontsize_text_watermark: int, opcional - Tamanho da fonte do texto de marca d'água. 
            Valor padrão: 39.
        :param fontcolor: str, opcional - Cor e transparência do texto da marca d'água, 
            no formato `fontcolor=color@opacity`. Exemplo: "fontcolor=white@0.4".
            Valor padrão: "fontcolor=white@0.4".
        :param overlay: str, opcional - Posição da imagem de marca d'água no vídeo, 
            definida no formato do filtro `overlay`. Exemplo: "overlay=W-w-10:10".
            Valor padrão: "overlay=W-w-10:10" (canto superior direito com margem de 10 pixels).
        :param watermark_width: int, opcional - Largura da imagem de marca d'água, em pixels. 
            Valor padrão: 100.
        :param watermark_height: int, opcional - Altura da imagem de marca d'água, em pixels. 
            Valor padrão: 43.
        :param fontfile: str, opcional - Caminho para o arquivo de fonte TrueType (.ttf) usado no texto
            da marca d'água. Valor padrão: 
            "fontfile=src_/CoreApp/ttf/PlaywriteGBS-ExtraLight.ttf".

        :return: None
            A função salva o vídeo processado no caminho especificado em `output_video`.
            Não há retorno direto de valor.
        """
        try:

            if self.dockerffmpegCPU == True:
                command = [
                    "ffmpeg",
                    '-y',
                    '-i', input_video,
                    '-i', watermark_image, 
                    '-filter_complex', (
                        f"[1:v]format=rgba,scale={watermark_width}:{watermark_height}[wm];[0:v][wm]{overlay}" 
                        f",drawtext={fontfile}"
                        f":text={text_watermark}:" 
                        "x=(W-text_w)/2:y=(H-text_h)/2:"
                        f"fontsize={fontsize_text_watermark}:{fontcolor}"

                    ),
                    "-c:v", "libx264",
                    "-preset", "fast",   
                    "-threads", "0", 
                    "-c:a", "copy", 
                    "-b:a", "128k",  
                    output_video  
                ]

            elif self.dockerffmpegGPU == True:
                command = [
                    "ffmpeg",
                    '-y',
                    '-hwaccel', 'cuda',
                    '-hwaccel_output_format', 'cuda',
                    '-i', input_video,
                    '-i', watermark_image, 
                    '-filter_complex', (
                        f"[1:v]format=rgba,scale={watermark_width}:{watermark_height}[wm];[0:v][wm]{overlay}" 
                        f",drawtext={fontfile}"
                        f":text={text_watermark}:" 
                        "x=(W-text_w)/2:y=(H-text_h)/2:"
                        f"fontsize={fontsize_text_watermark}:{fontcolor}"

                    ),
                    "-c:v", "h264_nvenc",
                    "-preset", 'p5',
                    "-c:a", "copy", 
                    "-b:a", "128k",  
                    output_video  
                ]

            #subprocess.run(command, shell=True)
          
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True,  encoding="utf-8")
            time_pattern = re.compile(r'time=(\d+:\d+:\d+\.\d+)')
            size_pattern = re.compile(r'size=\s*(\d+(\.\d+)?[A-Za-z]+)')
            counter = 0
            while True:
                output = process.stderr.readline()
                if output == "" and process.poll() is not None:
                    break
                if output:
                    time_match = time_pattern.search(output)
                    size_match = size_pattern.search(output)
                    if time_match and size_match:
                        time_value = time_match.group(1)
                        size_value = size_match.group(1)

                        log_message = f"⏳ Add watermark... | Time: {time_value} | Size: {size_value}"

                        cprint(log_message, "yellow")
                        # counter += 1
                        if self.webhook == True:
                            self.send_to_webhook(self.api_key, "info",  log_message, "yellow")
            


                    else:
                        pass
            process.wait() 
            process.terminate() 

        except subprocess.CalledProcessError as e:
            print(f"Erro ao adicionar a marca d'água: {e}")


    def adpte_srt_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Substituir vírgulas apenas nas linhas que não contêm "-->"
        lines = [line.replace(",", "") if "-->" not in line else line for line in lines]

        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(lines)


    def remove_ass_tags(self, text):
        """Remove tags ASS do texto para obter apenas o conteúdo textual."""
        import re
        return re.sub(r'\{[^}]*\}', '', text)


    def time_to_ms(self, time_str):
        """Converte tempo no formato ASS (H:MM:SS.CC) para milissegundos."""
        parts = time_str.split(':')
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds_parts = parts[2].split('.')
        seconds = int(seconds_parts[0])
        centiseconds = int(seconds_parts[1])
        
        total_ms = (hours * 3600 + minutes * 60 + seconds) * 1000 + centiseconds * 10
        return total_ms


    def ms_to_time(self, ms):
        """Converte milissegundos para formato ASS (H:MM:SS.CC)."""
        hours = ms // (3600 * 1000)
        ms %= (3600 * 1000)
        minutes = ms // (60 * 1000)
        ms %= (60 * 1000)
        seconds = ms // 1000
        centiseconds = (ms % 1000) // 10
        
        return f"{hours}:{minutes:02d}:{seconds:02d}.{centiseconds:02d}"



    def apply_typewriter_effect_simple(self, ass_file_path, char_reveal_time=120):
        """
        Versão mais simples e robusta do efeito máquina de escrever.
        Cria múltiplas linhas de diálogo sobrepondo-se para simular a digitação.
        """
        try:
            with open(ass_file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # Dividir em seções
            sections = content.split('\n\n')
            events_section = None
            events_index = -1
            
            for i, section in enumerate(sections):
                if '[Events]' in section:
                    events_section = section
                    events_index = i
                    break
            
            if events_section is None:
                return "Erro: Seção [Events] não encontrada no arquivo ASS"

            lines = events_section.split('\n')
            new_event_lines = []
            
            for line in lines:
                if line.strip().startswith('Dialogue:'):
                    # Processar linha de diálogo
                    parts = line.split(',', 9)
                    if len(parts) >= 10:
                        start_time = parts[1]
                        end_time = parts[2]
                        text = parts[9]
                        
                        # Remover tags existentes para obter texto limpo
                        clean_text = self.remove_ass_tags(text).strip()
                        
                        if clean_text:
                            # Criar efeito typewriter
                            typewriter_lines = self.create_simple_typewriter(
                                parts, start_time, end_time, clean_text, char_reveal_time
                            )
                            new_event_lines.extend(typewriter_lines)
                        else:
                            new_event_lines.append(line)
                    else:
                        new_event_lines.append(line)
                else:
                    new_event_lines.append(line)
            
            # Reconstruir o arquivo
            sections[events_index] = '\n'.join(new_event_lines)
            new_content = '\n\n'.join(sections)
            
            with open(ass_file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)

            return f"Efeito máquina de escrever aplicado com sucesso ao arquivo {ass_file_path}!"
            
        except Exception as e:
            print(f"Erro ao aplicar efeito máquina de escrever simples: {e}")
            return f"Erro: {e}"


    def create_simple_typewriter(self, original_parts, start_time, end_time, text, char_reveal_time):
        """
        Cria linhas de diálogo para efeito typewriter simples.
        Cada linha mostra uma parte progressivamente maior do texto.
        """
        lines = []
        start_ms = self.time_to_ms(start_time)
        
        # Considerar apenas caracteres visíveis para o timing
        visible_text = ""
        char_positions = []
        
        for i, char in enumerate(text):
            if char.strip() or visible_text:  # Inclui espaços após primeiro caractere visível
                visible_text += char
                char_positions.append(i)
        
        if not char_positions:
            # Se não há caracteres visíveis, retorna linha original
            return [','.join(original_parts)]
        
        # Criar uma linha para cada caractere revelado
        for i, pos in enumerate(char_positions):
            # Texto revelado até esta posição
            revealed_text = text[:pos + 1]
            
            # Calcular timing
            reveal_start = start_ms + (i * char_reveal_time)
            
            # Duração: até próximo caractere ou final
            if i < len(char_positions) - 1:
                reveal_end = start_ms + ((i + 1) * char_reveal_time)
            else:
                # Última revelação vai até o final original
                reveal_end = self.time_to_ms(end_time)
            
            # Garantir que não exceda o tempo final
            if reveal_start >= self.time_to_ms(end_time):
                break
                
            # Criar nova linha
            new_parts = original_parts.copy()
            new_parts[1] = self.ms_to_time(reveal_start)
            new_parts[2] = self.ms_to_time(min(reveal_end, self.time_to_ms(end_time)))
            new_parts[9] = revealed_text
            
            lines.append(','.join(new_parts))
        
        return lines


    def apply_typewriter_effect_fixed(self, ass_file_path, char_reveal_time=75):
        """
        Versão corrigida do efeito máquina de escrever que realmente funciona.
        Use esta função no lugar da original.
        """
        return self.apply_typewriter_effect_simple(ass_file_path, char_reveal_time)


    def apply_reveal_effect(self, ass_file_path, initial_color='&HFFFFFF&', final_color='&H00FFFF&', base_time=37):
        """
        Applies a sequential "reveal" effect to subtitles in an ASS (Advanced SubStation Alpha) file.

        This method processes the `[Events]` section of the ASS file, adding a color-changing effect to each character 
        in the subtitles. The characters transition from the initial color (`initial_color`) to the final color 
        (`final_color`) over a defined time interval (`base_time`).

        Args:
            ass_file_path (str): Path to the ASS file to be modified.
            initial_color (str, optional): The initial color for the effect in ASS color format (e.g., '&HFFFFFF&').
                Defaults to white ('&HFFFFFF&').
            final_color (str, optional): The final color for the effect in ASS color format (e.g., '&H00FFFF&').
                Defaults to cyan ('&H00FFFF&').
            base_time (int, optional): Base time (in milliseconds) for the color transition of each character.
                Defaults to 37 milliseconds.

        Returns:
            None

        Raises:
            Exception: If an error occurs while processing or saving the ASS file.
        """
        try:
            # Read the content of the .ass file
            with open(ass_file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            inside_events = False
            new_lines = []

            for line in lines:
                line = line.strip()

                # Detect the start of the [Events] section
                if line.startswith('[Events]'):
                    inside_events = True
                    new_lines.append(line)
                    continue

                # Process the [Events] section where subtitles are defined
                if inside_events:
                    if line.startswith('Dialogue:'):
                        # Dialogue line
                        fields = line.split(',')
                        text = fields[9]  # Subtitle text (last field)

                        # Create the sequential reveal effect
                        animated_text = f"{{\\c({initial_color})}}"  # Base color
                        total_time = 0

                        for char in text:
                            if char == ",":
                                char = char.replace(",", "")

                            if char.strip():  # Ignore whitespace
                                # Timing for each character
                                start = total_time
                                end_yellow = start + base_time
                                end_total = end_yellow + base_time

                                # Add color transition effect
                                animated_text += (
                                    f"{{\\t({end_yellow},{end_total},\\c({final_color}))}}{char}"
                                    f"{{\\t({start},{end_yellow},\\c({initial_color}))}}"
                                )

                                # Increment total time for the next character
                                total_time = end_total
                            else:
                                # For spaces, add without animation
                                animated_text += char

                        # Replace the text in the dialogue field
                        fields[9] = animated_text
                        new_lines.append(",".join(fields))
                    else:
                        new_lines.append(line)
                else:
                    new_lines.append(line)

            # Save the modified content back to the .ass file
            with open(ass_file_path, 'w', encoding='utf-8') as file:
                file.writelines("\n".join(new_lines))

            return f"Sequential reveal effect applied to the file {ass_file_path}!"
        except Exception as e:
            print(f"An error occurred while modifying the ASS file: {e}")

    def add_line_breaks(self, text):
        """
        Inserts line breaks into a given text after every 8 non-empty words.

        This function splits the text into words, counts the non-empty words,
        and appends a line break ("\n") after every 8 words. Empty spaces 
        are ignored in the word count.

        Args:
            text (str): The input text to process.

        Returns:
            str: The text with line breaks added after every 8 words.
        """
        words = text.split(" ")
        word_count = 0
        result = []

        for word in words:
            result.append(word)
            if word != "":  # Ensures empty spaces are not counted
                word_count += 1
                if word_count == 5:
                    result.append("\n")
                    word_count = 0

        return " ".join(result)

    def get_audio_duration(self, audio_path):
        cmd = [
            self.path_ffprobe,
            '-v', 'error',
            '-select_streams', 'a:0',
            '-show_entries', 'format=duration',
            '-of', 'json',
            audio_path
        ]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
        duration = json.loads(result.stdout)['format']['duration']
        return float(duration)



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

    def get_system_info(self):
        cpu_info = self.get_cpu_name()
        ram_info = psutil.virtual_memory()
        ram_gb = ram_info.total / (1024 ** 3) 
        gpus = []
        # try:
        #     import GPUtil
        #     gpus = GPUtil.getGPUs()
        # except ImportError:
        #     print("GPUtil não está instalado. Instale com 'pip install gputil'.")

        # gpu_info = ', '.join([gpu.name for gpu in gpus]) if gpus else "Nenhuma GPU detectada."

        return {
            'Processador': cpu_info,
            'RAM (GB)': ram_gb,
        }

    def get_machine_info(self):
        system_info = platform.uname()
        machine = system_info.node
        return machine

    def send_to_webhook(self, user, type, message, cor):
        """Envia uma mensagem para o webhook."""
        try:
            # Envia o conteúdo da mensagem como JSON; ajuste se necessário
            requests.post(self.WEBHOOK_URL, json={str(user): {"type": type, "message": message}})

        except Exception as e:
            # Evita erro recursivo chamando a função original de print
            print("Erro ao enviar mensagem para webhook:", e)

    ### CreateMediaBase 
    def download_all_media_in_playlist(self, 
                                    playlist_url="https://www.youtube.com/playlist?list=PLa5DLqsgytIY56wnpMqydgTMCF-3AjPaP",
                                    output_path=r"A:\Saas do site\Media Cuts (dev)\CoreApp\CreateMediaBase\%(title)s.%(ext)s",
                                    batch_size=5):

        def download_video(video_url, output_path):
            quality = "1080"
            format_string = f"bestvideo[height<={quality}]+bestaudio/best"
            ydl_opts = {
                'format': format_string,
                'outtmpl': output_path,
                'ffmpeg_location': self.path_ffmpeg,
                'ignoreerrors': True,
                'retries': 5,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])

        ydl_opts = {
            'extract_flat': 'in_playlist',  
            'playlistend': None,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(playlist_url, download=False)
            video_urls = [entry['url'] if 'url' in entry else f"https://www.youtube.com/watch?v={entry['id']}" for entry in info['entries']]
        with ThreadPoolExecutor(max_workers=batch_size) as executor:
            futures = []
            for video_url in video_urls:
                future = executor.submit(download_video, video_url, output_path)
                futures.append(future)
            for future in futures:
                future.result()

        # # Exemplo de uso
        # output_path = r"A:\Saas do site\Media Cuts (dev)\CoreApp\CreateMediaBase\%(title)s.%(ext)s"
        # playlist_url = "https://www.youtube.com/playlist?list=PLa5DLqsgytIY56wnpMqydgTMCF-3AjPaP"

    def list_sequence_and_rename(self,
                                lista=[],
                                pasta="CoreApp\\CreateMediaBase",
                                nome_capitulo="novela ausurpadora",
                                padrao=re.compile(r"(Cap[ií]tulo\s*\d+)", re.IGNORECASE),
                                padrao_capitulo=re.compile(r"Cap[ií]tulo\s*(\d+)", re.IGNORECASE),
                                ):

        def listar_sequencias_de_videos(pasta):
            videos_sequenciais = defaultdict(list)
            
            for arquivo in os.listdir(pasta):
                if arquivo.endswith(".mp4"):
                    caminho_completo = os.path.join(pasta, arquivo)
                    match = padrao.search(arquivo)
                    if match:
                        nome_base = match.group(1).strip()
                        videos_sequenciais[nome_base].append(caminho_completo)

            lista_videos_sequenciais = [videos for videos in videos_sequenciais.values() if len(videos) > 1]
            return lista_videos_sequenciais

        def extrair_nome_identificador(nome_base, parte_numero):
            
            match = padrao_capitulo.search(nome_base)
            if match:
                numero_capitulo = match.group(1)
                return f"{nome_capitulo} capitulo {numero_capitulo} parte {parte_numero}.mp4"
            return None
        
        def renomear_arquivos(sequencias, pasta, lista):
            for sequencia in sequencias:
                for parte_numero, video in enumerate(sequencia, start=1):
                    nome_identificador = extrair_nome_identificador(sequencia[0], parte_numero)
                    print(nome_identificador)
                    lista.append(nome_identificador)
                    novo_caminho = os.path.join(pasta, nome_identificador)
                    os.rename(video, novo_caminho) 
                    print(f"Arquivo renomeado para: {novo_caminho}")

        sequencias = listar_sequencias_de_videos(pasta)
        renomear_arquivos(sequencias, pasta, lista)
        time.sleep(15)

    def compile_episodes_of_soap_operas(self, 
                                        CreateMediaBase,
                                        padrao=re.compile(r"novela ausurpadora capitulo (\d+) parte (\d+)", re.IGNORECASE),
                                        max_workers=1,
                                        name_output_path="novela ausurpadora capitulo",
                                        ):

        """CreateMediaBase=os.path.join(self.diretorio_script, 'CoreApp', 'CreateMediaBase')"""


        #padrao = re.compile(r"novela ausurpadora capitulo (\d+) parte (\d+)", re.IGNORECASE)
        #diretorio_script = os.path.dirname(os.path.abspath(__file__))
        #caminho_ffmpeg = os.path.join(self.diretorio_script, 'CoreApp', 'utils', "ffmpeg", 'ffmpeg.exe')
        #CreateMediaBase = os.path.join(self.diretorio_script, 'CoreApp', 'CreateMediaBase')

        def create_media_base(video_paths, output_path):
            with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8', suffix='.txt', dir=CreateMediaBase) as file_list:
                for video_path in video_paths:
                    if os.path.exists(video_path):
                        file_list.write(f"file '{video_path}'\n")
                    else:
                        print(f"Arquivo não encontrado e ignorado: {video_path}")
                lista_videos_path = file_list.name
            ffmpeg_command = [
                self.path_ffmpeg, '-y', '-f', 'concat', '-safe', '0', '-hwaccel', self.hwaccel, '-hwaccel_device', self.hwaccel_encode_device, 
                '-i', lista_videos_path, '-c:v', self.vcodec, '-preset', self.preset, '-gpu', self.gpu_, 
                '-c:a', 'aac', '-b:a', self.bitrate, output_path
            ]
            time_pattern = re.compile(r'time=(\d+:\d+:\d+\.\d+)')   
            size_pattern = re.compile(r'size=\s*(\d+(\.\d+)?[A-Za-z]+)')
            process = subprocess.Popen(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            while True:
                output = process.stderr.readline()
                if output == "" and process.poll() is not None:
                    break
                if output:
                    time_match = time_pattern.search(output)
                    size_match = size_pattern.search(output)
                    
                    if time_match:
                        time_value = time_match.group(1)
                    if size_match:
                        size_value = size_match.group(1)
                    if self.text_edit_download is not None:
                        self.text_edit_download.emit(f"Time: {time_value}, Size: {size_value}")
                    else:
                        print(f"Time: {time_value}, Size: {size_value}")
            process.wait() 
            process.terminate() 
            os.remove(lista_videos_path)
            for video_path in video_paths:
                if os.path.exists(video_path):
                    os.remove(video_path)
                    
        def listar_videos_por_capitulo(pasta):
            capitulos = {}
            for arquivo in os.listdir(pasta):
                if arquivo.endswith(".mp4"):
                    caminho_completo = os.path.join(pasta, arquivo)
                    match = padrao.search(arquivo)
                    if match:
                        capitulo_numero = match.group(1)
                        parte_numero = int(match.group(2))
                        if capitulo_numero not in capitulos:
                            capitulos[capitulo_numero] = []
                        capitulos[capitulo_numero].append((parte_numero, caminho_completo))
            for capitulo in capitulos:
                capitulos[capitulo] = [caminho for _, caminho in sorted(capitulos[capitulo])]
            return capitulos

        def juntar_capitulo(capitulo, videos):
            output_path = os.path.join(self.diretorio_script, "CoreApp", "MediaBase", f"{name_output_path} {capitulo}.mp4")
            create_media_base(videos, output_path)

        def juntar_capitulos(pasta):
            capitulos = listar_videos_por_capitulo(pasta)
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = []
                for capitulo, videos in capitulos.items():
                    futures.append(executor.submit(juntar_capitulo, capitulo, videos))
                for future in futures:
                    future.result() 

        juntar_capitulos(CreateMediaBase)
    


    # tools

    def get_cpu_name(self):
        """Obtém a nomenclatura do processador."""
        if platform.system() == "Windows":
            # Comando para Windows
            command = "wmic cpu get name"
            cpu_name = subprocess.check_output(command, shell=True).decode().strip().split('\n')[1]
        elif platform.system() == "Linux":
            # Comando para Linux
            command = "cat /proc/cpuinfo | grep 'model name' | uniq"
            cpu_name = subprocess.check_output(command, shell=True).decode().strip().split(': ')[1]
        elif platform.system() == "Darwin":
            # Comando para macOS
            command = "sysctl -n machdep.cpu.brand_string"
            cpu_name = subprocess.check_output(command, shell=True).decode().strip()
        else:
            cpu_name = "Sistema não suportado."
        
        return cpu_name

    def get_system_info(self):
        # Nome do processador
        cpu_info = self.get_cpu_name()

        # Quantidade de RAM em GB
        ram_info = psutil.virtual_memory()
        ram_gb = ram_info.total / (1024 ** 3)  # Convertendo bytes para GB

        # Nome da GPU
        gpus = []
        # try:
        #     import GPUtil
        #     gpus = GPUtil.getGPUs()
        # except ImportError:
        #     print("GPUtil não está instalado. Instale com 'pip install gputil'.")

        # gpu_info = ', '.join([gpu.name for gpu in gpus]) if gpus else "Nenhuma GPU detectada."

        return {
            'Processador': cpu_info,
            'RAM (GB)': ram_gb,
        }



    def apply_ass_color_format(self, hex_color):
        """Converte uma cor do formato `#RRGGBB` para `&HBBGGRR&`, formato aceito por FFmpeg em ASS."""
        # Verifica se a cor está no formato hexadecimal `#RRGGBB`
        if hex_color.startswith("#") and len(hex_color) == 7:
            # Extrai RGB e reorganiza para o formato BGR
            bgr_value = hex_color[5:7] + hex_color[3:5] + hex_color[1:3]
            return f"&H{bgr_value}&"
        return hex_color  # Retorna a cor inalterada se não estiver no formato esperado


    def hex_to_ffmpeg_color(self, hex_color):
        """Converte uma cor no formato `&H00FFFF&` para `#RRGGBB`."""
        if hex_color.startswith("&H") and hex_color.endswith("&"):
            # Remove "&H" do início e "&" do final
            hex_value = hex_color[2:-1]
            # Reorganiza de BGR para RGB
            rgb_value = f"#{hex_value[4:6]}{hex_value[2:4]}{hex_value[0:2]}"
            return rgb_value
        return hex_color  # Retorna a cor inalterada se o formato não for o esperado

    def get_color_for_caption(self, color_name):
        default_color = "&H00FFFF&"  # Cor padrão
        with open(self.init_color_for_caption, "r") as file:
            for line in file:
                # Ignora linhas vazias e linhas que não contêm uma vírgula
                if "," in line:
                    nome_cor, valor_cor = line.strip().split(",", 1)  # Split apenas na primeira vírgula
                    if color_name == nome_cor: 
                        cor_legenda_ass = self.apply_ass_color_format(valor_cor)
                        print(cor_legenda_ass)
                        return cor_legenda_ass
        return default_color
    
    def get_effect_for_subtitle(self, subtitle_effect):
        effect_value = "box=1:boxcolor=black@0.5:"  # Efeito padrão
        with open(self.init_effects, "r") as file:
            for line in file:
                # Ignora linhas vazias ou que não contenham uma vírgula
                if "," in line:
                    nome_efeito, valor_efeito = line.strip().split(",", 1)  # Split apenas na primeira vírgula
                    if subtitle_effect == nome_efeito:
                        effect_value = valor_efeito
                        break
        return effect_value
        
    def get_alpha_for_animation(self, subtitle_animation):
        alpha = "alpha=1:"  # Valor padrão
        with open(self.init_alpha_for_animation, "r") as file:
            for line in file:
                # Ignora linhas sem vírgula ou vazias
                if "," in line:
                    nome_animacao, valor_alpha = line.strip().split(",", 1)  # Split apenas na primeira vírgula
                    if subtitle_animation == nome_animacao:
                        alpha = valor_alpha
                        break
        return alpha

    def get_cor_segundo_texto(self, color_title):
        cor_segundo_texto = "white"  # Valor padrão
        with open(self.init_cor_segundo_texto, "r") as file:
            for line in file:
                # Ignora linhas sem vírgula ou vazias
                if "," in line:
                    nome_cor, cor = line.strip().split(",", 1)  # Divide apenas na primeira vírgula
                    if color_title.lower() == nome_cor.lower():
                        cor_segundo_texto = cor
                        break
        return cor_segundo_texto




    def get_duration_video(self, video_path):
        # Converter para um caminho absoluto e garantir barras corretas
        video_path = Path(video_path).resolve()

        # Garantir que o arquivo existe antes de executar ffprobe
        if not video_path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {video_path}")

        # # Adicionar aspas ao caminho para evitar problemas com espaços
        # comando = [
        #     "ffprobe", "-v", "error", "-show_entries",
        #     "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(video_path)
        # ]
        # else:

        #     # Adicionar aspas ao caminho para evitar problemas com espaços
        #     comando = [
        #         self.path_ffprobe, "-v", "error", "-show_entries",
        #         "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(video_path)
        #     ]

        # resultado = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8")
        # stdout_result = resultado.stdout.strip()

        # if not stdout_result:
        #     print(f"Erro: ffprobe não retornou duração para {video_path}. Saída: {resultado.stderr}")
        duration = self.get_duration_video_opencv(video_path)
        return float(duration)
    
        # return float(stdout_result)

    def get_duration_video_opencv(self, video_path):
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise FileNotFoundError(f"Não foi possível abrir o vídeo: {video_path}")

        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        cap.release()

        if fps == 0:
            raise ValueError("FPS é zero, impossível calcular a duração.")

        duration = frame_count / fps
        return duration
    
    def seconds_to_hhmmss(self, segundos):
        horas = int(segundos // 3600)
        minutos = int((segundos % 3600) // 60)
        segundos = int(segundos % 60)
        return f"{horas:02}:{minutos:02}:{segundos:02}"

    def escolher_mp4_aleatorio(self, caminho_base, app1):
        """
        Escolhe um arquivo MP4 aleatório que não esteja em uso da lista de arquivos disponíveis no diretório.

        :param caminho_base: O diretório base onde estão os arquivos.
        :return: Caminho do arquivo MP4 escolhido ou None se não houver arquivos disponíveis.
        """
        pastas_usadas_ref = db.reference('ArquivosUsados', app=app1)  # Referência para arquivos usados
        # Lista todos os arquivos .mp4 no diretório base
        arquivos_mp4 = [arquivo for arquivo in os.listdir(caminho_base) if arquivo.endswith('.mp4')]

        # Obter arquivos já usados no Firebase
        arquivos_usados = pastas_usadas_ref.get() or {}
        print("Arquivos usados:", arquivos_usados)

        # Converte os arquivos usados em uma lista de nomes de arquivos
        arquivos_usados_nomes = [os.path.basename(arquivo) for arquivo in arquivos_usados.values()]
        
        # Verifica se o arquivo já está na lista de usados
        arquivos_disponiveis = [
            arquivo for arquivo in arquivos_mp4 
            if arquivo not in arquivos_usados_nomes
        ]

        if not arquivos_disponiveis:
            print("Nenhum arquivo MP4 disponível para escolha.")
            return None

        arquivo_escolhido = random.choice(arquivos_disponiveis)
        
        # Adiciona o arquivo escolhido à lista de arquivos usados no Firebase
        new_used_key = pastas_usadas_ref.push().key  # Gera uma nova chave
        pastas_usadas_ref.child(new_used_key).set(os.path.join(caminho_base, arquivo_escolhido))

        return os.path.join(caminho_base, arquivo_escolhido)

    def close_ffmpeg_win64(self):
        ffmpeg_processes = [proc for proc in psutil.process_iter(['pid', 'name']) if 'ffmpeg-win64-v4.2.2' in proc.info['name']]
        for proc in ffmpeg_processes:
            proc.kill()
        return True
        
    def remover_todos_arquivos(self, diretorio):
        if os.path.exists(diretorio):
            arquivos = os.listdir(diretorio)
        
            for arquivo in arquivos:
                caminho_completo = os.path.join(diretorio, arquivo)
                if os.path.isfile(caminho_completo):
                    print(f"Removendo: {caminho_completo}")
                    try:
                        os.remove(caminho_completo)
                    except:
                        pass
        
            print("Todos os arquivos foram removidos.")
        else:
            print(f"O diretório {diretorio} não existe.")







