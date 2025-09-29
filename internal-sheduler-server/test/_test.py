from cryptography.fernet import Fernet
# print(Fernet.generate_key().decode())
import os
import time
import json
from urllib.parse import urlencode
import math

from flask import Flask, redirect, request, jsonify
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# Firebase
import firebase_admin
from firebase_admin import credentials, db
diretorio_script = os.path.dirname(os.path.abspath(__file__)) 
env_file = os.path.join(diretorio_script, 'Keys', 'env.env')
load_dotenv(dotenv_path=env_file)
os.chdir(diretorio_script)
import logging

# --- Logger ---
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)
logger = logging.getLogger("tiktok_app")
# --- Config ---
CLIENT_KEY = os.getenv("TIKTOK_CLIENT_KEY")
CLIENT_SECRET = os.getenv("TIKTOK_CLIENT_SECRET")
REDIRECT_URI = os.getenv("TIKTOK_REDIRECT_URI")
TOKEN_ENDPOINT = "https://open.tiktokapis.com/v2/oauth/token/"

FIREBASE_DATABASE_URL = os.getenv("FIREBASE_DATABASE_URL")
FIREBASE_CREDENTIALS_PATH = os.getenv("FIREBASE_SERVICE_ACCOUNT_KEY_PATH")
FERNET_KEY = os.getenv("TIKTOK_FERNET_KEY")

if not all([CLIENT_KEY, CLIENT_SECRET, REDIRECT_URI, FIREBASE_DATABASE_URL, FIREBASE_CREDENTIALS_PATH, FERNET_KEY]):
    raise EnvironmentError("Uma ou mais variáveis obrigatórias não estão definidas no .env")

fernet = Fernet(FERNET_KEY.encode())

# Initialize Firebase Admin
cred = credentials.Certificate(FIREBASE_CREDENTIALS_PATH)
firebase_admin.initialize_app(cred, {
    'databaseURL': FIREBASE_DATABASE_URL
})

# Root reference for tokens
TOKENS_REF = db.reference('/user_tokens')

app = Flask(__name__)


# ---------- Helpers: encrypt / decrypt ----------
def encrypt(value: str) -> str:
    return fernet.encrypt(value.encode()).decode()


def decrypt(value: str) -> str:
    return fernet.decrypt(value.encode()).decode()


# ---------- RTDB helpers ----------
def save_user_token(open_id: str, access_token: str, refresh_token: str, expires_at: float):
    """
    Salva (ou atualiza) o token de um usuário no RTDB.
    Estrutura em RTDB: /user_tokens/{open_id} = {
        access_token: <encrypted>,
        refresh_token: <encrypted>,
        expires_at: <unix timestamp>,
        updated_at: <unix timestamp>
    }
    """
    payload = {
        "access_token": encrypt(access_token),
        "refresh_token": encrypt(refresh_token),
        "expires_at": expires_at,
        "updated_at": time.time()
    }
    TOKENS_REF.child(open_id).set(payload)


def get_user_token(open_id: str):
    record = TOKENS_REF.child(open_id).get()
    if not record:
        return None
    try:
        return {
            "open_id": open_id,
            "access_token": decrypt(record["access_token"]),
            "refresh_token": decrypt(record["refresh_token"]),
            "expires_at": record.get("expires_at")
        }
    except Exception as e:
        # Problema de desencriptação / dados inválidos
        print("Erro decrypting token:", e)
        return None


def list_all_user_tokens():
    """
    Retorna um dicionário { open_id: record_dict } do RTDB.
    """
    all_records = TOKENS_REF.get() or {}
    return all_records


# ---------- OAuth endpoints ----------
@app.route("/auth/start")
def auth_start():
    scopes = "user.info.basic,video.upload,video.publish"

        
    params = {
        "client_key": CLIENT_KEY,
        "response_type": "code",
        "scope": scopes,
        "redirect_uri": REDIRECT_URI,
        "state": f"{fernet}"
    }
    auth_url = "https://www.tiktok.com/v2/auth/authorize/?" + urlencode(params)
    return redirect(auth_url)


@app.route("/auth/callback")
def auth_callback():
    code = request.args.get("code")
    state = request.args.get("state")
    if not code:
        return "Missing code", 400

    data = {
        "client_key": CLIENT_KEY,
        "client_secret": CLIENT_SECRET,
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI
    }
    resp = requests.post(TOKEN_ENDPOINT, data=data)
    if resp.status_code != 200:
        return jsonify({"error": "token_exchange_failed", "details": resp.text}), 400

    body = resp.json()
    # Adaptações caso a API retorne dentro de data
    access_token = body.get("data", {}).get("access_token") or body.get("access_token")
    refresh_token = body.get("data", {}).get("refresh_token") or body.get("refresh_token")
    expires_in = body.get("data", {}).get("expires_in") or body.get("expires_in")
    open_id = body.get("data", {}).get("open_id") or body.get("open_id")

    if not (access_token and refresh_token and open_id):
        return jsonify({"error": "missing_token_fields", "body": body}), 400

    expires_at = time.time() + int(expires_in or 3600)

    save_user_token(open_id, access_token, refresh_token, expires_at)

    return f"Autorização concluída para open_id={open_id}. Pode fechar esta página."

import math

def calculate_tiktok_chunks(file_size: int, chunk_size: int = 10_000_000) -> int:
    """
    Calculate total chunk count according to TikTok's rules:
    - Each chunk must be at least 5MB (5,242,880 bytes)  
    - If the last chunk would be smaller than 5MB, merge it with the previous chunk
    """
    MIN_CHUNK_SIZE = 5_242_880  # 5MB in bytes
    
    if file_size <= chunk_size:
        return 1
    
    # Calculate basic chunks
    full_chunks = file_size // chunk_size
    remainder = file_size % chunk_size
    
    # Debug logging
    print(f"[DEBUG] file_size: {file_size}, chunk_size: {chunk_size}")
    print(f"[DEBUG] full_chunks: {full_chunks}, remainder: {remainder}")
    
    # If there's no remainder, return full_chunks
    if remainder == 0:
        return full_chunks
    
    # If remainder is less than 5MB, merge with last chunk
    if remainder < MIN_CHUNK_SIZE:
        print(f"[DEBUG] Remainder {remainder} < MIN_CHUNK_SIZE {MIN_CHUNK_SIZE}, merging with last chunk")
        return full_chunks  # merge remainder with last full chunk
    else:
        print(f"[DEBUG] Remainder {remainder} >= MIN_CHUNK_SIZE, creating separate chunk")
        return full_chunks + 1  # remainder is large enough to be its own chunk


def init_video_upload(access_token: str, title: str, filepath: str):
    if not os.path.exists(filepath):
        return {"error": "file_not_found", "filepath": filepath}
    
    file_size = os.path.getsize(filepath)
    
    # Try without chunking first - upload as single file
    url = "https://open.tiktokapis.com/v2/post/publish/video/init/"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json; charset=UTF-8"
    }
    
    # For files under 64MB, try without chunking
    if file_size < 64_000_000:  # 64MB
        body = {
            "post_info": {
                "title": title,
                "privacy_level": "SELF_ONLY",
                "disable_duet": False,
                "disable_comment": False,
                "disable_stitch": False,
                "video_cover_timestamp_ms": 1000
            },
            "source_info": {
                "source": "FILE_UPLOAD",
                "video_size": file_size,
                "chunk_size": file_size,  # Use entire file as single chunk
                "total_chunk_count": 1
            }
        }
        logger.debug(f"Using single chunk upload for file size {file_size}")
    else:
        # For larger files, use smaller chunks (5MB)
        chunk_size = 5_000_000  # 5MB chunks
        total_chunk_count = math.ceil(file_size / chunk_size)
        
        body = {
            "post_info": {
                "title": title,
                "privacy_level": "SELF_ONLY",
                "disable_duet": False,
                "disable_comment": False,
                "disable_stitch": False,
                "video_cover_timestamp_ms": 1000
            },
            "source_info": {
                "source": "FILE_UPLOAD",
                "video_size": file_size,
                "chunk_size": chunk_size,
                "total_chunk_count": total_chunk_count
            }
        }
        logger.debug(f"Using {total_chunk_count} chunks of {chunk_size} bytes each")

    logger.debug(f"init_video_upload -> POST {url} body={body}")
    
    resp = requests.post(url, headers=headers, json=body)
    logger.debug(f"Resposta HTTP {resp.status_code}: {resp.text}")
    
    try:
        json_resp = resp.json()
        if resp.status_code != 200:
            logger.error(f"TikTok API error: {json_resp}")
            return {"error": "api_error", "status_code": resp.status_code, "response": json_resp}
        return json_resp
    except Exception as e:
        logger.error(f"Falha ao parsear JSON init_video_upload: {e}, body={resp.text}")
        return {"error": "invalid_json", "raw": resp.text}



def upload_video_file(upload_url: str, filepath: str):
    """
    Upload video file to TikTok with proper chunking if needed
    """
    file_size = os.path.getsize(filepath)
    chunk_size = 10_000_000
    
    # For files smaller than chunk_size, upload directly
    if file_size <= chunk_size:
        headers = {
            "Content-Range": f"bytes 0-{file_size-1}/{file_size}",
            "Content-Type": "video/mp4"
        }
        logger.debug(f"Enviando arquivo {filepath} para {upload_url} (size={file_size})")
        with open(filepath, "rb") as f:
            resp = requests.put(upload_url, headers=headers, data=f)
        logger.debug(f"Resposta upload_file HTTP {resp.status_code}: {resp.text[:500]}")
        return resp.status_code, resp.text
    else:
        # For larger files, implement proper chunked upload
        logger.debug(f"Arquivo grande detectado ({file_size} bytes), implementando upload em chunks")
        # TODO: Implement chunked upload logic here
        # For now, try uploading as single file
        headers = {
            "Content-Range": f"bytes 0-{file_size-1}/{file_size}",
            "Content-Type": "video/mp4"
        }
        with open(filepath, "rb") as f:
            resp = requests.put(upload_url, headers=headers, data=f)
        return resp.status_code, resp.text





@app.route("/upload_video", methods=["POST"])
def upload_video():
    data = request.json
    open_id = data.get("open_id")
    filepath = data.get("filepath")  # caminho no servidor
    title = data.get("title", "Vídeo automático 🚀")

    if not open_id or not filepath:
        return jsonify({"error": "missing_required_fields", "required": ["open_id", "filepath"]}), 400

    user_token = get_user_token(open_id)
    if not user_token:
        return jsonify({"error": "user_not_found"}), 404

    access_token = user_token["access_token"]

    init_resp = init_video_upload(access_token, title, filepath)
    upload_url = init_resp["data"]["upload_url"]
    time.sleep(5)
    status_code, upload_resp = upload_video_file(upload_url, filepath)
    return jsonify({"init": init_resp, "upload_status": status_code, "upload_resp": upload_resp})








def check_publish_status(access_token: str, publish_id: str):
    url = "https://open.tiktokapis.com/v2/post/publish/status/fetch/"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json; charset=UTF-8"
    }
    body = {"publish_id": publish_id}
    logger.debug(f"check_publish_status -> POST {url} body={body}")
    resp = requests.post(url, headers=headers, json=body)
    logger.debug(f"Resposta HTTP {resp.status_code}: {resp.text}")
    try:
        return resp.json()
    except Exception as e:
        logger.error(f"Falha ao parsear JSON check_publish_status: {e}, body={resp.text}")
        return {"error": "invalid_json", "raw": resp.text}


# ---------- Token refresh ----------
def refresh_token_for_open_id(open_id: str) -> bool:
    """
    Tenta renovar os tokens para open_id. Retorna True se renovou.
    """
    rec = TOKENS_REF.child(open_id).get()
    if not rec:
        print(f"[refresh] Nenhum registro para open_id={open_id}")
        return False

    try:
        refresh_token_enc = rec.get("refresh_token")
        refresh_token = decrypt(refresh_token_enc)
    except Exception as e:
        print(f"[refresh] erro decrypt refresh_token for {open_id}: {e}")
        return False

    payload = {
        "client_key": CLIENT_KEY,
        "client_secret": CLIENT_SECRET,
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }
    resp = requests.post(TOKEN_ENDPOINT, data=payload)
    if resp.status_code != 200:
        print(f"[refresh] falha HTTP open_id={open_id} status={resp.status_code} body={resp.text}")
        return False

    body = resp.json()
    new_access = body.get("data", {}).get("access_token") or body.get("access_token")
    new_refresh = body.get("data", {}).get("refresh_token") or body.get("refresh_token")
    expires_in = body.get("data", {}).get("expires_in") or body.get("expires_in")

    if not (new_access and new_refresh):
        print(f"[refresh] campos faltando na resposta ao tentar refresh {body}")
        return False

    expires_at = time.time() + int(expires_in or 3600)
    # salvar no RTDB
    save_user_token(open_id, new_access, new_refresh, expires_at)
    print(f"[refresh] sucesso open_id={open_id}")
    return True


def schedule_refresh_job():
    """
    Procura tokens no RTDB e atualiza os que expiram em menos de 10 minutos.
    """
    all_tokens = list_all_user_tokens()
    now = time.time()
    for open_id, rec in (all_tokens or {}).items():
        expires_at = rec.get("expires_at") or 0
        # renovando quando faltar menos de 10 minutos
        if (expires_at - now) < 600:
            try:
                refresh_token_for_open_id(open_id)
            except Exception as e:
                print("Erro ao refrescar token para", open_id, e)


# Agenda (executa a cada 5 minutos)
scheduler = BackgroundScheduler()
scheduler.add_job(schedule_refresh_job, "interval", minutes=900, id="tiktok_refresh")
scheduler.start()


# Endpoint simples para debug (apenas para uso dev; remova em produção)
@app.route("/debug/list_tokens")
def debug_list_tokens():
    all_tokens = list_all_user_tokens()
    # Não expor tokens desencriptados aqui por segurança
    return jsonify({k: {"expires_at": v.get("expires_at"), "updated_at": v.get("updated_at")} for k, v in (all_tokens or {}).items()})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
