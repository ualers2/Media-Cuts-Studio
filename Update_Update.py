import threading
import time
import subprocess
import firebase_admin
import importlib.util
import os
import zipfile
import shutil
import pyautogui
import datetime
from firebase_admin import credentials, storage, db
import psutil
import firebase_admin
import time
import threading
import zipfile
import tempfile
import sys
from firebase_admin import credentials, initialize_app, storage, db, delete_app

# Caminho correto para `CoreApp`
coreapp_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "MediaCutsStudio", "Versions", "Version_2")
)

# Adiciona ao sys.path para que o Python possa encontrá-lo
if coreapp_path not in sys.path:
    sys.path.append(coreapp_path)
    import CoreApp
    print("CoreApp importado com sucesso!")
    

########################################################################
# IMPORT FirebaseKeys
from CoreApp.Firebase.FirebaseAppKeys import *
app1 = init_firebase()
bucket = init_bucket()
########################################################################

diretorio_script = os.path.dirname(os.path.abspath(__file__))



def fazendo_o_download_da_nova_versao(bucket):

    try:

        nome_da_versao_dentro_do_buckt = f'control_panel_update_2.zip'
        diretorio_script = os.path.dirname(os.path.abspath(__file__)) 
        extract_dir = os.path.join(diretorio_script)
        
        #extract_dir = f'Arquivos/Versionamento_do_protocolo/Versao_{nova_versao}'
        os.makedirs(extract_dir, exist_ok=True)

        with tempfile.NamedTemporaryFile(delete=False) as temp_zip_file:
            temp_zip_filename = temp_zip_file.name
            blob = bucket.blob(nome_da_versao_dentro_do_buckt)
            blob.download_to_filename(temp_zip_filename)

        with zipfile.ZipFile(temp_zip_filename, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)

        os.remove(temp_zip_filename)

    except Exception as eroo1:
        print(f"{eroo1}erro ao att ")


fazendo_o_download_da_nova_versao(bucket)
