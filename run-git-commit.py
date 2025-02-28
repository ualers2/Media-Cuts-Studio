import os
import git

import time

import os
import requests
from requests.auth import HTTPBasicAuth
import base64
from dotenv import load_dotenv
import os
import zipfile
import requests
import base64

load_dotenv("keys.env")

token = os.getenv("token")
repo_name = os.getenv("repo_name")
branch = "main"
# headers = {
#     "Authorization": f"token {token}",
#     "Accept": "application/vnd.github.v3+json"
# }
# colaboradores = [
#     "CloudArchitectt", "TigraoEscritor", "NexGenCoder756",
#     "SignalMaster727", "QuantummCore", "BobGerenteDeProjeto",
#     "DallasEquipeDeSolucoes"
# ]

# for colaborador in colaboradores:
#     collaborator_url = f"https://api.github.com/repos/{repo_name}/collaborators/{colaborador}"
#     collaborator_data = {"permission": "admin"}
    
#     collaborator_response = requests.put(collaborator_url, headers=headers, json=collaborator_data)
    
#     if collaborator_response.status_code in [201, 204]:
#         print(f"Colaborador {colaborador} adicionado com sucesso com permissões de administrador.")
#     else:
#         print(f"Falha ao adicionar {colaborador}. Status: {collaborator_response.status_code}, Resposta: {collaborator_response.json()}")


def get_file_sha(repo, path, token):
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["sha"]
    return None


#import os
import base64
import requests
import time

# Lista de diretórios a serem ignorados
IGNORE_TXT = {"keys.env"}
IGNORE_DIRS = {"save", "Build", "Qss/icons/icons", "Qss/icons/0F6464", "CoreApp/Firebase"}

def upload_files_to_github(directory):
    directory = os.path.abspath(directory)  # Normaliza caminho base
    
    for dirpath, dirnames, filenames in os.walk(directory):
        # Caminho relativo do diretório atual
        rel_dirpath = os.path.relpath(dirpath, start=directory)

        # Verifica se o diretório atual está na lista de ignorados
        if any(rel_dirpath.startswith(ignored) for ignored in IGNORE_DIRS):
            print(f"Ignorando diretório: {rel_dirpath}")
            continue  # Pula o diretório inteiro

        # Filtra diretórios ignorados antes de iterar
        dirnames[:] = [d for d in dirnames if not any(
            os.path.relpath(os.path.join(dirpath, d), start=directory).startswith(ignored)
            for ignored in IGNORE_DIRS
        )]

        for filename in filenames:
            # Ignorar arquivos específicos
            if filename in IGNORE_TXT or filename.endswith(".pyc"):
                continue  

            file_path = os.path.join(dirpath, filename)

            with open(file_path, "rb") as file:
                content = file.read()
                encoded_content = base64.b64encode(content).decode("utf-8")

            # Caminho relativo ajustado para GitHub
            relative_path = os.path.relpath(file_path, start=directory).replace("\\", "/")
            url = f"https://api.github.com/repos/{repo_name}/contents/{relative_path}"

            # Verifica se o arquivo já existe
            response = requests.get(url, headers={"Authorization": f"token {token}"})
            sha = response.json().get("sha") if response.status_code == 200 else None

            data = {
                "message": f"Add {filename}",
                "content": encoded_content,
                "branch": branch
            }
            if sha:
                data["sha"] = sha  # Atualiza se já existir

            response = requests.put(url, json=data, headers={"Authorization": f"token {token}"})
            print(f"Arquivo: {relative_path} - Status: {response.status_code}")
            time.sleep(1)

diretorio_script = os.path.dirname(os.path.abspath(__file__))
directorydata = os.path.join(diretorio_script)

upload_files_to_github(directorydata)
