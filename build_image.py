import subprocess
import os

os.chdir(os.path.join(os.path.dirname(__file__)))
# Adiciona o caminho do Docker Compose
os.environ["PATH"] += r";C:\Program Files\Docker\Docker\resources\bin"
# os.environ["COMPOSE_BAKE"] = "true"
path = os.path.join(os.path.dirname(__file__))


def executar_comando(comando):
    """Executa um comando sem abrir um novo terminal (funciona dentro do contêiner)."""
    subprocess.run(comando, shell=True)

executar_comando("docker-compose up --build -d redis")

# # Reinicia apenas o serviço nginx_proxy_server
# subprocess.run(
#     ["docker", "compose", "restart", "nginx_proxy_server"],
#     cwd=path,
#     check=True
# )

# executar_comando("docker-compose up --build -d nginx_proxy_server")


# # (Opcional) parar antes, se já estiver rodando
# subprocess.Popen([
#     "docker", "compose", "--compatibility", "stop", "landingpage_1"
# ], cwd=path).wait()

# # subir somente o serviço landingpage_1 em background
# subprocess.Popen([
#     "docker", "compose", "--compatibility", "up", "-d", "landingpage_api_1"
# ], cwd=path).wait()


# docker tag mediacutstudio/ffmpeg-gpu:v1.0 mediacutstudio/ffmpeg-gpu:v1.0 
# docker push mediacutstudio/ffmpeg-gpu:v1.0 