# Modules\utils.py
from flask import Flask, request, render_template, jsonify, abort, send_file, after_this_request
from flask_cors import CORS 
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import threading
import os
import requests
import secrets
import time
from firebase_admin import db, App
from datetime import datetime, timedelta
import requests
import pytz
from celery import Celery
import os
from celery.result import AsyncResult
from flask import Flask, request, jsonify
import hmac
import hashlib
import requests
import urllib.parse
import json
import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
from dotenv import load_dotenv, find_dotenv
from termcolor import cprint


# Carrega o arquivo .env
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
    # Envia o conteúdo da mensagem como JSON
    requests.post(os.getenv("WEBHOOK_URL"), json={str(user): {"type": type, "message": message}})

def get_tasks_weekly(email, appfb):

    ref_tasks2 = db.reference(f'save_tasks_users/task/{email}', app=appfb)
    todas_tarefas = ref_tasks2.get()

    cprint("🔍 Todas as tarefas recuperadas:", json.dumps(todas_tarefas, indent=4, ensure_ascii=False))

    tarefas_da_semana = {} 

    hoje = datetime.now()
    inicio_semana_atual = hoje - timedelta(days=hoje.weekday())
    inicio_semana = inicio_semana_atual - timedelta(days=7)
    fim_semana = inicio_semana + timedelta(days=8)

    cprint(f"📅 Período analisado (semana anterior): {inicio_semana.date()} até {fim_semana.date()}")

    if todas_tarefas:
        for id_tarefa, tarefa in todas_tarefas.items():
            data_tarefa_str = tarefa.get('scheduled_time')

            if not data_tarefa_str:
                cprint(f"⚠️ Tarefa {id_tarefa} ignorada: 'scheduled_time' ausente.")
                continue

            try:
                data_tarefa = datetime.strptime(data_tarefa_str, '%Y-%m-%d %H:%M:%S')
            except ValueError as e:
                cprint(f"❌ Erro ao processar data da tarefa {id_tarefa}: {e}")
                continue

            cprint(f"📌 Tarefa {id_tarefa}: {data_tarefa.date()}")

            if inicio_semana.date() <= data_tarefa.date() <= fim_semana.date():
                tarefas_da_semana[id_tarefa] = tarefa
                cprint(f"✅ Tarefa {id_tarefa} adicionada!")

    cprint("📋 Tarefas da semana:", json.dumps(tarefas_da_semana, indent=4, ensure_ascii=False))

    arquivo_tarefas = f'Cache/tarefas_da_semana_{email}.json'
    with open(arquivo_tarefas, 'w', encoding='utf-8') as f:
        json.dump(tarefas_da_semana, f, ensure_ascii=False, indent=4)

    cprint(f"📁 Arquivo JSON '{arquivo_tarefas}' criado com sucesso.", 'green')
    return arquivo_tarefas, tarefas_da_semana

# def criar_relatorio_pdf(analise, metricas, email):
#     nome_arquivo=f"Relatorios/relatorio_{email}.pdf"
    
#     doc = SimpleDocTemplate(nome_arquivo, pagesize=A4)
#     elementos = []
    
#     # Estilos
#     estilos = getSampleStyleSheet()
#     titulo_estilo = ParagraphStyle(
#         'Titulo',
#         parent=estilos['Title'],
#         fontSize=18,
#         textColor=colors.darkblue,
#         spaceAfter=20,
#         alignment=1  # Centralizado
#     )

#     texto_estilo = ParagraphStyle(
#         'TextoNormal',
#         parent=estilos['BodyText'],
#         fontSize=12,
#         leading=15
#     )

#     # Capa do relatório
#     elementos.append(Paragraph("Analysis Report", titulo_estilo))
#     elementos.append(Spacer(1, 20))
#     elementos.append(Paragraph("This report presents analysis of completed tasks, including performance metrics.", texto_estilo))
#     elementos.append(Spacer(1, 40))

#     # Seção de Análise
#     elementos.append(Paragraph("Complete Analysis", titulo_estilo))
#     elementos.append(Paragraph(analise, texto_estilo))
#     elementos.append(Spacer(1, 20))

#     # Seção de Métricas
#     elementos.append(Paragraph("Observed Metrics", titulo_estilo))
#     try:
#         dados_tabela = [
#             ["Total de Tarefas", metricas["total_tarefas"]],
#             ["Canal Mais Utilizado", metricas["canais_mais_utilizados"][0]["canal"]],
#             ["Tarefas no Canal", metricas["canais_mais_utilizados"][0]["tarefas"]],
#             ["Tempo Médio de Processamento", metricas["tempo_processamento"]["media"]],
#             ["Tempo Total", metricas["tempo_processamento"]["total"]],
#             ["Taxa de Sucesso Média", metricas["taxa_sucesso_media"]],
#             ["Tarefas Concluídas", metricas["status_tarefas"]["concluidas"]],
#             ["Tarefas Pendentes", metricas["status_tarefas"]["pendentes"]],
#             ["Tarefas com Falha", metricas["status_tarefas"]["falhas"]],
#         ]
#     except Exception as e:
#         try:
#             dados_tabela = [
#                 ["Total Tasks", metricas["total_tasks"]],
#                 ["Most Used Channel", metricas["most_used_channels"][0]["channel"]],
#                 ["Channel Tasks", metricas["most_used_channels"][0]["tasks"]],
#                 ["Average Processing Time", metricas["processing_time"]["median"]],
#                 ["Total Time", metricas["processing_time"]["total"]],
#                 ["Average Success Rate", metricas["average_success_rate"]],
#                 ["Completed Tasks", metricas["task_status"]["completed"]],
#                 ["Pending Tasks", metricas["task_status"]["pending"]],
#                 ["Failed Tasks", metricas["task_status"]["failed"]],
#             ]
#         except Exception as e:
#             dados_tabela = [
#                 ["Total de Tarefas", metricas["total_tarefas"]],
#                 ["Canal Mais Utilizado", metricas["canais_mais_utilizados"][0]["canal"]],
#                 ["Tarefas no Canal", metricas["canais_mais_utilizados"][0]["tarefas"]],
#                 ["Tempo Médio de Processamento", metricas["tempo_processamento"]["media"]],
#                 ["Tempo Total", metricas["tempo_processamento"]["total"]],
#                 ["Taxa de Sucesso Média", metricas["taxa_media_sucesso"]],
#                 ["Tarefas Concluídas", metricas["status_tarefas"]["concluidas"]],
#                 ["Tarefas Pendentes", metricas["status_tarefas"]["pendentes"]],
#                 ["Tarefas com Falha", metricas["status_tarefas"]["falhas"]],
#             ]
#     tabela = Table(dados_tabela, colWidths=[200, 200])
#     tabela.setStyle(TableStyle([
#         ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#         ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#         ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
#         ('GRID', (0, 0), (-1, -1), 1, colors.black),
#     ]))

#     elementos.append(tabela)
    
#     # Gera o PDF
#     doc.build(elementos)
#     cprint(f"✅ Relatório gerado: {os.path.abspath(nome_arquivo)}", "green")
#     return nome_arquivo
