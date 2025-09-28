# Internal-server\.py
import requests

def download_(UPLOAD_URL, save_path, PROJECT_NAME, VIDEO_ID, USER_ID_FOR_TEST) -> str:
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

    try:
        with requests.get(url, headers=headers, stream=True, timeout=120) as resp:
            resp.raise_for_status()

            # Grava em disco apenas chunks não vazios
            with open(save_path, "wb") as f:
                for chunk in resp.iter_content(8192):
                    if chunk:
                        f.write(chunk)

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Falha ao baixar vídeo: {e}") from e

    return save_path
