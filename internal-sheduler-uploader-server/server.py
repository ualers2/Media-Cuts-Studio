# uploadmediabulk.py
from flask import Flask, render_template, Response, request, jsonify, session, redirect,send_from_directory,  url_for
from flask_cors import CORS  
import time
from dotenv import load_dotenv
import os
import logging
import uuid
from firebase_admin import db
from datetime import datetime, timedelta
import json
from flask_limiter.util import get_remote_address
from werkzeug.formparser import parse_form_data
from werkzeug.utils import secure_filename 
import re
import shutil
from asgiref.wsgi import WsgiToAsgi

from Modules.upload_ import upload_

app = Flask(__name__)
asgi_app = WsgiToAsgi(app)
app.secret_key = 'sua_chave_secreta'  
app.permanent_session_lifetime = timedelta(minutes=60)  

diretorio_script = os.path.dirname(os.path.abspath(__file__)) 

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
os.makedirs(os.path.join(diretorio_script, 'Logs'), exist_ok=True)
file_handler = logging.FileHandler(os.path.join(diretorio_script, 'Logs', 'internaluploadmediabulk.log'))
file_handler.setFormatter(formatter)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)


@app.route('/')
def index():
    return jsonify({"message": "#1 Upload multiplos arquivos funcionando!"})

@app.route('/api/upload-media-bulk', methods=['POST'])
def upload_media_bulk():
    """Upload múltiplos arquivos sem carregar na memória e retorna tokens/ids para cada arquivo"""
    import hashlib, time, requests

    batch_id = hashlib.sha256(str(time.time()).encode()).hexdigest()[:16].replace(".", "")

    try:
        stream, form, files = parse_form_data(request.environ)
        
        if not files or 'files[]' not in files:
            return jsonify({"error": "Nenhum arquivo enviado. Esperado 'files[]'."}), 400
        
        files_list = files.getlist('files[]')
        if not files_list:
            return jsonify({"error": "Nenhum arquivo válido na requisição."}), 400
        
        temp_files_info = []
        files_response = []
        logger.info(f"(ID: {batch_id})")
        local_path = os.path.join(diretorio_script, "tmp", "uploads")
        if os.path.exists(local_path):
            shutil.rmtree(local_path)
        os.makedirs(local_path, exist_ok=True)
        contador = 0
        for i, file_storage in enumerate(files_list):
            if file_storage.filename:
                safe_name = secure_filename(file_storage.filename)
                temp_path = os.path.join(local_path, safe_name)
                logger.info(f"processamento {contador}/{len(files_list)} arquivos")

                with open(temp_path, 'wb') as temp_file:
                    while True:
                        chunk = file_storage.stream.read(2024 * 1024)  # 2mb chunks
                        if not chunk:
                            break
                        temp_file.write(chunk)

                TOKEN_ID = upload_(batch_id, temp_path, "freitasalexandre810@gmail_com")
                logger.info(f"TOKEN_ID {TOKEN_ID}")

                try:
                    os.remove(temp_path)
                    logger.info(f"Arquivo temporário removido: {temp_path}")
                except Exception as e:
                    logger.warning(f"Falha ao remover arquivo temporário {temp_path}: {e}")


                files_response.append({
                    "original_filename": file_storage.filename,
                    "safe_filename": safe_name,
                    "token_id": TOKEN_ID,
                    "batch_id": batch_id,

                    "mimetype": file_storage.mimetype or 'application/octet-stream'
                })

                temp_files_info.append((temp_path, file_storage.filename, file_storage.mimetype or 'application/octet-stream'))
            contador += 1

        logger.info(f"{len(temp_files_info)} arquivos recebidos e processados !")

        response_data = {
            "message": f"{len(temp_files_info)} arquivos recebidos e processados !",
            "status": "processing",
            "check_status_url": f"/api/upload-status/{batch_id}",
            # lista com map filename -> token
            "files": files_response
        }
        
        return jsonify(response_data), 202
        
    except Exception as e:
        logger.error(f"Erro processando upload bulk: {e}", exc_info=True)
        return jsonify({"error": f"Erro processando arquivos: {str(e)}"}), 500
    

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=4242)