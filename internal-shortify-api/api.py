# internal_api.py
from Modules.utils import create_task,send_to_webhook , get_tasks_weekly
from Modules.send_email import SendEmail
from firebase_admin import db, App
import os
import base64
import re
import json
import time
import uuid
import secrets
import logging
import hashlib
import unicodedata
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta

import pytz
import requests
from bs4 import BeautifulSoup
import yt_dlp
import stripe

from flask import Flask, render_template, request, jsonify, session, redirect, send_from_directory, url_for
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.utils import secure_filename  # Para sanitizar nomes de arquivos

from firebase_admin import db, initialize_app, credentials, storage, get_app

import asyncio
from typing import Dict, Any, Optional
from asgiref.wsgi import WsgiToAsgi
from dotenv import load_dotenv

# os.chdir(os.path.join(os.path.dirname(__file__)))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("_logger")


load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "Keys", "keys.env"))

cred = credentials.Certificate(os.getenv('DATABASEPATH'))
appfb = initialize_app(cred, {
    'databaseURL': os.getenv('DATABASEURL')
}, name="appfb")

cred = credentials.Certificate(os.getenv('DATABASEPATHDOCS'))
appdocs = initialize_app(cred, {
    'databaseURL': os.getenv('DATABASEURLDOCS')
}, name="appdocs")

app = Flask(__name__)
app.secret_key = 'chave_secreta_mediacutsstudio_api'  
app.permanent_session_lifetime = timedelta(minutes=60)  
if os.getenv("PRODUCTION_ENV") == "False":
    CORS(app, resources={r"/*": {"origins": "*"}}, origins=[
        "https://mediacutsstudio.com",
        "https://www.mediacutsstudio.com",
        "https://dev.mediacutsstudio.com",
        "https://2ba9c7d26547.ngrok-free.app",
        "https://4e799f508794.ngrok-free.app",  # novo domínio ngrok
        "http://localhost:3001",
        "http://localhost:4343",
    ])

asgi_app = WsgiToAsgi(app)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024 # 50 MB

WEBHOOK_URL = os.getenv("WEBHOOK_URL")

BR = pytz.timezone('America/Sao_Paulo')
key_openai = os.getenv("OPENAI_API_KEY")
# client = OpenAI(api_key=key_openai)
discord_token = os.getenv("discord_token")
ClientID = os.getenv("ClientID")
ClientSecret = os.getenv("ClientSecret")
TOKEN = os.getenv("TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
gmail_usuario = os.getenv("gmail_usuario")
gmail_senha = os.getenv("gmail_senha")
diretorio_script = os.path.dirname(os.path.abspath(__file__)) 
ffmpegpathnotexe = os.path.join(diretorio_script, 'Studio', 'Utils', 'ffmpeg')
path_ffmpeg = os.path.join(diretorio_script, 'Studio',  'Utils', 'ffmpeg', 'ffmpeg.exe')
path_ffprobe = os.path.join(diretorio_script,  'Studio',  'Utils', 'ffmpeg', 'ffprobe.exe')
path_ffmpegnotexe = ffmpegpathnotexe
COOKIES_FILE = os.path.join(os.path.dirname(__file__), 'Cookies', 'yt.json')
ADMIN_API_KEY = "apikey-Api-Landingpage-ZBQ2x5m_ae8Ubke9cI664PeCkerEp6EMHDyeriFFjq8"
host = os.getenv('SMTP_HOST')
port = int(os.getenv('SMTP_PORT', 587))
SMTP_USER = os.getenv('SMTP_USER')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
use_tls = os.getenv('SMTP_USE_TLS', 'true').lower() == 'true'
urlbase = os.getenv("urlbase")
createcheckout = os.getenv("createcheckout")
createlogin = os.getenv("createlogin")
login_url = os.getenv("login_url")
alfred_CreateAgent = os.getenv("alfred_CreateAgent")
alfred_agendamento = os.getenv("alfred_agendamento")
gmail_usuario = os.getenv("gmail_usuario")
gmail_senha = os.getenv("gmail_senha")
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
PRICE_ID = os.getenv("STRIPE_PRICE_ID")
WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")
UPLOAD_URL = os.getenv("UPLOAD_URL")
UPLOAD_URL_VIDEOMANAGER = os.getenv("UPLOAD_URL_VIDEOMANAGER")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
users_ref = db.reference("Users_Control_Panel", app=appfb)
schedules_ref_root = db.reference("user_schedules", app=appfb)
VIDEO_BASE_DIR = os.path.join(os.path.dirname(__file__), 'videos')
firebase_db_status = db.reference('status', app=appfb)

def key_func():
    api_key = get_api_key()
    return api_key if api_key else get_remote_address()

limiter = Limiter(
    app=app,         
    key_func=lambda: key_func(),  
    default_limits=["10 per minute"]
)

limit = "10 per minute"

def get_api_key():
    return request.headers.get('X-API-KEY')

def key_func():
    """
    Função utilizada pelo Flask-Limiter para identificar o cliente.
    Se a API Key estiver presente, utiliza-a como identificador; caso contrário,
    utiliza o endereço IP.
    """
    api_key = get_api_key()
    return api_key if api_key else get_remote_address()

def get_user_data_from_firebase(api_key, appfb):
    """
    Função que obtém os dados do usuário no Firebase Realtime Database
    a partir da chave da API, na referência 'Users_Control_Panel'.
    """
    ref = db.reference(f'Users_Control_Panel/{api_key}', app=appfb)
    user_data = ref.get() 
    return user_data

def dynamic_rate_limit(appfb: App):
    """
    Função que determina dinamicamente o limite de requisições com base na API Key do usuário.
    Se a chave estiver cadastrada, retorna o limite configurado para o perfil do usuário.
    Caso contrário, define um limite padrão para usuários não autenticados.
    """
    api_key = get_api_key()
    if api_key:
        user_data = get_user_data_from_firebase(api_key, appfb)
        if user_data:
            return user_data.get("limit", "10 per minute") 
    return "10 per minute"

def autenticar_usuario():
    """
    Função para validar a API Key.
    Retorna os dados do usuário caso a API Key seja válida,
    ou uma resposta de erro caso contrário.
    """
    api_key = get_api_key()
    if not api_key:
        response = jsonify({"error": "API Key inválida ou não fornecida."})
        response.status_code = 401 
        return None, response

    user_data = get_user_data_from_firebase(api_key, appfb)
    if not user_data:
        response = jsonify({"error": "Usuário não encontrado."})
        response.status_code = 401 
        return None, response

    return user_data, None

@app.route('/')
def index():
    return jsonify({"message": "#1 API Media Cuts Studio funcionando!"})

def extract_youtube_id(url):
    m = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11})', url)
    return m.group(1) if m else None

def scrape_youtube_metadata(url):
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=8)
    if r.status_code != 200:
        raise Exception(f"Status {r.status_code}")
    soup = BeautifulSoup(r.text, "html.parser")
    title = soup.find("meta", property="og:title")
    thumbnail = soup.find("meta", property="og:image")
    return title["content"] if title else "VideoSemTitulo", thumbnail["content"] if thumbnail else None




@app.route("/api/Media_Cuts_Studio/Shortify/Mode/Create", methods=["POST"])
@limiter.limit(lambda: dynamic_rate_limit(appfb))
def api_Media_Cuts_Studio_Shortify_Mode_Create():
    """
    Endpoint para agendar a execução do Shortify.
    Cria uma entrada no Firebase com um ID gerado e retorna esse ID.
    """
    usuario, erro = autenticar_usuario()
    if erro:
        return erro
    
    api_key = get_api_key()
    if not api_key:
        return jsonify({"error": "API Key não fornecida."}), 401

    data = request.get_json()
    user_email = data.get('user_email')
    user_email_filter = user_email.replace(".", "_")
    pasted_url = data.get("pastedUrl", "None")
    model = data.get("ShortifyMode", "")
    if pasted_url and pasted_url != "None":
        # 1) tenta yt_dlp com opções mais permissivas
        try:
            ydl_opts = {
                'cookiefile': COOKIES_FILE,
                'quiet': True,
                'skip_download': True,
                'nocheckcertificate': True,
                'ignoreerrors': True,
                'no_warnings': True,
                'format': 'best',
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(pasted_url, download=False)
                if isinstance(info, dict):
                    title_origin = info.get("title") or "VideoSemTitulo"
                    thumbnail_url = info.get("thumbnail")
                else:
                    # alguns extractors retornam lists/str; trate como falha
                    raise Exception("yt_dlp retornou formato inesperado")
        except Exception as e_yt:
            logger.warning(f"yt_dlp falhou para {pasted_url}: {e_yt}. Tentando fallback...")

            # 2) tenta oEmbed (não precisa de chave)
            try:
                oembed_url = f"https://www.youtube.com/oembed?url={requests.utils.requote_uri(pasted_url)}&format=json"
                r = requests.get(oembed_url, timeout=6)
                if r.status_code == 200:
                    j = r.json()
                    title_origin = j.get("title", "VideoSemTitulo")
                    # oEmbed fornece thumbnail_url em "thumbnail_url"
                    thumbnail_url = j.get("thumbnail_url")
                else:
                    raise Exception(f"oEmbed status {r.status_code}")
            except Exception as e_oembed:
                logger.warning(f"oEmbed falhou para {pasted_url}: {e_oembed}. Tentando scrape_youtube_metadata...")
                try:    
                    title_origin, thumbnail_url = scrape_youtube_metadata(pasted_url)
                except Exception as e_scrape_youtube_metadata:
                    raise Exception(f"e_scrape_youtube_metadata {e_scrape_youtube_metadata}")

        # try:
        #     with yt_dlp.YoutubeDL({'quiet': True,'skip_download': True}) as ydl:
        #         info = ydl.extract_info(pasted_url, download=False)
        #         title_origin = info.get("title", "VideoSemTitulo")
        #         thumbnail_url = info.get("thumbnail", "Thumbnail não encontrada")
        # except Exception as e:
        #     logger.warning(f"Erro ao extrair título da URL {pasted_url}: {str(e)}")
        #     # fallback: usar apenas o ID do vídeo como título
        #     video_id = pasted_url.split("v=")[-1]
        #     title_origin = f"Video_{video_id}"
        #     thumbnail_url = None

    else:
        lastlongvideotitle = data.get('videoTitleForLatestVideo', '')
        videoTitle = data.get('videoTitle', '')
        thumbnail_url = data.get('thumbnail_url')
        
        if lastlongvideotitle == "":
            title_origin = videoTitle
        elif videoTitle == "":
            title_origin = lastlongvideotitle

    logger.info(f"title_origin ? {title_origin}")
    logger.info(f"thumbnail_url ? {thumbnail_url}")

    mode = data.get('mode', 'date').lower()
    tz_str = data.get('timezone', 'America/Sao_Paulo')

    ref_queue = db.reference('shortify_queue', app=appfb)
    ref_projects = db.reference(f'projects/{user_email_filter}', app=appdocs)
    user_tasks_ref = db.reference(f'user_tasks/{user_email_filter}', app=appfb)

    try:
        tz = pytz.timezone(tz_str)
    except Exception as e:
        return jsonify({'error': f'Timezone inválido: {str(e)}'}), 400

    scheduled_time_str = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
    
    hash_obj = hashlib.sha256(scheduled_time_str.encode())
    hash_id = hash_obj.hexdigest()
    safe_project_name = secure_filename(title_origin).replace("-", "").replace("....", "").replace("...", "").replace("..", "").replace(".", "").replace("... - ", "").replace('"????????"', '').replace("...__", "_")
    safe_project_name_filter = re.sub(r'[^0-9A-Za-z_-]', '', safe_project_name)

    project_ref = ref_projects.child(safe_project_name_filter) 
    if not project_ref.get():
        # Se o projeto não existe, cria-o com um ID
        project_ref.set({
            "name": title_origin,
            "model_ai": model,
            "status": "Created",
            "url_original": pasted_url,
            "progress_percent": "0", # Inicia com 0%
            "used": False,
            "thumbnail_url": thumbnail_url,
            "createdAt": datetime.now(tz).isoformat(),
            "delete_after": (datetime.now(tz) + timedelta(days=3)).isoformat(),  # data 3 dias à frente
            "videos": {} # Inicializa a subcoleção de vídeos
        })
    user_tasks_ = {
        "payload": {**data, "title_origin": title_origin, "date_time": scheduled_time_str},
        "user_email": "",
        "timezone": "",
        "scheduled_time": "",
        "task_id": "",
        "yt_channel": "",
        "mode": "",
        "api_key": "",
        "status": "Created",
        "Success_rate": "0%",
        "Processing_time": "00:00:00",
        "TiktokAccount": "",
        "TiktokAccountCookies": "",

    }
    queue_item = {
        "user_email": user_email,
        "type_process": "shortify",
        "scheduled_time": scheduled_time_str,
        "api_key": api_key,
        "hash_id": hash_id,
        "payload": {**data, "title_origin": title_origin, "date_time": scheduled_time_str},
        "status": "PENDING",
        "created_at": scheduled_time_str,
    }
    id_task = scheduled_time_str.replace(".", "_").replace(":", "_").replace(" ", "_")
    ref_queue.child(id_task).set(queue_item)
    user_tasks_ref.child(id_task).set(user_tasks_)

    send_to_webhook(data['api_key'], "finish_timer_loader_shortify", "None", "yellow")

        
    return jsonify({
        "message": "✅ Task received and archived for availability check. Video placeholder created.",
        "id_task": id_task,
        'scheduled_time': scheduled_time_str,
        "user_email": user_email,
        "project_name": title_origin # Retorna o nome do projeto
    }), 202



@app.route("/api/Media_Cuts_Studio/Process/Mode/generate_subclip_ai_curation", methods=["POST"])
@limiter.limit(lambda: dynamic_rate_limit(appfb))
def api_Media_Cuts_Studio_Process_Mode_generate_subclip_ai_curation():
    """
    Endpoint para agendar a execução do Process.
    """
    usuario, erro = autenticar_usuario()
    if erro:
        return erro
    
    api_key = get_api_key()
    if not api_key:
        return jsonify({"error": "API Key não fornecida."}), 401

    data = request.get_json()
    date_time_str = data.get('date_time')
    user_email = data.get('user_email')
    tz_str = data.get('timezone', 'America/Sao_Paulo')

    ref_queue = db.reference('process_queue', app=appfb)

    try:
        tz = pytz.timezone(tz_str)
    except Exception as e:
        return jsonify({'error': f'Timezone inválido: {str(e)}'}), 400

    # -------------------- MODO DATE --------------------

    date_time_ = data.get('date_time')
    if not date_time_ or not isinstance(date_time_, str):
        return jsonify({'error': 'O parâmetro "date_time" deve ser uma string para o modo Date.'}), 400

    date_time_str = date_time_.replace("T", " ").replace(".000Z", "")
    try:
        # Tenta converter com segundos; se falhar, tenta sem segundos.
        try:
            scheduled_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
        except Exception:
            scheduled_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
    except Exception as e:
        return jsonify({'error': f'Formato de data e hora invalido !: {str(e)}'}), 400

    scheduled_time = tz.localize(scheduled_time)
    scheduled_time_str = scheduled_time.strftime('%Y-%m-%d %H:%M:%S')
    hash_obj = hashlib.sha256(scheduled_time_str.encode())
    hash_id = hash_obj.hexdigest()

    data['hash_id'] = hash_id
    queue_item = {
        "user_email": user_email,
        "type_process": "generate_subclip_ai_curation",
        "scheduled_time": scheduled_time_str,
        "hash_id": hash_id,
        "payload": data,
        "status": "PENDING",
        "created_at": datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S'),
    }
    id_task = scheduled_time_str.replace(".", "_").replace(":", "_").replace(" ", "_")
    ref_queue.child(id_task).set(queue_item)
    # ref_queue.push(queue_item)

    return jsonify({
        "message": "✅ Task received and archived for availability check.", 
        "id_task": id_task,
        'scheduled_time': scheduled_time_str,
        "user_email": user_email,
        "hash_id": hash_id
    }), 202



@app.route("/api/Media_Cuts_Studio/Process/Mode/audio_transcriber", methods=["POST"])
@limiter.limit(lambda: dynamic_rate_limit(appfb))
def api_Media_Cuts_Studio_Process_Mode_audio_transcriber():
    """
    Endpoint para agendar a execução do Process.
    """
    usuario, erro = autenticar_usuario()
    if erro:
        return erro
    
    api_key = get_api_key()
    if not api_key:
        return jsonify({"error": "API Key não fornecida."}), 401

    data = request.get_json()
    date_time_str = data.get('date_time')
    user_email = data.get('user_email')
    tz_str = data.get('timezone', 'America/Sao_Paulo')

    ref_queue = db.reference('process_queue', app=appfb)

    try:
        tz = pytz.timezone(tz_str)
    except Exception as e:
        return jsonify({'error': f'Timezone inválido: {str(e)}'}), 400

    # -------------------- MODO DATE --------------------

    date_time_ = data.get('date_time')
    if not date_time_ or not isinstance(date_time_, str):
        return jsonify({'error': 'O parâmetro "date_time" deve ser uma string para o modo Date.'}), 400

    date_time_str = date_time_.replace("T", " ").replace(".000Z", "")
    try:
        # Tenta converter com segundos; se falhar, tenta sem segundos.
        try:
            scheduled_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
        except Exception:
            scheduled_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
    except Exception as e:
        return jsonify({'error': f'Formato de data e hora invalido !: {str(e)}'}), 400

    scheduled_time = tz.localize(scheduled_time)
    scheduled_time_str = scheduled_time.strftime('%Y-%m-%d %H:%M:%S')
    hash_obj = hashlib.sha256(scheduled_time_str.encode())
    hash_id = hash_obj.hexdigest()
    data['hash_id'] = hash_id
    queue_item = {
        "user_email": user_email,
        "type_process": "audio_transcriber",
        "scheduled_time": scheduled_time_str,
        "hash_id": hash_id,
        "payload": data,
        "status": "PENDING",
        "created_at": datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S'),
    }
    id_task = scheduled_time_str.replace(".", "_").replace(":", "_").replace(" ", "_")
    ref_queue.child(id_task).set(queue_item)
    # ref_queue.push(queue_item)

    return jsonify({
        "message": "✅ Task received and archived for availability check.", 
        "id_task": id_task,
        'scheduled_time': scheduled_time_str,
        "user_email": user_email,
        "hash_id": hash_id
    }), 202





@app.route("/api/Media_Cuts_Studio/Process/Mode/thumbnail_vertical_fusion", methods=["POST"])
@limiter.limit(lambda: dynamic_rate_limit(appfb))
def api_Media_Cuts_Studio_Process_Mode_thumbnail_vertical_fusion():
    """
    Endpoint para agendar a execução do Process.
    """
    usuario, erro = autenticar_usuario()
    if erro:
        return erro
    
    api_key = get_api_key()
    if not api_key:
        return jsonify({"error": "API Key não fornecida."}), 401

    data = request.get_json()
    date_time_str = data.get('date_time')
    user_email = data.get('user_email')
    tz_str = data.get('timezone', 'America/Sao_Paulo')

    ref_queue = db.reference('process_queue', app=appfb)

    try:
        tz = pytz.timezone(tz_str)
    except Exception as e:
        return jsonify({'error': f'Timezone inválido: {str(e)}'}), 400

    # -------------------- MODO DATE --------------------

    date_time_ = data.get('date_time')
    if not date_time_ or not isinstance(date_time_, str):
        return jsonify({'error': 'O parâmetro "date_time" deve ser uma string para o modo Date.'}), 400

    date_time_str = date_time_.replace("T", " ").replace(".000Z", "")
    try:
        # Tenta converter com segundos; se falhar, tenta sem segundos.
        try:
            scheduled_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
        except Exception:
            scheduled_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
    except Exception as e:
        return jsonify({'error': f'Formato de data e hora invalido !: {str(e)}'}), 400

    scheduled_time = tz.localize(scheduled_time)
    scheduled_time_str = scheduled_time.strftime('%Y-%m-%d %H:%M:%S')
    hash_obj = hashlib.sha256(scheduled_time_str.encode())
    hash_id = hash_obj.hexdigest()
    data['hash_id'] = hash_id
    
    queue_item = {
        "user_email": user_email,
        "type_process": "thumbnail_vertical_fusion",
        "scheduled_time": scheduled_time_str,
        "hash_id": hash_id,
        "payload": data,
        "status": "PENDING",
        "created_at": datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S'),
    }
    id_task = scheduled_time_str.replace(".", "_").replace(":", "_").replace(" ", "_")
    ref_queue.child(id_task).set(queue_item)
    # ref_queue.push(queue_item)


    return jsonify({
        "message": "✅ Task received and archived for availability check.", 
        "id_task": id_task,
        'scheduled_time': scheduled_time_str,
        "user_email": user_email,
        "hash_id": hash_id
    }), 202



@app.route("/api/Media_Cuts_Studio/Process/Mode/AutoReframe", methods=["POST"])
@limiter.limit(lambda: dynamic_rate_limit(appfb))
def api_Media_Cuts_Studio_Process_Mode_AutoReframe():
    """
    Endpoint para agendar a execução do Process.
    """
    usuario, erro = autenticar_usuario()
    if erro:
        return erro
    
    api_key = get_api_key()
    if not api_key:
        return jsonify({"error": "API Key não fornecida."}), 401

    data = request.get_json()
    date_time_str = data.get('date_time')
    user_email = data.get('user_email')
    tz_str = data.get('timezone', 'America/Sao_Paulo')

    ref_queue = db.reference('process_queue', app=appfb)

    try:
        tz = pytz.timezone(tz_str)
    except Exception as e:
        return jsonify({'error': f'Timezone inválido: {str(e)}'}), 400

    # -------------------- MODO DATE --------------------

    date_time_ = data.get('date_time')
    if not date_time_ or not isinstance(date_time_, str):
        return jsonify({'error': 'O parâmetro "date_time" deve ser uma string para o modo Date.'}), 400

    date_time_str = date_time_.replace("T", " ").replace(".000Z", "")
    try:
        # Tenta converter com segundos; se falhar, tenta sem segundos.
        try:
            scheduled_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
        except Exception:
            scheduled_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
    except Exception as e:
        return jsonify({'error': f'Formato de data e hora invalido !: {str(e)}'}), 400

    scheduled_time = tz.localize(scheduled_time)
    scheduled_time_str = scheduled_time.strftime('%Y-%m-%d %H:%M:%S')
    hash_obj = hashlib.sha256(scheduled_time_str.encode())
    hash_id = hash_obj.hexdigest()
    data['hash_id'] = hash_id
    queue_item = {
        "user_email": user_email,
        "type_process": "AutoReframe",
        "scheduled_time": scheduled_time_str,
        "hash_id": hash_id,
        "payload": data,
        "status": "PENDING",
        "created_at": datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S'),
    }
    id_task = scheduled_time_str.replace(".", "_").replace(":", "_").replace(" ", "_")
    ref_queue.child(id_task).set(queue_item)
    # ref_queue.push(queue_item)

    return jsonify({
        "message": "✅ Task received and archived for availability check.", 
        "id_task": id_task,
        'scheduled_time': scheduled_time_str,
        "user_email": user_email,
        "hash_id": hash_id
    }), 202





@app.route("/api/Media_Cuts_Studio/InstagramUploader", methods=["POST"])
@limiter.limit(lambda: dynamic_rate_limit(appfb))
def api_Media_Cuts_Studio_InstagramUploader():
    """
    Endpoint para agendar a execução do Shortify.
    """
    usuario, erro = autenticar_usuario()
    if erro:
        return erro
    
    api_key = get_api_key()
    if not api_key:
        return jsonify({"error": "API Key não fornecida."}), 401

    # Get non-file data from request.form
    date_time_str = request.form.get('date_time')
    user_email = request.form.get('user_email')
    api_key = request.form.get('api_key')
    mode = request.form.get('mode', 'date').lower()
    tz_str = request.form.get('timezone', 'America/Sao_Paulo')
    title = request.form.get('title', '')
    description = request.form.get('description', '')
    tags = request.form.get('tags', '')
    ig_username = request.form.get('ig_username', '') 
    ig_password = request.form.get('ig_password', '')
    upload_video = request.form.get('upload_video', 'false').lower()
    upload_image = request.form.get('upload_image', 'false').lower()
    upload = request.files.get("file")
    if not upload:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400


    # leia todo o conteúdo em memória como bytes
    file_bytes: bytes = upload.read()

    # opcional: se quiser enviar como texto (JSON-safe), codifique em Base64
    file_b64: str = base64.b64encode(file_bytes).decode('utf-8')

    payloaddata = {
        "user_email": user_email,
        "title": title,
        "description": description,
        "tags": tags,
        "ig_username": ig_username,
        "ig_password": ig_password,
        "api_key": api_key,
        "upload_video": upload_video,
        "upload_image": upload_image,
        "timezone": tz_str,
        "mode": mode,
        "date_time": date_time_str,
        "file_bytes":    file_b64,
    }

    ref_queue = db.reference('InstagramUploader_queue', app=appfb)
    try:
        tz = pytz.timezone(tz_str)
    except Exception as e:
        return jsonify({'error': f'Timezone inválido: {str(e)}'}), 400

    # -------------------- MODO DATE --------------------
    if mode == 'date':
        date_time_str = payloaddata.get('date_time')
        if not date_time_str or not isinstance(date_time_str, str):
            return jsonify({'error': 'O parâmetro "date_time" deve ser uma string para o modo Date.'}), 400

        try:
            # Tenta converter com segundos; se falhar, tenta sem segundos.
            try:
                scheduled_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
            except Exception:
                scheduled_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
        except Exception as e:
            return jsonify({'error': f'Formato de data/hora inválido: {str(e)}'}), 400

        scheduled_time = tz.localize(scheduled_time)
        scheduled_time_str = scheduled_time.strftime('%Y-%m-%d %H:%M:%S')

        queue_item = {
            "user_email": user_email,
            "scheduled_time": scheduled_time_str,
            "payload": payloaddata,
            "status": "PENDING",
            "created_at": datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S'),
        }
        
        ref_queue.push(queue_item)

        return jsonify({
            "message": "✅ Task received and archived for availability check.", 'scheduled_time': scheduled_time_str
        }), 202

        # return jsonify({'message': 'Tarefa agendada com sucesso!', 'scheduled_time': scheduled_time_str}), 200






@app.route('/metrics/channel/youtube', methods=['GET'])
def metrics_channel_youtube():
    """
    GET /metrics/channel/youtube?channel=<URL>&limit=<n>&exclude=<id1,id2>
    Retorna os últimos vídeos de um canal YouTube e grava no Firebase.
    """
    canal_url = request.args.get('channel', '').strip()
    if not canal_url:
        return jsonify({"error": "Falta parâmetro 'channel'"}), 400

    try:
        limit = int(request.args.get('limit', 3))
    except ValueError:
        return jsonify({"error": "Parâmetro 'limit' inválido"}), 400

    exclude_raw = request.args.get('exclude')
    exclude_ids = []
    if exclude_raw:
        exclude_ids = [x.strip() for x in exclude_raw.split(',') if x.strip()]

    videos_url = "https://www.youtube.com/@" + canal_url.rstrip('/') + '/videos?hl=pt-BR&gl=BR'

    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'ignoreerrors': True,
        'skip_download': True,
        'extract_flat': 'in_playlist',
        'timeout': 30,
        'http_headers': {
            'Accept-Language': 'pt-BR,pt;q=0.9'
        },
        'playlist_items': '1-10'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(videos_url, download=False)
    except Exception as e:
        return jsonify({"error": f"Falha ao extrair vídeos: {e}"}), 500

    entries = info.get('entries') or []
    videos = []

    for entry in entries:
        if not entry:
            continue
        if entry.get("id") in exclude_ids:
            continue

        thumbs = entry.get('thumbnails') or []
        if thumbs:
            largest = max(thumbs, key=lambda t: t.get('height', 0))
            thumbnail_url = largest.get('url')
            logger.info(f"largest thumbnail_url {thumbnail_url}")

        else:
            thumbnail_url = entry.get('thumbnail')
            logger.info(f"thumbnail_url {thumbnail_url}")

        # from pytube_test import get_video_title_scrape

        title_origin = get_video_title_scrape(entry.get("id"))
        videos.append({
            "id": entry.get("id"),
            "title": title_origin,
            "title_ytdl": entry.get("title"),
            "thumbnail": thumbnail_url,
            "url": f"https://www.youtube.com/watch?v={entry.get('id')}"
        })

        # Parar o loop se já atingiu o limite após filtrar
        if len(videos) >= limit:
            break

    # Grava no Firebase
    key = canal_url.replace('https://', '').replace('/', '_')
    try:
        ref = db.reference(f'metrics/youtube/{key}', app=appfb)
        ref.set(videos)
    except Exception as e:
        app.logger.error(f"Erro ao gravar no Firebase: {e}")

    return jsonify({
        "status": "success",
        "channel": canal_url,
        "videos": videos
    }), 200

@app.route('/api/status', methods=['POST'])
def receive_status():
    if not request.is_json:
        return jsonify({"message": "Content-Type must be application/json"}), 400

    data = request.get_json()
    services = data.get('services')

    if not services or not isinstance(services, list):
        return jsonify({"message": "Dados inválidos. Esperado um array de serviços."}), 400

    try:
        current_time = datetime.now()
        # Formato ISO para consistência
        timestamp_iso = current_time.isoformat() + "Z" # Adiciona 'Z' para indicar UTC, se a sua hora for UTC
        
        # Cria uma chave única baseada no timestamp
        # Usamos o timestamp Unix (em milissegundos) para a chave, facilitando a ordenação
        update_key = f"uptime_{int(current_time.timestamp() * 1000)}"

        # Prepara os dados para salvar no Firebase
        data_to_save = {
            "timestamp": timestamp_iso,
            "services": []
        }

        for service in services:
            # Garante que `lastChecked` seja uma string ISO ou null
            last_checked = service.get('lastChecked')
            if last_checked:
                # O frontend já deve enviar como ISO string, mas garantimos que está no formato certo
                try:
                    # Se vier como string de data, tenta converter para ISO de novo
                    last_checked = datetime.fromisoformat(last_checked.replace('Z', '')).isoformat() + "Z"
                except ValueError:
                    pass # Se já for ISO válido ou outro formato, mantém como está ou trata

            data_to_save['services'].append({
                "name": service.get('name'),
                "url": service.get('url'),
                "type": service.get('type'),
                "status": service.get('status'),
                "responseTime": service.get('responseTime'),
                "message": service.get('message'),
                "lastChecked": last_checked
            })

        # Salva os dados no Firebase Realtime Database
        firebase_db_status.child(update_key).set(data_to_save)

        return jsonify({"message": "Dados de uptime salvos com sucesso!"}), 200

    except Exception as e:
        print(f"Erro ao salvar dados de uptime no Firebase: {e}")
        return jsonify({"message": f"Erro interno do servidor: {e}"}), 500

@app.route('/api/status/latest', methods=['GET'])
def get_latest_status():
    # Busca a última key no Firebase
    all_data = firebase_db_status.get()
    return jsonify(all_data), 200

@app.route('/proxy-create-login', methods=['POST'])
@limiter.limit(limit) 
def proxy_create_login():
    try:
        data = request.get_json()
        headers = {
            "Content-Type": "application/json",
            "X-API-KEY": ADMIN_API_KEY
        }
        response = requests.post(createlogin, json=data, headers=headers)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": f"Erro no servidor {e}"}), 500

@app.route("/api/leads", methods=["POST"])
def save_lead():
    data = request.json
    if not data or "email" not in data:
        return jsonify({"error": "E-mail é obrigatório"}), 400

    ref = db.reference("lead-form", app=appfb)
    new_lead_ref = ref.push({
        "name": data.get("name", ""),
        "email": data["email"],
        "whatsapp": data.get("whatsapp", ""),
    })

    return jsonify({"message": "Lead salvo com sucesso!", "id": new_lead_ref.key}), 201

@app.route("/api/chat-analytics", methods=["POST"])
def chat_analytics():
    """
    Endpoint para obter analytics detalhados de conversas
    Uso interno para dashboards e otimizações
    """
    try:
        data = request.json
        session_id = data.get("session_id")
        user_id = data.get("user_id")
        
        if not session_id and not user_id:
            return jsonify({
                "success": False,
                "error": "session_id or user_id required"
            }), 400
        
        # Aqui você implementaria a lógica para buscar analytics
        # de conversas passadas, patterns de uso, etc.
        # Por exemplo, consultando Firebase ou banco de dados
        
        # Placeholder para analytics
        analytics_data = {
            "success": True,
            "metrics": {
                "total_conversations": 0,
                "satisfaction_avg": 0,
                "resolution_rate": 0,
                "escalation_rate": 0,
                "top_topics": [],
                "marketing_conversion_rate": 0
            }
        }
        
        return jsonify(analytics_data)
        
    except Exception as e:
        logger.error(f"Error in chat_analytics: {str(e)}")
        return jsonify({
            "success": False,
            "error": "Failed to retrieve analytics"
        }), 500

@app.route("/api/chat-feedback", methods=["POST"])
def chat_feedback():
    """
    Endpoint para coletar feedback do usuário sobre a conversa
    """
    try:
        data = request.json
        session_id = data.get("session_id")
        satisfaction_score = data.get("satisfaction_score")  # 1-5
        feedback_text = data.get("feedback_text", "")
        
        if not session_id or not satisfaction_score:
            return jsonify({
                "success": False,
                "error": "session_id and satisfaction_score required"
            }), 400
        
        # Salvar feedback no banco/Firebase
        feedback_data = {
            "session_id": session_id,
            "satisfaction_score": satisfaction_score,
            "feedback_text": feedback_text,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        logger.info(f"Feedback received - Session: {session_id}, Score: {satisfaction_score}")
        
        # TODO: Implementar salvamento no Firebase/banco
        # db.collection("chat_feedback").add(feedback_data)
        
        return jsonify({
            "success": True,
            "message": "Obrigado pelo seu feedback!"
        })
        
    except Exception as e:
        logger.error(f"Error saving feedback: {str(e)}")
        return jsonify({
            "success": False,
            "error": "Failed to save feedback"
        }), 500

@app.route('/create/login', methods=['POST'])
@limiter.limit(limit) 
def endpoint_create_login():
    if not validate_api_key():
        return jsonify({'error': 'Acesso negado. API Key inválida.'}), 403

    try:
        # Obtém os dados enviados no corpo da requisição (JSON)
        data = request.get_json()

        # Extrai os campos do JSON
        email = data['email']
        password = data['password']
        try:
            subscription_plan = data['SUBSCRIPTION_PLAN']
        except:
            subscription_plan = data['subscription_plan']

        expiration = data['expiration']

        # -------------------------
        # Verifica se já existe usuário com o mesmo email
        all_users_ref = db.reference('Users_Control_Panel', app=appfb)
        all_users_data = all_users_ref.get() or {}

        existing_user_key = None
        for k, v in all_users_data.items():
            if v.get("email") == email:
                existing_user_key = v.get("api_key")
                break
        # -------------------------
        if subscription_plan == "startup":
            cuts_quality = "FULL HD"
            project_simultaneo = 1
            Real_time_AI_cuts = 30
            channels_for_auto_import = 1
            videos_base_for_cuts = 60
            themes_subtitles = 2
            themes_autoreframe = 2
            AI_models = "Studio-Startup"
            Analyse_Feeling = True
            Analyse_Justification = True
            Analyse_Viralization_potential = True
            Analyse_Viral_hashtags = True
            Task_Engagement_Analysis_of_created_tasks = False
            Task_control_area = False
            Cutting_creation_progress_visualization_area = False
            Dashboard_area = True
            Watermark_on_the_cuts = True
            Access_Time = "1, 10 minutes"


        elif subscription_plan == "content creator":
            cuts_quality = "Quad HD"
            project_simultaneo = 2
            Real_time_AI_cuts = 30
            channels_for_auto_import = 2
            videos_base_for_cuts = 90
            themes_subtitles = 2
            themes_autoreframe = 2
            AI_models = "Studio-Startup, Studio-Mini, Studio-Deep-Think"
            Analyse_Feeling = True
            Analyse_Justification = True
            Analyse_Viralization_potential = True
            Analyse_Viral_hashtags = True
            Task_Engagement_Analysis_of_created_tasks = False
            Task_control_area = False
            Cutting_creation_progress_visualization_area = False
            Dashboard_area = True
            Watermark_on_the_cuts = False
            Access_Time = "1, 10 minutes"

        elif subscription_plan== "studio":
            cuts_quality = "Ultra HD"
            project_simultaneo = 2
            Real_time_AI_cuts = 50
            channels_for_auto_import = 2
            videos_base_for_cuts = "unlimited"
            themes_subtitles = 2
            themes_autoreframe = 2
            AI_models = "all"
            Analyse_Feeling = True
            Analyse_Justification = True
            Analyse_Viralization_potential = True
            Analyse_Viral_hashtags = True
            Task_Engagement_Analysis_of_created_tasks = False
            Task_control_area = False
            Cutting_creation_progress_visualization_area = False
            Dashboard_area = True
            Watermark_on_the_cuts = False
            Access_Time = "1, 3 weekly"

        login = email

        # Se já existe usuário, usa a mesma api_key dele
        if existing_user_key:
            api_key = existing_user_key
        else:
            api_key = generate_api_key(subscription_plan)

        user_data = {
            'login': login,
            'email': email,
            'password': password,
            'subscription_plan': subscription_plan.lower(),
            'api_key': api_key,
            'expiration': expiration,
            'created_at': datetime.now().isoformat(),

            'projects_running': 0,
            'project_simultaneo': project_simultaneo,
            'cuts_quality': cuts_quality,
            'Real_time_AI_cuts': Real_time_AI_cuts,
            'channels_for_auto_import': channels_for_auto_import,
            'videos_base_for_cuts': videos_base_for_cuts,
            'themes_autoreframe': themes_autoreframe,
            'themes_subtitles': themes_subtitles,
            'AI_models': AI_models,
            'Analyse_Viralization_potential': Analyse_Viralization_potential,
            'Analyse_Feeling': Analyse_Feeling,
            'Analyse_Justification': Analyse_Justification,
            'Analyse_Viral_hashtags': Analyse_Viral_hashtags,
            'Task_Engagement_Analysis_of_created_tasks': Task_Engagement_Analysis_of_created_tasks,
            'Task_control_area': Task_control_area,
            'Cutting_creation_progress_visualization_area': Cutting_creation_progress_visualization_area,
            'Dashboard_area': Dashboard_area,
            'Watermark_on_the_cuts': Watermark_on_the_cuts,
            'Access_Time': Access_Time,
        }

        # Atualiza ou cria o usuário
        all_users_ref.child(api_key).set(user_data)

        # Se for novo usuário, envia email de boas-vindas
        if not existing_user_key:
            SendEmail(
                user_email_origin=email,
                html_attach_flag=True,
                email_type="Sucess Created Account",
                SMTP_ADM=SMTP_USER,
                SMTP_PASSWORD=SMTP_PASSWORD,
                SMTP_HOST=host,
                SMTP_PORT=port,
                use_tls=use_tls,
                erro_project="",
                title_origin="",
                new_scheduled_time=""
            )

            # Retorna os dados do usuário recém-criado
            return jsonify({
                'message': 'Usuário criado com sucesso!',
                'login': login,
                'password': password,
                'expiration': expiration,
                'subscription_plan': subscription_plan,
                'api_key': api_key,
            }), 200
        else:
            SendEmail(
                user_email_origin=email,
                html_attach_flag=True,
                email_type="Sucess Upgrated Account",
                SMTP_ADM=SMTP_USER,
                SMTP_PASSWORD=SMTP_PASSWORD,
                SMTP_HOST=host,
                SMTP_PORT=port,
                use_tls=use_tls,
                erro_project="",
                title_origin="",
                new_scheduled_time=""
            )


            # Retorna os dados do usuário recém-criado
            return jsonify({
                'message': 'Usuário Upado com sucesso!',
                'login': login,
                'password': password,
                'expiration': expiration,
                'subscription_plan': subscription_plan,
                'api_key': api_key,
            }), 200

    except Exception as e:
        # Em caso de erro, retorna a mensagem de erro com status 500 (Internal Server Error)
        logger.info(f"endpoint_create_login: error? {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/new-account/tiktok', methods=['POST'])
def new_account_tiktok():
    config = request.get_json()
    api_key = config['api_key']
    TiktokAccountUser = config['TiktokAccountUser']
    TiktokAccountCookies = config['TiktokAccountCookies']
    ref_tasks = db.reference(f'users_account_cookies/{api_key}', app=appfb)

    # 1) Recupera plano do usuário
    plano = get_user_plan(api_key)
    if not plano:
        return jsonify({'error': 'Plano do usuário não encontrado.'}), 404

    # 2) Determina limite de contas TikTok para o plano
    if plano == "startup":
        limite = 1
    elif plano == "content creator":
        limite = 3
    else:
        limite = 0

    # 3) Conta quantas contas TikTok ativas já existem
    existentes = count_tiktok_accounts(api_key)
    if existentes >= limite:
        return jsonify({
            'error': f'Limite de contas TikTok atingido para o plano "{plano}". Máximo permitido: {limite}.'
        }), 403


    json_task = {
        "platform": "Tiktok",
        "username": TiktokAccountUser,
        "status": "active",
        "AccountCookies": TiktokAccountCookies,
        "api_key": api_key,
    }
    ref_tasks.push(json_task)

    return jsonify(json_task), 200

@app.route('/api/new-account/instagram', methods=['POST'])
def new_account_instagram():
    config = request.get_json()
    api_key = config['api_key']
    ig_username = config['ig_username']
    ig_password = config['ig_password']
    ref_tasks = db.reference(f'users_account_instagram/{api_key}', app=appfb)

    # 1) Recupera plano do usuário
    plano = get_user_plan(api_key)
    if not plano:
        return jsonify({'error': 'Plano do usuário não encontrado.'}), 404

    # 2) Determina limite de contas IG para o plano
    if plano == "startup":
        limite = 1
    elif plano == "content creator":
        limite = 3
    else:
        limite = 0

    # 3) Conta quantas contas IG ativas já existem
    existentes = count_tiktok_IG(api_key)
    if existentes >= limite:
        return jsonify({
            'error': f'Limite de contas IG atingido para o plano "{plano}". Máximo permitido: {limite}.'
        }), 403


    json_task = {
        "platform": "Instagram",
        "ig_username": ig_username,
        "ig_password": ig_password,
        "api_key": api_key,
        "status": "active",
    }
    ref_tasks.push(json_task)

    return jsonify(json_task), 200

@app.route('/api/proxy/accounts/active', methods=['POST'])
def proxy_get_active_accounts():
    try:
        # Dados da requisição do frontend
        frontend_data = request.get_json()

        app.logger.info(f"{urlbase}/api/accounts/active")
        response = requests.post(
            f'{urlbase}/api/accounts/active',
            json=frontend_data,
            headers={'Content-Type': 'application/json'}
        )
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/accounts/active', methods=['POST'])
def get_active_accounts():
    try:
        config = request.get_json()
        api_key = config['api_key']
        ref1 = db.reference(f'users_account_cookies/{api_key}', app=appfb)
        snapshot1 = ref1.get() or {}
        ref2 = db.reference(f'users_account_instagram/{api_key}', app=appfb)
        snapshot2 = ref2.get() or {}

        # snapshot é um dict { account_id: {platform, username, status, ...}, ... }
        active_accounts = []
        for key, data in snapshot1.items():
            # app.logger.info(f"data? {data}")
            if isinstance(data, dict) and data.get('status') == 'active':
                active_accounts.append({
                    'id': key,
                    'platform': data.get('platform'),
                    'username': data.get('username'),
                    'status': data.get('status'),
                })
        for key, data in snapshot2.items():
            if isinstance(data, dict) and data.get('status') == 'active':
                active_accounts.append({
                    'id': key,
                    'platform': data.get('platform'),
                    'username': data.get('ig_username'),
                    'status': data.get('status'),
                })
        app.logger.info(f"active_accounts? {active_accounts}")
        return jsonify(active_accounts), 200

    except Exception as e:
        app.logger.error(f"Erro ao buscar contas ativas: {e}")
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/account/<email>', methods=['GET'])
def get_user_account(email):
    try:
        all_users_ref = db.reference('Users_Control_Panel', app=appfb)
        all_users = all_users_ref.get()

        if not all_users:
            return jsonify({'error': 'Nenhum usuário encontrado'}), 404

        # Varre os nós e busca pelo e-mail no campo `email`
        for user_id, data in all_users.items():
            if data.get('email') == email:
                return jsonify({
                    'status': 'success',
                    'action': 'get_account',
                    'email': email,
                    'account': data
                }), 200

        return jsonify({'error': 'Conta não encontrada'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/user-config/<user_id>', methods=['GET'])
def get_user_config(user_id):
    fixx_email = user_id.replace(".", "_")
    try:
        ref = db.reference(f'user_configs/{fixx_email}', app=appfb)
        config = ref.get()
        if config is None:
            return jsonify({'error': 'Configurações não encontradas'}), 404

        return jsonify({
            'status': 'success',
            'action': 'get',
            'user_id': user_id,
            'config': config
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/user-tasks/<user_id>', methods=['GET'])
def tarefas_config(user_id):
    fixx_email = user_id.replace(".", "_")
    try:
        ref = db.reference(f'user_tasks/{fixx_email}', app=appfb)
        tasks = ref.get()
        if tasks is None:
            return jsonify({'error': 'tasks não encontradas'}), 404

        return jsonify({
            'status': 'success',
            'action': 'get',
            'user_id': user_id,
            'tasks': tasks
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/account-instagram', methods=['POST'])
def user_account_instagram():
    config = request.get_json()
    api_key = config.get('api_key')
    raw_username = config.get('ig_username', '')
    username_busca = raw_username.strip().replace("  ", "").replace(" ", "").replace("\n", "").lower()
    logger.info(f"Buscando cookies para usuário normalizado: {username_busca}")

    def extrair_info(data):
        """
        Retorna tupla (ig_username, ig_password) se encontrar,
        ou (None, None) se não conseguir extrair.
        """
        if isinstance(data, dict):
            primeiro_valor = next(iter(data.values()), {})
            if isinstance(primeiro_valor, dict):
                return (
                    primeiro_valor.get('ig_username', '').strip().lower(),
                    primeiro_valor.get('ig_password', '')
                )
            return (
                data.get('ig_username', '').strip().lower(),
                data.get('ig_password', '')
            )
        return (None, None)

    def normalize_title(s: str) -> str:
        """
        Remove espaços nas pontas, colapsa múltiplos
        espaços internos em um só e normaliza Unicode.
        """
        collapsed = " ".join(s.split())
        return unicodedata.normalize("NFC", collapsed).casefold()

    for tentativa in range(4):
        logger.info(f"Tentativa {tentativa + 1} de 2 para localizar usuário")
        snapshot = db.reference(f'users_account_instagram/{api_key}', app=appfb).get() or {}
        if list(snapshot.keys()) == [api_key]:
            snapshot = snapshot[api_key]
            logger.info("Camada extra de api_key detectada — ajustando snapshot")
        for user_id, user_data in snapshot.items():
            try:
                ig_username, ig_password = extrair_info(user_data)
                logger.info(f"Comparando: db='{ig_username}' vs busca='{username_busca}'")
                usernm_db_ = normalize_title(ig_username)
                username_busca_ = normalize_title(username_busca)
                if usernm_db_ == username_busca_:
                    logger.info(f"Usuário encontrado na tentativa {tentativa + 1}")
                    return jsonify({'ig_username': ig_username, 'ig_password': ig_password}), 200
            except Exception as err:
                logger.info(f"Erro ao processar user_id={user_id}: {err}")
    logger.info(f"Nenhuma conta encontrada após 4 tentativas: {username_busca}")
    return jsonify({'error': "None Account"}), 500
    
@app.route('/api/cookies-account', methods=['POST'])
def user_account():
    config = request.get_json()
    api_key = config.get('api_key')
    raw_username = config.get('username_account', '')

    # Normaliza o username de busca
    username_busca = raw_username.strip().replace("  ", "").replace(" ", "").replace("\n", "").lower()
    logger.info(f"Buscando cookies para usuário normalizado: {username_busca}")

    def extrair_info(data):
        """
        Retorna tupla (username, cookies) se encontrar,
        ou (None, None) se não conseguir extrair.
        """
        if isinstance(data, dict):
            # 1) Estrutura aninhada
            primeiro_valor = next(iter(data.values()), {})
            if isinstance(primeiro_valor, dict):
                return (
                    primeiro_valor.get('username', '').strip().lower(),
                    primeiro_valor.get('AccountCookies', '')
                )
            # 2) Estrutura plana
            return (
                data.get('username', '').strip().lower(),
                data.get('AccountCookies', '')
            )
        return (None, None)

    def normalize_title(s: str) -> str:
        """
        Remove espaços nas pontas, colapsa múltiplos
        espaços internos em um só e normaliza Unicode.
        """
        # strip + colapsar espaços
        collapsed = " ".join(s.split())
        # normalização NFC
        return unicodedata.normalize("NFC", collapsed).casefold()

    # Faz até 4 tentativas completas de busca antes de retornar erro
    for tentativa in range(4):
        logger.info(f"Tentativa {tentativa + 1} de 2 para localizar usuário")
        snapshot = db.reference(f'users_account_cookies/{api_key}', app=appfb).get() or {}
        # logger.info(f"Snapshot bruto: {snapshot!r}")
        if list(snapshot.keys()) == [api_key]:
            snapshot = snapshot[api_key]
            logger.info("Camada extra de api_key detectada — ajustando snapshot")
        for user_id, user_data in snapshot.items():
            try:
                usernm_db, cookies = extrair_info(user_data)
                logger.info(f"Comparando: db='{usernm_db}' vs busca='{username_busca}'")
                usernm_db_ = normalize_title(usernm_db)
                username_busca_ = normalize_title(username_busca)
                if usernm_db_ == username_busca_:
                    logger.info(f"Usuário encontrado na tentativa {tentativa + 1}")
                    return jsonify({'AccountCookies': cookies}), 200
            except Exception as err:
                logger.info(f"Erro ao processar user_id={user_id}: {err}")
                # continua para o próximo registro

    # Se não achou após 4 tentativas
    logger.info(f"Nenhuma conta encontrada após 4 tentativas: {username_busca}")
    return jsonify({'error': "None Account"}), 500

@app.route('/api/user-config/<user_id>', methods=['PUT', 'POST'])
def upsert_user_config(user_id):
    fixx_email = user_id.replace(".", "_")
    try:
        config = request.get_json()
        if not isinstance(config, dict):
            return jsonify({'error': 'Payload inválido'}), 400

        ref = db.reference(f'user_configs/{fixx_email}', app=appfb)
        # update() faz merge: cria ou atualiza
        ref.update(config)

        return jsonify({
            'status': 'success',
            'action': 'upsert',
            'user_id': user_id,
            'config': config
        }), 200
    except Exception as e:
        logger.info(f"error{e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/user-config/<user_id>', methods=['DELETE'])
def delete_user_config(user_id):
    fixx_email = user_id.replace(".", "_")
    try:
        ref = db.reference(f'user_configs/{fixx_email}', app=appfb)
        ref.delete()
        return jsonify({
            'status': 'success',
            'action': 'delete',
            'user_id': user_id
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/login', methods=['POST'])
@limiter.limit(limit) 
def login():
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        
        # Busca todos os usuários cadastrados
        users = users_ref.get()
        if not users:
            return jsonify({'error': 'No user registered with this email'}), 404

        # Verifica se existe algum usuário com as credenciais informadas
        for key, user_data in users.items():
            if user_data.get('login') == username and user_data.get('password') == password:
                session.permanent = True
                session["user"] = username
                expire_time = user_data.get('expiration')
                api_key = user_data.get('api_key')
                return jsonify({'message': 'Login successfully', 'user': username, 'expire_time_license': expire_time, 'api_key': api_key}), 200

        # Caso não encontre, retorna erro
        return jsonify({"success": False, "message": "Invalid credentials."}), 401

    except Exception as e:
        logger.error(f"erro login {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/proxy-login', methods=['POST'])
@limiter.limit(limit) 
def proxy_login():
    try:
        data = request.get_json()
        headers = {
            "Content-Type": "application/json",
            "Api-Landingpage-API-KEY": ADMIN_API_KEY
        }
        response = requests.post(login_url, json=data, headers=headers)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        logger.error(f"Erro no servidor {e}")
        return jsonify({"error": f"Erro no servidor {e}"}), 500

@app.route("/create-checkout", methods=["POST"])
@limiter.limit(limit) 
def create_checkout():
    data = request.get_json()
    try:
        # Calcula a data de expiração: data atual + 31 dias
        expiration_time = datetime.now() + timedelta(days=31)
        plan = data["plano"]
        if plan == "studio":
            SUBSCRIPTION_PRICE_ID = os.getenv("STRIPE_SUBSCRIPTION_PRICE_ID_Studio")
        elif plan == "content creator":
            SUBSCRIPTION_PRICE_ID = os.getenv("STRIPE_SUBSCRIPTION_PRICE_ID_Content_Creator")

        session = stripe.checkout.Session.create(
            line_items=[{
                "price": SUBSCRIPTION_PRICE_ID,  # Usando o ID do preço definido no .env
                "quantity": 1
            }],
            mode="subscription",  # Modo de assinatura
            payment_method_types=["card"],
            success_url="https://mediacutsstudio.com/checkout/sucess",  # 
            cancel_url="https://mediacutsstudio.com/checkout/cancel",  # Caso o usuário cancele o pagamento
            metadata={"email": data["email"],
                      "password": data["password"],
                      "SUBSCRIPTION_PLAN": data["plano"],
                      "TIMESTAMP": expiration_time.isoformat()
                    },
        )
        print("Sessão criada:", session.id)
        return jsonify({"sessionId": session.id})
    except Exception as e:
        print("Erro ao criar a sessão de checkout:", e)
        return jsonify({"error": str(e)}), 500

@app.route('/proxy-checkout', methods=['POST'])
@limiter.limit(limit) 
def proxy_checkout():
    try:
        data = request.get_json()
        headers = {
            "Content-Type": "application/json",
            "Api-Landingpage-API-KEY": ADMIN_API_KEY
        }
        response = requests.post(createcheckout, json=data, headers=headers)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": f"Erro no servidor {e}"}), 500

# -------------------------------------------------------------------
# Endpoint Webhook Stripe
@app.route("/webhook", methods=["POST"])
def stripe_webhook():
    """
    Endpoint para tratar os webhooks enviados pela Stripe.
    """
    payload = request.data
    sig_header = request.headers.get("Stripe-Signature")
    event = None

    try:
        logger.info("event?")
        event = stripe.Webhook.construct_event(payload, sig_header, WEBHOOK_SECRET)
    except ValueError as e:
        logger.info("Payload inválido")
        return jsonify({"message": "Invalid payload"}), 400
    except stripe.error.SignatureVerificationError as e:
        logger.info("Assinatura inválida")
        return jsonify({"message": "Invalid signature"}), 400

    # Processa o evento conforme o seu tipo
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        if session.get("payment_status") == "paid":
            email_metadata = session["metadata"].get("email")
            password_metadata = session["metadata"].get("password")
            SUBSCRIPTION_PLAN = session["metadata"].get("SUBSCRIPTION_PLAN")
            TIMESTAMP = session["metadata"].get("TIMESTAMP")

            logger.info(f"Pagamento por cartão com sucesso: {SUBSCRIPTION_PLAN} {email_metadata}" )


            data = {
                "email": email_metadata,
                "password": password_metadata,
                "SUBSCRIPTION_PLAN": SUBSCRIPTION_PLAN,
                "expiration": TIMESTAMP
            }
            headers = {
                    "Content-Type": "application/json",
                    "X-API-KEY": ADMIN_API_KEY
                    }
            response = requests.post(createlogin, json=data, headers=headers)

            if response.status_code == 200:
                response_data = response.json()
                
                # Obtém cada argumento retornado pelo endpoint
                message = response_data.get("message")
                user_id = response_data.get("user_id")
                login = response_data.get("login")
                password = response_data.get("password")
                expiration = response_data.get("expiration")
                subscription_plan = response_data.get("subscription_plan")
                
                # Exibe os valores obtidos
                logger.info(f"Mensagem: {message}")
                logger.info(f"User ID: {user_id}")
                logger.info(f"Login: {login}")
                logger.info(f"Senha: {password}")
                logger.info(f"Expiração: {expiration}")
                logger.info(f"Plano de assinatura: {subscription_plan}")

                SendEmail(
                    user_email_origin=email_metadata,
                    html_attach_flag=True,
                    email_type="Sucess Upgrated Account",
                    SMTP_ADM=SMTP_USER,
                    SMTP_PASSWORD=SMTP_PASSWORD,
                    SMTP_HOST=host,
                    SMTP_PORT=port,
                    use_tls=use_tls,
                    erro_project="",
                    title_origin="",
                    new_scheduled_time=""
                )




            else:
                logger.info(f"Erro na requisição: {response.status_code}{response.text}")



        elif session.get("payment_status") == "unpaid" and session.get("payment_intent"):
            payment_intent = stripe.PaymentIntent.retrieve(session["payment_intent"])
            hosted_voucher_url = (
                payment_intent.next_action
                and payment_intent.next_action.get("boleto_display_details", {})
                .get("hosted_voucher_url")
            )
            if hosted_voucher_url:
                user_email = session.get("customer_details", {}).get("email")
                print("Gerou o boleto e o link é", hosted_voucher_url)
    
    elif event["type"] == "checkout.session.expired":
        session = event["data"]["object"]
        if session.get("payment_status") == "unpaid":
            teste_id = session["metadata"].get("testeId")
            print("Checkout expirado", teste_id)
    
    elif event["type"] == "checkout.session.async_payment_succeeded":
        session = event["data"]["object"]
        if session.get("payment_status") == "paid":
            teste_id = session["metadata"].get("testeId")
            print("Pagamento boleto confirmado", teste_id)
    
    elif event["type"] == "checkout.session.async_payment_failed":
        session = event["data"]["object"]
        if session.get("payment_status") == "unpaid":
            teste_id = session["metadata"].get("testeId")
            print("Pagamento boleto falhou", teste_id)
    
    elif event["type"] == "customer.subscription.deleted":
        print("Cliente cancelou o plano")
    
    return jsonify({"result": event, "ok": True})


def validate_api_key():
    api_key = get_api_key()
    if api_key != ADMIN_API_KEY:
        return False
    return True

def generate_api_key(subscription_plan):
    prefix_map = {
        "startup": "apikey-startup",
        "content creator": "apikey-content-creator",
        "studio": "apikey-studio"
    }
    prefix = prefix_map.get(subscription_plan.lower(), "apikey-default")
    unique_part = secrets.token_urlsafe(32)
    api_key = f"{prefix}-{unique_part}"
    return api_key

def get_api_key():
    """
    Extrai a API Key do header da requisição.
    É esperado que o header seja enviado com o nome 'X-API-KEY'
    """
    return request.headers.get('X-API-KEY')

def key_func():
    """
    Função utilizada pelo Flask-Limiter para identificar o cliente.
    Se a API Key estiver presente, utiliza-a como identificador; caso contrário,
    utiliza o endereço IP.
    """
    api_key = get_api_key()
    return api_key if api_key else get_remote_address()

def get_user_data_from_firebase(api_key, appfb):
    """
    Função que obtém os dados do usuário no Firebase Realtime Database
    a partir da chave da API, na referência 'Users_Control_Panel'.
    """
    ref = db.reference(f'Users_Control_Panel/{api_key}', app=appfb)
    user_data = ref.get()  # Obtém os dados do usuário com a chave especificada
    return user_data

def dynamic_rate_limit(appfb):
    """
    Função que determina dinamicamente o limite de requisições com base na API Key do usuário.
    Se a chave estiver cadastrada, retorna o limite configurado para o perfil do usuário.
    Caso contrário, define um limite padrão para usuários não autenticados.
    """
    api_key = get_api_key()
    if api_key:
        user_data = get_user_data_from_firebase(api_key, appfb)
        if user_data:
            return user_data.get("limit", "10 per minute")  # Retorna o limite configurado para o usuário
    # Limite para usuários sem autenticação ou com API Key inválida
    return "10 per minute"


def count_tiktok_accounts(api_key):
    """
    Conta quantas contas TikTok ativas o usuário já possui,
    lendo do nó 'users_account_cookies/{api_key}' onde platform == "Tiktok".
    """
    try:
        ref = db.reference(f'users_account_cookies/{api_key}', app=appfb)
        snapshot = ref.get() or {}
        count = 0
        for key, data in snapshot.items():
            if isinstance(data, dict) and data.get("platform", "").lower() == "tiktok" and data.get("status", "").lower() == "active":
                count += 1
        return count
    except Exception as e:
        logger.error(f"Erro ao contar contas TikTok para {api_key}: {e}")
        return 0

def count_tiktok_IG(api_key):
    """
    Conta quantas contas Instagram ativas o usuário já possui,
    lendo do nó 'users_account_cookies/{api_key}' onde platform == "Instagram".
    """
    try:
        ref = db.reference(f'users_account_cookies/{api_key}', app=appfb)
        snapshot = ref.get() or {}
        count = 0
        for key, data in snapshot.items():
            if isinstance(data, dict) and data.get("platform", "").lower() == "instagram" and data.get("status", "").lower() == "active":
                count += 1
        return count
    except Exception as e:
        logger.error(f"Erro ao contar contas TikTok para {api_key}: {e}")
        return 0

def count_monthly_schedules(api_key):
    """
    Conta quantos agendamentos de cortes o usuário já criou no mês corrente.
    Lê do nó 'user_schedules/{api_key}'.
    Espera que cada agendamento tenha o campo 'created_at' em ISO format.
    """
    try:
        ref = schedules_ref_root.child(api_key)
        snapshot = ref.get() or {}
        now = datetime.now()
        count = 0
        for key, data in snapshot.items():
            created_iso = data.get("created_at")
            if not created_iso:
                continue
            created_dt = datetime.fromisoformat(created_iso)
            if created_dt.year == now.year and created_dt.month == now.month:
                count += 1
        return count
    except Exception as e:
        logger.error(f"Erro ao contar agendamentos mensais para {api_key}: {e}")
        return 0
    
def get_user_plan(api_key):
    """
    Retorna o plano de assinatura do usuário (string) a partir do api_key.
    Se não encontrar, retorna None.
    """
    try:
        user_snapshot = users_ref.child(api_key).get()
        if user_snapshot and user_snapshot.get("subscription_plan"):
            return user_snapshot.get("subscription_plan").lower()
    except Exception as e:
        logger.error(f"Erro ao buscar plano do usuário {api_key}: {e}")
    return None

# Exemplo de rota protegida (você precisará de uma lógica de autenticação real)
def authenticate_user(req):
    # Lógica REAL de autenticação:
    # 1. Obter token do cabeçalho Authorization
    # 2. Validar token (JWT de Firebase Auth, por exemplo)
    # 3. Retornar o UID do usuário ou None se falhar
    # Por enquanto, um mock:
    mock_user_id = req.headers.get('X-User-Id') # Apenas para teste, NÃO USE EM PRODUÇÃO
    return mock_user_id



def get_video_title_scrape(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    headers = {
        'Accept-Language': 'pt-BR,pt;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    resp = requests.get(url, headers=headers, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')
    tag = soup.find('meta', property='og:title')
    if tag and tag.get('content'):
        return tag['content']
    tag = soup.find('meta', attrs={'name': 'title'})
    if tag and tag.get('content'):
        return tag['content']

    return "Desconhecido"














# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=5000)
