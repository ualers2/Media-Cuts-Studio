########################################################################
# IMPORT Libs 
########################################################################
## IMPORTAÇÃO DE BIBLIOTECAS
########################################################################

import os
import sys
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

def convert_and_move_src():
    comand = [
        "Custom_Widgets", "--convert-ui", "ui", "--qt-library", "PySide2"
    ]
    subprocess.run(comand, shell=True)
    comand = [
        "pyside2-rcc", "Qss/icons/_icons.qrc", "-o", "CoreApp/src_app/icons_interpreter.py"
    ]
    subprocess.run(comand, shell=True)

    src_list = os.listdir("src")
    for src_ in src_list:    
        shutil.copy(f"src\{src_}", f"CoreApp/src_app")

    shutil.rmtree("src")
convert_and_move_src()
