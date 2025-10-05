# celery_worker.py
# import time
# while True:
#     time.sleep(500)

from multiprocessing import Process
import os
from pathlib import Path
from datetime import datetime, timedelta
import pytz
import asyncio
from celery import Celery
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
from werkzeug.utils import secure_filename
import logging
from dotenv import load_dotenv
from celery.bin.worker import worker
from celery.schedules import crontab
from multiprocessing import Process
import subprocess
import requests
import time
from firebase_admin import credentials, initialize_app, storage, db, delete_app


load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "Keys", "keys.env"))

########################################################################
# IMPORT FirebaseKeys

cred = credentials.Certificate(os.getenv('DATABASEPATH'))
app1 = initialize_app(cred, {
    'databaseURL': os.getenv('DATABASEURL')
}, name="app1")

cred = credentials.Certificate(os.getenv('DATABASEPATHDOCS'))
appdocs = initialize_app(cred, {
    'databaseURL': os.getenv('DATABASEURLDOCS')
}, name="appdocs")

########################################################################
# IMPORT CoreApp
from Studio.Modules.utils import *
from Studio.Shortify import ShortifyAlgo
# from Studio.GramFlow import GramFlow
from Studio.Studio import MediaCutsStudio  
from Studio.AudioTranscriber import Audio_Transcriber  
from Studio.AutoReframe import AutoReframe, YOLO
from Studio.Modules.send_email import SendEmail
########################################################################

diretorio_script = os.path.dirname(os.path.abspath(__file__))

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
os.makedirs(os.path.join(diretorio_script, "Studio", 'Logs'), exist_ok=True)
file_handler = logging.FileHandler(os.path.join(diretorio_script, "Studio", 'Logs', 'celery_worker.log'))
file_handler.setFormatter(formatter)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)


PRODUCTION_ENV = os.getenv("PRODUCTION_ENV", "True")

if PRODUCTION_ENV == "True":
    # Production
    MediaCutsStudio_instance = MediaCutsStudio(dockerffmpegGPU=True,
                                               dockerffmpegCPU=False) 

    
if PRODUCTION_ENV == "False":
    # Local test
    MediaCutsStudio_instance = MediaCutsStudio(dockerffmpegCPU=True,
                                               dockerffmpegGPU=False) 

host = os.getenv('SMTP_HOST')
port = int(os.getenv('SMTP_PORT', 587))
SMTP_USER = os.getenv('SMTP_USER')
password = os.getenv('SMTP_PASSWORD')
use_tls = os.getenv('SMTP_USE_TLS', 'true').lower() == 'true'

UPLOAD_URL_VIDEOMANAGER = os.getenv("UPLOAD_URL_VIDEOMANAGER")
UPLOAD_URL = os.getenv("UPLOAD_URL")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
WEBHOOK_ZIP_URL =  os.getenv("WEBHOOK_ZIP_URL")
alfred_gmail_task = os.getenv("alfred_gmail_task")
url_YoutubeVibes_task_lofi = os.getenv("run_YoutubeVibes_task_lofi")

diretorio_script = os.path.dirname(os.path.abspath(__file__)) 
ffmpegpathnotexe = os.path.join(diretorio_script,  'Utils', 'ffmpeg')
path_ffmpeg = os.path.join(diretorio_script, 'Utils', 'ffmpeg', 'ffmpeg.exe')
path_ffprobe = os.path.join(diretorio_script,  'Utils', 'ffmpeg', 'ffprobe.exe')
path_ffmpegnotexe = ffmpegpathnotexe

celery_app = Celery(
    'shortify', 
    broker='redis://redis:6379/0', 
    backend='redis://redis:6379/0'
)

celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    task_acks_late=True,  
    task_track_started=True, 
    worker_log_format="[%(asctime)s: %(levelname)s/%(processName)s] %(message)s",
    worker_task_log_format="[%(asctime)s: %(levelname)s/%(processName)s] %(taskName)s %(task_id)s %(message)s",
    loglevel='DEBUG',
    worker_concurrency=2,  
    task_always_eager=False,  
)
celery_app.conf.task_default_queue = 'internal_queue'

# agenda para rodar a cada minuto
celery_app.conf.beat_schedule = {
    'process-shortify-queue-every-minute': {
        'task': 'celery_worker.process_queue',
        'schedule': crontab(minute='*/6'),
    },    
    'process-reset-monthly-counters-every-5-hour': {
        'task': 'celery_worker.reset_monthly_counters',
        'schedule': crontab(minute=0, hour=0),  # todo dia 00:00
    },
    
}

# celery_app.conf.task_routes = {
#     'celery_worker.tasks.run_shortify_task': {'queue': 'default'}
    
#     # 'celery_worker.tasks.run_instagram_uploader_task': {'queue': 'instagram'},
# }

celery_app.conf.timezone = 'America/Sao_Paulo'
celery_app.conf.enable_utc = False
shortify_queue = db.reference('shortify_queue', app=app1)
process_queue_ref = db.reference('process_queue', app=app1)
instagramUploader_queue = db.reference('InstagramUploader_queue', app=app1)

Audio_Transcriber_webhook=False
Audio_Transcriber_api_key=None
Audio_Transcriber_WEBHOOK_URL=None
Audio_Transcriber_model = "faster-whisper-local-small"
Audio_Transcriber_model_Cuts = "faster-whisper-local-small"

@celery_app.task(name="celery_worker.reset_monthly_counters")
def reset_monthly_counters():
    tz = pytz.timezone("America/Sao_Paulo")
    now = datetime.now(tz)

    if now.day == 1 and now.hour == 0:  
        users_ref = db.reference("Users_Control_Panel", app=app1)
        all_users = users_ref.get() or {}

        for api_key, user_data in all_users.items():
            users_ref.child(api_key).update({
                "projects_videos_base_completed": 0
            })

        logger.info("✅ Contadores de vídeos resetados para todos os usuários.")

@celery_app.task(name="celery_worker.process_queue")
def process_queue():
    # 1) Carrega tudo do shortify_queue e do process_queue_ref
    all_shortify = shortify_queue.get() or {}
    all_process = process_queue_ref.get() or {}
    all_items = {**all_shortify, **all_process}

    # Conta quantas shortify estão em Running mas ignora as que têm erro
    running_shortify = {
        k: v for k, v in all_shortify.items()
        if v.get('status') == 'Running' and not (v.get('error') and str(v.get('error')).strip())
    }
    running_count = len(running_shortify)

    # Filtra só os PENDING
    pending_items = {}
    for key, item in all_items.items():
        if item.get('status') != 'PENDING':
            continue
        if item.get('rescheduled'):
            try:
                tz_item = pytz.timezone(item['payload'].get('timezone', 'America/Sao_Paulo'))
                scheduled_dt = tz_item.localize(datetime.strptime(item['scheduled_time'], '%Y-%m-%d %H:%M:%S'))
                now_dt = datetime.now(tz_item)
                if now_dt >= scheduled_dt:
                    # chegou a hora reagendada -> limpa flags para tornar elegível de novo
                    shortify_queue.child(key).update({
                        "rescheduled": False,
                        "reschedule_count": 0
                    })
                else:
                    # ainda antes do horário reagendado -> ignora este item
                    continue
            except Exception as e:
                logger.warning(f"Erro ao processar horário reagendado de {key}: {e}")
                continue

        pending_items[key] = item
    
    for key, item in pending_items.items():

        try:

            rescheduled_item = item.get('rescheduled', False)
            reschedule_count_item = item.get('reschedule_count', 0)
            user_email_origin = item['user_email']
            user_email = user_email_origin.replace(".", "_")
            type_process = item['type_process']
            payload_task = item.get('payload', {}) or {}
            api_key = payload_task.get('api_key') or item.get('api_key')
            requested_AI_model = payload_task.get('ShortifyMode')
            sched_str = item['scheduled_time']
            user_tasks_ref = db.reference(f'user_tasks/{user_email}', app=app1)
            user_Control_Panel_ref = db.reference(f'Users_Control_Panel/{api_key}', app=app1)
            try:
                user_control_data = user_Control_Panel_ref.get()
                if not user_control_data or 'project_simultaneo' not in user_control_data:
                    logger.error(f"Dados de controle de usuário ou 'project_simultaneo' não encontrados para a api_key {api_key}. Pulando...")
                    continue
                limite_simultaneo = user_control_data['project_simultaneo']
                limite_AI_models = user_control_data['AI_models']
                limite_videos_base_for_cuts = user_control_data['videos_base_for_cuts']
                subscription_plan = user_control_data['subscription_plan']
                projects_running_count = user_control_data.get('projects_running', 0) # Novo campo para controle
                projects_videos_base_completed_count = user_control_data.get('projects_videos_base_completed', 0) # Novo campo para controle

            except Exception as e:
                logger.error(f"Erro ao buscar dados de controle para {api_key}: {e}")
                continue


            # Verifica se title_origin existe e não está vazio
            if item['payload'].get('title_origin'):
                title = item['payload']['title_origin']
            elif item['payload'].get('videoTitle'):
                title = item['payload']['videoTitle']
            elif item['payload'].get('videoTitleForLatestVideo'):
                title = item['payload']['videoTitleForLatestVideo']

            # Se quiser em uma única linha, pode usar:
            title = (
                item['payload'].get('title_origin')
                or item['payload'].get('videoTitle')
                or item['payload'].get('videoTitleForLatestVideo')
            )

            if type_process == "shortify":
                pass
            else:
                hash_id_str = item['hash_id']
                tz = pytz.timezone(item['payload']['timezone'])
                dt = tz.localize(datetime.strptime(sched_str, '%Y-%m-%d %H:%M:%S'))
            if type_process == "shortify":
                if running_count >= 2:
                    tz = pytz.timezone(item['payload'].get('timezone', 'America/Sao_Paulo'))
                    nova_data = datetime.now(tz) + timedelta(hours=1)
                    new_scheduled_time = nova_data.strftime('%Y-%m-%d %H:%M:%S')

                    # se já foi marcado como reagendado, ignora até o horário
                    if rescheduled_item:
                        logger.info(f"{key} já está reagendado. Pulando até {item.get('scheduled_time')}")
                        return "já está reagendado."
                    # se já foi reagendado pelo menos 1 vez, evita reenviar e-mail
                    if reschedule_count_item >= 1:
                        logger.info(f"{key} já foi reagendado 1 vez (reschedule_count >=1). Pulando envio de e-mail até {item.get('scheduled_time')}")
                        return "já foi reagendado 1 vez"
                    else:
                        SendEmail(
                            user_email_origin=user_email_origin,
                            html_attach_flag=True,
                            email_type="Server Limitation",
                            SMTP_ADM=SMTP_USER,
                            SMTP_PASSWORD=password,
                            SMTP_HOST=host,
                            SMTP_PORT=port,
                            use_tls=use_tls,
                            erro_project="",
                            title_origin=title,
                            new_scheduled_time=new_scheduled_time
                        )
                        shortify_queue.child(key).update({
                            "scheduled_time": new_scheduled_time,
                            "rescheduled": True,
                            "reschedule_count": item.get('reschedule_count', 0) + 1
                        })
                        continue

                # Novo: Verificação do limite de projetos simultâneos do usuário
                if int(projects_running_count) >= int(limite_simultaneo):
                    tz = pytz.timezone(item['payload'].get('timezone', 'America/Sao_Paulo'))
                    nova_data = datetime.now(tz) + timedelta(hours=1)
                    new_scheduled_time = nova_data.strftime('%Y-%m-%d %H:%M:%S')

                    # se já foi reagendado pelo menos 1 vez, evita reenviar e-mail
                    if reschedule_count_item >= 1:
                        logger.info(f"{key} já foi reagendado 1 vez (reschedule_count >=1). Pulando envio de e-mail até {item.get('scheduled_time')}")
                        return "já foi reagendado 1 vez"
                    else:
                        # Envia e-mail informando sobre a limitação do plano
                        SendEmail(
                            user_email_origin=user_email_origin,
                            html_attach_flag=True,
                            email_type="Plan Limitation",
                            SMTP_ADM=SMTP_USER,
                            SMTP_PASSWORD=password,
                            SMTP_HOST=host,
                            SMTP_PORT=port,
                            use_tls=use_tls,
                            erro_project=f"",
                            title_origin="",
                            new_scheduled_time=new_scheduled_time,
                            plan_limit=limite_simultaneo,
                            username=user_email_origin,
                            current_usage=projects_running_count,
                            plan_name=subscription_plan
                        )
                        shortify_queue.child(key).update({
                            "scheduled_time": new_scheduled_time,
                            "rescheduled": True,
                            "reschedule_count": item.get('reschedule_count', 0) + 1
                        })
                        continue

                lista_modelos = [m.strip() for m in limite_AI_models.split(',')]
                if requested_AI_model not in lista_modelos:
                    payload_task['ShortifyMode'] = "Studio-Startup"

                if projects_videos_base_completed_count >= limite_videos_base_for_cuts:
                    tz = pytz.timezone(item['payload'].get('timezone', 'America/Sao_Paulo'))
                    now = datetime.now(tz)

                    # verifica se amanhã já é dia 1
                    if (now + timedelta(days=1)).day == 1:
                        nova_data = now + timedelta(days=1)
                    else:
                        # pula direto pro dia 1 do próximo mês
                        if now.month == 12:  # se dezembro, avança para janeiro do ano seguinte
                            nova_data = tz.localize(datetime(year=now.year + 1, month=1, day=1, hour=0, minute=0, second=0))
                        else:
                            nova_data = tz.localize(datetime(year=now.year, month=now.month + 1, day=1, hour=0, minute=0, second=0))

                    new_scheduled_time = nova_data.strftime('%Y-%m-%d %H:%M:%S')

                    SendEmail(
                        user_email_origin=user_email_origin,
                        html_attach_flag=True,
                        email_type="Monthly Limit Reached",
                        SMTP_ADM=SMTP_USER,
                        SMTP_PASSWORD=password,
                        SMTP_HOST=host,
                        SMTP_PORT=port,
                        use_tls=use_tls,
                        erro_project="",
                        title_origin=title,
                        new_scheduled_time=new_scheduled_time,
                        plan_limit=limite_videos_base_for_cuts,
                        username=user_email_origin,
                        current_usage=projects_videos_base_completed_count,
                        plan_name=subscription_plan
                    )

                    shortify_queue.child(key).update({
                        "scheduled_time": new_scheduled_time,
                        "rescheduled": True,
                        "reschedule_count": item.get('reschedule_count', 0) + 1
                    })
                    continue


                try:
                    user_control_data = user_Control_Panel_ref.get()
                    if not user_control_data or 'project_simultaneo' not in user_control_data:
                        logger.error(f"Dados de controle de usuário ou 'project_simultaneo' não encontrados para a api_key {api_key}. Pulando...")
                        
                    limite_simultaneo = user_control_data['project_simultaneo']
                    subscription_plan = user_control_data['subscription_plan']
                    projects_videos_base_completed_count = user_control_data.get('projects_videos_base_completed', 0) 
                    projects_running_count = user_control_data.get('projects_running', 0) 
                except Exception as e:
                    logger.error(f"Erro ao buscar dados de controle para {api_key}: {e}")


                logger.info(f"Incrementando projects_running para {user_email_origin}")

                novo_valor = min(limite_simultaneo, projects_running_count + 1)
                user_Control_Panel_ref.update({
                    'projects_running': novo_valor
                    })
                user_Control_Panel_ref.update({
                    'projects_videos_base_completed': projects_videos_base_completed_count + 1
                    })





                task = run_shortify_task.delay(item['payload'])
                shortify_queue.child(key).update({
                    "status": "SCHEDULED",
                    "task_id": task.id
                })


                running_count += 1
          
                payload = item['payload']
                payload['task_id'] = task.id
                json_task = {
                    "user_email": user_email,
                    "timezone": payload.get('timezone'),
                    "scheduled_time": sched_str,
                    "task_id": task.id,
                    "yt_channel": payload.get('canal_do_yt'),
                    "mode": payload.get('mode'),
                    "api_key": payload.get('api_key'),
                    "status": "Created",
                    "Success_rate": "0%",
                    "Processing_time": "00:00:00",
                }
                id_task = sched_str.replace(".", "_").replace(":", "_").replace(" ", "_")
                user_tasks_ref.child(id_task).update(json_task)

            elif type_process == "generate_subclip_ai_curation":

                task = run_generate_subclip_ai_curation_task.delay(item['payload'])
                task_id = task.id
                process_queue_ref.child(key).update({
                    "status": "SCHEDULED",
                    "task_id": task_id
                })
                payload = item['payload']
                payload['task_id'] = task_id
                # data['hash_id'] = hash_id
                json_task = {
                    "user_email": user_email,
                    "timezone": payload.get('timezone'),
                    "scheduled_time": item['scheduled_time'],
                    "task_id": task_id,
                    "hash_id": hash_id_str,
                    "type_process": "generate_subclip_ai_curation",
                    "video_id": "None",
                    "status": "Created",
                    "Success_rate": "0%",
                    "Processing_time": "00:00:00",
                }
                create_task(user_email, task_id, json_task, app1)
    
            elif type_process == "audio_transcriber":

                task = run_audio_transcriber_task.delay(item['payload'])
                task_id = task.id
                process_queue_ref.child(key).update({
                    "status": "SCHEDULED",
                    "task_id": task_id
                })
                payload = item['payload']
                payload['task_id'] = task_id
                json_task = {
                    "user_email": user_email,
                    "timezone": payload.get('timezone'),
                    "scheduled_time": item['scheduled_time'],
                    "task_id": task_id,
                    "hash_id": hash_id_str,
                    "type_process": "audio_transcriber",
                    "ASS_ID": "None",
                    "SRT_ID": "None",
                    "status": "Created",
                    "Success_rate": "0%",
                    "Processing_time": "00:00:00",
                }
                create_task(user_email, task_id, json_task, app1)
            
            elif type_process == "thumbnail_vertical_fusion":

                task = run_thumbnail_vertical_fusion_task.delay(item['payload'])
                task_id = task.id
                process_queue_ref.child(key).update({
                    "status": "SCHEDULED",
                    "task_id": task_id
                })
                payload = item['payload']
                payload['task_id'] = task_id
                json_task = {
                    "user_email": user_email,
                    "timezone": payload.get('timezone'),
                    "scheduled_time": item['scheduled_time'],
                    "task_id": task_id,
                    "hash_id": hash_id_str,
                    "type_process": "thumbnail_vertical_fusion",
                    "video_id": "None",
                    "status": "Created",
                    "Success_rate": "0%",
                    "Processing_time": "00:00:00",
                }
                create_task(user_email, task_id, json_task, app1)
    
            elif type_process == "AutoReframe":

                task = run_autoreframe_task.delay(item['payload'])
                task_id = task.id
                process_queue_ref.child(key).update({
                    "status": "SCHEDULED",
                    "task_id": task_id
                })
                payload = item['payload']
                payload['task_id'] = task_id
                json_task = {
                    "user_email": user_email,
                    "timezone": payload.get('timezone'),
                    "scheduled_time": item['scheduled_time'],
                    "task_id": task_id,
                    "hash_id": hash_id_str,
                    "type_process": "AutoReframe",
                    "video_id": "None",
                    "status": "Created",
                    "Success_rate": "0%",
                    "Processing_time": "00:00:00",
                }
                create_task(user_email, task_id, json_task, app1)

        except Exception as e:
            logger.warning(f"Erro ao processar ? {key} {e}")
            shortify_queue.child(key).delete()

    return "Sucess"


@celery_app.task(name="celery_worker.run_shortify_task")
def run_shortify_task(task_params):
    """
    `task_params` é um dicionário com os parâmetros necessários
    """
    inicio = time.time() 
    user_email_origin = task_params.get('user_email')
    filtrer_user_email =  user_email_origin.replace(".", "_") 
    canal_do_yt = task_params.get('canal_do_yt')
    date_time = task_params.get('date_time')
    TiktokAccount = task_params.get('TiktokAccount')
    TiktokAccountCookies = task_params.get('TiktokAccountCookies')
    Cutting_seconds = task_params.get('Cutting_seconds')
    api_key = task_params.get('api_key')
    SubtitleColor = task_params.get('SubtitleColor')
    SubtitleAnimation = task_params.get('SubtitleAnimation')
    SubtitleFontName = task_params.get('SubtitleFontName')
    SubtitleEffects = task_params.get('SubtitleEffects')
    SubtitleFontsize = task_params.get('SubtitleFontsize')
    SubtitleVerticalReference = task_params.get('SubtitleVerticalReference')
    CaptionsColor = task_params.get('CaptionsColor')
    CaptionsFontName = task_params.get('CaptionsFontName')
    CaptionsAlignment = task_params.get('CaptionsAlignment')
    CaptionsFontsize = task_params.get('CaptionsFontsize')
    CaptionsPrimaryColour = task_params.get('CaptionsPrimaryColour')
    CaptionsSecondaryColour = task_params.get('CaptionsSecondaryColour')
    CaptionsOutlineColour = task_params.get('CaptionsOutlineColour')
    CaptionsBackColour = task_params.get('CaptionsBackColour')
    CaptionsBold = task_params.get('CaptionsBold')
    CaptionsItalic = task_params.get('CaptionsItalic')
    CaptionsUnderline = task_params.get('CaptionsUnderline')
    CaptionsOutline = task_params.get('CaptionsOutline')
    CaptionsShadow = task_params.get('CaptionsShadow')
    CaptionsRevealEffectInitialColor = task_params.get('CaptionsRevealEffectInitialColor')
    CaptionsRevealEffectFinalColor = task_params.get('CaptionsRevealEffectFinalColor')
    editiontheme = task_params.get('editiontheme')
    legendstheme = task_params.get('legendstheme')
    latest_enabled = task_params.get('latestEnabled')
    videoTitle = task_params.get('videoTitle')
    secondsScheduleTiktokVideo = task_params.get('secondsScheduleTiktokVideo')
    titleForTiktokCutsEnabled = task_params.get('titleForTiktokCutsEnabled')
    titleForTiktokCuts = task_params.get('titleForTiktokCuts')
    hashtagsForTiktokCutsEnabled = task_params.get('hashtagsForTiktokCutsEnabled')
    hashtagsForTiktokCuts = task_params.get('hashtagsForTiktokCuts')
    StudioMode = task_params.get('ShortifyMode')
    videoTitleForLatestVideo = task_params.get('videoTitleForLatestVideo')
    downloadToPanelEnabled = task_params.get('downloadToPanelEnabled')
    title_origin = task_params.get('title_origin')
    pastedUrl = task_params.get('pastedUrl')
    includeVertical = task_params.get('includeVertical')
    includeHorizontal = task_params.get('includeHorizontal')

    id_task_sheduled = date_time.replace(".", "_").replace(":", "_").replace(" ", "_")
    ref_user_tasks = db.reference(f'user_tasks/{filtrer_user_email}/{id_task_sheduled}', app=app1)
    ref_shortify = db.reference(f'shortify_queue/{id_task_sheduled}', app=app1)
    data = ref_shortify.get()
    status_task = data['status']
    if status_task == 'SCHEDULED':
        return f"uma tarefa com status SCHEDULED por algum motivo esta tentando rodar de novo"
    

    # lock_file_path = os.path.join(os.path.dirname(__file__), "tmp", "uploads")
    # lock_file = os.path.join(lock_file_path, f"upload_{post_id}.lock")
    # if os.path.exists(lock_file):
    #     logger.warning(f"Tarefa para {post_id} já agendada. Ignorando duplicata.")
    #     return "Já agendado"
    # open(lock_file, 'w').close()


    title_origin_for_project = secure_filename(title_origin).replace("-", "").replace("....", "").replace("...", "").replace("..", "").replace(".", "").replace("... - ", "").replace('"????????"', '').replace("...__", "_")
    ref_projects = db.reference(f'projects/{filtrer_user_email}/{title_origin_for_project}', app=appdocs)
    
    if task_params is None:
        raise ValueError("Parametros ausentes.")
    
    logger.info(f"Recebendo title_origin: {title_origin}")
    logger.info("Recebendo parâmetros:")
    logger.info(task_params)

    task_id_user_tasks, task_id_queue_tasks, current_date, hash_id = _running_task_status_fix(
        date_time,
        filtrer_user_email,
        process_flag=False
        )
    if task_id_user_tasks == None:
        logger.info('task_id_user_tasks nao encontrado')
        return
    
    user_Control_Panel_ref = db.reference(f'Users_Control_Panel/{api_key}', app=app1)
    try:
        user_control_data = user_Control_Panel_ref.get()
        if not user_control_data or 'project_simultaneo' not in user_control_data:
            logger.error(f"Dados de controle de usuário ou 'project_simultaneo' não encontrados para a api_key {api_key}. Pulando...")
            
        limite_simultaneo = user_control_data['project_simultaneo']
        subscription_plan = user_control_data['subscription_plan']
        projects_videos_base_completed_count = user_control_data.get('projects_videos_base_completed', 0) 
        projects_running_count = user_control_data.get('projects_running', 0) 
    except Exception as e:
        logger.error(f"Erro ao buscar dados de controle para {api_key}: {e}")

    try:

        shortify_instance = ShortifyAlgo(
            user_Control_Panel_ref=user_Control_Panel_ref,
            includeHorizontal=includeHorizontal,
            includeVertical=includeVertical,
            app1=app1,
            appdocs=appdocs,
            user_email=user_email_origin,
            TiktokAccount=TiktokAccount,
            TiktokAccountCookies=TiktokAccountCookies,
            canal_do_yt=canal_do_yt,
            current_date=current_date,
            date_time=date_time,
            Cutting_seconds=Cutting_seconds,
            secondsScheduleTiktokVideo=secondsScheduleTiktokVideo,
            StudioMode=StudioMode,
            downloadToPanelEnabled=downloadToPanelEnabled,
            task_id=task_id_user_tasks,
            hash_id=hash_id,
            title_origin=title_origin,
            pastedUrl=pastedUrl,
            UPLOAD_URL=UPLOAD_URL,
            api_key=api_key,
            WEBHOOK_URL=WEBHOOK_URL,
            WEBHOOK_ZIP_URL=WEBHOOK_ZIP_URL,
            text_edit_download=None,

            SubtitleColor=SubtitleColor,
            SubtitleAnimation=SubtitleAnimation, 
            SubtitleFontName=SubtitleFontName,
            SubtitleEffects=SubtitleEffects,
            SubtitleFontsize=SubtitleFontsize,
            SubtitleVerticalReference=SubtitleVerticalReference, 


            CaptionsColor=CaptionsColor,
            CaptionsFontName=CaptionsFontName,
            CaptionsAlignment=CaptionsAlignment,
            CaptionsFontsize=CaptionsFontsize, 
            CaptionsPrimaryColour=CaptionsPrimaryColour, 
            CaptionsSecondaryColour=CaptionsSecondaryColour, 
            CaptionsOutlineColour=CaptionsOutlineColour, 
            CaptionsBackColour=CaptionsBackColour, 
            CaptionsBold=CaptionsBold, 
            CaptionsItalic=CaptionsItalic, 
            CaptionsUnderline=CaptionsUnderline, 
            CaptionsOutline=CaptionsOutline, 
            CaptionsShadow=CaptionsShadow, 
            CaptionsRevealEffectInitialColor=CaptionsRevealEffectInitialColor, 
            CaptionsRevealEffectFinalColor=CaptionsRevealEffectFinalColor, 

            legendstheme=legendstheme,
            editiontheme=editiontheme,
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

            lastlongvideo=latest_enabled,
            videoTitleForLatestVideo=videoTitleForLatestVideo,
            lastlongvideotitle=videoTitle,
            titleForTiktokCutsEnabled=titleForTiktokCutsEnabled,
            titleForTiktokCuts=titleForTiktokCuts,
            hashtagsForTiktokCutsEnabled=hashtagsForTiktokCutsEnabled,
            hashtagsForTiktokCuts=hashtagsForTiktokCuts

            
        )

        asyncio.run(shortify_instance.Shortify())


        fim = time.time()  
        processing_time = fim - inicio
        horas, resto = divmod(processing_time, 3600)
        minutos, segundos = divmod(resto, 60)
        tempo_formatado = f"{int(horas):02}:{int(minutos):02}:{int(segundos):02}"

        ref_user_tasks.update({"status": "Completed",
                               "Success_rate": "100%",
                               "Processing_time": tempo_formatado
                               
                               }
        
        )
        ref_shortify.update({"status": "Completed",
                            "Success_rate": "100%",
                            "Processing_time": tempo_formatado
        
        })
        ref_projects.update({"status": "Completed"})
        user_Control_Panel_ref.update({'projects_running': max(0, projects_running_count - 1)})

        SendEmail(
            user_email_origin=user_email_origin,
            html_attach_flag=True,
            email_type="Sucess Project",
            SMTP_ADM=SMTP_USER,
            SMTP_PASSWORD=password,
            SMTP_HOST=host,
            SMTP_PORT=port,
            use_tls=use_tls,
            erro_project="",
            title_origin=title_origin,
            new_scheduled_time=""
        )
        return "Sucess"
    except Exception as erro_project:
        logger.info(erro_project)
        SendEmail(
            user_email_origin=user_email_origin,
            html_attach_flag=True,
            email_type="Failed Project",
            SMTP_ADM=SMTP_USER,
            SMTP_PASSWORD=password,
            SMTP_HOST=host,
            SMTP_PORT=port,
            use_tls=use_tls,
            erro_project=erro_project,
            title_origin=title_origin,
            new_scheduled_time=""
        )
        
        ref_user_tasks.update({"status": "Failed",
                               "error": f"{erro_project}"
                            })
        ref_shortify.update({"status": "Failed",
                             "error": f"{erro_project}"
                            })
        ref_projects.update({"status": "Failed"})
        user_Control_Panel_ref.update({'projects_running': max(0, projects_running_count - 1)})

        logger.info(f"Erro na tarefa run_shortify_task: {str(erro_project)}")
        
        return f"Erro na tarefa run_shortify_task: {str(erro_project)}"
    
 






@celery_app.task(name="celery_worker.run_generate_subclip_ai_curation_task")
def run_generate_subclip_ai_curation_task(task_params):
    """
    `task_params` é um dicionário com os parâmetros necessários
    """

    projectName = task_params.get('projectName')
    user_email = task_params.get('user_email')
    filtrer_user_email =  user_email.replace(".", "_") 
    VIDEO_ID = task_params.get('VIDEO_ID')
    VIDEO_ID_FOR_INPUT = VIDEO_ID.replace("-", "")
    hash_id = task_params.get('hash_id')
    task_id = task_params.get('task_id') 
    hash_id_str = str(hash_id)
    short_hash_id_str = hash_id_str[:8]
    VIDEO_ID_FOR_OUTPUT = hash_id_str[:10]
    start_time = task_params.get('start_time')
    end_time = task_params.get('end_time')
    date_time = task_params.get('date_time')
    timezone = task_params.get('timezone')
    output_filename = task_params.get('output_filename')
    output_filename_str = str(output_filename)
    output_filename_replace = output_filename_str.replace(".mp4", "").replace(".wav", "")
    ref_tasks = db.reference(f'user_tasks/{filtrer_user_email}', app=app1)

    save_path = os.path.join(os.path.dirname(__file__), 
                                "Studio",
                                "WorkEnvironment",
                                "StudioAPI",
                                "generate_subclip_ai_curation",
                                "tmp"
                            )
    os.makedirs(save_path, exist_ok=True)
    
    output_file = os.path.join(
                        save_path, 
                        f"{output_filename_replace}_{VIDEO_ID_FOR_OUTPUT}.mp4"
                    )
    save_file = os.path.join(
                    save_path, 
                    f"{VIDEO_ID_FOR_INPUT}_{short_hash_id_str}.mp4"
                )

    if task_params is None:
        raise ValueError("Parametros ausentes.")
    logger.info(f"Recebendo parâmetros: {task_params}")
    tz = pytz.timezone(timezone)
    os.environ['TZ'] = timezone  
    try:
        time.tzset()  
    except:
        logger.info('except timezone')

    task_id_user_tasks, task_id_process_queue_tasks, current_date, hash_id = _running_task_status_fix(date_time, filtrer_user_email)


    video_input = download_(save_file, VIDEO_ID, filtrer_user_email)


    try:

        output_file_return = MediaCutsStudio_instance.generate_subclip_with_ffmpeg_ai_curation(
                video_input=video_input, 
                start_time=start_time, 
                end_time=end_time, 
                output_filename=output_file
            )
        video_id = upload_(projectName, output_file_return, filtrer_user_email)
        ref_tasks.child(task_id_user_tasks).update({"status": "Completed", "video_id": video_id})
        process_queue_ref.child(task_id_process_queue_tasks).update({"status": "Completed", "video_id": video_id})
        logger.info(f"video_id '{video_id}'")
        return "success"
        
    except Exception as e:
        ref_tasks.child(task_id_user_tasks).update({"status": "Failed"})
        process_queue_ref.child(task_id_process_queue_tasks).update({"status": "Failed"})
        return f"Erro na tarefa run_shortify_task: {str(e)}"
    

@celery_app.task(name="celery_worker.run_audio_transcriber_task")
def run_audio_transcriber_task(task_params):
    """
    `task_params` é um dicionário com os parâmetros necessários
    """

    projectName = task_params.get('projectName')
    user_email = task_params.get('user_email')
    filtrer_user_email =  user_email.replace(".", "_") 
    VIDEO_ID = task_params.get('VIDEO_ID')
    VIDEO_ID_FOR_INPUT = VIDEO_ID.replace("-", "")
    hash_id = task_params.get('hash_id')
    hash_id_str = str(hash_id)
    short_hash_id_str = hash_id_str[:8]
    VIDEO_ID_FOR_OUTPUT = hash_id_str[:10]
    task_id = task_params.get('task_id') 
    date_time = task_params.get('date_time')
    timezone = task_params.get('timezone')
    output_filename = task_params.get('output_filename')
    output_filename_str = str(output_filename)
    output_filename_replace = output_filename_str.replace(".mp4", "").replace(".wav", "")
    ref_tasks = db.reference(f'user_tasks/{filtrer_user_email}', app=app1)

    save_path = os.path.join(os.path.dirname(__file__), 
                                "Studio",
                                "WorkEnvironment",
                                "StudioAPI",
                                "Transcriber",
                                "tmp"
                            )
    os.makedirs(save_path, exist_ok=True)
    
    output_file = os.path.join(
                        save_path, 
                        f"{VIDEO_ID_FOR_INPUT}_{short_hash_id_str}.wav"
                    )
    
    file_srt = os.path.join(save_path, 
                            f"{VIDEO_ID_FOR_INPUT}_{short_hash_id_str}.srt")
    file_ass = os.path.join(save_path, 
                            f"{VIDEO_ID_FOR_INPUT}_{short_hash_id_str}.ass")

    save_file = os.path.join(
                    save_path, 
                    f"{VIDEO_ID_FOR_INPUT}_{short_hash_id_str}.mp4"
                )

    if task_params is None:
        raise ValueError("Parametros ausentes.")
    logger.info(f"Recebendo parâmetros: {task_params}")
    tz = pytz.timezone(timezone)
    os.environ['TZ'] = timezone  
    try:
        time.tzset()  
    except:
        logger.info('except timezone')


    task_id_user_tasks, task_id_process_queue_tasks, current_date, hash_id = _running_task_status_fix(date_time, filtrer_user_email)
    logger.info(f"task_id_user_tasks '{task_id_user_tasks}'...")
    logger.info(f"task_id_process_queue_tasks '{task_id_process_queue_tasks}'...")


    video_input = download_(save_file, VIDEO_ID, filtrer_user_email)

    try:

        transcriber = Audio_Transcriber(
                        model_type=Audio_Transcriber_model_Cuts, 
                        webhook=Audio_Transcriber_webhook,
                        api_key=Audio_Transcriber_api_key,
                        WEBHOOK_URL=Audio_Transcriber_WEBHOOK_URL
                    )
        resultado, total_time_str = transcriber.main(
            path_videofile=video_input, 
            path_file_audio=output_file
                        
            )
        logger.info(f"resultado '{resultado}'")
        MediaCutsStudio_instance.adpte_srt_file(file_path=file_srt)
        flag = transcriber.convert_to_ass(subtitlesrt=file_srt, subtitleass=file_ass)
        logger.info(f"{flag}")
        SRT_ID = upload_(projectName, file_srt, filtrer_user_email)
        ASS_ID = upload_(projectName, file_ass, filtrer_user_email)
        ref_tasks.child(task_id_user_tasks).update({
            "status": "Completed",
            "SRT_ID": SRT_ID,
            "ASS_ID": ASS_ID,

        })
        process_queue_ref.child(task_id_process_queue_tasks).update({
            "status": "Completed",
            "SRT_ID": SRT_ID,
            "ASS_ID": ASS_ID
            })

        logger.info(f"SRT_ID '{SRT_ID}'")
        logger.info(f"ASS_ID '{ASS_ID}'")

        return "success"
        
    except Exception as e:
        ref_tasks.child(task_id_user_tasks).update({"status": "Failed"})
        process_queue_ref.child(task_id_process_queue_tasks).update({"status": "Failed"})
        return f"Erro na tarefa run_shortify_task: {str(e)}"
    

@celery_app.task(name="celery_worker.run_thumbnail_vertical_fusion_task")
def run_thumbnail_vertical_fusion_task(task_params):
    """
    `task_params` é um dicionário com os parâmetros necessários
    """

    projectName = task_params.get('projectName')
    user_email = task_params.get('user_email')
    filtrer_user_email =  user_email.replace(".", "_") 
    VIDEO_ID = task_params.get('VIDEO_ID')
    IMAGE_ID = task_params.get('IMAGE_ID')
    ASS_ID = task_params.get('ASS_ID')
    VIDEO_ID_FOR_INPUT = VIDEO_ID.replace("-", "")
    date_time = task_params.get('date_time')
    timezone = task_params.get('timezone')
    hash_id = task_params.get('hash_id')
    task_id = task_params.get('task_id') 
    hash_id_str = str(hash_id)
    short_hash_id_str = hash_id_str[:8]
    VIDEO_ID_FOR_OUTPUT = hash_id_str[:8]

    output_filename = task_params.get('output_filename')
    SubtitleFontName = task_params.get('SubtitleFontName')
    texto_drawtext = task_params.get('texto_drawtext')
    CaptionsAlignment = task_params.get('CaptionsAlignment')
    SubtitleFontsize = task_params.get('SubtitleFontsize')
    SubtitleColor = task_params.get('SubtitleColor')
    SubtitleVerticalReference = task_params.get('SubtitleVerticalReference')
    ref_tasks = db.reference(f'user_tasks/{filtrer_user_email}', app=app1)


    output_filename_str = str(output_filename)
    output_filename_replace = output_filename_str.replace(".mp4", "").replace(".wav", "")

    save_path = os.path.join(os.path.dirname(__file__), 
                                "Studio",
                                "WorkEnvironment",
                                "StudioAPI",
                                "thumbnail_vertical_fusion",
                                "tmp"
                            )
    os.makedirs(save_path, exist_ok=True)
    
    output_file = os.path.join(
                        save_path, 
                        f"{output_filename_replace}_{VIDEO_ID_FOR_OUTPUT}.mp4"
                    )

    file_ass = os.path.join(save_path, 
                            f"{VIDEO_ID_FOR_INPUT}_{short_hash_id_str}.ass")
    file_image = os.path.join(save_path, 
                            f"{output_filename_replace}.jpg")
    save_file = os.path.join(
                    save_path, 
                    f"{VIDEO_ID_FOR_INPUT}_{short_hash_id_str}.mp4"
                )
    if task_params is None:
        raise ValueError("Parametros ausentes.")
    logger.info(f"Recebendo parâmetros: {task_params}")
    tz = pytz.timezone(timezone)
    os.environ['TZ'] = timezone  
    try:
        time.tzset()  
    except:
        logger.info('except timezone')



    task_id_user_tasks, task_id_process_queue_tasks, current_date, hash_id = _running_task_status_fix(date_time, filtrer_user_email)

    
    video_input = download_(save_file, VIDEO_ID, filtrer_user_email)
    output_miniatura = download_(file_image, IMAGE_ID, filtrer_user_email)
    audio_ass_windows = download_(file_ass, ASS_ID, filtrer_user_email)

    try:

        MediaCutsStudio_instance.theme_VerticalFusion(
            video_cima=video_input,
            imagem_baixo=output_miniatura,
            fonte=SubtitleFontName,
            texto_drawtext=texto_drawtext,
            ass_file=audio_ass_windows,
            saida=output_file,
            CaptionsAlignment=CaptionsAlignment,
            SubtitleFontsize=SubtitleFontsize,
            SubtitleColor=SubtitleColor,
            SubtitleVerticalReference=SubtitleVerticalReference
        )
        file_id_video = upload_(projectName, output_file, filtrer_user_email)

        ref_tasks.child(task_id_user_tasks).update({
            "status": "Completed",
            "video_id": file_id_video,
        })
        process_queue_ref.child(task_id_process_queue_tasks).update({
            "status": "Completed",
            "video_id": file_id_video,
        })

        logger.info(f"video_id '{file_id_video}'")
        return "success"
        
    except Exception as e:
        ref_tasks.child(task_id_user_tasks).update({"status": "Failed"})
        process_queue_ref.child(task_id_process_queue_tasks).update({"status": "Failed"})
        return f"Erro na tarefa run_shortify_task: {str(e)}"
    

@celery_app.task(name="celery_worker.run_autoreframe_task")
def run_autoreframe_task(task_params):
    """
    `task_params` é um dicionário com os parâmetros necessários
    """

    projectName = task_params.get('projectName')
    user_email = task_params.get('user_email')
    filtrer_user_email =  user_email.replace(".", "_") 
    VIDEO_ID = task_params.get('VIDEO_ID')
    ASS_ID = task_params.get('ASS_ID')
    VIDEO_ID_FOR_INPUT = VIDEO_ID.replace("-", "")
    date_time = task_params.get('date_time')
    timezone = task_params.get('timezone')
    hash_id = task_params.get('hash_id')
    task_id = task_params.get('task_id') 
    hash_id_str = str(hash_id)
    short_hash_id_str = hash_id_str[:8]
    VIDEO_ID_FOR_OUTPUT = hash_id_str[:10]
    output_filename = task_params.get('output_filename')
    SubtitleFontName = task_params.get('SubtitleFontName')
    CaptionsFontsize = task_params.get('CaptionsFontsize')
    CaptionsColor = task_params.get('CaptionsColor')
    CaptionsAlignment = task_params.get('CaptionsAlignment')
    SubtitleFontsize = task_params.get('SubtitleFontsize')
    SubtitleColor = task_params.get('SubtitleColor')
    SubtitleVerticalReference = task_params.get('SubtitleVerticalReference')
    ref_tasks = db.reference(f'user_tasks/{filtrer_user_email}', app=app1)


    YOLO_MODEL = os.path.join(
        os.path.dirname(__file__), 
        "Studio",
        "Models", "Yollo",
        "yolov11n-face.pt"#"yolov12n-face.pt"
    ) 
    output_filename_str = str(output_filename)
    output_filename_replace = output_filename_str.replace(".mp4", "").replace(".wav", "")

    save_path = os.path.join(os.path.dirname(__file__), 
                                "Studio",
                                "WorkEnvironment",
                                "StudioAPI",
                                "AutoReframe",
                                "tmp"
                            )
    os.makedirs(save_path, exist_ok=True)
    
    output_file = os.path.join(
                        save_path, 
                        f"{output_filename_replace}_{short_hash_id_str}.mp4"
                    )

    file_ass = os.path.join(save_path, 
                            f"{VIDEO_ID_FOR_INPUT}_{short_hash_id_str}.ass")

    save_file = os.path.join(
                    save_path, 
                    f"{VIDEO_ID_FOR_INPUT}_{short_hash_id_str}.mp4"
                )
    if task_params is None:
        raise ValueError("Parametros ausentes.")
    logger.info(f"Recebendo parâmetros: {task_params}")
    tz = pytz.timezone(timezone)
    os.environ['TZ'] = timezone  
    try:
        time.tzset()  
    except:
        logger.info('except timezone')


    task_id_user_tasks, task_id_process_queue_tasks, current_date, hash_id = _running_task_status_fix(date_time, filtrer_user_email)


    video_input = download_(save_file, VIDEO_ID, filtrer_user_email)
    audio_ass_windows = download_(file_ass, ASS_ID, filtrer_user_email)

    try:

        if not Path(YOLO_MODEL).exists():
            logger.info(f"AVISO: O modelo YOLO '{YOLO_MODEL}' não foi encontrado.")
            logger.info(f"Tentando baixar '{YOLO_MODEL}'...")
            try:
                YOLO(YOLO_MODEL) 
                logger.info(f"Modelo '{YOLO_MODEL}' baixado com sucesso.")
            except Exception as e:
                logger.info(f"ERRO: Falha ao baixar o modelo YOLO '{YOLO_MODEL}'. Por favor, baixe-o manualmente.")
                logger.info(f"Você pode tentar 'pip install ultralytics --upgrade' e depois executar 'python -c \"from ultralytics import YOLO; YOLO(\'{YOLO_MODEL}\')\"'")
                exit()
        try:
            reframe_processor = AutoReframe(
                ass_file_path=audio_ass_windows,
                input_video_path=video_input,
                output_video_mp4=output_file,
                text_overlay=" ",
                padding_x_ratio_left = 0.0,   
                padding_x_ratio_right = 0.0, 
                padding_y_ratio_top = 0.0,   
                padding_y_ratio_bottom = 0.0,
                fixed_padding_x_left = 70,   
                fixed_padding_x_right = 70,    
                fixed_padding_y_top = 100, 
                fixed_padding_y_bottom = 100,
                font_path=SubtitleFontName,
                captions_alignment=CaptionsAlignment,
                captions_fontsize=CaptionsFontsize,
                captions_color=CaptionsColor,
                subtitle_fontsize=SubtitleFontsize,
                subtitle_fontcolor=SubtitleColor,
                SubtitleVerticalReference=SubtitleVerticalReference,

                yolo_model_path=YOLO_MODEL,
                show_preview=False,
                dockerffmpegGPU=True,
            )
            reframe_processor.run()
        except Exception as e:
            logger.info(f"Um erro inesperado ocorreu: {e}")

        file_id_video = upload_(projectName, output_file, filtrer_user_email)

        ref_tasks.child(task_id_user_tasks).update({
            "status": "Completed",
            "video_id": file_id_video,
        })
        process_queue_ref.child(task_id_process_queue_tasks).update({
            "status": "Completed",
            "video_id": file_id_video,
        })

        logger.info(f"video_id '{file_id_video}'")
        return "success"
        
    except Exception as e:
        ref_tasks.child(task_id_user_tasks).update({"status": "Failed"})
        process_queue_ref.child(task_id_process_queue_tasks).update({"status": "Failed"})
        return f"Erro na tarefa run_shortify_task: {str(e)}"
    



def _running_task_status_fix(scheduled_time_str, filtrer_user_email, process_flag=True):
    date_str = None
    task_id = None
    hash_id = None
    id_task = scheduled_time_str.replace(".", "_").replace(":", "_").replace(" ", "_")
    real_filtrer_user_email = filtrer_user_email.replace(".", "_")
    if process_flag == True:
        ref_queue = db.reference(f'process_queue/{id_task}', app=app1)
        queue = ref_queue.get() or {}
        date_str = queue.get("scheduled_time")
        task_id =  queue.get("task_id")
        hash_id =  queue.get("hash_id")
        ref_queue.update({"status": "Running"})
    else:
        ref_shortify = db.reference(f'shortify_queue/{id_task}', app=app1)
        shortify = ref_shortify.get() or {}
        date_str = shortify.get("scheduled_time")
        task_id =  shortify.get("task_id")
        hash_id =  shortify.get("hash_id")
        ref_shortify.update({"status": "Running"})

    id_task_scheduled_time = scheduled_time_str.replace(".", "_").replace(":", "_").replace(" ", "_")
    ref_tasks = db.reference(f'user_tasks/{real_filtrer_user_email}/{id_task_scheduled_time}', app=app1)
    short_data = ref_tasks.get()
    if short_data.get('status') in ['Running', 'Completed']:
        logger.info(f"Post {task_id} já está com status “{short_data['status']}”, evitando duplicata.")
        return task_id, id_task, date_str, hash_id
    logger.info(f"task {task_id} marcado como EM_ANDAMENTO com sucesso.")
    ref_tasks.update({"status": "Running"})
    return task_id, id_task, date_str, hash_id

def _valid_hash(scheduled_time, hash_db):
    scheduled_time_str = str(scheduled_time)
    hash_obj = hashlib.sha256(scheduled_time_str.encode())
    hash_id_origin = hash_obj.hexdigest()
    hash_id = hash_db
    logger.info(f"hash_id? {hash_id}")
    logger.info(f"hash_id_origin? {hash_id_origin}")
    if hash_id == hash_id_origin:
        logger.info(f"hash_id sao iguais")
        return True
    return None

def download_(save_path: str, VIDEO_ID: str, USER_ID_FOR_TEST: str) -> str:
    url = f"{UPLOAD_URL_VIDEOMANAGER}/api/videos/{VIDEO_ID}"
    headers={
        "X-User-Id": USER_ID_FOR_TEST
    }
    try:
        with requests.get(url, headers=headers, stream=True, timeout=120) as resp:
            resp.raise_for_status()
            with open(save_path, "wb") as f:
                for chunk in resp.iter_content(8192):
                    if chunk:
                        f.write(chunk)
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Falha ao baixar vídeo: {e}") from e
    return save_path


def upload_(name_project, VIDEO_FILE_PATH, USER_ID_FOR_TEST):
    
    video_metadata = {
        "projectName": name_project,
        "type_project": "files",

    }

    # --- Verificações Iniciais ---
    if not os.path.exists(VIDEO_FILE_PATH):
        logger.info(f"Erro: O arquivo '{VIDEO_FILE_PATH}' não foi encontrado.")
        logger.info("Por favor, crie um arquivo MP4 com este nome ou ajuste o caminho.")
        exit()

    try:
        with open(VIDEO_FILE_PATH, 'rb') as video_file:
            files = {
                'file': (os.path.basename(VIDEO_FILE_PATH), video_file, 'video/mp4')
            }
            data = {
                'metadata': json.dumps(video_metadata) # Converte o dicionário de metadados para uma string JSON
            }
            headers = {
                'X-User-Id': USER_ID_FOR_TEST 
            }
            logger.info(f"Tentando enviar '{VIDEO_FILE_PATH}' para {UPLOAD_URL}...")
            logger.info(f"Com metadados: {json.dumps(video_metadata, indent=2)}")
            response = requests.post(UPLOAD_URL, files=files, data=data, headers=headers)

            if response.status_code == 201:
                logger.info("\nUpload bem-sucedido!")
                logger.info("Resposta do servidor:")
                logger.info(json.dumps(response.json(), indent=2))
                payload = response.json()
                VIDEO_ID = payload['video_id']
                logger.info(f"video_id: {VIDEO_ID}")
                return VIDEO_ID
            else:
                logger.info(f"\nErro no upload: Código de status {response.status_code}")
                logger.info("Resposta do servidor:")
                try:
                    logger.info(json.dumps(response.json(), indent=2))
                except json.JSONDecodeError:
                    logger.info(response.text) # Se a resposta não for JSON
                logger.info("\nCertifique-se de que seu servidor Flask está rodando e o endpoint está acessível.")
                logger.info("Verifique também se o 'USER_ID_FOR_TEST' e o 'UPLOAD_URL' estão corretos.")

    except FileNotFoundError:
        logger.info(f"Erro: O arquivo '{VIDEO_FILE_PATH}' não foi encontrado.")
    except requests.exceptions.ConnectionError:
        logger.info("Erro de conexão: O servidor não está acessível.")
        logger.info("Certifique-se de que o backend Flask está rodando em 'http://localhost:5000'.")
    except Exception as e:
        logger.info(f"Ocorreu um erro inesperado: {e}")

# @celery_app.task(name="celery_worker.run_instagram_uploader_task")
# def run_instagram_uploader_task(task_params):
#     """
#     Essa função encapsula a execução do InstagramUploader.
#     `task_params` é um dicionário com os parâmetros necessários
#     """
#     user_email = task_params.get('user_email')
#     filtrer_user_email =  user_email.replace(".", "") 
#     ig_username = task_params.get('ig_username')
#     ig_password = task_params.get('ig_password')
#     date_time = task_params.get('date_time')
#     timezone = task_params.get('timezone')
#     api_key = task_params.get('api_key')
#     upload_video = task_params.get('upload_video')
#     upload_image = task_params.get('upload_image')
#     title = task_params.get('title')
#     description = task_params.get('description')
#     tags = task_params.get('tags')

#     file_b64 = task_params.get('file_bytes')
#     if file_b64:
#         file_bytes = base64.b64decode(file_b64)
#     else:
#         raise ValueError("Não recebi nenhum 'file_bytes'")

#     # Detecta tipo de imagem
#     img_type = imghdr.what(None, h=file_bytes) 
#     if not img_type:
#         raise ValueError("Formato de imagem não reconhecido")

#     # Cria pasta temporária
#     UPLOAD_DIR = os.path.join(os.getcwd(), "tmp_uploads")
#     os.makedirs(UPLOAD_DIR, exist_ok=True)

#     # Gera nome com extensão correta
#     filename = secure_filename(f"{user_email}_{int(time.time())}.{img_type}")
#     file_path = os.path.join(UPLOAD_DIR, filename)

#     # Escreve o arquivo
#     with open(file_path, "wb") as f:
#         f.write(file_bytes)
#     try:
#         if task_params is None:
#             raise ValueError("Parametros ausentes.")
#         # logger.info(f"Recebendo parâmetros:{task_params}")
#         tz = pytz.timezone(timezone)
#         os.environ['TZ'] = timezone  
#         try:
#             time.tzset() 
#         except:
#             logger.error('except timezone')
#         now = datetime.now(tz)
#         current_date = None
#         if isinstance(date_time, str):
#             date_time = [date_time]
#         for date_str in date_time:
#             try:
#                 scheduled_time_naive = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
#                 scheduled_time = tz.localize(scheduled_time_naive)
#                 if scheduled_time - timedelta(seconds=65) <= now <= scheduled_time + timedelta(seconds=65):
#                     current_date = date_str
#                     logger.info(f"Data correspondente encontrada! {current_date}")
#                     break
#             except ValueError as e:
#                 logger.error(f"Erro ao converter a data '{date_str}': {e}")

#         if not current_date:
#             logger.warning("Nenhuma data corresponde ao horário atual dentro do intervalo de 65s.")
#             return      

#         if upload_image == "true" or upload_image == "True":
#             upload_image = True
#         elif upload_image == "false" or upload_image == "False":
#             upload_image = False

#         if upload_video == "true" or upload_video == "True":
#             upload_video = True
#         elif upload_video == "false" or upload_video == "False":
#             upload_video = False

#         InstagramUploader_instance = GramFlow(
#                                             username=ig_username, 
#                                             password=ig_password,
#                                             webhook_flag=True,
#                                             gmail_flag=False,
#                                             docker_flag=True,
#                                             api_key=api_key
#                                             )
#         InstagramUploader_instance.main(
#             file_path=file_path,
#             upload_image=upload_image,
#             upload_video=upload_video,
#             title=title, 
#             description=description, 
#             tags=tags
#         )
#         return "Instagram Uploader Sucess"
#     except Exception as e:
#         ref_tasks = db.reference(f'user_tasks/{filtrer_user_email}', app=app1)
#         tasks = ref_tasks.get()  
#         if tasks:
#             for task_id, task_data in tasks.items():
#                 scheduled_time = task_data.get("scheduled_time")
#                 logger.info(scheduled_time)
#                 if str(scheduled_time) == str(current_date):
#                     ref_tasks.child(task_id).update({"status": "Failed"})

#         return f"Erro na tarefa run_instagram_uploader_task: {str(e)}"
    
# @celery_app.task(name="celery_worker.process_instagram_uploader_queue")
# def process_instagram_uploader_queue():
#     all_items = instagramUploader_queue.get() or {}
#     items = {
#         key: item
#         for key, item in all_items.items()
#         if item.get('status') == 'PENDING'
#     }

#     for key, item in items.items():
#         # print(item['payload'])
#         user = item['user_email']
#         user_email = user.replace(".", "_")
#         sched_str = item['scheduled_time']
#         tz = pytz.timezone(item['payload']['timezone'])
#         dt = tz.localize(datetime.strptime(sched_str, '%Y-%m-%d %H:%M:%S'))
#         start = dt - timedelta(minutes=30)
#         end   = dt + timedelta(minutes=30)
#         ref_tasks = db.reference(f'user_tasks/{user_email}', app=app1)
#         all_tasks = ref_tasks.get() or {}
#         tasks = {
#             tid: tdata
#             for tid, tdata in all_tasks.items()
#             if (
#                 start <= tz.localize(datetime.strptime(
#                     tdata.get('scheduled_time'),
#                     '%Y-%m-%d %H:%M:%S'
#                 )) <= end
#             )
#             and tdata.get('status') != 'Completed'
#         }
#         logger.info(tasks)
#         if tasks:
#             instagramUploader_queue.child(key).update({"status": "CONFLICT"})
#             send_to_webhook(item['payload']['api_key'], "finish_timer_loader", "None", "yellow")
#         else:
#             task = run_instagram_uploader_task.apply_async(
#                 args=[item['payload']],
#                 eta=dt
#             )
#             task_id = task.id
#             instagramUploader_queue.child(key).update({
#                 "status": "SCHEDULED",
#                 "task_id": task_id
#             })
#             hash_str = hashlib.sha256(f"{item['scheduled_time']}".encode()).hexdigest()
#             json_task = {
#                 "user_email": user_email,
#                 "timezone": item['payload']['timezone'],
#                 "scheduled_time": item['scheduled_time'],
#                 "hash_task": hash_str,
#                 "task_id": task_id,
#                 "ig_username": item['payload']['ig_username'],
#                 "ig_password": item['payload']['ig_password'],
#                 "upload_video": item['payload']['upload_video'],
#                 "upload_image": item['payload']['upload_image'],
#                 "title": item['payload']['title'],
#                 "description": item['payload']['description'],
#                 "file_bytes": item['payload']['file_bytes'],
#                 "api_key": item['payload']['api_key'],
#                 "status": "Created",
#                 "Success_rate": "0%",
#                 "Processing_time": "00:00:00",
#             }
#             create_task(user_email, task_id, json_task, app1)
#             send_to_webhook(item['payload']['api_key'], "finish_timer_loader", "None", "yellow")
    
#     return "process_instagram_uploader_queue Sucess"



































































