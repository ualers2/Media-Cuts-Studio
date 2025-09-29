# Internal-server\api.py
import os
from flask import Flask, request, jsonify, redirect, url_for, session
from werkzeug.utils import secure_filename
from datetime import datetime, timezone, timedelta
from dateutil.parser import isoparse  # ADICIONE ESSA IMPORTAÇÃO
import pytz 
import logging
from firebase_admin import db
import pickle
import requests
import json
import multiprocessing
from google_auth_oauthlib.flow import Flow
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.exceptions import RefreshError
from oauthlib.oauth2.rfc6749.errors import InsecureTransportError # Import the specific error for clarity
from flask_cors import CORS
from flask_session import Session
from dotenv import load_dotenv, find_dotenv
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process
import threading

from firebase_admin import initialize_app, credentials, storage, get_app

import uuid
import tempfile
from werkzeug.datastructures import FileStorage
import io
from asgiref.wsgi import WsgiToAsgi

import time
from dotenv import load_dotenv
import os
import logging
import uuid
import json
from flask_limiter.util import get_remote_address
from werkzeug.formparser import parse_form_data
from werkzeug.utils import secure_filename 
import re
import shutil
import hashlib, time, requests


from Modules.download_ import download_
from Modules.upload_ import upload_
from Modules.config import Config
from celery_worker import celery_app, upload_short_task, upload_tiktok_task, upload_tiktok_and_shorts_task

diretorio_script = os.path.dirname(os.path.abspath(__file__)) 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
os.makedirs(os.path.join(diretorio_script, 'Logs'), exist_ok=True)
file_handler = logging.FileHandler(os.path.join(diretorio_script, 'Logs', 'api.log'))
file_handler.setFormatter(formatter)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)


load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "Keys", "keys.env"))

cred = credentials.Certificate(os.getenv('DATABASEPATH'))
app1 = initialize_app(cred, {
    'databaseURL': os.getenv('DATABASEURL')
}, name="app1")


cred = credentials.Certificate(os.getenv('DATABASEPATHSHEDULER'))
appsheduler = initialize_app(cred, {
    'databaseURL': os.getenv('DATABASEURLSHEDULER')
}, name="appsheduler")

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
asgi_app = WsgiToAsgi(app)
app.config.from_object(Config)
app.config.update(
    SESSION_COOKIE_SAMESITE="None",
    SESSION_COOKIE_SECURE=True
)
app.secret_key = 'uma_chave_muito_secreta'
# app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024 * 1024  # 10 GB
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


shorts_ref = db.reference("shorts", app=appsheduler)
if not os.path.exists(Config.UPLOAD_FOLDER):
    os.makedirs(Config.UPLOAD_FOLDER)

CLIENT_SECRETS_FILE = os.path.join(os.path.dirname(__file__), "Keys", "client_secret_1.json")
redirect_uri = "https://api.sheduler.mediacutsstudio.com/oauth2callback"
redirect_base = "https://mediacutsstudio.com/new-post"
SCOPES = ["https://www.googleapis.com/auth/youtube.upload", "https://www.googleapis.com/auth/youtube.readonly"]
TOKEN_DIR = os.path.join(os.path.dirname(__file__), "Tokens") 
USER_ID_FOR_TEST = os.getenv("USER_ID_FOR_TEST")
UPLOAD_URL = os.getenv("UPLOAD_URL_VIDEOMANAGER")
os.makedirs(TOKEN_DIR, exist_ok=True)

if os.getenv("PRODUCTION_ENV") == "False":
    CORS(app, resources={r"/*": {"origins": "*"}}, origins=[
        "https://mediacutsstudio.com",
        "https://www.mediacutsstudio.com",
        "https://dev.mediacutsstudio.com",
        "https://b0fa7d68e312.ngrok-free.app",
        "https://4e799f508794.ngrok-free.app",
        "http://localhost:3001",
        "http://localhost:4343",
        "*"
    ])
    redirect_uri = "https://b0fa7d68e312.ngrok-free.app/oauth2callback"
    redirect_base = "http://localhost:4343/new-post"

@app.route('/')
def index():
    return "Servidor de Agendamentos de Shorts está funcionando! Para autorizar o YouTube, acesse <a href='/authorize'>este link</a>."

# Endpoint para agendar um post
@app.route('/api/posts/agendar', methods=['POST'])
def schedule_post():
    # Verifica se há um arquivo na requisição
    if 'video_file' not in request.files:
        return jsonify({"error": "Nenhum arquivo de vídeo fornecido."}), 400

    video_file = request.files['video_file']
    if video_file.filename == '':
        return jsonify({"error": "Nome de arquivo de vídeo vazio."}), 400

    # Obtém outros dados do formulário
    title = request.form.get('title')
    description = request.form.get('description')
    category_id = request.form.get('category_id', '22')
    video_tags_str = request.form.get('video_tags', '')
    video_tags = [tag.strip() for tag in video_tags_str.split(',') if tag.strip()]
    privacy_status = request.form.get('privacy_status', 'private')
    post_social_networks = request.form.get('socialNetworks', ['youtube'])
    logger.info(f"post_social_networks? {post_social_networks}")
    scheduled_publish_at_str = request.form.get('scheduled_publish_at')

    # ==== YouTube + TikTok ====
    if 'youtube' in post_social_networks and 'tiktok' in post_social_networks:
        canal_id_tiktok = request.form.get('canal_id_tiktok')
        canal_id = request.form.get('canal_id')
        logger.info(f"canal_id_tiktok {canal_id_tiktok}")
        logger.info(f"canal_id {canal_id}")

        canal_data_tiktok = db.reference(f"canais/{canal_id_tiktok}", app=appsheduler).get()
        if not canal_data_tiktok:
            return jsonify({"error": f"Canal com ID {canal_id_tiktok} não encontrado."}), 404
        
        canal_data_youtube = db.reference(f"canais/{canal_id}", app=appsheduler).get()
        if not canal_data_youtube:
            return jsonify({"error": f"Canal com ID {canal_id} não encontrado."}), 404
        
        filename = secure_filename(video_file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        try:
            video_file.save(file_path)
        except Exception as e:
            return jsonify({"error": f"Erro ao salvar o arquivo: {str(e)}"}), 500
        local_tz = pytz.timezone('America/Sao_Paulo') 
        scheduled_publish_at = local_tz.localize(datetime.strptime(scheduled_publish_at_str, '%Y-%m-%d %H:%M:%S'))
        
        try:
            tiktok_data_to_save = {
                'id': '',
                'status': 'scheduled',  
                'socialNetworks': post_social_networks,
                'canal_id_tiktok': canal_id_tiktok,
                'canal_id': canal_id,
                'caminho_arquivo': file_path,
                'title': title,
                'description': description,
                'tags': video_tags,
                'category_id': category_id,
                'visibility': privacy_status,
                'scheduledAt': scheduled_publish_at.isoformat() if scheduled_publish_at else None,
                'createdAt': datetime.now(local_tz).isoformat(),
                'data_upload_real': None,
                'youtube_video_id': None,
                'youtube_url': None,
                'erro_mensagem': None
            }
            new_short_ref = shorts_ref.push(tiktok_data_to_save)
            post_id = new_short_ref.key
            new_short_ref.update({'id': post_id})
            tiktok_data_to_save['id'] = post_id
            post_data_celery = {
                'post_id': post_id,
            }

            logger.info(f"⏳ Agendando upload T+Y para post {post_id}")
            upload_tiktok_and_shorts_task.apply_async(
                args=[post_data_celery],
                eta=scheduled_publish_at,
                queue='posts_queue' 
            )
            logger.info("Posts agendado com sucesso! O upload será processado em segundo plano.")
            return jsonify({
                "message": "Posts agendado com sucesso! O upload será processado em segundo plano.",
                # "short_id": "none",
                "status": tiktok_data_to_save['status']
            }), 202 # 202 Accepted - a requisição foi aceita para processamento

        except Exception as e:
            # Se ocorrer um erro, tente remover o arquivo salvo temporariamente
            if os.path.exists(file_path):
                os.remove(file_path)
            return jsonify({"error": f"Erro ao agendar o Short: {str(e)}"}), 500

    # ==== Somente YouTube ====
    elif 'youtube' in post_social_networks and 'tiktok' not in post_social_networks:
        canal_id = request.form.get('canal_id')

        if not canal_id:
            return jsonify({"error": "ID do canal é obrigatório."}), 400

        # Valida se o canal existe diretamente no DB
        canal_data = db.reference(f"canais/{canal_id}", app=appsheduler).get()
        if not canal_data:
            return jsonify({"error": f"Canal com ID {canal_id} não encontrado."}), 404

        # Salva o arquivo temporariamente
        filename = secure_filename(video_file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        try:
            video_file.save(file_path)
        except Exception as e:
            return jsonify({"error": f"Erro ao salvar o arquivo: {str(e)}"}), 500

        # Converte a string de data/hora para objeto datetime consciente do fuso horário
        local_tz = pytz.timezone('America/Sao_Paulo') # Defina o fuso horário padrão aqui
        scheduled_publish_at = local_tz.localize(datetime.strptime(scheduled_publish_at_str, '%Y-%m-%d %H:%M:%S'))
            
        try:

            # Cria o registro do Short no Firebase diretamente
            short_data_to_save = {
                'status': 'scheduled',  
                'socialNetworks': post_social_networks,
                'canal_id': canal_id,
                'caminho_arquivo': file_path,
                'title': title,
                'description': description,
                'tags': video_tags,
                'category_id': category_id,
                'visibility': privacy_status,
                'scheduledAt': scheduled_publish_at.isoformat() if scheduled_publish_at else None,
                'createdAt': datetime.now(local_tz).isoformat(),
                'data_upload_real': None,
                'youtube_video_id': None,
                'youtube_url': None,
                'erro_mensagem': None
            }

            new_short_ref = shorts_ref.push(short_data_to_save)
            short_id = new_short_ref.key
            
            new_short_ref.update({'id': short_id})
            short_data_to_save['id'] = short_id # Adiciona o ID ao dicionário retornado
            short_data_celery = {
                'short_id': short_id,
            }

            # lock_file = os.path.join(app.config['UPLOAD_FOLDER'], f".lock_{filename}")
            # if os.path.exists(lock_file):
            #     logger.warning(f"Tarefa para {filename} já agendada. Ignorando duplicata.")
            #     return jsonify({"message": "Já agendado"}), 200
            # open(lock_file, 'w').close()
            logger.info(f"⏳ Agendando upload Y para post {short_id}")
            upload_short_task.apply_async(
                args=[short_data_celery],
                eta=scheduled_publish_at,
                queue='posts_queue' 
            )
            logger.info("Shorts agendado com sucesso! O upload será processado em segundo plano.")
            return jsonify({
                "message": "Shorts agendado com sucesso! O upload será processado em segundo plano.",
                # "short_id": "none",
                "status": short_data_to_save['status']
            }), 202 # 202 Accepted - a requisição foi aceita para processamento

        except Exception as e:
            # Se ocorrer um erro, tente remover o arquivo salvo temporariamente
            if os.path.exists(file_path):
                os.remove(file_path)
            return jsonify({"error": f"Erro ao agendar o Short: {str(e)}"}), 500

    # ==== Somente TikTok ====    
    elif 'tiktok' in post_social_networks and 'youtube' not in post_social_networks:
        canal_id = request.form.get('canal_id_tiktok')

        if not canal_id:
            return jsonify({"error": "ID do canal é obrigatório."}), 400

        # Valida se o canal existe diretamente no DB
        canal_data = db.reference(f"canais/{canal_id}", app=appsheduler).get()
        if not canal_data:
            return jsonify({"error": f"Canal com ID {canal_id} não encontrado."}), 404

        # Salva o arquivo temporariamente
        filename = secure_filename(video_file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        try:
            video_file.save(file_path)
        except Exception as e:
            return jsonify({"error": f"Erro ao salvar o arquivo: {str(e)}"}), 500

        # Converte a string de data/hora para objeto datetime consciente do fuso horário
        local_tz = pytz.timezone('America/Sao_Paulo') # Defina o fuso horário padrão aqui
        scheduled_publish_at = local_tz.localize(datetime.strptime(scheduled_publish_at_str, '%Y-%m-%d %H:%M:%S'))
            
        try:

            # Cria o registro do Tiktok no Firebase diretamente
            tiktok_data_to_save = {
                'status': 'scheduled',  
                'socialNetworks': post_social_networks,
                'canal_id': canal_id,
                'caminho_arquivo': file_path,
                'title': title,
                'description': description,
                'tags': video_tags,
                'category_id': category_id,
                'visibility': privacy_status,
                'scheduledAt': scheduled_publish_at.isoformat() if scheduled_publish_at else None,
                'createdAt': datetime.now(local_tz).isoformat(),
                'data_upload_real': None,
                'youtube_video_id': None,
                'youtube_url': None,
                'erro_mensagem': None
            }

            new_short_ref = shorts_ref.push(tiktok_data_to_save)
            tiktok_id = new_short_ref.key
            
            new_short_ref.update({'id': tiktok_id})
            tiktok_data_to_save['id'] = tiktok_id # Adiciona o ID ao dicionário retornado
            tiktok_data_celery = {
                'tiktok_id': tiktok_id,
            }

            # lock_file = os.path.join(app.config['UPLOAD_FOLDER'], f".lock_{filename}")
            # if os.path.exists(lock_file):
            #     logger.warning(f"Tarefa para {filename} já agendada. Ignorando duplicata.")
            #     return jsonify({"message": "Já agendado"}), 200
            # open(lock_file, 'w').close()
            logger.info(f"⏳ Agendando upload T para post {tiktok_id}")
            upload_tiktok_task.apply_async(
                args=[tiktok_data_celery],
                eta=scheduled_publish_at,
                queue='posts_queue' 
            )
            logger.info("Tiktok agendado com sucesso! O upload será processado em segundo plano.")            
            return jsonify({
                "message": "Tiktok agendado com sucesso! O upload será processado em segundo plano.",
                # "short_id": "none",
                "status": tiktok_data_to_save['status']
            }), 202 # 202 Accepted - a requisição foi aceita para processamento

        except Exception as e:
            # Se ocorrer um erro, tente remover o arquivo salvo temporariamente
            if os.path.exists(file_path):
                os.remove(file_path)
            return jsonify({"error": f"Erro ao agendar o Short: {str(e)}"}), 500



@app.route('/api/upload-media-bulk', methods=['POST'])
def upload_media_bulk():
    """Upload múltiplos arquivos usando upload_() e stream direto do request"""
    logger.info("Upload media_bulk iniciado")

    batch_id = hashlib.sha256(str(time.time()).encode()).hexdigest()[:16].replace(".", "")
    logger.info(f"batch_id {batch_id}")

    try:
        stream, form, files = parse_form_data(request.environ)
        logger.info("parse_form_data sucess")

        if not files or 'files[]' not in files:
            return jsonify({"error": "Nenhum arquivo enviado. Esperado 'files[]'."}), 400
        
        files_list = files.getlist('files[]')
        if not files_list:
            return jsonify({"error": "Nenhum arquivo válido na requisição."}), 400

        files_response = []
        logger.info(f"(ID: {batch_id})")

        for i, file_storage in enumerate(files_list):
            if not file_storage.filename:
                continue

            safe_name = secure_filename(file_storage.filename)
            logger.info(f"processamento {i+1}/{len(files_list)} arquivos: {safe_name}")

            # em vez de salvar em disco, passamos o stream diretamente para upload_()
            token_id = upload_(
                name_project=batch_id,
                VIDEO_FILE_PATH={"fileobj": file_storage.stream, "filename": safe_name},
                USER_ID_FOR_TEST="freitasalexandre810@gmail.com",
                type_project="files"
            )

            files_response.append({
                "original_filename": file_storage.filename,
                "safe_filename": safe_name,
                "token_id": token_id,
                "batch_id": batch_id,
                "mimetype": file_storage.mimetype or 'application/octet-stream'
            })

        logger.info(f"{len(files_response)} arquivos recebidos e processados via stream!")

        response_data = {
            "message": f"{len(files_response)} arquivos recebidos e processados via stream!",
            "status": "processing",
            "check_status_url": f"/api/upload-status/{batch_id}",
            "files": files_response
        }
        
        return jsonify(response_data), 202

    except Exception as e:
        logger.error(f"Erro processando upload bulk: {e}", exc_info=True)
        return jsonify({"error": f"Erro processando arquivos: {str(e)}"}), 500



@app.route('/api/process-bulk-posts', methods=['POST'])
def process_bulk_posts():
    """
    Endpoint para receber o JSON de metadados de agendamento em massa.
    Agora compatível com YouTube, TikTok e ambos (seguindo a lógica de /api/posts/agendar).
    """
    try:
        bulk_posts_data = request.json
    except Exception as e:
        return jsonify({"error": f"Formato JSON inválido: {str(e)}"}), 400

    if not isinstance(bulk_posts_data, list):
        return jsonify({"error": "O corpo da requisição deve ser um array JSON."}), 400

    if not bulk_posts_data:
        return jsonify({"message": "Nenhum post para processar."}), 200

    batch_id = str(uuid.uuid4())
    posts_processed_count = 0
    errors = []

    local_tz = pytz.timezone('America/Sao_Paulo')

    for post_item in bulk_posts_data:
        try:
            title = post_item.get('title', 'Post sem título')
            description = post_item.get('description', '')
            tags_str = post_item.get('tags', '')
            tags = [tag.strip() for tag in tags_str.split(',') if tag.strip()]
            social_networks = post_item.get('social_networks', ['youtube'])
            visibility = post_item.get('visibility', 'private')
            category_id = post_item.get('category_id', '24')
            media_filename = post_item.get('filename')
            token_id = post_item.get('token_id')
            batch_id = post_item.get('batch_id')
            filename = secure_filename(media_filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            download_(
                UPLOAD_URL=UPLOAD_URL, 
                save_path=file_path, 
                PROJECT_NAME=batch_id, 
                VIDEO_ID=token_id, 
                USER_ID_FOR_TEST="freitasalexandre810@gmail_com"
            )

            scheduled_at_str = post_item.get('schedule_time')
            scheduled_publish_at = local_tz.localize(datetime.strptime(scheduled_at_str, '%Y-%m-%d %H:%M:%S'))

            canal_id_youtube = post_item.get('canal_id')
            canal_id_tiktok = post_item.get('canal_id_tiktok')

            # ==== YouTube + TikTok ====
            if 'youtube' in social_networks and 'tiktok' in social_networks:
                canal_data_tiktok = db.reference(f"canais/{canal_id_tiktok}", app=appsheduler).get()
                canal_data_youtube = db.reference(f"canais/{canal_id_youtube}", app=appsheduler).get()
                if not canal_data_tiktok or not canal_data_youtube:
                    raise Exception("Canal TikTok ou YouTube não encontrado.")

                data_to_save = {
                    'id': '',
                    'status': 'scheduled',
                    'bulkUploadBatchId': batch_id,
                    'socialNetworks': social_networks,
                    'canal_id_tiktok': canal_id_tiktok,
                    'canal_id': canal_id_youtube,
                    'caminho_arquivo': file_path,
                    'title': title,
                    'description': description,
                    'tags': tags,
                    'category_id': category_id,
                    'visibility': visibility,
                    'scheduledAt': scheduled_publish_at.isoformat(),
                    'createdAt': datetime.now(local_tz).isoformat(),
                    'data_upload_real': None,
                    'youtube_video_id': None,
                    'youtube_url': None,
                    'erro_mensagem': None
                }

                new_ref = shorts_ref.push(data_to_save)
                post_id = new_ref.key
                new_ref.update({'id': post_id})
                data_to_save['id'] = post_id

                upload_tiktok_and_shorts_task.apply_async(
                    args=[{'post_id': post_id}],
                    eta=scheduled_publish_at,
                    queue='posts_queue'
                )

            # ==== Somente YouTube ====
            elif 'youtube' in social_networks and 'tiktok' not in social_networks:
                canal_data_youtube = db.reference(f"canais/{canal_id_youtube}", app=appsheduler).get()
                if not canal_data_youtube:
                    raise Exception("Canal YouTube não encontrado.")

                data_to_save = {
                    'status': 'scheduled',
                    'bulkUploadBatchId': batch_id,
                    'socialNetworks': social_networks,
                    'canal_id': canal_id_youtube,
                    'caminho_arquivo': file_path,
                    'title': title,
                    'description': description,
                    'tags': tags,
                    'category_id': category_id,
                    'visibility': visibility,
                    'scheduledAt': scheduled_publish_at.isoformat(),
                    'createdAt': datetime.now(local_tz).isoformat(),
                    'data_upload_real': None,
                    'youtube_video_id': None,
                    'youtube_url': None,
                    'erro_mensagem': None
                }

                new_ref = shorts_ref.push(data_to_save)
                short_id = new_ref.key
                new_ref.update({'id': short_id})

                upload_short_task.apply_async(
                    args=[{'short_id': short_id}],
                    eta=scheduled_publish_at,
                    queue='posts_queue'
                )

            # ==== Somente TikTok ====
            elif 'tiktok' in social_networks and 'youtube' not in social_networks:
                canal_data_tiktok = db.reference(f"canais/{canal_id_tiktok}", app=appsheduler).get()
                if not canal_data_tiktok:
                    raise Exception("Canal TikTok não encontrado.")

                data_to_save = {
                    'status': 'scheduled',
                    'bulkUploadBatchId': batch_id,
                    'socialNetworks': social_networks,
                    'canal_id': canal_id_tiktok,
                    'caminho_arquivo': file_path,
                    'title': title,
                    'description': description,
                    'tags': tags,
                    'category_id': category_id,
                    'visibility': visibility,
                    'scheduledAt': scheduled_publish_at.isoformat(),
                    'createdAt': datetime.now(local_tz).isoformat(),
                    'data_upload_real': None,
                    'youtube_video_id': None,
                    'youtube_url': None,
                    'erro_mensagem': None
                }

                new_ref = shorts_ref.push(data_to_save)
                tiktok_id = new_ref.key
                new_ref.update({'id': tiktok_id})

                upload_tiktok_task.apply_async(
                    args=[{'tiktok_id': tiktok_id}],
                    eta=scheduled_publish_at,
                    queue='posts_queue'
                )

            posts_processed_count += 1

        except Exception as e:
            error_msg = f"Erro ao processar post '{post_item.get('title', 'sem título')}': {str(e)}"
            logger.error(error_msg, exc_info=True)
            errors.append({"post_data": post_item, "error": error_msg})

    return jsonify({
        "message": f"{posts_processed_count} posts recebidos para agendamento em massa.",
        "batchId": batch_id,
        "processedCount": posts_processed_count,
        "errors": errors,
        "status": "Accepted for processing"
    }), 202


@app.route('/authenticate-google')
def authenticate_google():
    """
    Inicia o fluxo OAuth do Google usando canal_id como identificador.
    """
    # 1) Lê canal_id da query string
    canal_id = request.args.get('canal_id')
    if not canal_id:
        return jsonify({"error": "canal_id é obrigatório na query string."}), 400
    session['canal_id'] = canal_id

    # 2) Monta o Flow
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri=redirect_uri
    )
    authorization_url, state = flow.authorization_url(
        prompt='consent',
        access_type='offline',
        include_granted_scopes='true'
    )
    session['oauth_state'] = state

    # 3) Redireciona para autorização Google
    return redirect(authorization_url)

@app.route('/oauth2callback')
def oauth2callback():
    """
    Callback do Google: troca código por tokens, salva em disco
    e atualiza token_path no Firebase usando canal_id.
    """
    # 1) Valida estado CSRF
    state = request.args.get('state')
    if 'oauth_state' not in session or session['oauth_state'] != state:
        session.pop('oauth_state', None)
        session.pop('canal_id', None)
        return jsonify({"error": "State mismatch ou ausente."}), 400

    # 2) Recupera canal_id
    canal_id = session.get('canal_id')
    if not canal_id:
        session.pop('oauth_state', None)
        return jsonify({"error": "canal_id ausente da sessão."}), 400

    # 3) Recria o Flow e troca token
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri=redirect_uri
    )
    try:
        flow.fetch_token(authorization_response=request.url)
        credentials = flow.credentials
        canal_id_str = f"{canal_id}"
        canal_id_replace = canal_id_str.replace(".", "_").replace(" ", "-")
        token_file = os.path.join(TOKEN_DIR, f"token_{canal_id_replace}.pickle")
        with open(token_file, "wb") as f:
            pickle.dump(credentials, f)

        TOKEN_ID = upload_(canal_id_replace, token_file, "freitasalexandre810@gmail.com")
        logger.info(f"TOKEN_ID {TOKEN_ID}")

        # 5) Atualiza apenas o token_path no Firebase
        canais_ref = db.reference("canais", app=appsheduler).child(canal_id_replace)
        canais_ref.update({
            "id": canal_id_replace,
            "nome": canal_id,
            'TOKEN_ID': TOKEN_ID,
            'socialNetwork': 'youtube',
            'scopes': SCOPES,
            'data_criacao': datetime.now(pytz.utc).isoformat()

        })

        # 6) Limpa sessão
        session.pop('oauth_state', None)
        session.pop('canal_id', None)

        # 7) Redireciona com sucesso
        return redirect(f"{redirect_base}?auth_success=true")

    except Exception as e:
        logger.error(f"Erro ao trocar token: {e}")
        session.pop('oauth_state', None)
        session.pop('canal_id', None)
        return redirect(
            f"{redirect_base}?"
            "auth_success=false&error=auth_failed"
        )

@app.route('/check-auth-status/<user_id>')
def check_auth_status(user_id):
    """
    Endpoint para o frontend verificar o status de autenticação de um usuário.
    """
    credentials = get_or_create_credentials(user_id)
    if credentials:
        return jsonify({"authenticated": True, "message": "Conta autenticada."})
    else:
        return jsonify({"authenticated": False, "message": "Conta não autenticada ou token expirado/revogado."})

@app.route('/api/canais', methods=['POST'])
def create_canal():
    nome = request.json.get('nome')
    socialNetwork = request.json.get('socialNetwork')

    if socialNetwork == "youtube":
        token_path = request.json.get('token_path')

        canal_id_str = f"{nome}"
        canal_id_replace = canal_id_str.replace(".", "_").replace(" ", "-")

        TOKEN_ID = upload_(canal_id_replace, token_path, "freitasalexandre810@gmail.com")
        logger.info(f"TOKEN_ID {TOKEN_ID}")
        if not all([nome, token_path]):
            return jsonify({"error": "Todos os campos (nome,  token_path, scopes) são obrigatórios."}), 400

        # 5) Atualiza apenas o token_path no Firebase
        canais_ref = db.reference("canais", app=appsheduler).child(canal_id_replace)
        canais_ref.update({
            'id': canal_id_replace,
            'nome': nome,
            'TOKEN_ID': TOKEN_ID,
            'socialNetwork': socialNetwork,
            'scopes': SCOPES,
            'data_criacao': datetime.now(pytz.utc).isoformat()

        })
        canal_id = canal_id_replace
        new_canal_ref.update({'id': canal_id}) # Salva o ID dentro do próprio nó
        canal_data_to_save['id'] = canal_id # Adiciona o ID ao dicionário retornado

        return jsonify({
            "message": "Canal criado com sucesso!",
            "canal_id": canal_id,
            "canal_data": canal_data_to_save
        }), 201

    if socialNetwork == "tiktok":
        canal_id_str = f"{nome}"
        canal_id_replace = canal_id_str.replace(".", "_").replace(" ", "-")
        token_content = request.json.get('token_content')
        token_file = os.path.join(TOKEN_DIR, f"{canal_id_replace}.json")
        with open(token_file, "w", encoding="utf-8") as f:
            json.dump(token_content, f, ensure_ascii=False, indent=2)

        TOKEN_ID = upload_(canal_id_replace, token_file, "freitasalexandre810@gmail.com")
        logger.info(f"TOKEN_ID {TOKEN_ID}")

        canal_data_to_save = {
            'nome': nome,
            'TOKEN_ID': TOKEN_ID,
            'socialNetwork': socialNetwork,
            'data_criacao': datetime.now(pytz.utc).isoformat()
        }
        
        canais_ref = db.reference("canais", app=appsheduler)
        new_canal_ref = canais_ref.push(canal_data_to_save)
        canal_id = new_canal_ref.key
        new_canal_ref.update({'id': canal_id}) # Salva o ID dentro do próprio nó
        canal_data_to_save['id'] = canal_id # Adiciona o ID ao dicionário retornado

        return jsonify({
            "message": "Canal criado com sucesso!",
            "canal_id": canal_id,
            "canal_data": canal_data_to_save
        }), 201

@app.route('/api/canais', methods=['GET'])
def get_all_canais():
    try:
        canais_data = db.reference("canais", app=appsheduler).get()
        if not canais_data:
            logger.info("get_all_canais: nenhum canal encontrado (canais node vazio)")
            return jsonify([]), 200

        canais_list = []
        # Se já for lista
        if isinstance(canais_data, list):
            canais_list = canais_data
        # Se vier como dict (ex: Firebase Realtime DB): { key: { ... }, ... }
        elif isinstance(canais_data, dict):
            for key, data in canais_data.items():
                item = data or {}
                # Normaliza campos mínimos
                item_id = item.get('id') or key
                item_nome = item.get('nome') or item.get('name') or ''
                social_raw = (item.get('socialNetwork') or item.get('social_network') or '').lower()
                social = 'tiktok' if 'tiktok' in social_raw else ('youtube' if 'youtube' in social_raw else social_raw)
                canais_list.append({
                    **item,
                    'id': item_id,
                    'nome': item_nome,
                    'socialNetwork': social
                })
        else:
            logger.warning("get_all_canais: formato inesperado retornado pelo DB", extra={"data": str(type(canais_data))})
            return jsonify([]), 200

        logger.info(f"get_all_canais: retornando {len(canais_list)} canais")
        return jsonify(canais_list), 200
    except Exception as e:
        logger.exception("Erro em get_all_canais")
        return jsonify([]), 500
    
@app.route('/api/canais/<string:canal_id>', methods=['GET'])
def get_canal_details(canal_id):
    canal_data = db.reference(f"canais/{canal_id}", app=appsheduler).get()
    if not canal_data:
        return jsonify({"error": "Canal não encontrado."}), 404
    canal_data['id'] = canal_id # Adiciona o ID ao objeto retornado
    return jsonify(canal_data), 200

@app.route('/api/shorts', methods=['GET'])
def get_all_shorts():
    shorts_data = db.reference("shorts", app=appsheduler).get()
    if not shorts_data:
        return jsonify({}), 200 # Retorna um objeto vazio se não houver shorts
    
    # Converte o dicionário de dicionários para uma lista de dicionários
    shorts_list = [{**data, 'id': key} for key, data in shorts_data.items()]
    return jsonify(shorts_list), 200

@app.route('/api/shorts/<string:short_id>', methods=['GET'])
def get_short_details(short_id):
    short_data = db.reference(f"shorts/{short_id}", app=appsheduler).get()
    if not short_data:
        return jsonify({"error": "Short não encontrado."}), 404
    short_data['id'] = short_id # Adiciona o ID ao objeto retornado
    return jsonify(short_data), 200

@app.route('/api/shorts/<string:short_id>/cancelar', methods=['PUT'])
def cancel_short(short_id):
    short_ref = db.reference(f"shorts/{short_id}", app=appsheduler)
    short_data = short_ref.get()
    if not short_data:
        return jsonify({"error": "Short não encontrado."}), 404

    if short_data['status'] == 'CONCLUIDO':
        return jsonify({"message": "Não é possível cancelar um Short já concluído."}), 400

    # Atualiza o status para CANCELADO
    short_ref.update({'status': 'CANCELADO', 'erro_mensagem': 'Agendamento cancelado pelo usuário.'})

    return jsonify({"message": f"Short {short_id} cancelado com sucesso."}), 200

@app.route('/api/posts', methods=['GET'])
def list_posts():
    # current_user_id = get_current_user_id() # REMOVIDO: Autenticação
    
    # Get query parameters
    search_query = request.args.get('searchQuery', '').lower()
    status_filter = request.args.get('status', 'all')
    social_network_filter = request.args.get('socialNetwork', 'all')
    sort_by = request.args.get('sortBy', 'createdAt')
    sort_order = request.args.get('sortOrder', 'desc')
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))

    all_posts = shorts_ref.get()
    if not all_posts:
        return jsonify({"posts": [], "totalPosts": 0, "totalPages": 0, "currentPage": page}), 200
    # logger.info(f"all_posts{all_posts}")
    filtered_posts = []
    for post_id, post_data in all_posts.items():
        # REMOVIDO: A verificação de pertencimento ao usuário
        # if post_data.get('userId') != current_user_id:
        #     continue
        
        # Apply searchQuery filter (case-insensitive on title and description)
        if search_query and \
           search_query not in post_data.get('title', '').lower() and \
           search_query not in post_data.get('description', '').lower():
            continue

        # Apply status filter
        if status_filter != 'all' and post_data.get('status') != status_filter:
            continue

        # Apply socialNetwork filter
        if social_network_filter != 'all':
            post_social_networks = post_data.get('socialNetworks', [])
            if social_network_filter not in post_social_networks:
                continue
        
        # Add ID to post data
        post_data['id'] = post_id
        filtered_posts.append(post_data)

    # Sort the filtered posts

    def get_sort_key(post):
        value = post.get(sort_by, '')
        try:
            return isoparse(value).astimezone(timezone.utc)  # Converte tudo para UTC
        except Exception:
            return datetime.min.replace(tzinfo=timezone.utc)  # Também com timezone!

    filtered_posts.sort(key=get_sort_key, reverse=(sort_order == 'desc'))

    # Paginate the results
    total_posts = len(filtered_posts)
    start_index = (page - 1) * limit
    end_index = start_index + limit
    paginated_posts = filtered_posts[start_index:end_index]
    total_pages = (total_posts + limit - 1) // limit

    return jsonify({
        "posts": paginated_posts,
        "totalPosts": total_posts,
        "totalPages": total_pages,
        "currentPage": page
    }), 200

@app.route('/api/posts/<string:post_id>', methods=['GET'])
def get_post_by_id(post_id):
    post_data = shorts_ref.child(post_id).get()

    if not post_data:
        return jsonify({"error": "Post não encontrado."}), 404
    
    # REMOVIDO: A verificação de autorização
    # if post_data.get('userId') != current_user_id:
    #     return jsonify({"error": "Não autorizado a visualizar este post."}), 403 # Forbidden

    post_data['id'] = post_id
    return jsonify(post_data), 200

@app.route('/api/posts/<string:post_id>', methods=['PATCH'])
def update_post(post_id):
    # current_user_id = get_current_user_id() # REMOVIDO: Autenticação
    data = request.json
    
    post_ref = shorts_ref.child(post_id)
    existing_post = post_ref.get()

    if not existing_post:
        return jsonify({"error": "Post não encontrado."}), 404
    
    # REMOVIDO: A verificação de autorização
    # if existing_post.get('userId') != current_user_id:
    #     return jsonify({"error": "Não autorizado a editar este post."}), 403 # Forbidden

    # Update only provided fields
    updated_fields = {}
    for key, value in data.items():
        if key == 'scheduledAt':
            try:
                # Convert to UTC before storing (MANTIDO)
                scheduled_at_dt = datetime.fromisoformat(value)
                if scheduled_at_dt.tzinfo is None:
                    local_tz = pytz.timezone('America/Sao_Paulo')
                    scheduled_at_dt = local_tz.localize(scheduled_at_dt).astimezone(pytz.utc)
                else:
                    scheduled_at_dt = scheduled_at_dt.astimezone(pytz.utc)
                updated_fields[key] = scheduled_at_dt.isoformat()
            except ValueError:
                # Se o formato for inválido, mantém a string original ou define como None
                updated_fields[key] = value # Ou None
        else:
            updated_fields[key] = value
    
    updated_fields['updatedAt'] = datetime.now(pytz.utc).isoformat() # Update timestamp

    post_ref.update(updated_fields)
    
    # Fetch the updated post to return the complete object
    updated_post_data = post_ref.get()
    updated_post_data['id'] = post_id
    return jsonify(updated_post_data), 200

@app.route('/api/posts/<string:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post_ref = shorts_ref.child(post_id)
    existing_post = post_ref.get()

    if not existing_post:
        return jsonify({"error": "Post não encontrado."}), 404
    
    # REMOVIDO: A verificação de autorização
    # if existing_post.get('userId') != current_user_id:
    #     return jsonify({"error": "Não autorizado a excluir este post."}), 403 # Forbidden

    post_ref.delete()
    return '', 204 # No Content

def get_or_create_credentials(user_id):
    """
    Carrega credenciais existentes para um user_id específico ou inicia o fluxo OAuth.
    Retorna as credenciais ou None se o fluxo precisar ser iniciado.
    """
    token_file = os.path.join(TOKEN_DIR, f"token_{user_id}.pickle")
    credentials = None

    if os.path.exists(token_file):
        with open(token_file, "rb") as token:
            credentials = pickle.load(token)

    if credentials and credentials.valid:
        return credentials
    
    if credentials and credentials.expired and credentials.refresh_token:
        try:
            credentials.refresh(Request())
            with open(token_file, "wb") as token:
                pickle.dump(credentials, token)
            return credentials
        except Exception as e:
            print(f"Erro ao refrescar token para {user_id}: {e}")
            # Se o refresh falhar, as credenciais não são mais válidas,
            # o usuário precisará reautenticar.
            return None
    
    # Se não há credenciais válidas ou refresh token, o usuário precisa autenticar
    return None

def save_credentials(user_id, credentials):
    """Salva as credenciais para um user_id específico."""
    token_file = os.path.join(TOKEN_DIR, f"token_{user_id}.pickle")
    with open(token_file, "wb") as token:
        pickle.dump(credentials, token)

def save_file(file, upload_folder):
    filename = secure_filename(file.filename)
    file_path = os.path.join(upload_folder, filename)

    try:
        file.save(file_path)
        logger.info(f"file_path: {file_path}")
        return {
            "filename": filename,
            "url": f"/uploads/{filename}",
            "type": file.mimetype.split('/')[0]
        }
    except Exception as e:
        logger.error(f"Erro ao salvar o arquivo {filename}: {str(e)}", exc_info=True)
        return None

# # Executa a aplicação Flask (para desenvolvimento)
# if __name__ == '__main__':

#     app.run(host='0.0.0.0', port=5029)