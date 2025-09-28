# Internal-server\.py
import os
import json
import requests
import logging
diretorio_script = os.path.dirname(__file__) 
os.makedirs(os.path.join(diretorio_script, '../', 'Logs'), exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
os.makedirs(os.path.join(os.path.dirname(__file__), '../',  "Logs"), exist_ok=True)
file_handler = logging.FileHandler(os.path.join(diretorio_script, '../', 'Logs', 'upload_py.log'))
file_handler.setFormatter(formatter)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def upload_(name_project, VIDEO_FILE_PATH, USER_ID_FOR_TEST):
    UPLOAD_URL = "https://videomanager.api.mediacutsstudio.com"
    
    video_metadata = {
        "projectName": name_project,
        "type_project": "files",

    }

    # --- Verificações Iniciais ---
    if not os.path.exists(VIDEO_FILE_PATH):
        logger.info(f"Erro: O arquivo '{VIDEO_FILE_PATH}' não foi encontrado.")
        logger.info("Por favor, crie um arquivo MP4 com este nome ou ajuste o caminho.")
        exit()

    # --- Preparação da Requisição ---

    # Abre o arquivo de vídeo em modo binário
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
            response = requests.post(F"{UPLOAD_URL}/api/upload-video", files=files, data=data, headers=headers)

            if response.status_code == 201 or response.status_code == 200:
                logger.info("\nUpload bem-sucedido!")
                logger.info("Resposta do servidor:")
                logger.info(json.dumps(response.json(), indent=2))
                payload = response.json()
                ID = payload['video_id']
                logger.info(f"ID: {ID}")
                return ID
            else:
                logger.info(f"\nErro no upload: Código de status {response.status_code}")
                logger.info("Resposta do servidor:")
                try:
                    logger.info(json.dumps(response.json(), indent=2))
                except json.JSONDecodeError:
                    print(response.text) # Se a resposta não for JSON
                logger.info("\nCertifique-se de que seu servidor Flask está rodando e o endpoint está acessível.")
                logger.info("Verifique também se o 'USER_ID_FOR_TEST' e o 'UPLOAD_URL' estão corretos.")

    except FileNotFoundError:
        logger.info(f"Erro: O arquivo '{VIDEO_FILE_PATH}' não foi encontrado.")
    except requests.exceptions.ConnectionError:
        logger.info("Erro de conexão: O servidor não está acessível.")
        logger.info("Certifique-se de que o backend Flask está rodando em 'http://localhost:5000'.")
    except Exception as e:
        logger.info(f"Ocorreu um erro inesperado: {e}")
