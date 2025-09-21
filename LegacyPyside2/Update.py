########################################################################
# IMPORT Libs 
########################################################################
## IMPORTAÇÃO DE BIBLIOTECAS
########################################################################

import os
import sys
import json
import time
import zipfile
import random
import re
import subprocess
import platform
import tempfile
from datetime import datetime, timedelta
from typing import Dict, Any
from collections import defaultdict
from queue import Queue, Empty
import threading

try:
    import requests
    import GPUtil
    import shutil
    import whisper
    import glob
    import math
    import torch
    import traceback
    import hashlib
    from concurrent.futures import ThreadPoolExecutor
    import uiautomator2 as u2
    import cv2
    import numpy as np
    import wave
    import srt
    import yt_dlp
    import psutil
    import schedule
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload

    

    import websockets
    import asyncio
    import av
    import logging
    import io


    from dotenv import load_dotenv, find_dotenv
    from firebase_admin import credentials, initialize_app, storage, db, delete_app
    from transformers import (
        AutoModelForSpeechSeq2Seq,
        AutoTokenizer,
        AutoFeatureExtractor,
        pipeline,
    )
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
    from PySide2 import QtWidgets, QtCore, QtGui
    from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEngineSettings, QWebEngineScript

    from proglog import ProgressBarLogger
except ImportError as e:
    print(f"Erro ao importar bibliotecas: {e}")
    
import requests
import ctypes
import pytz
import calendar
import sys
import os

# Caminho correto para `CoreApp`
coreapp_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "Versions", "Version_2")
)

# Adiciona ao sys.path para que o Python possa encontrá-lo
if coreapp_path not in sys.path:
    sys.path.append(coreapp_path)
    import CoreApp
    print("CoreApp importado com sucesso!")

########################################################################
# IMPORT Splash 
from CoreApp.src_app.ui_splash_screen import *
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
########################################################################


########################################################################
# IMPORT FirebaseKeys
from CoreApp.Firebase.FirebaseAppKeys import *
app1 = init_firebase()
bucket = init_bucket()
########################################################################


diretorio_script = os.path.dirname(os.path.abspath(__file__))
# Crie uma classe para interceptar as escritas e registrar o progresso
class ProgressLogger:
    def __init__(self, file_obj, total_size, progress_signal):
        """
        :param file_obj: Objeto de arquivo onde os dados serão escritos.
        :param total_size: Tamanho total do arquivo (em bytes).
        :param progress_signal: Sinal que será emitido com o progresso (valor float de 0 a 100).
        """
        self.file_obj = file_obj
        self.total_size = total_size
        self.downloaded = 0
        self.progress_signal = progress_signal

    def write(self, data):
        self.file_obj.write(data)
        self.downloaded += len(data)
        # Calcula a porcentagem de progresso
        percent = (self.downloaded / self.total_size) * 100 if self.total_size else 100
        # Emite o sinal com o valor percentual
        self.progress_signal.emit(percent)

    def flush(self):
        self.file_obj.flush()

########################################################################
# Thread para atualizar o loading
class Updateloader(QThread):
    messagesignal = Signal(str)
    circleColor1signal = Signal(QColor)
    circleColor2signal = Signal(QColor)
    finishedd = Signal()
    progress_signal = Signal(float)  # Emite o progresso em porcentagem

    def __init__(self, message, color1, color2, parent=None):
        super().__init__(parent)
        self.message = message
        self.color1 = color1
        self.color2 = color2

    def nova_versao_disponivel(self, app1):
        ref1 = db.reference(f'Controle_de_versao/Controle_2', app=app1)
        data1 = ref1.get()
        x = data1["versao"]
        nome_versao_atual = f"{x}"
        numero_versao_atual = int(nome_versao_atual.split("_")[-1].split(".")[0])
        blobs = bucket.list_blobs()
        self.messagesignal.emit("Searching Version")
        self.circleColor1signal.emit(self.color1)
        for blob in blobs:
            try:
                if blob.name != nome_versao_atual and blob.name.startswith("update_control_panel_"):
                    numero_versao_nova = int(blob.name.split("_")[-1].split(".")[0])
                    if numero_versao_nova > numero_versao_atual:
                        self.messagesignal.emit("Version found")
                        self.circleColor2signal.emit(self.color2)

                        return True, numero_versao_nova, numero_versao_atual, blob.name
            except:
                pass
        
        return False, None, numero_versao_atual, x
            

    def run(self):

        # Etapa 1: Mensagem inicial
        self.messagesignal.emit(self.message)
        time.sleep(1)  # Simula uma operação de carregamento

        Y, nova_versao, versao_atual, nome_versao_atual = self.nova_versao_disponivel(app1)

        if Y:

            self.messagesignal.emit("Loading Version...")
            self.circleColor1signal.emit(self.color1)

            time.sleep(1)

            try:
                nome_da_versao_dentro_do_buckt = f'update_control_panel_{nova_versao}.zip'
                diretorio_script = os.path.dirname(os.path.abspath(__file__)) 
                extract_dir = os.path.join(diretorio_script, 'Versions', f'Version_{nova_versao}')
                print(nova_versao)
                os.makedirs(extract_dir, exist_ok=True)

                self.circleColor1signal.emit(self.color1)

                # Cria um arquivo temporário para salvar o download
                with tempfile.NamedTemporaryFile(delete=False) as temp_zip_file:
                    temp_zip_filename = temp_zip_file.name

                # Obtenha o blob do bucket e verifique o tamanho total (em bytes)
                blob = bucket.blob(nome_da_versao_dentro_do_buckt)
                total_size = blob.size  # Certifique-se de que o blob possui essa propriedade

                # Abra o arquivo para escrita e utilize o wrapper para logar o progresso
                with open(temp_zip_filename, "wb") as f:
                    progress_file = ProgressLogger(f, total_size, self.progress_signal)
                    blob.download_to_file(progress_file)

                os.remove(temp_zip_filename)

            except Exception as eroo1:
                print(f"{eroo1}erro ao att ")


            # try:

            #     nome_da_versao_dentro_do_buckt = f'control_panel_update_{nova_versao}.zip'
            #     diretorio_script = os.path.dirname(os.path.abspath(__file__)) 
            #     extract_dir = os.path.join(diretorio_script)
            #     print(nova_versao)
            #     os.makedirs(extract_dir, exist_ok=True)

            #     self.messagesignal.emit("Version Being Downloaded..")
            #     self.circleColor2signal.emit(self.color2)
                
            #     with tempfile.NamedTemporaryFile(delete=False) as temp_zip_file:
            #         temp_zip_filename = temp_zip_file.name
            #         blob = bucket.blob(nome_da_versao_dentro_do_buckt)
            #         blob.download_to_filename(temp_zip_filename)

            #     with zipfile.ZipFile(temp_zip_filename, 'r') as zip_ref:
            #         zip_ref.extractall(extract_dir)

            #     self.messagesignal.emit("Version Being\n Downloaded...")
            #     self.circleColor2signal.emit(self.color2)

            #     os.remove(temp_zip_filename)

            # except Exception as eroo1:
            #     print(f"{eroo1}erro ao att ")


            self.messagesignal.emit("Version has\nbeen downloaded!")
            self.circleColor2signal.emit(self.color2)
            # Conclui o loading
            self.finishedd.emit()

    def stop(self):
        # Método caso queira interromper a thread de forma controlada
        self.quit()
        self.wait()

########################################################################
# MainWindow Loading Screen
class LoadingScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow_splash()
        self.ui.setupUi(self)

        # Garante que a janela tenha foco ao abrir
        self.activateWindow()
        self.raise_()
        self.setFocus()
        jsonFile_path = os.path.abspath(os.path.join("MediaCutsStudio", "Versions", "Version_2", "CoreApp", "JsonStyle", "style_Splash.json"))
        loadJsonStyle(self=self, ui=self.ui, jsonFiles = {jsonFile_path})
        
        self.myParentWidget = self.ui.widget
        
        self.myParentWidget.message="LOADING."
        self.myParentWidget.size=QSize(600, 600)
        self.myParentWidget.color=QColor("white")
        self.myParentWidget.fontFamily="Ebrima"
        self.myParentWidget.fontSize=30
        self.myParentWidget.rayon=200
        self.myParentWidget.duration=60 * 1000
        self.myParentWidget.noiseOctaves=0.8
        self.myParentWidget.noiseSeed=int(time.time())
        self.myParentWidget.backgroundColor=QColor("transparent")
        self.myParentWidget.circleColor1=QColor("#ff2e63")
        self.myParentWidget.circleColor2=QColor("#082e63")
        self.myParentWidget.circleColor3=QColor(57, 115, 171, 100)

        message = "LOADING."
        circleColor1 = QColor("#1e0880")
        circleColor2 = QColor("#000000")


        self.threadUpdateloader = Updateloader(message, circleColor1, circleColor2)
        self.threadUpdateloader.messagesignal.connect(self.message_signal)
        self.threadUpdateloader.progress_signal.connect(self.progress_signal_signal)
        self.threadUpdateloader.circleColor1signal.connect(self.circleColor1_signal)
        self.threadUpdateloader.circleColor2signal.connect(self.circleColor2_signal)
        self.threadUpdateloader.finishedd.connect(self.finish_loading)
        self.threadUpdateloader.start()


        #self.show()
        QAppSettings.updateAppSettings(self, generateIcons=False)

    def circleColor1_signal(self, color1):
        self.myParentWidget.circleColor1 = color1

    def circleColor2_signal(self, color2):
        self.myParentWidget.circleColor2 = color2

    def message_signal(self, mensagem):
        self.myParentWidget.message = mensagem

    def progress_signal_signal(self, value):
        self.myParentWidget.message = f"Version \nDownload:{value}%"


    def finish_loading(self):
        # Aguarda um curto intervalo antes de prosseguir para a janela principal
        QTimer.singleShot(1000, self.show_main_window)

    def show_main_window(self):
        # Encerra o thread de loading e fecha a tela de loading
        self.threadUpdateloader.stop()
        self.close()

        comando_terminal = ['start', 'MediaCutsStudio/Python/python', f'MediaCutsStudio/Versions/Version_2/main_control_panel.py']
        subprocess.Popen(comando_terminal, shell=True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    loading_screen = LoadingScreen()
    loading_screen.show()

    sys.exit(app.exec())