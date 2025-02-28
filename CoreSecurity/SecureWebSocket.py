import asyncio
import websockets
import ssl
from PySide2.QtCore import QThread, Signal
import os

class SecureWebSocket:
    def __init__(self, API_KEY, Name_Server, SOCKET_URL="wss://localhost:3010/socket.io/?EIO=4&transport=websocket", *args, **kwargs):
        self.API_KEY = API_KEY
        self.Name_Server = Name_Server
        self.SOCKET_URL = SOCKET_URL
        self.trusted_cert_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "myCA.pem"))
        self.ssl_context = self.create_ssl_context()


    def create_ssl_context(self):
        """Cria o contexto SSL e carrega o certificado confiável."""
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)  # 🔹 CLIENTE TLS
        context.load_verify_locations(self.trusted_cert_path)

        return context

    async def connect(self, url):
        """Conectar ao WebSocket seguro."""
        if not url.startswith("wss://"):
            raise ValueError("⚠️ Apenas WebSockets seguros (wss://) são permitidos!")
        
        try:
            async with websockets.connect(url, ssl=self.ssl_context) as websocket:
                print(f"🔗 Conectado a {url}")
                await self.listen(websocket)
        except Exception as e:
            print(f"❌ Erro ao conectar ao WebSocket: {e}")
            
    async def listen(self, websocket):
        """Ouvir mensagens do WebSocket e processá-las."""
        try:
            async for message in websocket:
                print(f"Mensagem recebida: {message}")
                # Aqui você pode chamar o callback para processar o 'webhook_data'
                await self.on_webhook_data_callback(message)

        except Exception as e:
            print(f"Erro ao ouvir mensagens: {e}")

    async def on_webhook_data_callback(self, data):
        """Processa dados do webhook e emite sinais correspondentes para a interface Qt."""
        try:
            # Assumindo que o 'data' é uma string JSON que pode ser decodificada
            import json
            data = json.loads(data)

            user_received = data.get(self.API_KEY, None)
            if user_received is None:
                return

            msg_type = user_received.get("type", None)
            message = user_received.get("message", "Mensagem não encontrada")

            if msg_type == "info":
                self.log_signal.emit(f"{message}")
            elif msg_type == "progress":
                self.progress_signal.emit(int(message))
            elif msg_type == "target":
                self.target_signal.emit(f"Target: {message}")
            elif msg_type == "mediabase":
                self.mediabase_signal.emit(f"Mediabase: {message}")
            elif msg_type == "Thread":
                self.thread_id_signal.emit(f"Thread: {message}")
            elif msg_type == "Createdat":
                self.created_at_signal.emit(f"Created-at: {message}")
            elif msg_type == "weather_forecast":
                self.weather_forecast_signal.emit(f"{message}")
            elif msg_type == "cuts_duration":
                self.cuts_duration_signal.emit(f"{message}")
            elif msg_type == "notification":
                self.notification_signal.emit(f"{message}")

            
        except Exception as e:
            self.log_signal.emit(f"Erro ao conectar: {e}")
