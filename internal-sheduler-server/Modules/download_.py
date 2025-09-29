# Internal-server\.py
import os
import requests
import logging
import time

diretorio_script = os.path.dirname(os.path.abspath(__file__)) 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
os.makedirs(os.path.join(os.path.dirname(__file__), '../',  "Logs"), exist_ok=True)
file_handler = logging.FileHandler(os.path.join(diretorio_script, '../', 'Logs', 'download_.log'))
file_handler.setFormatter(formatter)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def download_(UPLOAD_URL, save_path, PROJECT_NAME, VIDEO_ID, USER_ID_FOR_TEST, max_retries=3) -> str:
    """
    Faz o download de um vídeo usando o endpoint otimizado de performance.
    Endpoint: /api/projects/<project_name>/videos/<video_id>/download

    Args:
        UPLOAD_URL (str): URL base do servidor Flask
        save_path (str): Caminho local para salvar o arquivo
        PROJECT_NAME (str): Nome do projeto
        VIDEO_ID (str): ID do vídeo
        USER_ID_FOR_TEST (str): ID do usuário autenticado (passado no header)

    Returns:
        str: Caminho local do arquivo baixado
    """
    UPLOAD_URL_BASE = "https://videomanager.api.mediacutsstudio.com" 
    
    url = f"{UPLOAD_URL_BASE}/api/projects/{PROJECT_NAME}/videos/{VIDEO_ID}/download"
    headers = {
        "X-User-Id": USER_ID_FOR_TEST,
    }
    logger.info(f"download in progress {save_path}")

    for attempt in range(1, max_retries + 1):
        try:
            resume_byte_pos = os.path.getsize(save_path) if os.path.exists(save_path) else 0
            if resume_byte_pos > 0:
                headers["Range"] = f"bytes={resume_byte_pos}-"
                mode = "ab"
                logger.warning(f"Retomando download a partir de {resume_byte_pos} bytes")
            else:
                mode = "wb"

            with requests.get(url, headers=headers, stream=True, timeout=120) as resp:
                resp.raise_for_status()

                with open(save_path, mode) as f:
                    for chunk in resp.iter_content(1024 * 512):  # 512 KB
                        if chunk:
                            f.write(chunk)

            logger.info(f"download success {save_path}")
            return save_path

        except (requests.exceptions.RequestException, requests.exceptions.ChunkedEncodingError) as e:
            logger.error(f"Tentativa {attempt}/{max_retries} falhou: {e}")
            time.sleep(3)  # espera antes de tentar de novo

    raise RuntimeError(f"Falha ao baixar vídeo após {max_retries} tentativas: {url}")