try:
    from PySide2.QtCore import QThread, Signal
    import socketio
    import json
except ImportError as e:
    print(f"Erro ao importar bibliotecas: {e}")

class SocketIOClient(QThread):
    log_signal = Signal(str)
    progress_signal = Signal(int)
    target_signal = Signal(str)
    mediabase_signal = Signal(str)
    thread_id_signal = Signal(str)
    created_at_signal = Signal(str)
    weather_forecast_signal = Signal(str)
    cuts_duration_signal = Signal(str)
    notification_signal = Signal(str)
    
    def __init__(self, API_KEY, Name_Server, SOCKET_URL):
        super().__init__()
        self.API_KEY = API_KEY
        self.Name_Server = Name_Server
        self.SOCKET_URL = SOCKET_URL  
        self.sio = socketio.Client()
        
        @self.sio.event
        def connect():
            msg = f"🔗 Connected to the server {self.Name_Server[0]}"
            self.log_signal.emit(msg)
            
        @self.sio.event
        def disconnect():
            msg = f"❌ Disconnected from the server {self.Name_Server[0]}"
            self.log_signal.emit(msg)

        @self.sio.on('webhook_data')
        def on_webhook_data(data):
            """Recebe e processa os dados do webhook."""
            self.process_data(data)

    def process_data(self, data):
        """Processa os dados recebidos e emite sinais para o Qt."""
        try:
            if isinstance(data, dict):
                user_api = data.get(self.API_KEY, None)
                if not user_api:
                    return  # Ignora mensagens sem a API_KEY correspondente

                msg_type = user_api.get("type", None)
                message = user_api.get("message", "Mensagem não encontrada")

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
            self.log_signal.emit(f"Erro ao processar dados: {e}")

    def run(self):
        """Inicia a conexão e permanece aguardando os eventos."""
        try:
            # Conecta forçando o uso do transporte WebSocket
            self.sio.connect(self.SOCKET_URL)
            # Bloqueia a thread para que continue recebendo eventos
            self.sio.wait()
        except Exception as e:
            self.log_signal.emit(f"Erro de conexão: {e}")

    def stop(self):
        """Desconecta o Socket.IO e finaliza a thread."""
        self.sio.disconnect()
        self.quit()
