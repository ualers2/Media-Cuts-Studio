import os
from dotenv import load_dotenv
diretorio_script = os.path.dirname(os.path.abspath(__file__)) 


load_dotenv(os.path.join(diretorio_script, "../", "Keys", "env.env")) # Carrega variáveis de ambiente do .env

class Config:
    # Configurações do Flask
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', '')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', '/') 

    # Configurações do Celery
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', '')
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', '')
    CELERY_TASK_TRACK_STARTED = True

    # Configurações do Firebase
    FIREBASE_SERVICE_ACCOUNT_KEY_PATH = os.environ.get('FIREBASE_SERVICE_ACCOUNT_KEY_PATH', 'firebase-service-account.json')
    FIREBASE_DATABASE_URL = os.environ.get('FIREBASE_DATABASE_URL', '')
    FIREBASE_DB_URL = os.environ.get('FIREBASE_DATABASE_URL', '')  

    # Configurações do YouTube API (caminhos para arquivos dentro do container)
    YOUTUBE_CLIENT_SECRETS_BASE_PATH = os.environ.get('YOUTUBE_CLIENT_SECRETS_BASE_PATH', '')
    YOUTUBE_TOKEN_BASE_PATH = os.environ.get('YOUTUBE_TOKEN_BASE_PATH', '')

    # Certifique-se de que a pasta de uploads exista
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
