# webhook.py
from flask import Flask, request, jsonify, render_template_string
from flask_socketio import SocketIO
import logging
import base64
import os
import io

# import eventlet
# eventlet.monkey_patch()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'minha_chave_secreta'

socketio = SocketIO(
    app, 
    async_mode="threading", 
    cors_allowed_origins=[
        "https://mediacutsstudio.com",
        "http://localhost:3001",
        "http://localhost:4343",
        "*"
    ]
)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50 MB, adjust as needed
app.logger.info("???????")

logger = logging.getLogger('webhook_logger')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

@app.route('/')
def index():
    return jsonify({"message": "#1 Webhook Media Cuts Studio funcionando!"})

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    logger.info("Webhook recebido com dados: %s", data)
    socketio.emit('webhook_data', data)
    return jsonify({"status": "sucesso", "dados": data}), 200

@app.route('/webhook_video_zip', methods=['POST'])
def webhook_video_zip():
    data = request.get_json()

    if 'arquivo_zip' not in data or 'api_key' not in data or 'filename' not in data:
        logger.error("Campos 'arquivo_zip', 'api_key' ou 'filename' ausentes no JSON")
        return jsonify({"error": "Parâmetros inválidos"}), 400

    user = data['api_key']
    filename = data['filename']
    zip_base64 = data['arquivo_zip']

    try:
        # Decodifica o ZIP e armazena em memória
        zip_bytes = base64.b64decode(zip_base64)
        zip_buffer = io.BytesIO(zip_bytes)

        # Enviar via SocketIO para o cliente
        socketio.emit('webhook_data', {str(user): {"type": "zip", "filename": filename, "message": zip_base64}})

        return jsonify({"status": "sucesso"}), 200

    except Exception as e:
        logger.error(f"Erro ao processar ZIP: {e}")
        return jsonify({"error": "Erro ao processar ZIP"}), 500
    

app.logger.info("inicialized")
socketio.run(app, host="0.0.0.0", port=3008, allow_unsafe_werkzeug=True)
