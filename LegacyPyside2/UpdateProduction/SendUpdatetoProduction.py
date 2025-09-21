
from firebase_admin import credentials, initialize_app, storage, db, delete_app


import os
import time
import zipfile
import subprocess
import shutil
import random
import sys
import threading
import os
import platform
import subprocess
import psutil
import re
import time
import urllib
import requests
import json
from firebase_admin import credentials, initialize_app, storage, db, delete_app
import firebase_admin
import sys

sys.path.append(os.path.join(os.path.dirname(__file__)))

########################################################################
# IMPORT FirebaseKeys
from CoreApp.Firebase.FirebaseAppKeys import *
app1 = init_firebase()
bucket = init_bucket()
########################################################################

time.sleep(3)

start_time = time.time()

diretorio_script = os.path.dirname(os.path.abspath(__file__))

elevate_path = "../"
projeto_dir = os.path.abspath(os.path.join(diretorio_script, f'{elevate_path}'))

os.chdir(projeto_dir)

env = os.environ.copy()
env["PYTHONPATH"] = projeto_dir

scripts = [f'main_control_panel.py']
for script in scripts:
    subprocess.run([
        "pyarmor", "gen", "--assert-import", "--assert-call",
        "--enable-themida", "--enable-jit", "--mix-str",
        "--obf-code", "2", script
    ], env=env)
    

subprocess.run(["pyarmor", "gen", "-O", f"dist", "-r", f"CoreApp", "--assert-import", "--assert-call", "--enable-themida",  "--enable-jit",  "--mix-str",  "--obf-code", "2"])
shutil.copytree(f'CoreApp/JsonStyle', f'dist/CoreApp/JsonStyle')
shutil.copytree(f'generated-files', f'dist/generated-files')
shutil.copytree(f'logs', f'dist/logs')
shutil.copytree(f'Qss', f'dist/Qss')
shutil.copy(f'watermask.jpg', f'dist')
time.sleep(3)

def buscar_arquivo(nome_arquivo):
    blob = bucket.blob(nome_arquivo)
    if blob.exists():
        return blob
    else:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado no bucket.")
        return None


ref1 = db.reference(f'Controle_de_versao/Controle_2', app=app1)
data1 = ref1.get()
try:
    x = data1["versao"]
except Exception as erroversion:
    ref1 = db.reference(f'Controle_de_versao', app=app1)
    data1 = ref1.get()                         
    controle_das_funcao2 = "Controle_2"
    controle_das_funcao_info_2 = {
    "versao": "update_control_panel_1.zip",
    }
    ref1.child(controle_das_funcao2).set(controle_das_funcao_info_2)
    x = "update_control_panel_1.zip"
    

nome_arquivo = f"{x}"
blob_arquivo = buscar_arquivo(nome_arquivo)
if blob_arquivo:
    print(f"O arquivo '{nome_arquivo}' foi encontrado no bucket criando nova versao.")
    numero_versao_atual = int(nome_arquivo.split("_")[-1].split(".")[0])
    nova_versao = numero_versao_atual + 1
    folder_to_zip = f"dist"
    zip_folder_name = "update_control_panel"    
    zip_file_name = zip_folder_name + f"_{nova_versao}" + ".zip"


    with zipfile.ZipFile(zip_file_name, "w", zipfile.ZIP_DEFLATED) as zipf:
        for foldername, subfolders, filenames in os.walk(folder_to_zip):
            for filename in filenames:
                filepath = os.path.join(foldername, filename)
                arcname = os.path.relpath(filepath, folder_to_zip)
                zipf.write(filepath, arcname)


    blob = bucket.blob(zip_file_name)
    blob.upload_from_filename(zip_file_name)
    print("ZIPADO E ENVIADO PARA FIREBASE COM sucesso !")

    time.sleep(3)
    os.remove(zip_file_name)
    

    time.sleep(3)
    try:
        shutil.rmtree(folder_to_zip)
        print(f"A pasta '{folder_to_zip}' foi excluída com sucesso.")
    except Exception as e:
        print(f"Erro ao excluir a pasta '{folder_to_zip}': {str(e)}")

    ref1 = db.reference(f'Controle_de_versao', app=app1)
    data1 = ref1.get()                         
    controle_das_funcao = "Controle_1"
    controle_das_funcao_info_ = {
    "versao": zip_file_name,
    }
    ref1.child(controle_das_funcao).set(controle_das_funcao_info_)
    
    ref1 = db.reference(f'Controle_de_versao', app=app1)
    data1 = ref1.get()                         
    controle_das_funcao2 = "Controle_2"
    controle_das_funcao_info_2 = {
    "versao": nome_arquivo,
    }
    ref1.child(controle_das_funcao2).set(controle_das_funcao_info_2)
    

else:
    print("Não foi possível encontrar o arquivo.")



scripts = [f'Update.py', f"Update_Update.py"]
for script in scripts:
    subprocess.run([
        "pyarmor", "gen", "--assert-import", "--assert-call",
        "--enable-themida", "--enable-jit", "--mix-str",
        "--obf-code", "2", script
    ], env=env)



ref1 = db.reference(f'Controle_de_versao/Controle_update_2', app=app1)
data1 = ref1.get()
try:
    x = data1["versao"]
except Exception as erroversion:
    ref1 = db.reference(f'Controle_de_versao', app=app1)
    data1 = ref1.get()                         
    controle_das_funcao2 = "Controle_update_2"
    controle_das_funcao_info_2 = {
    "versao": "control_panel_update_1.zip",
    }
    ref1.child(controle_das_funcao2).set(controle_das_funcao_info_2)
    x = "control_panel_update_1.zip"
    

nome_arquivo = f"{x}"
blob_arquivo = buscar_arquivo(nome_arquivo)
if blob_arquivo:
    print(f"O arquivo '{nome_arquivo}' foi encontrado no bucket criando nova versao.")
    numero_versao_atual = int(nome_arquivo.split("_")[-1].split(".")[0])
    nova_versao = numero_versao_atual + 1
    folder_to_zip = f"dist"
    zip_folder_name = f"control_panel_update"    
    zip_file_name = zip_folder_name + f"_{nova_versao}" + ".zip"

    with zipfile.ZipFile(zip_file_name, "w", zipfile.ZIP_DEFLATED) as zipf:
        for foldername, subfolders, filenames in os.walk(folder_to_zip):
            for filename in filenames:
                filepath = os.path.join(foldername, filename)
                arcname = os.path.relpath(filepath, folder_to_zip)
                zipf.write(filepath, arcname)


    blob = bucket.blob(zip_file_name)
    blob.upload_from_filename(zip_file_name)
    print("ZIPADO E ENVIADO PARA FIREBASE COM sucesso !")

    ref1 = db.reference(f'Controle_de_versao', app=app1)
    data1 = ref1.get()                         
    controle_das_funcao = "Controle_update_1"
    controle_das_funcao_info_ = {
    "versao": zip_file_name,
    }
    ref1.child(controle_das_funcao).set(controle_das_funcao_info_)
    
    ref1 = db.reference(f'Controle_de_versao', app=app1)
    data1 = ref1.get()                         
    controle_das_funcao2 = "Controle_update_2"
    controle_das_funcao_info_2 = {
    "versao": nome_arquivo,
    }
    ref1.child(controle_das_funcao2).set(controle_das_funcao_info_2)
    
    os.remove(zip_file_name)


    time.sleep(3)
    try:
        shutil.rmtree(folder_to_zip)
        print(f"A pasta '{folder_to_zip}' foi excluída com sucesso.")
    except Exception as e:
        print(f"Erro ao excluir a pasta '{folder_to_zip}': {str(e)}")


else:
    print("Não foi possível encontrar o arquivo.")



ende = time.time()
segundos = ende - start_time
minutos = segundos / 60

print(f"Segundos: {segundos}")
print(f"Minutos: {minutos}")
