
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

import firebase_admin
import sys
sys.path.append(os.path.join(os.path.dirname(__file__)))

time.sleep(3)

elevate_path = "../"
projeto_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), f'{elevate_path}'))

os.chdir(projeto_dir)

start_time = time.time()

env = os.environ.copy()
env["PYTHONPATH"] = projeto_dir
env["PYTHONUTF8"] = "1"



scripts = [f'main_control_panel.py']
for script in scripts:
    subprocess.run([
        "pyarmor", "gen", "--assert-import", "--assert-call",
        "--enable-themida", "--enable-jit", "--mix-str",
        "--obf-code", "2", script
    ], env=env)


subprocess.run(["pyarmor", "gen", "-O", f"dist", "-r", f"CoreApp", "--assert-import", "--assert-call", "--enable-themida",  "--enable-jit",  "--mix-str",  "--obf-code", "2"])

shutil.copytree(f'dist/CoreApp', f'Build/MediaCutsStudio/Versions/Version_2/CoreApp', dirs_exist_ok=True)

try:
    shutil.copytree(f'CoreApp/JsonStyle', f'Build/MediaCutsStudio/Versions/Version_2/CoreApp/JsonStyle')
    shutil.copytree(f'generated-files', f'Build/MediaCutsStudio/Versions/Version_2/generated-files')
    shutil.copytree(f'logs', f'Build/MediaCutsStudio/Versions/Version_2/logs')
    shutil.copytree(f'Qss', f'Build/MediaCutsStudio/Versions/Version_2/Qss')
    shutil.copy(f'watermask.jpg', f'Build/MediaCutsStudio/Versions/Version_2')
except Exception as e:
    print(f"Erro")

# Copia toda a pasta para 'Build/MediaCutsStudio/pyarmor_runtime_004289'
shutil.copytree(f'dist/pyarmor_runtime_004289', f'Build/MediaCutsStudio/Versions/Version_2/pyarmor_runtime_004289', dirs_exist_ok=True)

shutil.copy(f'dist/main_control_panel.py', f'Build/MediaCutsStudio/Versions/Version_2')

try:
    shutil.rmtree(f"dist")
except Exception as e:
    print(f"Erro {str(e)}")



time.sleep(3)

scripts = [f'Update.py', f'Update_Update.py']
for script in scripts:
    subprocess.run([
        "pyarmor", "gen", "--assert-import", "--assert-call",
        "--enable-themida", "--enable-jit", "--mix-str",
        "--obf-code", "2", script
    ], env=env)


# Copia toda a pasta para 'Build/MediaCutsStudio/pyarmor_runtime_004289'
shutil.copytree(f'dist/pyarmor_runtime_004289', f'Build/MediaCutsStudio/pyarmor_runtime_004289', dirs_exist_ok=True)

shutil.copy(f'dist/Update.py', f'Build/MediaCutsStudio')

shutil.copy(f'dist/Update_Update.py', f'Build/MediaCutsStudio')
    
try:
    shutil.rmtree(f"dist")
except Exception as e:
    print(f"Erro {str(e)}")

time.sleep(3)

scripts = [f'MediaCutsStudio.py']
for script in scripts:
    subprocess.run([
        "pyarmor", "gen", "--assert-import", "--assert-call",
        "--enable-themida", "--enable-jit", "--mix-str",
        "--obf-code", "2", script
    ], env=env)

shutil.copytree(f'dist/pyarmor_runtime_004289', f'Build/pyarmor_runtime_004289', dirs_exist_ok=True)

try:
    shutil.copy(f'dist/MediaCutsStudio.py', f'Build')
except Exception as e:
    print(f"Erro {str(e)}")

try:
    shutil.rmtree(f"dist")
except Exception as e:
    print(f"Erro {str(e)}")



# scripts = [f'Build/MediaCutsStudio.py']
# for script in scripts:
#     subprocess.run([
#         "pyinstaller",
#         "--windowed",
#         "--name=Media-Cuts-Studio",
#         "--onefile",
#         "--icon=MediaCutsStudio.ico", 
#         "--noconsole", script
#     ], env=env)


# time.sleep(3)

# try:
#     shutil.copy(f'dist/Media-Cuts-Studio.exe', f'Build')
# except Exception as e:
#     print(f"Erro .exe {str(e)}")

# try:
#     os.remove(f"Build/MediaCutsStudio.py")
# except Exception as e:
#     print(f"Erro {str(e)}")

try:
    shutil.rmtree(f"Build/MediaCutsStudio/localpycs")
except Exception as e:
    print(f"Erro {str(e)}")

try:
    shutil.rmtree(f"dist")
except Exception as e:
    print(f"Erro {str(e)}")

try:
    os.remove(f"Build/MediaCutsStudio/Analysis-00.toc")
    os.remove(f"Build/MediaCutsStudio/base_library.zip")
    os.remove(f"Build/MediaCutsStudio/EXE-00.toc")
    os.remove(f"Build/MediaCutsStudio/MediaCutsStudio.exe.manifest")
    os.remove(f"Build/MediaCutsStudio/MediaCutsStudio.pkg")
    os.remove(f"Build/MediaCutsStudio/PKG-00.toc")
    os.remove(f"Build/MediaCutsStudio/PYZ-00.pyz")
    os.remove(f"Build/MediaCutsStudio/PYZ-00.toc")
    os.remove(f"Build/MediaCutsStudio/warn-MediaCutsStudio.txt")
    os.remove(f"Build/MediaCutsStudio/xref-MediaCutsStudio.html")
    os.remove(f"MediaCutsStudio.spec")
except Exception as e:
    print(f"Erro ")
    try:
        shutil.rmtree(f"Build/Media-Cuts-Studio")
    except Exception as e:
        print(f"Erro {str(e)}")

ende = time.time()
segundos = ende - start_time
minutos = segundos / 60

print(f"Segundos: {segundos}")
print(f"Minutos: {minutos}")
