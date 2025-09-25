
# Studio\Shortify.py
import os
import sys
import json
import time
import random
import re
import subprocess
import platform
from datetime import datetime, timedelta
from queue import Queue, Empty
import unicodedata
import requests
import yt_dlp
from firebase_admin import credentials, initialize_app, storage, db, delete_app
from termcolor import cprint
from dotenv import dotenv_values
from pathlib import Path
import unicodedata
from queue import Queue, Empty
import unicodedata
from pathlib import Path
import threading
import shutil
import whisper
import math
from concurrent.futures import ThreadPoolExecutor
import wave
import srt
import yt_dlp
import psutil
from firebase_admin import credentials, initialize_app, storage, db, delete_app
from pathlib import Path
from termcolor import cprint
import cv2

import base64
import os
import requests
import zipfile
import logging

import unicodedata
def get_video_thumbnail(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info.get("thumbnail", "Thumbnail não encontrada")

def download_thumbnail(thumbnail_url, output_path):
    response = requests.get(thumbnail_url)
    if response.status_code == 200:
        with open(output_path, 'wb') as file:
            file.write(response.content)
        print(f"Thumbnail baixada com sucesso: {output_path}")
        return True
    else:
        print(f"Falha ao baixar a thumbnail. Status code: {response.status_code}")
        return False
video_id = "Ubp9ARe9KoA"
thumbnail_url = get_video_thumbnail(video_id)
print(thumbnail_url)
output_path = os.path.join(os.path.dirname(__file__), f"{video_id}.jpg")
download_thumbnail(thumbnail_url, output_path)