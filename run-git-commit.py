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


import os
import base64
import requests
import time


def load_gitignore(directory):
    """Carrega as regras do .gitignore e retorna uma lista de padrões"""
    gitignore_path = os.path.join(directory, ".gitignore")
    ignored_paths = set()

    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r") as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith("#"):  # Ignora comentários e linhas vazias
                    ignored_paths.add(os.path.normpath(line))
    
    return ignored_paths

def is_ignored(file_path, base_directory, ignored_paths):
    """Verifica se um arquivo ou diretório deve ser ignorado"""
    rel_path = os.path.relpath(file_path, start=base_directory)
    for pattern in ignored_paths:
        if rel_path.startswith(pattern):
            return True
    return False

def upload_files_to_github(directory):
    directory = os.path.abspath(directory)
    ignored_paths = load_gitignore(directory)  # Carregar as regras do .gitignore

    for dirpath, dirnames, filenames in os.walk(directory):
        if is_ignored(dirpath, directory, ignored_paths):
            print(f"Ignorando diretório: {dirpath}")
            continue
        
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if is_ignored(file_path, directory, ignored_paths):
                print(f"Ignorando arquivo: {file_path}")
                continue  

            with open(file_path, "rb") as file:
                content = file.read()
                encoded_content = base64.b64encode(content).decode("utf-8")

            relative_path = os.path.relpath(file_path, start=directory).replace("\\", "/")
            url = f"https://api.github.com/repos/{repo_name}/contents/{relative_path}"

            response = requests.get(url, headers={"Authorization": f"token {token}"})
            sha = response.json().get("sha") if response.status_code == 200 else None

            data = {"message": f"Add {filename}", "content": encoded_content, "branch": branch}
            if sha:
                data["sha"] = sha

            response = requests.put(url, json=data, headers={"Authorization": f"token {token}"})
            print(f"Arquivo: {relative_path} - Status: {response.status_code}")
            time.sleep(1)

diretorio_script = os.path.dirname(os.path.abspath(__file__))
directorydata = os.path.join(diretorio_script)

upload_files_to_github(directorydata)
