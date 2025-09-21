# internalsheduleserver\Internal-server\Uploaders\YoutubeOfficialUploader.py
import os
os.chdir(os.path.join(os.path.dirname(__file__)))
import os
import subprocess
from firebase_admin import db
import secrets
import logging
from datetime import datetime, timedelta

from googleapiclient.errors import HttpError
import time
from flask import url_for
import requests
from dotenv import load_dotenv
import os
import pickle
import google.auth
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from Modules.send_email import SendEmail

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../', 'Keys', 'env.env'))

diretorio_script = os.path.dirname(os.path.abspath(__file__)) 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
path_logger = os.path.join(diretorio_script, '../', 'Logs')
os.makedirs(path_logger, exist_ok=True)
file_handler = logging.FileHandler(os.path.join(path_logger, 'YoutubeOfficialUploader.log'))
file_handler.setFormatter(formatter)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

host = os.getenv('SMTP_HOST')
port = int(os.getenv('SMTP_PORT', 587))
SMTP_USER = os.getenv('SMTP_USER')
password = os.getenv('SMTP_PASSWORD')
use_tls = os.getenv('SMTP_USE_TLS', 'true').lower() == 'true'

def upload_media_Youtube(
                file_name, 
                title=None,
                description=None, 
                category_id='22', 
                video_tags=['tag1', 'tag2', 'tag3'],
                TOKEN_FILE="tokens/token_Relaxing_pixel_art_vibes.pickle",
                SCOPES = ["https://www.googleapis.com/auth/youtube.upload"],
                privacyStatus="public",
                email_to_send=""
            ):
    """
    privacyStatus: 'private', 'unlisted', ou 'public'
    """
    logger.info(f"Iniciando upload do youtube: {file_name}")
    logger.info(f"Título: {title}, Categoria: {category_id}, Privacidade: {privacyStatus}")

    # carrega o pickle
    credentials = None
    if os.path.exists(TOKEN_FILE):
        logger.info(f"Arquivo de token encontrado: {TOKEN_FILE}")
        with open(TOKEN_FILE, "rb") as f:
            credentials = pickle.load(f)
            logger.info("Credenciais carregadas do pickle")
    else:
        logger.warning(f"Arquivo de token NÃO encontrado: {TOKEN_FILE}")

    # se não existe ou expirou sem refresh, aborta imediatamente
    if credentials is None:
        logger.error("Credenciais inválidas")
        raise RuntimeError(f"Arquivo de credenciais não encontrado ou inválido: {TOKEN_FILE}")

    if credentials.expired and credentials.refresh_token:
        logger.info("Credenciais expiradas. Tentando refresh...")
        credentials.refresh(Request())
        # só sobrescreve se o refresh der certo
        with open(TOKEN_FILE, "wb") as f:
            pickle.dump(credentials, f)
        logger.info("Credenciais atualizadas e salvas com sucesso.")
    elif not credentials.valid:
        # expirado sem refresh token
        logger.error("Credenciais expiradas e sem refresh token.")
        raise RuntimeError(f"Credenciais expiradas sem refresh token: {TOKEN_FILE}")

    logger.info("Criando cliente YouTube API...")
    youtube = build('youtube', 'v3', credentials=credentials)

    logger.info("Preparando arquivo para upload...")
    media_file = MediaFileUpload(file_name, mimetype='video/*', resumable=True)

    logger.info("Enviando requisição de upload para o YouTube...")
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": video_tags,
                "categoryId": category_id
            },
            "status": {
                "privacyStatus": privacyStatus, 
            }
        },
        media_body=media_file
    )

    try:
        logger.info("Executando upload...")
        response = request.execute()
        video_url = f"https://www.youtube.com/watch?v={response['id']}"
        logger.info(f"Upload completado com sucesso! Vídeo disponível em: {video_url}")
        return "Upload", None, video_url
    except HttpError as e:
        error_content = e.content.decode('utf-8') if hasattr(e, 'content') else str(e)
        logger.error(f"Erro no upload: {error_content}")
        SendEmail(
            user_email_origin=email_to_send,
            html_attach_flag=True,
            email_type="Youtube Publish Fail",
            SMTP_ADM=SMTP_USER,
            SMTP_PASSWORD=password,
            SMTP_HOST=host,
            SMTP_PORT=port,
            use_tls=use_tls,
            erro_project=error_content,
            title_origin=title,
            new_scheduled_time="new_scheduled_time"
        )
        
        if "uploadLimitExceeded" in error_content:
            logger.warning("Limite de upload do YouTube atingido. Reagendando ou pausando uploads...")
            # exemplo: esperar 1h antes de tentar novamente
            # time.sleep(3600)
            return "Failed", error_content, None
        return "Failed", None, None

if __name__ == '__main__':
    TOKEN_FILE= os.path.join(os.path.dirname(__file__), "../", "Tokens", "token_1.pickle")
    file_name= r"C:\Users\Media Cuts DeV\Downloads\HomeServer\HomeServer\internalsheduleserver\tmp\uploads\Musculacao_apos_tiro_no_pulmao.mp4"

    upload_media_Youtube(file_name, 
                    title="teste", 
                    description="teste", 
                    category_id= '22',
                    video_tags= ['tag1', 'tag2', 'tag3'],
                    TOKEN_FILE=TOKEN_FILE,
                    SCOPES = ["https://www.googleapis.com/auth/youtube.upload"],
                    privacyStatus="public"
                )