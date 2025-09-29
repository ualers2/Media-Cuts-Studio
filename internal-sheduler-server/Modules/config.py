import os
from dotenv import load_dotenv
diretorio_script = os.path.dirname(os.path.abspath(__file__)) 
load_dotenv(os.path.join(diretorio_script, "../", "Keys", "keys.env")) 

class Config:
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', '/') 
    CELERY_TASK_TRACK_STARTED = True
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
