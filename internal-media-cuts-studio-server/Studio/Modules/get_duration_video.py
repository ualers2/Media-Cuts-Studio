

import os
PRODUCTION_ENV = os.getenv("PRODUCTION_ENV", "True")

if PRODUCTION_ENV == "True":
    # Production
    from Studio.Modules.__init_libs__ import *

elif PRODUCTION_ENV == "False":
    # Local test
    from Modules.__init_libs__ import *

def get_duration_video(video_path):
    video_path = Path(video_path).resolve()
    if not video_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {video_path}")
    comando = [
        "ffprobe", "-v", "error", "-show_entries",
        "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(video_path)
    ]
    resultado = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8")
    stdout_result = resultado.stdout.strip()
    if not stdout_result:
        print(f"Erro: ffprobe não retornou duração para {video_path}. Saída: {resultado.stderr}")
        duration = get_duration_video_opencv(video_path)
        return float(duration)
    return float(stdout_result)

def get_duration_video_opencv(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise FileNotFoundError(f"Não foi possível abrir o vídeo: {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    cap.release()

    if fps == 0:
        raise ValueError("FPS é zero, impossível calcular a duração.")

    duration = frame_count / fps
    return duration