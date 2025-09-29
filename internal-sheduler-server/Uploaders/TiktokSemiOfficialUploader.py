# internalsheduleserver\Internal-server\Uploaders\TiktokSemiOfficialUploader.py
import os
os.chdir(os.path.join(os.path.dirname(__file__)))
import logging
import subprocess
from firebase_admin import db
import secrets
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from Uploaders.TiktokAutoUploader.tiktok_uploader import tiktok
from Modules.send_email import SendEmail

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../', 'Keys', 'env.env'))

diretorio_script = os.path.dirname(os.path.abspath(__file__)) 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
path_logger = os.path.join(diretorio_script, '../', 'Logs')
os.makedirs(path_logger, exist_ok=True)
file_handler = logging.FileHandler(os.path.join(path_logger, 'TiktokUploader.log'))
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

def upload_media_Tiktok(
        token_file="",
        VIDEO_PATH="",
        title=None,
        visibility=0,
        email_to_send=''
    ):
    with open(token_file, "r", encoding="utf-8") as f:
        TiktokAccountCookies = json.load(f)  
    logger.info(f"🎥 Inicializando Upload de video vertical para Tiktok")

    flag, video_id, upload_id, creation_id = tiktok.upload_video(
                        session_user_cookie=TiktokAccountCookies, 
                        video=VIDEO_PATH, 
                        title=title, 
                        visibility_type=visibility,
                        webhook=False
                    )
    if flag == True:
        message = f"✅ Upload de {title} para tiktok foi um sucesso !"
        logger.info(message)
        return "Upload", None
    else:
            
        errupload1 = ""
        logger.error(f"errupload1 {errupload1}")
        message = f"Failed {errupload1}"
        logger.info(message)
        SendEmail(
            user_email_origin=email_to_send,
            html_attach_flag=True,
            email_type="Tiktok Publish Fail",
            SMTP_ADM=SMTP_USER,
            SMTP_PASSWORD=password,
            SMTP_HOST=host,
            SMTP_PORT=port,
            use_tls=use_tls,
            erro_project=errupload1,
            title_origin=title,
            new_scheduled_time="new_scheduled_time"
        )

        return "Failed", errupload1
