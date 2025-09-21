import os
import hmac
import hashlib
import time
import subprocess
import shutil
import logging
from flask import Flask, request, abort
from dotenv import load_dotenv
import threading
# Configura logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
        
def copy_keys_folder(keys_path, destin_path):
    # Define o caminho final como destin_path/Keys
    target_path = os.path.join(destin_path, os.path.basename(keys_path))
    os.makedirs(target_path, exist_ok=True)

    for root, dirs, files in os.walk(keys_path):
        relative_path = os.path.relpath(root, keys_path)
        dest_dir = os.path.join(target_path, relative_path)
        os.makedirs(dest_dir, exist_ok=True)

        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir, file)
            shutil.copy2(src_file, dest_file)

def copy_filess(origin, destin):

    try:
            
        shutil.copy(origin, destin)
    except Exception as er1:
        try:
            shutil.copy2(origin, destin)
        except Exception as er2:
            try:
                shutil.copyfile(origin, destin)
            except Exception as er3:
                logger.info(er3)


def build_env():
    time.sleep(5)
    path = os.path.join(os.path.dirname(__file__))
    logger.info(f"path? {path}")

    logger.info("Copy NginxServer")

    NginxServer_path_origin = os.path.join(os.path.dirname(__file__), "pipelines", "backend", "Dev", "internalnginxserver")
    NginxServer_path_destin = os.path.join(os.path.dirname(__file__), "internalnginxserver")

    try:
        if os.path.exists(NginxServer_path_destin):
            shutil.rmtree(NginxServer_path_destin)  
        shutil.copytree(NginxServer_path_origin, NginxServer_path_destin)
    except Exception as e:
        logger.error(f"Erro ao copiar diretório: {e}")

    logger.info("Copy vite.config.ts")
    vite_config_ts_origin = os.path.join(os.path.dirname(__file__), "pipelines", "backend", "Dev", "vite.config.ts")
    vite_config_ts_destin = os.path.join(os.path.dirname(__file__), "webproject", "vite.config.ts")

    copy_filess(vite_config_ts_origin, vite_config_ts_destin)
    
    logger.info("Copy .env")
    web_project_env_origin = os.path.join(os.path.dirname(__file__), "pipelines", "backend", "Dev", ".env")
    web_project_env_destin = os.path.join(os.path.dirname(__file__), "webproject", ".env")

    copy_filess(web_project_env_origin, web_project_env_destin)

    logger.info("Copy docker-compose.yml")
    docker_compose_origin = os.path.join(os.path.dirname(__file__), "pipelines", "backend", "Dev", "docker-compose.yml")
    docker_compose_destin = os.path.join(os.path.dirname(__file__), "docker-compose.yml")

    copy_filess(docker_compose_origin, docker_compose_destin)

    logger.info("Copy env.env")
    env_env_origin = os.path.join(os.path.dirname(__file__), "pipelines", "backend", "Dev", "env.env")
    env_env_destin = os.path.join(os.path.dirname(__file__), "internalserver", "Studio", "Keys","env.env")

    copy_filess(env_env_origin, env_env_destin)


    logger.info("Copy env.env")
    env_env_origin = os.path.join(os.path.dirname(__file__), "pipelines", "backend", "Dev", "env.env")
    env_env_destin = os.path.join(os.path.dirname(__file__), "internal_api", "Keys","env.env")

    copy_filess(env_env_origin, env_env_destin)

    logger.info("Copy env.env")
    env_env_origin = os.path.join(os.path.dirname(__file__), "pipelines", "backend", "Dev", "env.env")
    env_env_destin = os.path.join(os.path.dirname(__file__), "internallandingapi", "Keys","env.env")

    copy_filess(env_env_origin, env_env_destin)
    
    logger.info("Copy internal_webhook.py")
    internal_webhook_origin = os.path.join(os.path.dirname(__file__), "pipelines", "backend", "Dev", "internal_webhook.py")
    internal_webhook_destin = os.path.join(os.path.dirname(__file__), "internalwebhook", "internal_webhook.py")

    copy_filess(internal_webhook_origin, internal_webhook_destin)


    # Reinicia containers sem rebuild completo
    subprocess.Popen([
        "docker", "compose", "--compatibility", "down"], cwd=path
    ).wait()
    subprocess.Popen([
        "docker", "compose", "--compatibility", "up", "-d"], cwd=path
    )

build_env()