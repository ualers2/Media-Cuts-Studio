# Modules\utils.py
from flask import Flask, request, render_template, jsonify, abort, send_file, after_this_request
from flask_cors import CORS 
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from firebase_admin import db, App
from datetime import datetime, timedelta
import requests
import pytz
import os
import base64
from flask import Flask, request, jsonify
import yt_dlp
import requests
from dotenv import load_dotenv, find_dotenv
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import json
import logging
from werkzeug.utils import secure_filename

load_dotenv(dotenv_path="../Studio/Keys/env.env")
ADMIN_API_KEY = "apikey-Api-Landingpage-ZBQ2x5m_ae8Ubke9cI664PeCkerEp6EMHDyeriFFjq8"


def create_task(user_email, task_id, new_task, appfb):
    filter_ = user_email.replace(".", "_")
    ref_tasks = db.reference(f'user_tasks/{filter_}', app=appfb)
    ref_tasks.child(task_id).set(new_task)
    # ref_tasks.push(new_task)
    return True
    


def send_to_webhook(user, type, message, cor):
    """Envia uma mensagem para o webhook."""
    requests.post(os.getenv("WEBHOOK_URL"), json={str(user): {"type": type, "message": message}})

def get_tasks_weekly(email, appfb):
    ref_tasks2 = db.reference(f'save_tasks_users/task/{email}', app=appfb)
    todas_tarefas = ref_tasks2.get()
    print("🔍 Todas as tarefas recuperadas:", json.dumps(todas_tarefas, indent=4, ensure_ascii=False))
    tarefas_da_semana = {} 
    hoje = datetime.now()
    inicio_semana_atual = hoje - timedelta(days=hoje.weekday())
    inicio_semana = inicio_semana_atual - timedelta(days=7)
    fim_semana = inicio_semana + timedelta(days=8)
    print(f"📅 Período analisado (semana anterior): {inicio_semana.date()} até {fim_semana.date()}")
    if todas_tarefas:
        for id_tarefa, tarefa in todas_tarefas.items():
            data_tarefa_str = tarefa.get('scheduled_time')
            if not data_tarefa_str:
                print(f"⚠️ Tarefa {id_tarefa} ignorada: 'scheduled_time' ausente.")
                continue
            try:
                data_tarefa = datetime.strptime(data_tarefa_str, '%Y-%m-%d %H:%M:%S')
            except ValueError as e:
                print(f"❌ Erro ao processar data da tarefa {id_tarefa}: {e}")
                continue
            print(f"📌 Tarefa {id_tarefa}: {data_tarefa.date()}")
            if inicio_semana.date() <= data_tarefa.date() <= fim_semana.date():
                tarefas_da_semana[id_tarefa] = tarefa
                print(f"✅ Tarefa {id_tarefa} adicionada!")

    print("📋 Tarefas da semana:", json.dumps(tarefas_da_semana, indent=4, ensure_ascii=False))
    arquivo_tarefas = f'Cache/tarefas_da_semana_{email}.json'
    with open(arquivo_tarefas, 'w', encoding='utf-8') as f:
        json.dump(tarefas_da_semana, f, ensure_ascii=False, indent=4)
    print(f"📁 Arquivo JSON '{arquivo_tarefas}' criado com sucesso.", 'green')
    return arquivo_tarefas, tarefas_da_semana
