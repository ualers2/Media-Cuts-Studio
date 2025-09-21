# Internal-server\celery_worker.py
import os
from celery import Celery
from datetime import datetime
import pytz
import json
import firebase_admin
from firebase_admin import db
from dotenv import load_dotenv, find_dotenv
import queue
import json
import re
from werkzeug.utils import secure_filename
import logging
from flask import Flask, request, jsonify, redirect, url_for, session
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Modules.config import Config
import os
import pickle
import logging
from datetime import datetime, timedelta
import pytz
from celery.schedules import crontab
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google.auth.exceptions import RefreshError
from firebase_admin import initialize_app, credentials, storage, get_app

os.makedirs(os.path.join(os.path.dirname(__file__), "Logs"), exist_ok=True)

from Modules.upload_ import upload_
from Modules.download_ import download_

from Uploaders.YoutubeOfficialUploader import upload_media_Youtube
from Uploaders.TiktokSemiOfficialUploader import upload_media_Tiktok


load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "Keys", "keys.env"))
cred = credentials.Certificate(os.getenv('DATABASEPATH'))
app1 = initialize_app(cred, {
    'databaseURL': os.getenv('DATABASEURL')
}, name="app2")

diretorio_script = os.path.dirname(os.path.abspath(__file__)) 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
os.makedirs(os.path.join(diretorio_script, 'Logs'), exist_ok=True)
file_handler = logging.FileHandler(os.path.join(diretorio_script, 'Logs', 'celery.log'))
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

USER_ID_FOR_TEST = os.getenv("USER_ID_FOR_TEST")
UPLOAD_URL = os.getenv("UPLOAD_URL_VIDEOMANAGER")

local_tz = pytz.timezone('America/Sao_Paulo')
celery_app = Celery(
    'api', 
    broker='redis://redis:6379/1', 
    backend='redis://redis:6379/1'
)

celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    task_track_started=True, # Permite o acompanhamento do progresso
    worker_log_format="[%(asctime)s: %(levelname)s/%(processName)s] %(message)s",
    worker_task_log_format="[%(asctime)s: %(levelname)s/%(processName)s] %(taskName)s %(task_id)s %(message)s",
    loglevel='DEBUG',
    worker_concurrency=10,  
    task_always_eager=False,  
    task_acks_late=False,  # Garante que a tarefa só será confirmada após sua execução
    task_reject_on_worker_lost=True,
)
celery_app.conf.worker_prefetch_multiplier = 1

celery_app.conf.timezone = 'America/Sao_Paulo'
celery_app.conf.enable_utc = False
celery_app.conf.task_default_queue = 'posts_queue'

# celery_app.conf.task_routes = {
#     'celery_worker.tasks.upload_short_task': {'queue': 'shorts_queue'},
#     'celery_worker.tasks.upload_tiktok_task': {'queue': 'tiktok_queue'}
# }

# celery_app.conf.beat_schedule = {
#     'refresh-youtube-tokens-every-30-mins': {
#         'task': 'celery_worker.refresh_youtube_tokens_task',
#         'schedule': crontab(minute='*/30'),
#     }
# }

@celery_app.task(name="celery_worker.refresh_youtube_tokens_task")
def refresh_youtube_tokens_task():
    logger.info("Iniciando tarefa periódica: refresh_youtube_tokens_task")
    resultados = varrer_e_atualizar_tokens_youtube()
    logger.info(f"refresh_youtube_tokens_task resultados: {resultados}")
    return resultados

# TTL antes de considerar "precisa renovar" (ex.: 10 minutos)
REFRESH_BEFORE = timedelta(minutes=10)
# pasta local temporária para tokens (pode ser TOKEN_DIR ou "Tokens")
LOCAL_TOKEN_DIR = os.path.join(os.path.dirname(__file__), "Tokens")
os.makedirs(LOCAL_TOKEN_DIR, exist_ok=True)

def _send_reauth_email(to_email, canal_id, reason):
    try:
        subject = f"[API] Necessária reautenticação do canal {canal_id}"
        body = (
            f"O sistema tentou renovar o token do canal {canal_id} e falhou.\n\n"
            f"Motivo: {reason}\n\n"
            "Por favor reautorize via painel para evitar falhas em publicações."
        )
        msg = MIMEMultipart()
        msg['From'] = SMTP_USER
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP(host, port)
        if use_tls:
            server.starttls()
        server.login(SMTP_USER, password)
        server.sendmail(SMTP_USER, [to_email], msg.as_string())
        server.quit()
        logger.info(f"E-mail de reauth enviado para {to_email} (canal {canal_id}).")
    except Exception as e:
        logger.error(f"Erro ao enviar email de reauth para {to_email}: {e}")

def refresh_token_for_canal(canal_id_key, canal_data):
    """
    canal_id_key: chave usada no DB (ex: 'meu_canal_id' já sanitizado)
    canal_data: dados do canal (dicionário)
    """
    try:
        if canal_data.get('socialNetwork') != 'youtube':
            return {"status": "skipped", "reason": "not_youtube"}

        TOKEN_ID = canal_data.get('TOKEN_ID')
        if not TOKEN_ID:
            logger.info(f"Canal {canal_id_key} sem TOKEN_ID — pular.")
            return {"status": "no_token"}

        # montar path local do token (consistente com seu uso atual)
        # você salva pickles como f"{name_id}.pickle" em vários pontos; adaptar se necessário
        token_local_path = os.path.join(LOCAL_TOKEN_DIR, f"{TOKEN_ID}.pickle")

        # Baixar o token (usa sua função existente)
        # Project name: tentamos usar canal_id_key como PROJECT_NAME - compatibilize se necessário
        try:
            download_(UPLOAD_URL=UPLOAD_URL, save_path=token_local_path, PROJECT_NAME=canal_id_key, VIDEO_ID=TOKEN_ID, USER_ID_FOR_TEST=USER_ID_FOR_TEST)
        except Exception as e:
            logger.error(f"Falha ao baixar token {TOKEN_ID} para canal {canal_id_key}: {e}")
            return {"status": "download_failed", "error": str(e)}

        # Carregar credenciais
        try:
            with open(token_local_path, "rb") as f:
                credentials = pickle.load(f)
        except Exception as e:
            logger.error(f"Falha ao carregar pickle para {token_local_path}: {e}")
            return {"status": "load_failed", "error": str(e)}

        # Se for dict/json em vez de pickle adapt, mas normalmente é Credentials/pickle
        if isinstance(credentials, Credentials) is False:
            # tentar construir Credentials se for dict:
            if isinstance(credentials, dict):
                credentials = Credentials(
                    token=credentials.get('token'),
                    refresh_token=credentials.get('refresh_token'),
                    token_uri=credentials.get('token_uri'),
                    client_id=credentials.get('client_id'),
                    client_secret=credentials.get('client_secret'),
                    scopes=credentials.get('scopes', [])
                )
            else:
                logger.error("Formato de token desconhecido.")
                return {"status": "bad_format"}

        # checar expiração atual
        now = datetime.utcnow()
        expiry = getattr(credentials, "expiry", None)
        # se expiry for None, tentamos refresh direto (p.ex.: token apenas com access_token sem expiry info)
        needs_refresh = False
        if expiry:
            # convert expiry para naive UTC
            if expiry.tzinfo is not None:
                expiry_naive = expiry.astimezone(pytz.utc).replace(tzinfo=None)
            else:
                expiry_naive = expiry
            delta = expiry_naive - now
            if delta <= REFRESH_BEFORE:
                needs_refresh = True
        else:
            # sem info de expiry: tentar refresh se houver refresh_token
            needs_refresh = True

        if not needs_refresh:
            return {"status": "ok", "reason": "still_valid", "expires_at": str(expiry)}

        # Tentar refresh
        try:
            # precisa de Request
            request = Request()
            credentials.refresh(request)
            # salvou automaticamente new token, atualizar arquivo pickle
            with open(token_local_path, "wb") as f:
                pickle.dump(credentials, f)

            # subir novo token para storage e atualizar TOKEN_ID no Firebase
            # usamos o mesmo padrão upload_(project_name, filepath, user) como no oauth2callback
            new_TOKEN_ID = upload_(canal_id_key, token_local_path, SMTP_USER.replace(".", "_"))
            logger.info(f"Token renovado para canal {canal_id_key}. novo TOKEN_ID: {new_TOKEN_ID}")

            # atualizar DB - grava novo TOKEN_ID e timestamps
            canais_ref = db.reference("canais", app=app1).child(canal_id_key)
            canais_ref.update({
                "TOKEN_ID": new_TOKEN_ID,
                "token_expires_at": credentials.expiry.isoformat() if credentials.expiry else None,
                "needs_reauth": False,
                "last_refreshed_at": datetime.now(pytz.utc).isoformat()
            })

            # remover token local se quiser
            try:
                os.remove(token_local_path)
            except:
                pass

            return {"status": "refreshed", "new_TOKEN_ID": new_TOKEN_ID}

        except RefreshError as re:
            logger.error(f"RefreshError canal {canal_id_key}: {re}")
            # marcar para reauth e notificar dono
            canais_ref = db.reference("canais", app=app1).child(canal_id_key)
            canais_ref.update({"needs_reauth": True, "last_refresh_error": str(re)})
            # tenta enviar e-mail para o usuário (se tiver e-mail salvo)
            to_email = canal_data.get('owner_email') or canal_data.get('email') or SMTP_USER
            _send_reauth_email(to_email, canal_id_key, str(re))
            return {"status": "refresh_failed", "error": str(re)}
        except Exception as e:
            logger.exception(f"Erro genérico ao tentar refresh do canal {canal_id_key}: {e}")
            canais_ref = db.reference("canais", app=app1).child(canal_id_key)
            canais_ref.update({"last_refresh_error": str(e)})
            return {"status": "error", "error": str(e)}

    except Exception as e:
        logger.exception(f"Erro inesperado no refresh_token_for_canal({canal_id_key}): {e}")
        return {"status": "error", "error": str(e)}


def varrer_e_atualizar_tokens_youtube(dry_run=False, limit=None):
    """
    Varre /canais do RTDB, filtra socialNetwork == 'youtube' e tenta refresh.
    Se dry_run=True apenas reporta sem alterar.
    """
    canais_ref = db.reference("canais", app=app1)
    all_canais = canais_ref.get() or {}
    resultados = {}
    count = 0
    for key, data in all_canais.items():
        if limit and count >= limit:
            break
        if not data:
            continue
        if data.get('socialNetwork') != 'youtube':
            continue
        count += 1
        try:
            result = refresh_token_for_canal(key, data) if not dry_run else {"status": "dry_run", "canal": key}
            resultados[key] = result
        except Exception as e:
            resultados[key] = {"status": "error", "error": str(e)}
    return resultados


@celery_app.task(name="celery_worker.upload_tiktok_and_shorts_task",  acks_late=True)
def upload_tiktok_and_shorts_task(task_params):
    """
    Tarefa Celery para fazer o upload de um Short e Tikok 
    """
    post_id = task_params.get('post_id')
    logger.info(f"🔥 Iniciando upload_tiktok_and_shorts_task para post {post_id}")


    lock_file_path = os.path.join(os.path.dirname(__file__), "tmp", "uploads")
    lock_file = os.path.join(lock_file_path, f"upload_{post_id}.lock")
    if os.path.exists(lock_file):
        logger.warning(f"Tarefa para {post_id} já agendada. Ignorando duplicata.")
        return "Já agendado"
    open(lock_file, 'w').close()

    try:
        short_ref = db.reference(f"shorts/{post_id}", app=app1)
        short_data = short_ref.get()
        if not short_data:
            return "não encontrado no banco de dados."
        if short_data.get('status') == 'canceled':
            logger.info(f"Post {post_id} foi cancelado. Abortando upload.")
            return "foi cancelado"
        if short_data.get('status') in ['EM_ANDAMENTO', 'published']:
            logger.info(f"Post {post_id} já está com status “{short_data['status']}”, abortando duplicata.")
            return "Já agendado"

        logger.info(f"canal_id_tiktok {short_data['canal_id_tiktok']}...")
        logger.info(f"canal_id {short_data['canal_id']}...")

        canal_ref = db.reference(f"canais/{short_data['canal_id']}", app=app1)
        canal_data = canal_ref.get()
        if not canal_data:
            return f"Canal com ID {short_data['canal_id']} não encontrado ."
        
        canal_ref_tiktok = db.reference(f"canais/{short_data['canal_id_tiktok']}", app=app1)
        canal_data_tiktok = canal_ref_tiktok.get()
        if not canal_data_tiktok:
            return f"Canal com ID {short_data['canal_id_tiktok']} não encontrado."
                
        def mark_em_andamento(short_data):
            if short_data is None:
                raise ValueError("Short não encontrado")
            status = short_data.get('status')
            if status in ['EM_ANDAMENTO', 'published', 'canceled']:
                # Abortamos e retornamos sinal que não deve prosseguir
                return None  # ou alguma flag especial
            short_data['status'] = 'EM_ANDAMENTO'
            return short_data

        # Dentro da task, ao invés de short_ref.update():
        result = short_ref.transaction(mark_em_andamento)
        if result is None:
            logger.info(f"Post {post_id} já em andamento ou concluído — abortando.")
            return "Já agendado"
        logger.info(f"Post {post_id} marcado como EM_ANDAMENTO com sucesso.")
        email_user_origin = "freitasalexandre810@gmail.com"
        email_user = email_user_origin.replace(".", "_")
        VIDEO_PATH = short_data['caminho_arquivo']
        title = short_data.get('title', None)
        description = short_data.get('description', None)
        category_id = short_data.get('category_id', '24')
        video_tags = short_data.get('tags', [''])
        privacy_status = short_data['visibility']
        if privacy_status == "public":
            visibility = 0
        elif privacy_status == "private":
            visibility = 1
        scopes = canal_data['scopes']
        name_id_YOUTUBE = canal_data['id']
        TOKEN_ID_YOUTUBE = canal_data['TOKEN_ID']
        logger.info(f"TOKEN_ID_YOUTUBE {TOKEN_ID_YOUTUBE}...")
        TOKEN_ID_TIKTOK = canal_data_tiktok['TOKEN_ID']
        logger.info(f"TOKEN_ID_TIKTOK {TOKEN_ID_TIKTOK}...")

        nome_TIKTOK = canal_data_tiktok['nome']
        safe_project_name = secure_filename(nome_TIKTOK).replace("-", "")
        name_TIKTOK_filter = re.sub(r'[^0-9A-Za-z_-]', '', safe_project_name)

        nome_yt = canal_data['nome']
        safe_project_name = secure_filename(nome_yt).replace("-", "")
        name_yt_filter = re.sub(r'[^0-9A-Za-z_-]', '', safe_project_name)


        canal_id_str_TIKTOK = f"{nome_TIKTOK}"
        canal_id_replace_TIKTOK = canal_id_str_TIKTOK.replace(".", "_").replace(" ", "-")
        token_file_TIKTOK = os.path.join(os.path.dirname(__file__), "Tokens", f"{canal_id_replace_TIKTOK}.json")
        logger.info(f"token_file_TIKTOK {token_file_TIKTOK}...")
        token_file = os.path.join(os.path.dirname(__file__), "Tokens", f"{name_id_YOUTUBE}.pickle")
        logger.info(f"token_file {token_file}...")
        
        download_(
            UPLOAD_URL=UPLOAD_URL, 
            save_path=token_file_TIKTOK, 
            PROJECT_NAME=name_TIKTOK_filter, 
            VIDEO_ID=TOKEN_ID_TIKTOK, 
            USER_ID_FOR_TEST=email_user
        )

        download_(
            UPLOAD_URL=UPLOAD_URL, 
            save_path=token_file, 
            PROJECT_NAME=name_yt_filter, 
            VIDEO_ID=TOKEN_ID_YOUTUBE, 
            USER_ID_FOR_TEST=email_user
        )
            

        def upload_media_youtubex():

                logger.info(f"Iniciando upload para o Short {post_id}...")
                flag_y, error_y, youtube_url = upload_media_Youtube(
                    file_name=VIDEO_PATH,
                    title=title,
                    description=description,
                    category_id=category_id,
                    video_tags=video_tags,
                    TOKEN_FILE=token_file,
                    SCOPES=scopes,
                    privacyStatus=privacy_status,
                    email_to_send=email_user_origin
          
                )
                return {
                    "plataforma": "YouTube",
                    "flag": flag_y,
                    "error": error_y,
                    "result": youtube_url
                }

        def upload_media_tiktokx():

                logger.info(f"Iniciando upload para o Tiktok {post_id}...")
                flag_t, error_t = upload_media_Tiktok(
                    token_file=token_file_TIKTOK,
                    VIDEO_PATH=VIDEO_PATH,
                    title=title,
                    visibility=visibility,
                    email_to_send=email_user_origin
                )
                return {
                    "plataforma": "TikTok",
                    "flag": flag_t,
                    "error": error_t,
                    "result": None  # não há URL para TikTok
                }

        def executar_uploads_em_paralelo():
            resultados = []
            with ThreadPoolExecutor(max_workers=2) as executor:
                futures = {
                    executor.submit(upload_media_youtubex): "YouTube",
                    executor.submit(upload_media_tiktokx): "TikTok"
                }
                for future in as_completed(futures):
                    try:
                        resultados.append(future.result())
                    except Exception as e:
                        plataforma = futures[future]
                        resultados.append({"plataforma": plataforma, "flag": "Failed", "error": str(e), "result": None})
            return resultados

        resultados = executar_uploads_em_paralelo()

        flag_y = flag_t = None
        error_y = error_t = None
        youtube_url = None

        for r in resultados:
            if r["plataforma"] == "YouTube":
                flag_y = r["flag"]
                error_y = r["error"]
                youtube_url = r["result"]
            elif r["plataforma"] == "TikTok":
                flag_t = r["flag"]
                error_t = r["error"]

        if flag_y == "Failed":
            short_ref.update({'status': 'error', 'erro_mensagem': error_y})
        if flag_t == "Failed":
            short_ref.update({'status': 'error', 'erro_mensagem': error_t})

        if flag_y == "Upload" and flag_t == "Upload":
            short_ref.update({
                'status': 'published',
                'data_upload_real': datetime.now(local_tz).isoformat(),
                'youtube_video_id': youtube_url.split('=')[-1] if youtube_url else None,
                'youtube_url': youtube_url,
                'tiktok_flagmessage': flag_t,
                'erro_mensagem': None
            })
            if os.path.exists(VIDEO_PATH):
                os.remove(VIDEO_PATH)
            # garante limpeza
            if os.path.exists(lock_file):
                os.remove(lock_file)

            # se quiser também apagar tokens temporários:
            if os.path.exists(token_file_TIKTOK):
                os.remove(token_file_TIKTOK)
            if os.path.exists(token_file):
                os.remove(token_file)
            
            return "sucess post!"

        return "falhou"


    except Exception as e:
        error_message = f"Falha no upload do Post {post_id}: {str(e)}"
        print(error_message)
        # Atualizar status para FALHOU
        short_ref.update({
            'status': 'error',
            'erro_mensagem': error_message
        })
        return "falhou"
        # Tentar novamente a tarefa em caso de erro (com limite de retentativas)
        # retry(exc=e)




@celery_app.task(name="celery_worker.upload_short_task")
def upload_short_task(task_params):
    """
    Tarefa Celery para fazer o upload de um Short para o YouTube.
    """
    short_id = task_params.get('short_id')
    logger.info(f"🔥 Iniciando upload_shorts_task para post {short_id}")
    lock_file_path = os.path.join(os.path.dirname(__file__), "tmp", "uploads")
    lock_file = os.path.join(lock_file_path, f"upload_{short_id}.lock")
    if os.path.exists(lock_file):
        logger.warning(f"Tarefa para {short_id} já agendada. Ignorando duplicata.")
        return "Já agendado"
    open(lock_file, 'w').close()
    try:
        short_ref = db.reference(f"shorts/{short_id}", app=app1)
        short_data = short_ref.get()
        if not short_data:
            raise ValueError(f"Short com ID {short_id} não encontrado no banco de dados.")
        if short_data.get('status') == 'canceled':
            logger.info(f"Short {short_id} foi cancelado. Abortando upload.")
            return "foi cancelado"
        if short_data.get('status') in ['EM_ANDAMENTO', 'published']:
            logger.info(f"Short {short_id} já está com status “{short_data['status']}”, abortando duplicata.")
            return "Já agendado"

        canal_ref = db.reference(f"canais/{short_data['canal_id']}", app=app1)
        canal_data = canal_ref.get()
        if not canal_data:
            raise ValueError(f"Canal com ID {short_data['canal_id']} não encontrado para o Short {short_id}.")
        short_ref.update({'status': 'EM_ANDAMENTO'})
        logger.info(f"Short {short_id} status atualizado para EM_ANDAMENTO.")
        email_user_origin = "freitasalexandre810@gmail.com"
        email_user = email_user_origin.replace(".", "_")
        file_name = short_data['caminho_arquivo']
        title = short_data.get('title', None)
        description = short_data.get('description', None)
        category_id = short_data.get('category_id', '24')
        video_tags = short_data.get('tags', [''])
        privacy_status = short_data['visibility']
        scopes = canal_data['scopes']
        name_id = canal_data['id']
        name_ = canal_data['nome']
        safe_project_name = secure_filename(name_).replace("-", "")
        name_filter = re.sub(r'[^0-9A-Za-z_-]', '', safe_project_name).replace("_", "")
        TOKEN_ID = canal_data['TOKEN_ID']
        logger.info(f"TOKEN_ID {TOKEN_ID}...")
        token_file = os.path.join(os.path.dirname(__file__), "Tokens", f"{name_id}.pickle")
        download_(
            UPLOAD_URL=UPLOAD_URL, 
            save_path=token_file, 
            PROJECT_NAME=name_filter, 
            VIDEO_ID=TOKEN_ID, 
            USER_ID_FOR_TEST=email_user
        )
        logger.info(f"token_file {token_file}...")
        logger.info(f"Iniciando upload para o Short {short_id}...")

        Flag_message, Error_message, youtube_url = upload_media_Youtube(
            file_name=file_name,
            title=title,
            description=description,
            category_id=category_id,
            video_tags=video_tags,
            TOKEN_FILE=token_file,
            SCOPES=scopes,
            privacyStatus=privacy_status,
            email_to_send=email_user_origin

        )
        if Flag_message == "Failed":
            short_ref.update({
                'status': 'error',
                'erro_mensagem': Error_message,
            })
            logger.info(f"error do tiktok {Error_message}")
            if os.path.exists(file_name):
                os.remove(file_name)
                logger.info(f"Arquivo {file_name} removido após upload.")
                # garante limpeza
                if os.path.exists(lock_file):
                    os.remove(lock_file)

                if os.path.exists(token_file):
                    os.remove(token_file)

                return "falhou"
        elif Flag_message == "Upload":
            short_ref.update({
                'status': 'published',
                'data_upload_real': datetime.now(local_tz).isoformat(), # Salva como string ISO
                'youtube_video_id': youtube_url.split('=')[-1], # Extrai o ID do vídeo
                'youtube_url': youtube_url,
                'erro_mensagem': None
            })
            logger.info(f"Upload do Short {short_id} concluído. URL: {youtube_url}")

            # Opcional: Remover o arquivo de vídeo após o upload bem-sucedido
            if os.path.exists(file_name):
                os.remove(file_name)
                logger.info(f"Arquivo {file_name} removido após upload.")
                # garante limpeza
                if os.path.exists(lock_file):
                    os.remove(lock_file)

                if os.path.exists(token_file):
                    os.remove(token_file)

                return "sucess post!"

    except Exception as e:
        error_message = f"Falha no upload do Short {short_id}: {str(e)}"
        logger.info(error_message)
        # Atualizar status para FALHOU
        short_ref.update({
            'status': 'error',
            'erro_mensagem': error_message
        })
        return "falhou"
        # Tentar novamente a tarefa em caso de erro (com limite de retentativas)
        # retry(exc=e)


@celery_app.task(name="celery_worker.upload_tiktok_task")
def upload_tiktok_task(task_params):
    """
    Tarefa Celery para fazer o upload de um tiktok .
    """
    tiktok_id = task_params.get('tiktok_id')

    logger.info(f"🔥 Iniciando upload_tiktok_task para post {tiktok_id}")


    lock_file_path = os.path.join(os.path.dirname(__file__), "tmp", "uploads")
    lock_file = os.path.join(lock_file_path, f"upload_{tiktok_id}.lock")
    if os.path.exists(lock_file):
        logger.warning(f"Tarefa para {tiktok_id} já agendada. Ignorando duplicata.")
        return "Já agendado"
    open(lock_file, 'w').close()

            
    try:
        short_ref = db.reference(f"shorts/{tiktok_id}", app=app1)
        short_data = short_ref.get()
        if not short_data:
            raise ValueError(f"tiktok com ID {tiktok_id} não encontrado no banco de dados.")
        if short_data.get('status') == 'canceled':
            logger.info(f"Post {tiktok_id} foi cancelado. Abortando upload.")
            return "foi cancelado"
        if short_data.get('status') in ['EM_ANDAMENTO', 'published']:
            logger.info(f"Post {tiktok_id} já está com status “{short_data['status']}”, abortando duplicata.")
            return "Já agendado"


        # Valida se o canal existe diretamente no DB
        canal_data_tiktok = db.reference(f"canais/{short_data['canal_id']}", app=app1).get()
        if not canal_data_tiktok:
            return f"Canal com ID {short_data['canal_id']} não encontrado."

        short_ref.update({'status': 'EM_ANDAMENTO'})
        logger.info(f"tiktok {tiktok_id} status atualizado para EM_ANDAMENTO.")
        email_user_origin = "freitasalexandre810@gmail.com"
        email_user = email_user_origin.replace(".", "_")
        VIDEO_PATH = short_data['caminho_arquivo']
        title = short_data.get('title', None)
        visibility = short_data.get('visibility', None)
        if visibility == "public":
            visibility = 0
        elif visibility == "private":
            visibility = 1
        TOKEN_ID_ = canal_data_tiktok['TOKEN_ID']
        nome_ = canal_data_tiktok['nome']
        canal_id_str_ = f"{nome_}"
        canal_id_replace_ = canal_id_str_.replace(".", "_").replace(" ", "-")
        
        logger.info(f"TOKEN_ID {TOKEN_ID_}...")
        token_file = os.path.join(os.path.dirname(__file__), "Tokens", f"{canal_id_replace_}.json")

        safe_project_name = secure_filename(nome_).replace("-", "")
        name_filter = re.sub(r'[^0-9A-Za-z_-]', '', safe_project_name).replace("_", "")

        download_(
            UPLOAD_URL=UPLOAD_URL, 
            save_path=token_file, 
            PROJECT_NAME=name_filter, 
            VIDEO_ID=TOKEN_ID_, 
            USER_ID_FOR_TEST=email_user
        )

        logger.info(f"token_file {token_file}...")
        logger.info(f"Iniciando upload para o Short {tiktok_id}...")

        flag_message, error_message = upload_media_Tiktok(
            token_file=token_file,
            VIDEO_PATH=VIDEO_PATH,
            title=title,
            visibility=visibility,
            email_to_send=email_user_origin

        )
        if flag_message == "Failed":
            short_ref.update({
                'status': 'error',
                'erro_mensagem': error_message,
            })
            logger.info(f"error do tiktok {tiktok_id}")
            if os.path.exists(VIDEO_PATH):
                os.remove(VIDEO_PATH)
                logger.info(f"Arquivo {VIDEO_PATH} removido após upload.")

                # garante limpeza
                if os.path.exists(lock_file):
                    os.remove(lock_file)

                if os.path.exists(token_file):
                    os.remove(token_file)
                    
                return "falhou"
        elif flag_message == "Upload":
            short_ref.update({
                'status': 'published',
                'data_upload_real': datetime.now(local_tz).isoformat(), # Salva como string ISO
                'flag_message': flag_message,
                'erro_mensagem': None
            })
            logger.info(f"Upload do tiktok {tiktok_id} concluído. ")
            if os.path.exists(VIDEO_PATH):
                os.remove(VIDEO_PATH)
                logger.info(f"Arquivo {VIDEO_PATH} removido após upload.")

                # garante limpeza
                if os.path.exists(lock_file):
                    os.remove(lock_file)

                if os.path.exists(token_file):
                    os.remove(token_file)
                    
                return "sucess post!"
            


    except Exception as e:
        error_message = f"Falha no upload do tiktok {tiktok_id}: {str(e)}"
        logger.error(error_message)
        # Atualizar status para FALHOU
        short_ref.update({
            'status': 'error',
            'erro_mensagem': error_message
        })
        return "falhou"
        # Tentar novamente a tarefa em caso de erro (com limite de retentativas)
        # retry(exc=e)



        