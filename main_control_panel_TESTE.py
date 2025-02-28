########################################################################
# IMPORT Libs 
########################################################################
## IMPORTAÇÃO DE BIBLIOTECAS
########################################################################

import os

import json
import time
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
from PySide2.QtCore import QThread, Signal
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEngineSettings, QWebEngineScript
from proglog import ProgressBarLogger
import requests
import ctypes
import pytz
import calendar
import asyncio
import websockets
import ssl 
import os
import sys


# sys.path.append(os.path.abspath(os.path.dirname(__file__)))
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "MediaCutsStudio")))
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "MediaCutsStudio", "Versions", "Version_2", "CoreApp")))
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "MediaCutsStudio", "Versions", "Version_2", "CoreSecurity")))

# projeto_dir = os.path.abspath(os.path.dirname(__file__))

# os.chdir(projeto_dir)

########################################################################
# IMPORT FirebaseKeys
from CoreApp.Firebase.FirebaseAppKeys import *
app1 = init_firebase()  
bucket = init_bucket()
########################################################################

########################################################################
# IMPORT icons 
from CoreApp.src_app import icons_interpreter
########################################################################

########################################################################
# IMPORT GUI 
from CoreApp.src_app.ui_ControlPanel import *
########################################################################

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
# IMPORT Pyside2
from PySide2extn.RoundProgressBar import roundProgressBar 
from PySide2.QtCore import QTimer, Signal, QThread
from PySide2 import QtCore
########################################################################

########################################################################
# IMPORT Core
from CoreApp.Login.HandleTextEdit import setup_plain_text_qtextedit
from CoreApp.Login.Session import *
from CoreApp.QProcess.QWebhook import SocketIOClient
from CoreApp.CustomModals.ErroModal import update_custommodals_ErroModal
from CoreApp.CustomModals.SuccessModal import update_custommodals_SuccessModal
from CoreApp.CustomModals.Warning import update_custommodals_Warning
from CoreApp.CustomModals.Custom import update_custommodals_Custom
from CoreApp.CustomQDialog.QDialog import custom_dialog
from CoreApp.Preview.PreviewWidget import PreviewWidget
from CoreApp.QProcess.QTaskManager import TaskManager
from CoreApp.QProcess.QTaskCount import CountTasks
  
########################################################################

# ########################################################################
# IMPORT CoreSecurity
# from CoreSecurity.SecureWebSocket import SecureWebSocket
# ########################################################################

icon_window = u":/web_icons/icons/web_icons/rectangle-3370.png"

def close_window(ws_thread):
    ws_thread.stop()

def messageClicked():
    QMessageBox.information(None,
                            "System tray message",
                            "You just clicked your system tray message.\n"
                            "Add your custom function here")

def show_message():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowIcon(QtGui.QIcon(icon_window))

    msg.setWindowTitle("Message Box")
    msg.setText("This is a message for you")

    msg.setInformativeText("Additional information can be put here")
    msg.setDetailedText("Give more details about your message here")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.exec_()

def show_tray_message(Title: str, Message: str, tray: QSystemTrayIcon):
    notificationTitle = Title
    notificationMessage = Message
    icon = QIcon(icon_window)
    duration = 3 * 1000 
    
    if len(notificationTitle) == 0 or len(notificationMessage) == 0:
        tray.showMessage("Input Something", "Enter your notification tittle and message", icon, duration)
    else:
        tray.showMessage(notificationTitle, notificationMessage, icon, duration)

# Classe customizada para desenhar o header com ícone
class IconHeaderView(QHeaderView):
    def __init__(self, orientation, parent=None):
        super().__init__(orientation, parent)
        # Alinha o texto à esquerda, se desejar
        self.setDefaultAlignment(Qt.AlignLeft | Qt.AlignVCenter)

    def paintSection(self, painter, rect, logicalIndex):
        painter.save()
        
        # Configura o estilo do header
        option = QStyleOptionHeader()
        self.initStyleOption(option)
        option.rect = rect

        # Obtém os dados do header: texto e ícone
        text = self.model().headerData(logicalIndex, self.orientation(), Qt.DisplayRole)
        icon = self.model().headerData(logicalIndex, self.orientation(), Qt.DecorationRole)
        
        option.text = text if text is not None else ""
        # Se existir um ícone válido, define-o na opção
        if isinstance(icon, QIcon) and not icon.isNull():
            option.icon = icon

        # Desenha o header usando o estilo padrão
        self.style().drawControl(QStyle.CE_Header, option, painter, self)
        painter.restore()

########################################################################
# Thread para atualizar o loading
class Updateloader(QThread):
    messagesignal = Signal(str)
    circleColor1signal = Signal(QColor)
    circleColor2signal = Signal(QColor)
    finishedd = Signal()

    def __init__(self, message, color1, color2, parent=None):
        super().__init__(parent)
        self.message = message
        self.color1 = color1
        self.color2 = color2

    def run(self):
        # Etapa 1: Mensagem inicial
        self.messagesignal.emit(self.message)
        time.sleep(1)  # Simula uma operação de carregamento

        # Etapa 2: Atualiza mensagem e cor do círculo 1
        self.messagesignal.emit("LOADING..")
        self.circleColor1signal.emit(self.color1)
        time.sleep(1)

        # Etapa 3: Atualiza mensagem e cor do círculo 2
        self.messagesignal.emit("LOADING...")
        self.circleColor2signal.emit(self.color2)
        time.sleep(1)

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

        json_style_Splash = os.path.abspath(os.path.join("CoreApp", "JsonStyle", "style_Splash.json"))
        loadJsonStyle(self=self, ui=self.ui, jsonFiles = {json_style_Splash})
     
        
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

    def finish_loading(self):
        # Aguarda um curto intervalo antes de prosseguir para a janela principal
        QTimer.singleShot(1000, self.show_main_window)

    def show_main_window(self):
        # Encerra o thread de loading e fecha a tela de loading
        self.threadUpdateloader.stop()
        self.close()

        # Instancia e exibe a janela principal
        self.main_window = Main_Control_Panel()
        self.main_window.show()

class Main_Control_Panel(QMainWindow):
    new_tasks_data_signal = Signal(dict)
    cancell_task_data_signal = Signal(dict)
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
 
 
        global window_obj
        window_obj = self.ui

        self.liveCompileQss = True

        json_style_control_panel = os.path.abspath(os.path.join("CoreApp", "JsonStyle", "style_control_panel.json"))
        loadJsonStyle(self=self, ui=self.ui, jsonFiles = {json_style_control_panel})

        self.email_input = self.ui.email_input.toPlainText().replace(".", "").replace("@", "")
        self.email_input_no_filtred = self.ui.email_input.toPlainText()
        
        self.ref_tasks2 = db.reference(f'save_tasks_users/task/{self.email_input}', app=app1)
        self.SESSION_DB_PATH = f"sessions/{self.email_input}"
        self.Name_server_1 = ["#1 Media Cuts Studio API server"]
        self.SOCKET_URL = "https://accepted-poorly-maggot.ngrok-free.app"
        self.url_login = 'https://pure-poorly-fly.ngrok-free.app/proxy-login'
        self.API_URL_Shortify = "https://dynamic-supreme-jackal.ngrok-free.app/api/Media_Cuts_Studio/Shortify/Mode/Create"
        self.url_endpoint_delet_task = "https://dynamic-supreme-jackal.ngrok-free.app/api/Media_Cuts_Studio/Shortify/Mode/Delete"
        
        self.session_flag = None
        self.task_id = None

        self.watermark_image = "watermask.jpg"

        self.widget_area_task = self.ui.TasksView
        self.diretorio_script = os.path.dirname(os.path.abspath(__file__))

        self.rpb_Tasks_Created = self.ui.widget_Tasks_Created
        self.rpb_Tasks_Created.rpb_setLineWidth(10)
        self.rpb_Tasks_Created.rpb_setLineColor((29, 18, 117)) 
        self.rpb_Tasks_Created.rpb_setTextFormat('Value')
        self.rpb_Tasks_Created.rpb_setValue(0)

        self.rpb_Tasks_Running = self.ui.widget_Tasks_Running
        self.rpb_Tasks_Running.rpb_setLineWidth(10)
        self.rpb_Tasks_Running.rpb_setLineColor((29, 18, 117)) 
        self.rpb_Tasks_Running.rpb_setTextFormat('Value')
        self.rpb_Tasks_Running.rpb_setValue(0)

        self.rpb_Tasks_Completed = self.ui.widget_Tasks_Completed
        self.rpb_Tasks_Completed.rpb_setLineWidth(10)
        self.rpb_Tasks_Completed.rpb_setLineColor((29, 18, 117)) 
        self.rpb_Tasks_Completed.rpb_setTextFormat('Value')
        self.rpb_Tasks_Completed.rpb_setValue(0)


        self.ui.Captions_Bold_Bool.customizeQCustomCheckBox(
            bgColor = "#c3c3c3",
            circleColor = "#fff",
            activeColor = "#17a8e3",
            animationEasingCurve = QEasingCurve.Linear,
            animationDuration = 200
        )

        self.ui.Captions_Italic_Bool.customizeQCustomCheckBox(
            bgColor = "#c3c3c3",
            circleColor = "#fff",
            activeColor = "#17a8e3",
            animationEasingCurve = QEasingCurve.Linear,
            animationDuration = 200
        )

        self.ui.Captions_Underline_Bool.customizeQCustomCheckBox(
            bgColor = "#c3c3c3",
            circleColor = "#fff",
            activeColor = "#17a8e3",
            animationEasingCurve = QEasingCurve.Linear,
            animationDuration = 200
        )

        self.ui.Captions_Shadow_Bool.customizeQCustomCheckBox(
            bgColor = "#c3c3c3",
            circleColor = "#fff",
            activeColor = "#17a8e3",
            animationEasingCurve = QEasingCurve.Linear,
            animationDuration = 200
        )

        layout = QVBoxLayout(self.ui.widget_preview_watermark)
        self.preview_widget = PreviewWidget(self.watermark_image)
        layout.addWidget(self.preview_widget)

        self.time_edit = self.ui.timeEdit
        self.time_edit.setDisplayFormat("HH:mm:ss")  
        self.time_edit.setTime(QTime(0, 0, 0))  
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)  

        # Cria o modelo e define os cabeçalhos
        self.tree_model = QStandardItemModel()
        headers = ['Hash256 Task', 'Date/Time', 'TimeZone', 'Mode', 'YouTube Channel', 'Status', 'Cancel Scheduling']
        icons = [
            ":/feather/icons/feather/database.png",
            ":/font_awesome/icons/font_awesome/calendar-days.png",
            ":/material_design/icons/material_design/timer.png",
            ":/feather/icons/feather/settings.png",
            ":/font_awesome/icons/font_awesome/youtube.png",
            ":/material_design/icons/material_design/track_changes.png",
            ":/feather/icons/feather/trash.png"
        ]

        # Define os rótulos (isso cria as colunas)
        self.tree_model.setHorizontalHeaderLabels(headers)

        # Associa os ícones a cada coluna (usando DecorationRole)
        for i, icon_path in enumerate(icons):
            icon = QIcon(icon_path)
            self.tree_model.setHeaderData(i, Qt.Horizontal, icon, Qt.DecorationRole)

        # Configura o modelo no QTreeView
        self.widget_area_task.setModel(self.tree_model)

        # Substitui o header padrão por um customizado que desenha ícones
        custom_header = IconHeaderView(Qt.Horizontal, self.widget_area_task)
        self.widget_area_task.setHeader(custom_header)

        # Ajusta a largura das colunas
        for i in range(self.tree_model.columnCount()):
            self.widget_area_task.setColumnWidth(i, 150)

        self.api_key = self.ui.api_key_input.toPlainText()
        self.username = self.ui.username_input
        self.password = self.ui.username_password

        self.ui.pushButton_login.clicked.connect(lambda: self.login(self.username.toPlainText(), self.password.toPlainText()))
        self.ui.Select_Time.clicked.connect(self.custom_dialog_Select_Time)
        self.ui.upload_image_watermark.clicked.connect(self.custom_dialog_upload_image_watermark)
        self.ui.selector_color_subtitles.clicked.connect(self.custom_dialog_selector_color_subtitles)
        self.ui.upload_image_watermark_.clicked.connect(self.DialogUploadImage)
        self.ui.selector_animation_subtitles.clicked.connect(self.custom_dialog_selector_animation_subtitles)
        self.ui.selector_Effects_subtitles.clicked.connect(self.custom_dialog_selector_effects_subtitles)
        self.ui.selector_FontName_subtitles.clicked.connect(self.custom_dialog_selector_fontname_subtitles)
        self.ui.selector_Captions_FontName_.clicked.connect(self.custom_dialog_selector_fontname_captions)
        self.ui.selector_PrimaryColour_Captions.clicked.connect(self.custom_dialog_selector_primary_color_captions)
        self.ui.selector_SecondaryColour_Captions.clicked.connect(self.custom_dialog_selector_secondary_color_captions)
        self.ui.selector_OutlineColour_Captions.clicked.connect(self.custom_dialog_selector_outline_color_captions)
        self.ui.selector_BackColour_Captions.clicked.connect(self.custom_dialog_selector_back_color_captions)
        self.ui.selector_Reveal_Effect_Initial_Color_Captions.clicked.connect(self.custom_dialog_selector_reveal_effect_initial_color_captions)
        self.ui.selector_Reveal_Effect_Final_Color_Captions.clicked.connect(self.custom_dialog_selector_reveal_effect_final_color_captions)
        self.ui.Start_Shortify.clicked.connect(self.Start_Shortify)

        self._init_change_animation_sub_()
        self._init_change_efects_sub_()
        self._init_change_font_sub_()
        self._init_change_fontname_cc_()

        self.ui.Dashboard.clicked.connect(self.navegate_Dashboard)
        self.ui.Control_panel.clicked.connect(self.navegate_Control_panel)
        self.ui.Control_panel_process.clicked.connect(self.navegate_Control_panel_process)
        self.ui.Control_panel_Tasks.clicked.connect(self.navegate_Control_panel_tasksview)
        self.ui.Control_panel_report.clicked.connect(self.navegate_Control_panel_Report)

        
        self.ui.myaccount.clicked.connect(self.navegate_myaccount)
        self.ui.get_myaccount.clicked.connect(self.navegate_get_myaccount)
        self.ui.API_Server_AVAIBLE.addItems(self.Name_server_1)
        self.ui.Mode_Shortify.clicked.connect(self.navegate_Mode_Shortify)
        self.ui.Mode_Batch_processing.clicked.connect(self.navegate_Mode_Batch_processing)
        self.ui.Mode_1_long_video.clicked.connect(self.navegate_Mode_1_long_video)

        setup_plain_text_qtextedit(self.username)
        setup_plain_text_qtextedit(self.password)
        
        action_hide.triggered.connect(lambda: self.hide())
        action_show.triggered.connect(lambda: self.showNormal())


        self.check_login()

        QAppSettings.updateAppSettings(self, generateIcons=False)

    # 📌 Event Login
    def check_login(self):
        session_data = load_session(app1, self.SESSION_DB_PATH)
        if is_session_valid(session_data):
            self.session_data = session_data
            self.session_flag = True
            self.inicializer_login(session_data)
            self.init_threads()

            self.instance_Qtaskmanager = TaskManager(self.ref_tasks2)
            self.instance_Qtaskmanager.tasks_fetched.connect(self.update_treeview_tasks_fetched)
            #self.instance_Qtaskmanager.new_tasks.connect(self.update_treeview_add_new_task)
            self.new_tasks_data_signal.connect(self.instance_Qtaskmanager.add_new_task)
            self.instance_Qtaskmanager.start()

            self.initi_count_tasks()
            self.load_config()

        else:
            self.session_flag = False
            self.session_data = None
            if session_data is not None:
                refremove = db.reference(self.SESSION_DB_PATH, app=app1)
                refremove.delete()

    def login(self, username, password):
        username = username.replace("\n", "").strip()
        password = password.replace("\n", "").strip()
        if not username:
            update_custommodals_ErroModal("The user field is empty.", "Login error", 'top-right', self.ui.centralwidget)
            return

        if not password:
            update_custommodals_ErroModal("The password field is empty.", "Login error", 'top-right', self.ui.centralwidget)
            return

        headers = {
            'Content-Type': 'application/json',
        }
        payload = {
            'username': username,
            'password': password
        }

        try:
            response = requests.post(self.url_login, headers=headers, json=payload)
            data = response.json()
            
            if response.ok:
                login_time_obj = datetime.now()
                login_time_str = login_time_obj.strftime("%Y-%m-%d %H:%M:%S")
                expires_at = time.time() + 24 * 3600
                session_data = {
                    "username": username,
                    "login_time": login_time_str,  
                    "expires_at": expires_at,
                    "expire_time_license": data.get("expire_time_license"),
                    "api_key": data.get("api_key"),
                }
                save_session(self.SESSION_DB_PATH, app1, session_data)
                update_custommodals_SuccessModal('Login successfully!', "Success", 'top-right', self.ui.centralwidget)
                print(f"Session valid until: {time.ctime(expires_at)}")
                update_custommodals_Custom(f'Session valid until: {time.ctime(expires_at)}', "Session", 'top-right', self.ui.centralwidget)

                self.session_flag = True
                self.inicializer_login(session_data)
                self.init_threads()

            else:
                error_message = data.get('message') or data.get('error')
                update_custommodals_ErroModal(error_message, "Login error", 'top-right', self.ui.centralwidget)

        except Exception as error:
            print('Erro ao fazer login:', error)
            update_custommodals_ErroModal('Erro ao tentar fazer login. Por favor, tente novamente.', "Login error", 'top-right', self.ui.centralwidget)

    def inicializer_login(self, session_data):
        api_key = session_data.get("api_key")
        login_time = session_data.get("login_time")
        login_time_dt = datetime.strptime(login_time, "%Y-%m-%d %H:%M:%S")
        formatted_login_time = login_time_dt.strftime("%a-%b-%d-%Y  %H:%M:%S")
        expire_time_license = session_data.get("expire_time_license")
        session_name_complet = session_data.get("username")
        session_name = f'{session_name_complet}'
        session_name = session_name.replace("@gmail.com", "")
        if len(session_name) >= 20:
            self.ui.get_myaccount.setText(f"{session_name[:25]}...")
        else:
            self.ui.get_myaccount.setText(f"{session_name}")
        self.ui.label_hello.setText(f"Hello, {session_name}")

        self.ui.label_datetime.setText(f"Last login: {formatted_login_time}")
        self.ui.email_input.setText(session_name_complet)
        self.ui.label_License_expiration.setText(f"License expiration: {expire_time_license}")
        self.ui.api_key_input.setText(f"{api_key}")
        self.ui.stackedWidget.slideToWidgetIndex(14)
        self.ui.pushButton_menu.click()
    
    # 📌 Schedule
    def Schedule_Shortify(self):
        # ----- Verifica os modos escolhidos pelo usuário -----
        # Modo Date: executar apenas uma vez em data/hora específica
        execute_only_once = self.ui.Execute_only_1_time_on_the_date_Date_Mode.isChecked()
        # Modo Weekly com agendamento para o mês: agendar para todas as ocorrências deste mês
        schedule_monthly = self.ui.Schedule_the_month_Weekly_Mode.isChecked()

        # ----- Modo Date (Execute_only_1_time_on_the_date_Date_Mode) -----
        if execute_only_once:
            # Obtém a data/hora informada pelo usuário (ex: "2025-02-20 15:30:00")
            time_date_mode_str = self.ui.Time_Date_Mode.toPlainText().strip()

            # Seleciona o timezone com base nos checkboxes do modo Date
            if self.ui.checkBox_Sao_Paulo_time_zone_Date_Mode.isChecked():
                tz = pytz.timezone('America/Sao_Paulo')
                timezone = 'America/Sao_Paulo'
            elif self.ui.checkBox_UTC_time_zone_Date_Mode.isChecked():
                tz = pytz.timezone('UTC')
                timezone = 'UTC'
            else:
                tz = pytz.utc  # fallback

            # Tenta converter o texto para datetime (supondo o formato "YYYY-MM-DD HH:MM:SS")
            try:
                scheduled_time = datetime.strptime(time_date_mode_str, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                # Se não tiver os segundos, tenta "YYYY-MM-DD HH:MM"
                scheduled_time = datetime.strptime(time_date_mode_str, '%Y-%m-%d %H:%M')

            # Localiza o datetime no timezone escolhido
            scheduled_time = tz.localize(scheduled_time)
            scheduled_time_str = scheduled_time.strftime('%Y-%m-%d %H:%M:%S')

            print("Agendamento único (Date Mode):", scheduled_time_str)
            return scheduled_time_str, "date", timezone

        # ----- Modo Weekly (caso não seja Date Mode) -----
        else:
            # Obtém os dados informados para Weekly Mode
            day_weekly_mode = self.ui.Day_Weekly_Mode.toPlainText().strip().lower()  # ex: "sexta-feira"
            time_weekly_mode = self.ui.Time_Weekly_Mode.toPlainText().strip()         # ex: "20:00" ou "20:00:00"

            # Seleciona o timezone para Weekly Mode
            if self.ui.checkBox_Sao_Paulo_time_zone_Weekly_Mode.isChecked():
                tz = pytz.timezone('America/Sao_Paulo')
                timezone = 'America/Sao_Paulo'
            elif self.ui.checkBox_UTC_time_zone_Weekly_Mode.isChecked():
                tz = pytz.timezone('UTC')
                timezone = 'UTC'
            else:
                tz = pytz.utc

            # Mapeia os dias da semana para números (segunda=0, ..., domingo=6)
            dias_da_semana = {
                'segunda-feira': 0, 'segunda': 0, 'monday': 0,
                'terça-feira': 1, 'terça': 1, 'terca': 1,'tuesday': 1,
                'quarta-feira': 2, 'quarta': 2, 'wednesday': 2,
                'quinta-feira': 3, 'quinta': 3, 'thursday': 3,
                'sexta-feira': 4, 'sexta': 4, 'friday': 4,
                'sábado': 5, 'sabado': 5, 'saturday': 5,
                'domingo': 6, 'sunday': 6
            }

            if day_weekly_mode not in dias_da_semana:
                raise ValueError("Dia da semana inválido: {}".format(day_weekly_mode))
            target_weekday = dias_da_semana[day_weekly_mode]

            # Converte o horário informado (suporta "HH:MM" ou "HH:MM:SS")
            partes = time_weekly_mode.split(':')
            if len(partes) == 2:
                hora, minuto = map(int, partes)
                segundo = 0
            elif len(partes) == 3:
                hora, minuto, segundo = map(int, partes)
            else:
                raise ValueError("Formato de horário inválido: {}".format(time_weekly_mode))

            # Data/hora atual no timezone selecionado
            now = datetime.now(tz)

            # ----- Se o usuário deseja agendar para todas as ocorrências deste mês -----
            if schedule_monthly:
                year = now.year
                month = now.month
                last_day = calendar.monthrange(year, month)[1]
                scheduled_times = []

                # Itera por todos os dias do mês
                for day in range(1, last_day + 1):
                    try:
                        candidate = datetime(year, month, day, hora, minuto, segundo)
                    except ValueError:
                        continue  # ignora datas inválidas
                    candidate = tz.localize(candidate)
                    # Se o candidato cair no dia da semana desejado
                    if candidate.weekday() == target_weekday:
                        # Opcional: incluir somente datas futuras (ou incluir todas do mês)
                        if candidate >= now:
                            scheduled_times.append(candidate)

                # Formata a lista de agendamentos como strings
                scheduled_times_str = [dt.strftime('%Y-%m-%d %H:%M:%S') for dt in scheduled_times]
                print("Agendamentos para este mês (Weekly Mode):", scheduled_times_str)
                return scheduled_times_str, "weekly", timezone

            # ----- Caso contrário, agenda apenas o próximo horário correspondente -----
            else:
                dias_ate = target_weekday - now.weekday()
                if dias_ate < 0:
                    dias_ate += 7
                # Se hoje é o dia escolhido, mas o horário já passou, agenda para a próxima semana
                if dias_ate == 0:
                    candidate = now.replace(hour=hora, minute=minuto, second=segundo, microsecond=0)
                    if candidate <= now:
                        dias_ate = 7
                scheduled_date = now + timedelta(days=dias_ate)
                scheduled_time = scheduled_date.replace(hour=hora, minute=minuto, second=segundo, microsecond=0)
                scheduled_time_str = scheduled_time.strftime('%Y-%m-%d %H:%M:%S')
                print("Próximo agendamento (Weekly Mode):", scheduled_time_str)
                return scheduled_time_str, "weekly", timezone

    # 📌 Event Start Shortify
    def Start_Shortify(self):
        scheduled_time, mode, timezone = self.Schedule_Shortify()
        hash_task_list = []
        if isinstance(scheduled_time, list):
            for scheduled_time_ in scheduled_time:
                hash_task = hashlib.sha256(f"{scheduled_time_}".encode()).hexdigest()
                hash_task_list.append(hash_task)
        elif isinstance(scheduled_time, str):
            hash_task = hashlib.sha256(f"{scheduled_time}".encode()).hexdigest()
            hash_task_list.append(hash_task)

        print(scheduled_time)    
        print(mode)  
        print(timezone)  
        watermark_image = self.watermark_image
        text_watermark = self.ui.text_watermark.toPlainText()

        api_key = self.ui.api_key_input.toPlainText()
        canal_do_yt = self.ui.channel_yt.toPlainText()

        SubtitleVerticalReference = str(self.ui.Subtitle_Vertical_Reference.value())
        SubtitleFontsize = str(self.ui.Subtitle_Fontsize.value())
        SubtitleColor = self.ui.Subtitle_Color.toPlainText()
        SubtitleAnimation = self.ui.Subtitle_Animation.toPlainText()
        SubtitleEffects = self.ui.Subtitle_Effects.toPlainText()
        SubtitleFontName = self.ui.Subtitle_FontName.toPlainText()

        CaptionsAlignment = self.ui.Captions_Alignment.value()
        CaptionsColor = self.ui.Captions_PrimaryColour.toPlainText()
        CaptionsFontName = self.ui.Captions_FontName.toPlainText()
        CaptionsFontsize = self.ui.Captions_Fontsize.value()
        CaptionsPrimaryColour = self.ui.Captions_PrimaryColour.toPlainText()
        CaptionsSecondaryColour = self.ui.Captions_SecondaryColour.toPlainText()
        CaptionsOutlineColour = self.ui.Captions_OutlineColour.toPlainText()
        CaptionsBackColour = self.ui.Captions_BackColour.toPlainText()

        CaptionsBold = int(self.ui.Captions_Bold_Bool.isChecked())
        CaptionsShadow = int(self.ui.Captions_Shadow_Bool.isChecked())
        CaptionsItalic = int(self.ui.Captions_Italic_Bool.isChecked())
        CaptionsUnderline = int(self.ui.Captions_Underline_Bool.isChecked())
        CaptionsOutline = self.ui.Captions_Outline.value()

        CaptionsRevealEffectInitialColor = self.ui.Captions_Reveal_Effect_Initial_Color.toPlainText()
        CaptionsRevealEffectFinalColor = self.ui.Captions_Reveal_Effect_Final_Color.toPlainText()
        Cutting_seconds = self.ui.Cutting_seconds.value()

        user_email = self.ui.email_input.toPlainText().replace(".", "").replace("@", "")

        headers = {"X-API-KEY": api_key}
        payload = {
            "timezone": timezone,
            "mode": mode,
            "user_email": user_email,
            "date_time": scheduled_time, 
            "hash_task_list": hash_task_list,
            "canal_do_yt": canal_do_yt,
            "watermark_image": watermark_image,
            "text_watermark": text_watermark,
            "Cutting_seconds": Cutting_seconds,
            "api_key": api_key,
            "SubtitleColor": SubtitleColor,
            "SubtitleAnimation": SubtitleAnimation,  
            "SubtitleFontName": SubtitleFontName,
            "SubtitleEffects": SubtitleEffects,
            "SubtitleFontsize": SubtitleFontsize,
            "SubtitleVerticalReference": SubtitleVerticalReference,
            "CaptionsColor": CaptionsColor,
            "CaptionsFontName": CaptionsFontName,
            "CaptionsAlignment": CaptionsAlignment,
            "CaptionsFontsize": CaptionsFontsize,
            "CaptionsPrimaryColour": CaptionsPrimaryColour,
            "CaptionsSecondaryColour": CaptionsSecondaryColour,
            "CaptionsOutlineColour": CaptionsOutlineColour,
            "CaptionsBackColour": CaptionsBackColour,
            "CaptionsBold": CaptionsBold,
            "CaptionsItalic": CaptionsItalic,
            "CaptionsUnderline": CaptionsUnderline,
            "CaptionsOutline": CaptionsOutline,
            "CaptionsShadow": CaptionsShadow,
            "CaptionsRevealEffectInitialColor": CaptionsRevealEffectInitialColor,
            "CaptionsRevealEffectFinalColor": CaptionsRevealEffectFinalColor
        }
        self.save_config(payload)
        try:
            response = requests.post(self.API_URL_Shortify, json=payload, headers=headers)
            response_json = response.json()
            response_message = response_json.get("message", "Mensagem não encontrada")
            self.task_id = response_json.get("task_id", "Mensagem não encontrada")
            response_scheduled_times = response_json.get("scheduled_times", [])

            # response_json = {
            #     "scheduled_times": response_scheduled_times,
            #     "channel_yt": canal_do_yt
            # }
            # #self.update_treeview_add_new_task(response_json)
            # self.new_tasks_data_signal.emit(response_json)

            update_custommodals_SuccessModal(title=f"Tasks", description=f"{response_message}", parent=self.ui.centralwidget)
            update_custommodals_SuccessModal(title=f"Times", description=f"{response_scheduled_times}", parent=self.ui.centralwidget)
            
            tasks_data = self.ref_tasks2.get()
            self.update_treeview_tasks_fetched(tasks_data)    

            self.ui.stackedWidget.slideToWidgetIndex(13)  

        except requests.exceptions.RequestException as err:
            print(f"Erro ao enviar a requisição: {err}")

    # 📌 Event _init_
    def _init_change_efects_sub_(self):
        self.ui.button_effects_Shadow_sub.clicked.connect(lambda: self.change_efects_sub("Shadow"))
        self.ui.button_GlowEffect_Shadow_sub.clicked.connect(lambda: self.change_efects_sub("Glow Effect"))
        self.ui.button_effects_NeonGlow_sub.clicked.connect(lambda: self.change_efects_sub("Neon Glow"))
        self.ui.button_effects_DottedOutline_sub.clicked.connect(lambda: self.change_efects_sub("Dotted Outline"))
        self.ui.button_effects_BoldShadow_sub.clicked.connect(lambda: self.change_efects_sub("Bold Shadow"))
        self.ui.button_effects_InnerGlow_sub.clicked.connect(lambda: self.change_efects_sub("Inner Glow"))
        self.ui.button_effects_WavyOutline_sub.clicked.connect(lambda: self.change_efects_sub("Wavy Outline"))
        self.ui.button_effects_DropShadow_sub.clicked.connect(lambda: self.change_efects_sub("Drop Shadow"))
        self.ui.button_effects_ThickOutline_sub.clicked.connect(lambda: self.change_efects_sub("Thick Outline"))
        self.ui.button_effects_DoubleOutline_sub.clicked.connect(lambda: self.change_efects_sub("Double Outline"))
        self.ui.button_effects_BlurredShadow_sub.clicked.connect(lambda: self.change_efects_sub("Blurred Shadow"))
        self.ui.button_effects_HardGlow_sub.clicked.connect(lambda: self.change_efects_sub("Hard Glow"))
        self.ui.button_effects_SoftGlow_sub.clicked.connect(lambda: self.change_efects_sub("Soft Glow"))
        self.ui.button_effects_Emboss_sub.clicked.connect(lambda: self.change_efects_sub("Emboss"))
        self.ui.button_effects_TransparentOutline_sub.clicked.connect(lambda: self.change_efects_sub("Transparent Outline"))
        self.ui.button_effects_SoftShadow_sub.clicked.connect(lambda: self.change_efects_sub("Soft Shadow"))
        self.ui.button_effects_Outline_sub.clicked.connect(lambda: self.change_efects_sub("Outline"))
        self.ui.button_effects_None_sub.clicked.connect(lambda: self.change_efects_sub("None"))

    def _init_change_animation_sub_(self):
        self.ui.button_animation_FadeIn_sub.clicked.connect(lambda: self.change_animation_sub("Fade-In"))
        self.ui.button_animation_Pulse_sub.clicked.connect(lambda: self.change_animation_sub("Pulse"))
        self.ui.button_animation_SlowFadeOut_sub.clicked.connect(lambda: self.change_animation_sub("Slow Fade-Out"))
        self.ui.button_animation_FastBlink_sub.clicked.connect(lambda: self.change_animation_sub("Fast Blink"))
        self.ui.button_animation_AppearDisappear_sub.clicked.connect(lambda: self.change_animation_sub("Appear-Disappear"))
        self.ui.button_animation_Gradual_Blink_sub.clicked.connect(lambda: self.change_animation_sub("Gradual Blink"))
        self.ui.button_animation_Soft_Fade_In_Out_sub.clicked.connect(lambda: self.change_animation_sub("Soft Fade-In-Out"))
        self.ui.button_animation_FadeInandHold_sub.clicked.connect(lambda: self.change_animation_sub("Fade-In and Hold"))
        self.ui.button_animation_PulseOut_sub.clicked.connect(lambda: self.change_animation_sub("Pulse Out"))
        self.ui.button_animation_FadeOut_and_Hold_sub.clicked.connect(lambda: self.change_animation_sub("Fade-Out and Hold"))
        self.ui.button_animation_BlinkingText_sub.clicked.connect(lambda: self.change_animation_sub("Blinking Text"))
        self.ui.button_animation_QuickFadeOut_sub.clicked.connect(lambda: self.change_animation_sub("Quick Fade-Out"))
        self.ui.button_animation_QuickFadeIn_sub.clicked.connect(lambda: self.change_animation_sub("Quick Fade-In"))
        self.ui.button_animation_None_sub.clicked.connect(lambda: self.change_animation_sub("None"))

    def _init_change_font_sub_(self):
        self.ui.button_Impact_sub.clicked.connect(lambda: self.change_fontname_sub("Impact"))
        self.ui.button_Calibri_sub.clicked.connect(lambda: self.change_fontname_sub("Calibri"))
        self.ui.button_LucidaConsole_sub.clicked.connect(lambda: self.change_fontname_sub("Lucida Console"))
        self.ui.button_Garamond_sub.clicked.connect(lambda: self.change_fontname_sub("Garamond"))
        self.ui.button_Trebuchet_MS_sub.clicked.connect(lambda: self.change_fontname_sub("Trebuchet MS"))
        self.ui.button_FranklinGothic_sub.clicked.connect(lambda: self.change_fontname_sub("Franklin Gothic"))
        self.ui.button_CenturyGothic_sub.clicked.connect(lambda: self.change_fontname_sub("Century Gothic"))
        self.ui.button_Comic_Sans_MS_sub.clicked.connect(lambda: self.change_fontname_sub("Comic Sans MS"))
        self.ui.button_Tahoma_sub.clicked.connect(lambda: self.change_fontname_sub("Tahoma"))
    
    def _init_change_fontname_cc_(self):
        self.ui.button_Impact_Captions.clicked.connect(lambda: self.change_fontname_cc("Impact"))
        self.ui.button_Calibri_Captions.clicked.connect(lambda: self.change_fontname_cc("Calibri"))
        self.ui.button_LucidaConsole_Captions.clicked.connect(lambda: self.change_fontname_cc("Lucida Console"))
        self.ui.button_Garamond_Captions.clicked.connect(lambda: self.change_fontname_cc("Garamond"))
        self.ui.button_Trebuchet_MS_Captions.clicked.connect(lambda: self.change_fontname_cc("Trebuchet MS"))
        self.ui.button_FranklinGothic_Captions.clicked.connect(lambda: self.change_fontname_cc("Franklin Gothic"))
        self.ui.button_CenturyGothic_Captions.clicked.connect(lambda: self.change_fontname_cc("Century Gothic"))
        self.ui.button_Comic_Sans_MS_Captions.clicked.connect(lambda: self.change_fontname_cc("Comic Sans MS"))
        self.ui.button_Tahoma_Captions.clicked.connect(lambda: self.change_fontname_cc("Tahoma"))


    def cancel_task(self, hash_value):
        """
        Percorre todos os nós em 'save_tasks_users/task/{machine}' e,
        se uma tarefa possuir um scheduled_time cujo hash seja igual a hash_value,
        remove apenas esse horário. Se após a remoção a lista de horários ficar vazia,
        o nó é excluído; caso contrário, ele é atualizado com os horários restantes.
        """
        tasks_data = self.ref_tasks2.get()
        if tasks_data:
            for id, task in tasks_data.items():
                for id_task, task in task.items():
                    computed_hash = task.get('task_id')
                    if task.get("user_email") == self.ui.email_input.toPlainText().replace(".", "").replace("@", ""):
                        scheduled_time = task.get('scheduled_time')
                        hash_task = task.get('hash_task')
                        task_id_celery = task.get('task_id')

                        print(f"Horário '{scheduled_time}' da tarefa com hash {hash_task} cancelado.")
                        print(f"Horário '{scheduled_time}' da tarefa {task_id_celery[:8]}... cancelado.")
                        email_input = self.ui.email_input.toPlainText().replace(".", "").replace("@", "")
                        self.ref_tasks_delet = db.reference(f'save_tasks_users/task/{email_input}/{id_task}', app=app1)
                        self.ref_tasks_delet.delete()
                        data = {"task_id": task_id_celery,
                                "eta": scheduled_time
                            }
                        headers = {"X-API-KEY": f"{self.ui.api_key_input.toPlainText()}"}
                        response = requests.post(self.url_endpoint_delet_task, json=data, headers=headers)
                        if response.status_code == 200:
                            print("Tarefa cancelada com sucesso!")
                            print("Resposta:", response.json())
                        else:
                            print(f"Erro ao cancelar a tarefa: {response.status_code}")
                            print("Detalhes:", response.text)

                        update_custommodals_SuccessModal(title=f"Task Canceled", description=f"Time '{scheduled_time}' of the task {hash_task[:8]}... canceled.", parent=self.ui.centralwidget)
                        tasks_data = self.ref_tasks2.get()
                        self.update_treeview_tasks_fetched(tasks_data)         
                        break
                break        

   

    def update_treeview_tasks_fetched(self, tasks_data):
        self.tree_model.removeRows(0, self.tree_model.rowCount())
        try:
            for id, task2 in tasks_data.items():
                for id, task in task2.items():
                    if task.get("user_email") == self.ui.email_input.toPlainText().replace(".", "").replace("@", ""):
                        scheduled_time = task.get('scheduled_time', "")
                        mode = task.get('mode', "")
                        timezone = task.get('timezone', "")
                        channel_yt = task.get('yt_channel', '')
                        hash_task = task.get('task_id', '')
                        status = task.get("status", '')

                        item_hash = QStandardItem()
                        item_hash.setText(hash_task)
                        #item_hash.setIcon(QIcon(QPixmap(":/feather/icons/feather/database.png")))

                        
                        item_timezone = QStandardItem()
                        item_timezone.setText(timezone)
                        #item_mode.setIcon(QIcon(QPixmap(":/feather/icons/feather/settings.png")))


                        item_time = QStandardItem()
                        item_time.setText(scheduled_time)
                        #item_time.setIcon(QIcon(QPixmap(":/font_awesome/icons/font_awesome/calendar-days.png")))

                        
                        item_mode = QStandardItem()
                        item_mode.setText(mode)
                        #item_mode.setIcon(QIcon(QPixmap(":/feather/icons/feather/settings.png")))



                        item_channel = QStandardItem()
                        item_channel.setText(channel_yt)
                        #item_channel.setIcon(QIcon(QPixmap(":/font_awesome/icons/font_awesome/youtube.png")))

                        status_item = self.create_status_item(status) 
                        cancel_item = QStandardItem()
                        current_row = self.tree_model.rowCount()


                        self.tree_model.appendRow([item_hash, item_time, item_timezone, item_mode, item_channel, status_item, cancel_item])

                        button = QPushButton()
                        button.setIcon(QIcon(':/font_awesome/icons/font_awesome/trash-can.png'))
                        button.setText("Cancel Task")
                        button.setStyleSheet("qproperty-alignment: Alignleft; color: white; background: transparent; border: none;")
                        button.clicked.connect(lambda *args, h=hash_task: self.cancel_task(h))
                        index_cancel = self.tree_model.index(current_row, 6)
                        self.widget_area_task.setIndexWidget(index_cancel, button)
        except:
            pass


    def create_status_item(self, status):
        """
        Cria um QStandardItem representando o status da tarefa.

        """
        status_icons = {
            "Created": QIcon(QPixmap(":/material_design/icons/material_design/create.png")),
            "Running": QIcon(QPixmap(":/material_design/icons/material_design/pending_actions.png")),
            "Completed": QIcon(QPixmap(":/material_design/icons/material_design/check_circle.png")),
        }
        
        status_item = QStandardItem()
        status_item.setText(status)
        status_item.setIcon(status_icons.get(status, QIcon()))  # Ícone padrão vazio se não encontrado
        return status_item

    def update_treeview_add_new_task(self, tasks_data):
        print(tasks_data)
        """
        Adiciona uma nova tarefa:
          - Armazena a tarefa no Firebase.
          - Atualiza a TreeView.
        
        :param response_json: JSON contendo a chave "scheduled_times" com uma lista de datas/horários.
        """
        # Obtém a lista de datas/horários da resposta e o canal do YouTube do widget
        response_scheduled_times = tasks_data.get("scheduled_times", [])
        canal_do_yt = self.ui.channel_yt.toPlainText()
        
        # Opcional: coletar outras informações, por exemplo, informações da máquina
        machine_info = self.get_machine_info()
        
        # Cria o dicionário que representa a nova tarefa
        new_task = {
            'scheduled_times': response_scheduled_times,
            'channel_yt': canal_do_yt,
            'machine_info': machine_info
        }
        
        # Salva a nova tarefa no Firebase (o push gera uma nova chave única para a tarefa)
        new_task_ref = self.ref_tasks.push(new_task)
        print(f"Tarefa adicionada com ID: {new_task_ref.key}")
        
        # Atualiza a TreeView adicionando as novas linhas com o status
        for scheduled_time in response_scheduled_times:
            hash_task = hashlib.sha256(f"{scheduled_time}".encode()).hexdigest()
            item_hash = QStandardItem(hash_task)
            item_time = QStandardItem(scheduled_time)
            item_channel = QStandardItem(canal_do_yt)
            status_item = self.create_status_item(scheduled_time)
            cancel_item = QStandardItem()  # Placeholder
            
            current_row = self.tree_model.rowCount()

            self.tree_model.appendRow([
                item_hash, item_time, item_channel, status_item, cancel_item
            ])
            
            button = QPushButton()
            button.setIcon(QIcon(':/font_awesome_regular/icons/font_awesome/regular/trash-can.png'))
            button.setToolTip("Cancelar tarefa")
            # Define um stylesheet para que o botão fique com fundo transparente e sem borda
            button.setStyleSheet("background: transparent; border: none;")

            # Usa lambda com parâmetro default para capturar o hash do horário atual
            button.clicked.connect(lambda *args, h=hash_task: self.cancel_task(h))
            
            index_cancel = self.tree_model.index(current_row, 4)
            self.widget_area_task.setIndexWidget(index_cancel, button)
        else:
            print("Nenhuma tarefa encontrada no Firebase.")

    # 📌 Event Handle Accept and reject
    def handle_accepted_selector_reveal_effect_final_color_captions(self):
        update_custommodals_SuccessModal(title=f"Your Reveal Effect Final Color setting", description=f"Your Reveal Effect Final color setting has been added to the panel", parent=self.ui.centralwidget)

    def handle_rejected_selector_reveal_effect_final_color_captions(self):
        update_custommodals_Warning(title=f"Your Reveal Effect Final Color setting", description=f"Your Reveal Effect Final color setting has not been added to the panel", parent=self.ui.centralwidget)

    def handle_accepted_selector_reveal_effect_initial_color_captions(self):
        update_custommodals_SuccessModal(title=f"Your Reveal Effect Initial color setting", description=f"Your  Reveal Effect Initial color setting has been added to the panel", parent=self.ui.centralwidget)

    def handle_rejected_selector_reveal_effect_initial_color_captions(self):
        update_custommodals_Warning(title=f"Your Reveal Effect Initial color setting", description=f"Your Reveal Effect Initial color setting has not been added to the panel", parent=self.ui.centralwidget)

    def handle_accepted_selector_back_color_captions(self):
        update_custommodals_SuccessModal(title=f"Your Back color setting", description=f"Your Back color setting has been added to the panel", parent=self.ui.centralwidget)

    def handle_rejected_selector_back_color_captions(self):
        update_custommodals_Warning(title=f"Your Back color setting", description=f"Your Back color setting has not been added to the panel", parent=self.ui.centralwidget)

    def handle_accepted_selector_outline_color_captions(self):
        update_custommodals_SuccessModal(title=f"Your Outline color setting", description=f"Your Outline color setting has been added to the panel", parent=self.ui.centralwidget)

    def handle_rejected_selector_outline_color_captions(self):
        update_custommodals_Warning(title=f"Your Outline color setting", description=f"Your Outline color setting has not been added to the panel", parent=self.ui.centralwidget)

    def handle_accepted_selector_secondary_color_captions(self):
        update_custommodals_SuccessModal(title=f"Your Secondary color setting", description=f"Your Secondary color setting has been added to the panel", parent=self.ui.centralwidget)

    def handle_rejected_selector_secondary_color_captions(self):
        update_custommodals_Warning(title=f"Your Secondary color setting", description=f"Your Secondary color setting has not been added to the panel", parent=self.ui.centralwidget)

    def handle_accepted_selector_primary_color_captions(self):
        update_custommodals_SuccessModal(title=f"Your Primary color setting", description=f"Your Primary color setting has been added to the panel", parent=self.ui.centralwidget)

    def handle_rejected_selector_primary_color_captions(self):
        update_custommodals_Warning(title=f"Your Primary color setting", description=f"Your Primary color setting has not been added to the panel", parent=self.ui.centralwidget)

    def handle_accepted_selector_fontname_captions(self):
        update_custommodals_SuccessModal(title=f"Your FontName setting", description=f"Your FontName setting has been added to the panel", parent=self.ui.centralwidget)

    def handle_rejected_selector_fontname_captions(self):
        update_custommodals_Warning(title=f"Your FontName setting", description=f"Your FontName color setting has not been added to the panel", parent=self.ui.centralwidget)

    def handle_accepted_selector_fontname_subtitles(self):
        update_custommodals_SuccessModal(title=f"Your FontName setting", description=f"Your FontName setting has been added to the panel", parent=self.ui.centralwidget)

    def handle_rejected_selector_fontname_subtitles(self):
        update_custommodals_Warning(title=f"Your FontName setting", description=f"Your FontName color setting has not been added to the panel", parent=self.ui.centralwidget)
    
    def handle_accepted_selector_effects_subtitles(self):
        update_custommodals_SuccessModal(title=f"Your effects setting", description=f"Your Effects setting has been added to the panel", parent=self.ui.centralwidget)

    def handle_rejected_selector_effects_subtitles(self):
        update_custommodals_Warning(title=f"Your effects setting", description=f"Your effects color setting has not been added to the panel", parent=self.ui.centralwidget)
    
    def handle_accepted_selector_animation_subtitles(self):
        update_custommodals_SuccessModal(title=f"Your animation setting", description=f"Your Animation configuration has been added to the panel", parent=self.ui.centralwidget)

    def handle_rejected_selector_animation_subtitles(self):
        update_custommodals_Warning(title=f"Your animation setting", description=f"Your animation color setting has not been added to the panel", parent=self.ui.centralwidget)

    def handle_accepted_selector_color_subtitles(self):
        update_custommodals_SuccessModal(title=f"Your color setting", description=f"Your color setting has been added to the panel", parent=self.ui.centralwidget)

    def handle_rejected_selector_color_subtitles(self):
        update_custommodals_Warning(title=f"Your color setting", description=f"Your color setting has not been added to the panel", parent=self.ui.centralwidget)
        self.ui.Subtitle_Color.clear()

    def handle_accepted_upload_image_watermark(self):
        update_custommodals_SuccessModal(title=f"Your Watermark Image", description=f"Your Watermark Image has been added to the dashboard", parent=self.ui.centralwidget)

    def handle_rejected_upload_image_watermark(self):
        update_custommodals_Warning(title=f"Your Watermark Image",  description=f"Your Watermark setting has not been added to the panel", parent=self.ui.centralwidget)

    def handle_accepted_Select_Time(self):
        update_custommodals_SuccessModal(title=f"Your Scheduling Setting",  description=f"Your Scheduling Setting has been added to the dashboard", parent=self.ui.centralwidget)

    def handle_rejected_Select_Time(self):
        update_custommodals_Warning(title=f"Your Scheduling Setting",  description=f"Your Scheduling Setting has not been added to the dashboard", parent=self.ui.centralwidget)

    # 📌 Event Change States
    def change_animation_sub(self, animation):
        self.SubtitleAnimation = animation
        update_custommodals_SuccessModal(title=f"Your animation", description=f"Your animation {animation} has been selected", parent=self.ui.centralwidget)
        self.ui.Subtitle_Animation.setText(animation)

    def change_efects_sub(self, efects):
        self.SubtitleEffects = efects
        update_custommodals_SuccessModal(title=f"Your effects", description=f"Your effect {efects} has been selected", parent=self.ui.centralwidget)
        self.ui.Subtitle_Effects.setText(efects)

    def change_fontname_sub(self, FontName):
        self.SubtitleFontName = FontName
        update_custommodals_SuccessModal(title=f"Your Subtitles FontName", description=f"Your FontName {FontName} has been selected", parent=self.ui.centralwidget)
        self.ui.Subtitle_FontName.setText(FontName)

    def change_fontname_cc(self, FontName):
        self.CaptionsFontName = FontName
        update_custommodals_SuccessModal(title=f"Your Captions FontName", description=f"Your FontName {FontName} has been selected", parent=self.ui.centralwidget)
        self.ui.Captions_FontName.setText(FontName)

    # 📌 Event Selector Color
    def change_background_color(self, color):
        self.ui.Subtitle_Color.setText(f"{color.name()}")
        self.SubtitleColor = color.name()

    def change_background_color_selector_primary_color_captions(self, color):
        color_hex = "&H" + color.name()[1:].upper()
        self.ui.Captions_PrimaryColour.setText(f"{color_hex}")
        self.CaptionsPrimaryColour = color_hex
        self.CaptionsColor = color.name()

    def change_background_color_selector_secondary_color_captions(self, color):
        color_hex = "&H" + color.name()[1:].upper()
        self.ui.Captions_SecondaryColour.setText(f"{color_hex}")
        self.CaptionsSecondaryColour = color_hex

    def change_background_color_selector_outline_color_captions(self, color):
        color_hex = "&H" + color.name()[1:].upper()
        self.ui.Captions_OutlineColour.setText(f"{color_hex}")
        self.CaptionsOutlineColour = color_hex

    def change_background_color_selector_back_color_captions(self, color):
        color_hex = "&H" + color.name()[1:].upper()
        self.ui.Captions_BackColour.setText(f"{color_hex}")
        self.CaptionsBackColour = color_hex

    def change_background_color_selector_reveal_effect_initial_color_captions(self, color):
        color_hex = "&H" + color.name()[1:].upper()
        self.ui.Captions_Reveal_Effect_Initial_Color.setText(f"{color_hex}")
        self.CaptionsRevealEffectInitialColor = color_hex

    def change_background_color_selector_reveal_effect_final_color_captions(self, color):
        color_hex = "&H" + color.name()[1:].upper()
        self.ui.Captions_Reveal_Effect_Final_Color.setText(f"{color_hex}")
        self.CaptionsRevealEffectFinalColor = color_hex

    # 📌 Dialog Upload Image
    def DialogUploadImage(self):
        dialog = QFileDialog()
        dialog.setStyleSheet("""
            QFileDialog {
                background-color: white;
                border: 1px solid #F7F7F7;
                border-radius: 13px;
                color: black;
                font-size: 16px;
            }
            /* Personalizar os botões */
            QPushButton {
                background-color: #F7F7F7;
                border: 1px solid #CCCCCC;
                border-radius: 8px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #E6E6E6;
            }
            QPushButton:pressed {
                background-color: #D6D6D6;
            }
            /* Personalizar lista de arquivos */
            QListView, QTreeView {
                background-color: white;
                border: none;
                color: black;
                font-size: 14px;
            }
            /* Barra de navegação */
            QLineEdit {
                background-color: #F7F7F7;
                border: 1px solid #CCCCCC;
                border-radius: 6px;
                padding: 3px;
            }
        """)
        dialog.setFileMode(QFileDialog.ExistingFile) 
        dialog.setWindowTitle("Select the Image")
        dialog.setNameFilter("Imagens (*.png *.jpg *.jpeg)")
        if dialog.exec_():
            self.selected_file = dialog.selectedFiles()[0]
            self.watermark_image = self.selected_file
            update_custommodals_Custom(title=f"Your Image", description=f"Your Image has been Configured Save to confirm", parent=self.ui.centralwidget)
            self.preview_widget.setImage(self.watermark_image)

    # 📌 Custom Dialogs
    def custom_dialog_selector_reveal_effect_final_color_captions(self):
        layout = QVBoxLayout(self.ui.widget_Selector_Reveal_Effect_Final_Colour_Captions)
        color_dialog = QColorDialog()
        color_dialog.setOption(QColorDialog.DontUseNativeDialog, True)
        color_dialog.setOption(QColorDialog.NoButtons, True)
        color_dialog.setMinimumSize(400, 300)
        color_dialog.currentColorChanged.connect(self.change_background_color_selector_reveal_effect_final_color_captions)
        custom_dialog(
            yesButtonText="Save Reveal Effect Final Color Setting",
            cancelButtonText="Leave Reveal Effect Final Color Setting",
            myParentWidget=self.ui.centralwidget,
            yourNewWidget=color_dialog,
            handle_accepted=self.handle_accepted_selector_reveal_effect_final_color_captions,
            handle_rejected=self.handle_rejected_selector_reveal_effect_final_color_captions
        )

    def custom_dialog_selector_reveal_effect_initial_color_captions(self):
        layout = QVBoxLayout(self.ui.widget_Selector_Reveal_Effect_Initial_Colour_Captions)
        color_dialog = QColorDialog()
        color_dialog.setOption(QColorDialog.DontUseNativeDialog, True)
        color_dialog.setOption(QColorDialog.NoButtons, True)
        color_dialog.setMinimumSize(400, 300)
        color_dialog.currentColorChanged.connect(self.change_background_color_selector_reveal_effect_initial_color_captions)
        custom_dialog(
            yesButtonText="Save Reveal Effect Initial Color Setting",
            cancelButtonText="Leave Reveal Effect Initial Color Setting",
            myParentWidget=self.ui.centralwidget,
            yourNewWidget=color_dialog,
            handle_accepted=self.handle_accepted_selector_reveal_effect_initial_color_captions,
            handle_rejected=self.handle_rejected_selector_reveal_effect_initial_color_captions
        )

    def custom_dialog_selector_back_color_captions(self):
        layout = QVBoxLayout(self.ui.widget_Selector_Back_Colour_Captions)
        color_dialog = QColorDialog()
        color_dialog.setOption(QColorDialog.DontUseNativeDialog, True)
        color_dialog.setOption(QColorDialog.NoButtons, True)
        color_dialog.setMinimumSize(400, 300)
        color_dialog.currentColorChanged.connect(self.change_background_color_selector_back_color_captions)
        custom_dialog(
            yesButtonText="Save Back Color Setting",
            cancelButtonText="Leave Back Color Setting",
            myParentWidget=self.ui.centralwidget,
            yourNewWidget=color_dialog,
            handle_accepted=self.handle_accepted_selector_back_color_captions,
            handle_rejected=self.handle_rejected_selector_back_color_captions
        )

    def custom_dialog_selector_outline_color_captions(self):
        layout = QVBoxLayout(self.ui.widget_Selector_Outline_Colour_Captions)
        color_dialog = QColorDialog()
        color_dialog.setOption(QColorDialog.DontUseNativeDialog, True)
        color_dialog.setOption(QColorDialog.NoButtons, True)
        color_dialog.setMinimumSize(400, 300)
        color_dialog.currentColorChanged.connect(self.change_background_color_selector_outline_color_captions)
        custom_dialog(
            yesButtonText="Save Outline Color Setting",
            cancelButtonText="Leave Outline Color Setting",
            myParentWidget=self.ui.centralwidget,
            yourNewWidget=color_dialog,
            handle_accepted=self.handle_accepted_selector_outline_color_captions,
            handle_rejected=self.handle_rejected_selector_outline_color_captions
        )

    def custom_dialog_selector_secondary_color_captions(self):
        layout = QVBoxLayout(self.ui.widget_Selector_Secondary_Colour_Captions)
        color_dialog = QColorDialog()
        color_dialog.setOption(QColorDialog.DontUseNativeDialog, True)
        color_dialog.setOption(QColorDialog.NoButtons, True)
        color_dialog.setMinimumSize(400, 300)
        color_dialog.currentColorChanged.connect(self.change_background_color_selector_secondary_color_captions)
        custom_dialog(
            yesButtonText="Save Secondary Color Setting",
            cancelButtonText="Leave Secondary Color Setting",
            myParentWidget=self.ui.centralwidget,
            yourNewWidget=color_dialog,
            handle_accepted=self.handle_accepted_selector_secondary_color_captions,
            handle_rejected=self.handle_rejected_selector_secondary_color_captions
        )

    def custom_dialog_selector_primary_color_captions(self):
        layout = QVBoxLayout(self.ui.widget_Selector_Primary_Colour_Captions)
        color_dialog = QColorDialog()
        color_dialog.setOption(QColorDialog.DontUseNativeDialog, True)
        color_dialog.setOption(QColorDialog.NoButtons, True)
        color_dialog.setMinimumSize(400, 300)
        color_dialog.currentColorChanged.connect(self.change_background_color_selector_primary_color_captions)
        custom_dialog(
            yesButtonText="Save Primary Color Setting",
            cancelButtonText="Leave Primary Color Setting",
            myParentWidget=self.ui.centralwidget,
            yourNewWidget=color_dialog,
            handle_accepted=self.handle_accepted_selector_primary_color_captions,
            handle_rejected=self.handle_rejected_selector_primary_color_captions
        )

    def custom_dialog_selector_fontname_captions(self):
        custom_dialog(
            yesButtonText="Save FontName Setting",
            cancelButtonText="Leave FontName Setting",
            myParentWidget=self.ui.centralwidget,
            yourNewWidget=self.ui.widget_Selector_FontName_Captions,
            handle_accepted=self.handle_accepted_selector_fontname_captions,
            handle_rejected=self.handle_rejected_selector_fontname_captions
        )

    def custom_dialog_selector_fontname_subtitles(self):
        custom_dialog(
            yesButtonText="Save FontName Setting",
            cancelButtonText="Leave FontName Setting",
            myParentWidget=self.ui.centralwidget,
            yourNewWidget=self.ui.widget_Selector_FontName_Subtitles,
            handle_accepted=self.handle_accepted_selector_fontname_subtitles,
            handle_rejected=self.handle_rejected_selector_fontname_subtitles
        )

    def custom_dialog_selector_effects_subtitles(self):
        custom_dialog(
            yesButtonText="Save Effects Setting",
            cancelButtonText="Leave Effects Setting",
            myParentWidget=self.ui.centralwidget,
            yourNewWidget=self.ui.widget_Selector_Effects_Subtitles,
            handle_accepted=self.handle_accepted_selector_effects_subtitles,
            handle_rejected=self.handle_rejected_selector_effects_subtitles
        )

    def custom_dialog_selector_animation_subtitles(self):
        custom_dialog(
            yesButtonText="Save Animation Setting",
            cancelButtonText="Leave Animation Setting",
            myParentWidget=self.ui.centralwidget,
            yourNewWidget=self.ui.widget_Selector_Animation_Subtitles,
            handle_accepted=self.handle_accepted_selector_animation_subtitles,
            handle_rejected=self.handle_rejected_selector_animation_subtitles
        )

    def custom_dialog_selector_color_subtitles(self):
        layout = QVBoxLayout(self.ui.widget_Color_Subtitles)
        self.color_dialog = QColorDialog()
        self.color_dialog.setOption(QColorDialog.DontUseNativeDialog, True)
        self.color_dialog.setOption(QColorDialog.NoButtons, True)
        self.color_dialog.setMinimumSize(400, 300)
        self.color_dialog.currentColorChanged.connect(self.change_background_color)
        custom_dialog(
            title="Select Color For Subtitles",
            yesButtonText="Save Color Setting",
            cancelButtonText="Leave Color Setting",
            myParentWidget=self.ui.centralwidget,
            yourNewWidget=self.color_dialog,
            handle_accepted=self.handle_accepted_selector_color_subtitles,
            handle_rejected=self.handle_rejected_selector_color_subtitles
        )

    def custom_dialog_upload_image_watermark(self):
        custom_dialog(
            title="Upload Image Watermark",
            yesButtonText="Save Upload Watermark Setting",
            cancelButtonText="Leave Upload Watermark Setting",
            myParentWidget=self.ui.centralwidget,
            yourNewWidget=self.ui.widget_Upload_image_watermark,
            handle_accepted=self.handle_accepted_upload_image_watermark,
            handle_rejected=self.handle_rejected_upload_image_watermark

        )

    def custom_dialog_Select_Time(self):
        custom_dialog(
            title="Selector Date and time",
            yesButtonText="Save Schedule Setting",
            cancelButtonText="Leave Schedule Setting",
            myParentWidget=self.ui.centralwidget,
            yourNewWidget=self.ui.widget_Select_Time,
            handle_accepted=self.handle_accepted_Select_Time,
            handle_rejected=self.handle_rejected_Select_Time
        )

    # 📌 Inicializando Webhook
    def init_threads(self):
        """Inicializa as threads de WebSocket e cronômetro."""

        API_KEY = self.ui.api_key_input.toPlainText()

        self.ws_thread = SocketIOClient(API_KEY, self.Name_server_1, SOCKET_URL=self.SOCKET_URL)

        self.ws_thread.log_signal.connect(self.append_log)
        self.ws_thread.progress_signal.connect(self.update_progress)
        self.ws_thread.target_signal.connect(self.update_target)
        self.ws_thread.mediabase_signal.connect(self.update_mediabase)
        self.ws_thread.thread_id_signal.connect(self.update_thread_id)
        self.ws_thread.created_at_signal.connect(self.update_created_at)
        self.ws_thread.weather_forecast_signal.connect(self.update_weather_forecast_signal)
        self.ws_thread.cuts_duration_signal.connect(self.update_cuts_duration_signal)
        self.ws_thread.notification_signal.connect(self.update_notification)

        # Iniciar as threads
        self.ws_thread.start()

        self.start_cronometro()
   
    # 📌 Inicializando Contadores de tarefas do dashboard
    def initi_count_tasks(self):
        email_input = self.ui.email_input.toPlainText().replace(".", "").replace("@", "")
        self.count_tasks = CountTasks(self.ui, update_custommodals_SuccessModal, app1, email_input)
        self.count_tasks.Tasks_Created_signal.connect(self.update_Tasks_Created)
        self.count_tasks.Tasks_Running_signal.connect(self.update_Tasks_Running)
        self.count_tasks.Tasks_Completed_signal.connect(self.update_Tasks_Completed)
        self.count_tasks.start()

    # 📌 Slots para atualização da interface gráfica
    def append_log(self, message):
        """Adiciona mensagens ao log."""
        self.ui.log.append(message)

    def update_Tasks_Completed(self, value):
        self.rpb_Tasks_Completed.rpb_setTextFormat('Value')
        try:
            self.rpb_Tasks_Completed.rpb_setValue(value)
        except:
            pass
        
    def update_Tasks_Running(self, value):
        self.rpb_Tasks_Running.rpb_setTextFormat('Value')
        try:
            self.rpb_Tasks_Running.rpb_setValue(value)
        except:
            pass

    def update_Tasks_Created(self, value):
        self.rpb_Tasks_Created.rpb_setTextFormat('Value')
        try:
            self.rpb_Tasks_Created.rpb_setValue(value)
        except:
            pass

    def update_progress(self, value):
        """Atualiza a barra de progresso."""
        self.ui.progressBar.setValue(value)

    def update_target(self, message):
        """Atualiza o label do target."""
        self.ui.label_Target.setText(message)

    def update_mediabase(self, message):
        """Atualiza o label do mediabase."""
        self.ui.label_mediabase.setText(message)

    def update_thread_id(self, message):
        """Atualiza o label do Thread ID."""
        self.ui.label_Thread_id.setText(message)

    def update_created_at(self, message):
        """Atualiza o label do Created At."""
        self.ui.label_Created_at.setText(message)

    def update_weather_forecast_signal(self, message):
        """Atualiza o label do weather forecast."""
        self.ui.label_WeatherForecast.setText(message)

    def update_cuts_duration_signal(self, message):
        """Atualiza o label do weather forecast."""
        self.ui.label_Cuts_Duration.setText(message)

    def update_notification(self, message):
        """Atualiza"""
        show_tray_message("Media Cuts Studio", message, tray)

    # 📌 Navegação da interface gráfica
    def navegate_Dashboard(self):
        if self.session_flag == False:
            update_custommodals_Warning("You must be logged in to access this section", "Login", 'top-right', self.ui.centralwidget)
            self.ui.stackedWidget.slideToWidgetIndex(11)   
        elif self.session_flag == True:
            self.ui.stackedWidget.slideToWidgetIndex(14)
        
    def navegate_Control_panel(self):
        if self.session_flag == False:
            update_custommodals_Warning("You must be logged in to access this section", "Login", 'top-right', self.ui.centralwidget)
            self.ui.stackedWidget.slideToWidgetIndex(11)       
        elif self.session_flag == True:
            self.ui.stackedWidget.slideToWidgetIndex(15)
        
    def navegate_Control_panel_process(self):
        if self.session_flag == False:
            update_custommodals_Warning("You must be logged in to access this section", "Login", 'top-right', self.ui.centralwidget)
            self.ui.stackedWidget.slideToWidgetIndex(11)       
        elif self.session_flag == True:
            self.ui.stackedWidget.slideToWidgetIndex(16)
    
    def navegate_Control_panel_tasksview(self):
        if self.session_flag == False:
            update_custommodals_Warning("You must be logged in to access this section", "Login", 'top-right', self.ui.centralwidget)
            self.ui.stackedWidget.slideToWidgetIndex(11)       
        elif self.session_flag == True:
            self.ui.stackedWidget.slideToWidgetIndex(13)

    def navegate_Control_panel_Report(self):
        if self.session_flag == False:
            update_custommodals_Warning("You must be logged in to access this section", "Login", 'top-right', self.ui.centralwidget)
            self.ui.stackedWidget.slideToWidgetIndex(11)       
        elif self.session_flag == True:
            self.ui.stackedWidget.slideToWidgetIndex(12)
        
    def navegate_myaccount(self):
        if self.session_flag == False:
            update_custommodals_Warning("You must be logged in to access this section", "Login", 'top-right', self.ui.centralwidget)
            self.ui.stackedWidget.slideToWidgetIndex(11)       
        elif self.session_flag == True:
            self.ui.stackedWidget.slideToWidgetIndex(17)
        
    def navegate_get_myaccount(self):
        if self.session_flag == False:
            update_custommodals_Warning("You must be logged in to access this section", "Login", 'top-right', self.ui.centralwidget)
            self.ui.stackedWidget.slideToWidgetIndex(11)       
        elif self.session_flag == True:
            self.ui.stackedWidget.slideToWidgetIndex(17)
        
    def navegate_Mode_Shortify(self):
        self.ui.stackedWidget_Main.slideToWidgetIndex(2)

    def navegate_Mode_Batch_processing(self):
        self.ui.stackedWidget_Main.slideToWidgetIndex(0)

    def navegate_Mode_1_long_video(self):
        self.ui.stackedWidget_Main.slideToWidgetIndex(1)

    # 📌 Cronometro
    def start_cronometro(self):
        self.timer.start(1000)  

    def update_time(self):
        current_time = self.time_edit.time()
        new_time = current_time.addSecs(1)  
        self.time_edit.setTime(new_time)
    
    # 📌 CloseEvent
    def closeEvent(self, event):
        try:
            self.ws_thread.stop()
        except:
            pass
        show_tray_message("Still Running", "Media Cuts Studio is Still Running To close open notifications and right click and then 'Exit'", tray)
        super().closeEvent(event)

    # 📌 Save and Load Settings User
    def get_machine_info(self):
        system_info = platform.uname()
        machine = system_info.node
        return machine
    
    def save_config(self, payload):
        user_email = self.ui.email_input.toPlainText().replace(".", "").replace("@", "")
        ref1 = db.reference(f'save_settings_users/{user_email}', app=app1)
        data1 = ref1.get()
        controle_das_funcao_info_2 = payload
        ref1.set(controle_das_funcao_info_2)

    def load_config(self):
        try:
            

            user_email = self.ui.email_input.toPlainText().replace(".", "").replace("@", "")
            ref1 = db.reference(f'save_settings_users/{user_email}', app=app1)
            data1 = ref1.get()
            canal_do_yt = data1["canal_do_yt"]
            text_watermark = data1["text_watermark"]
            SubtitleVerticalReference = data1["SubtitleVerticalReference"]
            SubtitleFontsize = data1["SubtitleFontsize"]
            SubtitleColor = data1["SubtitleColor"]
            SubtitleAnimation = data1["SubtitleAnimation"]
            SubtitleEffects = data1["SubtitleEffects"]
            SubtitleFontName = data1["SubtitleFontName"]
            CaptionsAlignment = data1["CaptionsAlignment"]
            CaptionsColor = data1["CaptionsColor"]
            CaptionsFontName = data1["CaptionsFontName"]
            CaptionsFontsize = data1["CaptionsFontsize"]
            CaptionsPrimaryColour = data1["CaptionsPrimaryColour"]
            CaptionsSecondaryColour = data1["CaptionsSecondaryColour"]
            CaptionsOutlineColour = data1["CaptionsOutlineColour"]
            CaptionsBackColour = data1["CaptionsBackColour"]

            CaptionsRevealEffectInitialColor = data1["CaptionsRevealEffectInitialColor"]
            CaptionsRevealEffectFinalColor = data1["CaptionsRevealEffectFinalColor"]
            Cutting_seconds = data1["Cutting_seconds"]

            self.ui.channel_yt.setText(canal_do_yt)
            self.ui.text_watermark.setText(text_watermark)
            self.ui.Subtitle_Vertical_Reference.setValue(int(SubtitleVerticalReference))
            self.ui.Subtitle_Fontsize.setValue(int(SubtitleFontsize))
            self.ui.Subtitle_Color.setText(str(SubtitleColor))
            self.ui.Subtitle_Animation.setText(str(SubtitleAnimation))
            self.ui.Subtitle_Effects.setText(str(SubtitleEffects))
            self.ui.Subtitle_FontName.setText(str(SubtitleFontName))
            self.ui.Captions_Alignment.setValue(int(CaptionsAlignment))
            self.ui.Captions_PrimaryColour.setText(str(CaptionsColor))
            self.ui.Captions_FontName.setText(str(CaptionsFontName))
            self.ui.Captions_Fontsize.setValue(int(CaptionsFontsize))
            self.ui.Captions_PrimaryColour.setText(str(CaptionsPrimaryColour))
            self.ui.Captions_SecondaryColour.setText(str(CaptionsSecondaryColour))
            self.ui.Captions_OutlineColour.setText(str(CaptionsOutlineColour))
            self.ui.Captions_BackColour.setText(str(CaptionsBackColour))

            self.ui.Captions_Reveal_Effect_Initial_Color.setText(str(CaptionsRevealEffectInitialColor))
            self.ui.Captions_Reveal_Effect_Final_Color.setText(str(CaptionsRevealEffectFinalColor))
            self.ui.Cutting_seconds.setValue(int(Cutting_seconds))







        except Exception as e:
           
            print(f"ee {e}")
            #self.save_config()

if __name__ == "__main__":
    # myappid = "com.SoftwareAICompany.MediaCutsStudio" 
    # ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app = QApplication(sys.argv)
    
    if not QSystemTrayIcon.isSystemTrayAvailable():
        QMessageBox.critical(None, "System Tray", "System tray was not detected!")
        sys.exit(1)
    app.setQuitOnLastWindowClosed(False)
    app.setWindowIcon(QIcon(icon_window))
    tray = QSystemTrayIcon(QIcon(icon_window), app)
    menu = QMenu()
    action_show = QAction("Show Window")
    menu.addAction(action_show)
    action_hide = QAction("Hide Window")
    menu.addAction(action_hide)
    action_exit = QAction("Exit")
    action_exit.triggered.connect(app.quit)
    menu.addAction(action_exit)
    tray.setToolTip("Media Cuts Studio")
    tray.setContextMenu(menu)
    tray.show()

    # Exibe somente a tela de loading inicialmente
    loading_screen = LoadingScreen()
    loading_screen.show()

    sys.exit(app.exec())