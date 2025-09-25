# internal_api.py
from Modules.utils import *
import hashlib
import re
from bs4 import BeautifulSoup
import requests

from firebase_admin import initialize_app, credentials, storage, get_app

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

WEBHOOK_URL = os.getenv("WEBHOOK_URL")

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

app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "*"}}, origins=[
#   "https://mediacutsstudio.com",
#   "https://www.mediacutsstudio.com",
#   "https://dev.mediacutsstudio.com",
#   "https://www.dev.mediacutsstudio.com",
#   "http://localhost:3001",
#   "http://localhost:4343",
# ]) 
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024 # 50 MB
    
COOKIES_FILE = os.path.join(os.path.dirname(__file__), 'Cookies', 'yt.json')

limiter = Limiter(
    app=app,         
    key_func=lambda: key_func(),  
    default_limits=["5 per minute"]
)

# 🚫 Rejeita requisições sem autenticação válida
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
    user_data = ref.get()  # Obtém os dados do usuário com a chave especificada
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
            return user_data.get("limit", "10 per minute")  # Retorna o limite configurado para o usuário
    # Limite para usuários sem autenticação ou com API Key inválida
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
        response.status_code = 401  # Unauthorized
        return None, response

    user_data = get_user_data_from_firebase(api_key, appfb)
    if not user_data:
        response = jsonify({"error": "Usuário não encontrado."})
        response.status_code = 401  # Unauthorized
        return None, response

    return user_data, None

@app.route('/')
def index():
    return jsonify({"message": "#1 API Media Cuts Studio funcionando!"})

def extract_youtube_id(url):
    # tenta extrair o ID de 11 chars do vídeo
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


# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=5000)
