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


# Lista de diretórios a serem ignorados
IGNORE_TXT = {"Media-Cuts-Studio.spec"}
IGNORE_DIRS = {"save", "Build/MediaCutsStudio/Python", "CoreApp/Firebase", "save"}

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

def upload_files_to_github(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        # Filtra diretórios ignorados
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        
        for filename in filenames:
            
            if filename.endswith(".pyc"):
                continue  # Ignora arquivos .pyc
            
            file_path = os.path.join(dirpath, filename)
            with open(file_path, "rb") as file:
                content = file.read()
                encoded_content = base64.b64encode(content).decode("utf-8")

            # Caminho relativo ajustado para GitHub
            relative_path = os.path.relpath(file_path, start=directory)
            github_path = relative_path.replace("\\", "/")

            url = f"https://api.github.com/repos/{repo_name}/contents/{github_path}"
            
            # Verifica se o arquivo já existe
            response = requests.get(url, headers={"Authorization": f"token {token}"})
            if response.status_code == 200:
                response_json = response.json()
                if isinstance(response_json, dict):  # Verifica se a resposta é um dicionário (arquivo)
                    sha = response_json.get("sha")
                else:
                    sha = None  # Evita erro se for uma lista (diretório)
            else:
                sha = None

            data = {
                "message": f"Add {filename}",
                "content": encoded_content,
                "branch": branch
            }
            if sha:
                data["sha"] = sha  # Atualiza se já existir

            response = requests.put(url, json=data, headers={"Authorization": f"token {token}"})
            print(f"Arquivo: {github_path} - Status: {response.status_code}")
            time.sleep(1)

diretorio_script = os.path.dirname(os.path.abspath(__file__))
directorydata = os.path.join(diretorio_script)

upload_files_to_github(directorydata)
