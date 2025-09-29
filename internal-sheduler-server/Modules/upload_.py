# Substituir /app/Modules/upload_.py 
import os
import json
import requests
import logging
import tempfile
import shutil
from typing import IO
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

CHUNK_SIZE = 1024 * 1024  # 1MB por chunk para streaming

diretorio_script = os.path.dirname(__file__)
os.makedirs(os.path.join(diretorio_script, '../', 'Logs'), exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler(os.path.join(diretorio_script, '../', 'Logs', 'upload_py.log'))
file_handler.setFormatter(formatter)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

def _guess_filename_from_fileobj(fileobj):
    name = getattr(fileobj, "name", None)
    if isinstance(name, str):
        return os.path.basename(name)
    name2 = getattr(fileobj, "filename", None)
    if isinstance(name2, str):
        return os.path.basename(name2)
    return None

def _get_content_length(fileobj: IO):
    try:
        cur = fileobj.tell()
        fileobj.seek(0, os.SEEK_END)
        size = fileobj.tell()
        fileobj.seek(cur, os.SEEK_SET)
        return size
    except Exception:
        return None

def _create_session(max_retries=5, backoff_factor=1):
    session = requests.Session()
    retries = Retry(
        total=max_retries,
        backoff_factor=backoff_factor,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=frozenset(['HEAD', 'GET', 'OPTIONS', 'POST', 'PUT']),
        raise_on_status=False,
        respect_retry_after_header=True
    )
    adapter = HTTPAdapter(max_retries=retries, pool_connections=10, pool_maxsize=10)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session

def upload_(name_project, VIDEO_FILE_PATH, USER_ID_FOR_TEST,
            type_project="files",
            title='',
            description='',
            hashtags='',
            minutagemdeInicio='',
            minutagemdeFim='',
            urltumbnail='',
            justificativa='',
            sentimento_principal='',
            potencial_de_viralizacao=''):
    """
    Versão streaming-first do upload:
      - path (string) -> multipart
      - fileobj seekable -> multipart (fileobj)
      - fileobj não-seekable -> STREAM RAW direto para /api/upload-video (X-Filename + X-Metadata)
      - fallback: temp file (apenas em caso extremo)
    """
    UPLOAD_URL = "https://videomanager.api.mediacutsstudio.com"
    session = _create_session(max_retries=5, backoff_factor=1)

    if type_project == "files":
        video_metadata = {
            "projectName": name_project,
            "type_project": type_project,
        }
    else:
        video_metadata = {
            "projectName": name_project,
            "type_project": "video",
            "title": title,
            "description": description,
            "hashtags": hashtags,
            "minutagemdeInicio": minutagemdeInicio,
            "minutagemdeFim": minutagemdeFim,
            "urltumbnail": urltumbnail,
            "justificativa": justificativa,
            "sentimento_principal": sentimento_principal,
            "potencial_de_viralizacao": potencial_de_viralizacao
        }

    # ----- Caso 1: caminho de arquivo (string path) -> multipart (recomendado) -----
    if isinstance(VIDEO_FILE_PATH, str):
        if not os.path.exists(VIDEO_FILE_PATH):
            logger.info(f"Erro: O arquivo '{VIDEO_FILE_PATH}' não foi encontrado.")
            return None

        try:
            with open(VIDEO_FILE_PATH, 'rb') as video_file:
                files = {
                    'file': (os.path.basename(VIDEO_FILE_PATH), video_file, 'video/mp4')
                }
                data = {
                    'metadata': json.dumps(video_metadata)
                }
                headers = {
                    'X-User-Id': USER_ID_FOR_TEST
                }
                logger.info(f"Tentando enviar '{VIDEO_FILE_PATH}' para {UPLOAD_URL} (multipart)...")
                logger.info(f"Com metadados: {json.dumps(video_metadata, indent=2)}")
                response = session.post(f"{UPLOAD_URL}/api/upload-video",
                                        files=files,
                                        data=data, headers=headers,
                                        timeout=3600)

                if response.status_code in (200, 201):
                    logger.info("Upload bem-sucedido (multipart).")
                    payload = response.json()
                    return payload.get('video_id') or payload.get('item_id') or None
                else:
                    logger.warning(f"Erro no upload (multipart): Código {response.status_code}")
                    try:
                        logger.warning(json.dumps(response.json(), indent=2))
                    except Exception:
                        logger.warning(response.text)
                    return None

        except requests.exceptions.SSLError as e:
            logger.exception("SSLError durante upload multipart: %s", e)
            return None
        except Exception as e:
            logger.exception(f"Erro ao enviar arquivo (multipart): {e}")
            return None

    # ----- Caso 2/3: fileobj (dict ou file-like) -----
    fileobj = None
    filename = None
    if isinstance(VIDEO_FILE_PATH, dict) and 'fileobj' in VIDEO_FILE_PATH:
        fileobj = VIDEO_FILE_PATH['fileobj']
        filename = VIDEO_FILE_PATH.get('filename') or _guess_filename_from_fileobj(fileobj) or 'upload.bin'
    elif hasattr(VIDEO_FILE_PATH, 'read'):
        fileobj = VIDEO_FILE_PATH
        filename = _guess_filename_from_fileobj(fileobj) or 'upload.bin'
    else:
        logger.info("Parâmetro VIDEO_FILE_PATH inválido. Deve ser path (string), file-like ou dict {'fileobj', 'filename'}.")
        return None

    # tenta obter tamanho e saber se é seekable
    content_length = _get_content_length(fileobj)
    seekable = True
    try:
        seekable = fileobj.seekable()
    except Exception:
        seekable = False

    headers_base = {'X-User-Id': USER_ID_FOR_TEST}

    # Se fileobj tem tamanho/seekable, faça multipart usando fileobj (não raw stream)
    if content_length is not None and seekable:
        try:
            # garante posição no início
            fileobj.seek(0)
            files = {'file': (filename, fileobj, 'video/mp4')}
            logger.info(f"Tentando enviar stream '{filename}' via multipart (fileobj seekable) para {UPLOAD_URL} ...")
            logger.info(f"Com metadados: {json.dumps(video_metadata, indent=2)}, Content-Length: {content_length}")
            response = session.post(f"{UPLOAD_URL}/api/upload-video",
                                    files=files,
                                    data={'metadata': json.dumps(video_metadata)},
                                    headers=headers_base,
                                    timeout=3600)
            if response.status_code in (200, 201):
                logger.info("Upload bem-sucedido (multipart, fileobj).")
                payload = response.json()
                return payload.get('video_id') or payload.get('item_id') or None
            else:
                logger.warning(f"Erro no upload (multipart, fileobj): Código {response.status_code}")
                try:
                    logger.warning(json.dumps(response.json(), indent=2))
                except Exception:
                    logger.warning(response.text)
                return None
        except requests.exceptions.SSLError as e:
            logger.exception("SSLError durante upload multipart (fileobj): %s", e)
            return None
        except Exception as e:
            logger.exception(f"Erro no upload multipart (fileobj): {e}")
            return None

    # -------------------- NOVO: stream RAW direto (sem gravar tmp) --------------------
    # Quando não-seekable, fazemos POST streaming puro para o servidor que aceita X-Filename + X-Metadata
    try:
        def chunk_generator(f):
            while True:
                chunk = f.read(CHUNK_SIZE)
                if not chunk:
                    break
                # requests aceita bytes generator como corpo
                yield chunk

        headers = headers_base.copy()
        headers.update({
            'X-Filename': filename,
            'X-Metadata': json.dumps(video_metadata),
            'Content-Type': 'application/octet-stream',
            # Forçar chunked transfer para evitar Content-Length
            'Transfer-Encoding': 'chunked'
        })

        logger.info(f"Tentando enviar stream não-seekable '{filename}' via RAW streaming para {UPLOAD_URL} ...")
        logger.info(f"Com metadados: {json.dumps(video_metadata, indent=2)}")
        # nota: data=generator -> requests usará streaming e não carrega tudo na memória.
        response = session.post(f"{UPLOAD_URL}/api/upload-video",
                                data=chunk_generator(fileobj),
                                headers=headers,
                                timeout=3600)
        if response.status_code in (200, 201):
            logger.info("Upload bem-sucedido (streaming RAW).")
            try:
                payload = response.json()
            except Exception:
                payload = {}
            return payload.get('video_id') or payload.get('item_id') or None
        else:
            logger.warning(f"Erro no upload (streaming RAW): Código {response.status_code}")
            try:
                logger.warning(json.dumps(response.json(), indent=2))
            except Exception:
                logger.warning(response.text)
            # não retorna ainda, tenta fallback abaixo
    except requests.exceptions.SSLError as e:
        logger.exception("SSLError durante upload streaming RAW: %s", e)
    except Exception as e:
        logger.exception(f"Erro no upload streaming RAW: {e}")

    # -------------------- Fallback (opcional) -> gravar em temp file e enviar (último recurso) --------------------
    tmp_path = None
    try:
        tmp_fd, tmp_path = tempfile.mkstemp(suffix='.upload', prefix='upload_tmp_')
        os.close(tmp_fd)
        logger.info(f"[FALLBACK] Gravando stream em arquivo temporário {tmp_path} antes do upload...")
        with open(tmp_path, 'wb') as out_f:
            while True:
                chunk = fileobj.read(CHUNK_SIZE)
                if not chunk:
                    break
                out_f.write(chunk)
        # agora reusar a lógica de multipart com path
        with open(tmp_path, 'rb') as video_file:
            files = {'file': (filename, video_file, 'video/mp4')}
            logger.info(f"[FALLBACK] Tentando enviar '{filename}' (via temp file) para {UPLOAD_URL} (multipart)...")
            logger.info(f"Com metadados: {json.dumps(video_metadata, indent=2)}")
            response = session.post(f"{UPLOAD_URL}/api/upload-video",
                                    files=files, data={'metadata': json.dumps(video_metadata)}, headers=headers_base,
                                    timeout=3600)
            if response.status_code in (200, 201):
                logger.info("[FALLBACK] Upload bem-sucedido (multipart via temp file).")
                payload = response.json()
                return payload.get('video_id') or payload.get('item_id') or None
            else:
                logger.warning(f"[FALLBACK] Erro no upload (multipart via temp file): Código {response.status_code}")
                try:
                    logger.warning(json.dumps(response.json(), indent=2))
                except Exception:
                    logger.warning(response.text)
                return None

    except requests.exceptions.SSLError as e:
        logger.exception("SSLError durante upload via temp file: %s", e)
        return None
    except Exception as e:
        logger.exception(f"Erro no upload via temp file: {e}")
        return None
    finally:
        if tmp_path and os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except Exception:
                pass
