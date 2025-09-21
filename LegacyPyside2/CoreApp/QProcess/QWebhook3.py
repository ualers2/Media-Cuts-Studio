try:
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
    import socketio
    import os
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

    def connect_socket(self):
        """Conecta ao servidor Socket.IO"""
        self.sio.connect(self.SOCKET_URL)
        print("🔗 Conectado ao servidor Socket.IO")
        self.log_signal.emit(f"🔗 Conectado ao servidor Socket.IO")

        # Escutando eventos
        self.sio.on('webhook_data', self.on_webhook_data)

    def on_webhook_data(self, data):
        """Recebe e processa os dados do webhook"""
        self.process_data(data)

    def process_data(self, data):
        """Processa os dados recebidos e emite sinais para o Qt"""
        try:
            if isinstance(data, dict):
                user_api = data.get(self.API_KEY, None)
                
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
        """Inicia a conexão e ouve o servidor"""
        self.connect_socket()

    def stop(self):
        """Desconecta o Socket.IO"""
        self.sio.disconnect()
        self.quit()

