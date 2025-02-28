import pkg_resources
import subprocess
import sys

# Lista dos pacotes que você deseja manter (em letras minúsculas, pois o pip trata os nomes dessa forma)
packages = [
    "PySide2",
    "PyQt5",
    "PySide2extn",
    "PySide6"
    "shiboken2",
    "python-socketio",
    "ffmpeg-python",
    "requests",
    "gputil",
    "whisper",
    "torch",
    "uiautomator2",
    "opencv-python",
    "numpy",
    "srt",
    "yt_dlp",
    "psutil",
    "schedule",
    "google-auth",
    "google-api-python-client",
    "websockets",
    "av",
    "python-dotenv",
    "firebase-admin",
    "transformers",
    "QT-PyQt-PySide-Custom-Widgets",
    "proglog",
    "pytz",
    "shutil",
    "glob",
    "wave",
    "asyncio",
    "logging",
    "io",

]

subprocess.run(["Build/MediaCutsStudio/Python/python", "-m", "pip", "uninstall", "-y", "torch"])
subprocess.run(["Build/MediaCutsStudio/Python/python", "-m", "pip", "uninstall", "-y", "transformers"])

# subprocess.run(["Build/MediaCutsStudio/Python/python", "-m", "pip", "install", "websocket-client"])



# for pkg in packages:
#     subprocess.run(["Build/MediaCutsStudio/Python/python", "-m", "pip", "install", "--force-reinstall", pkg])

print("Concluído!")
