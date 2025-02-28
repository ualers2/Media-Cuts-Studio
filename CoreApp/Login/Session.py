import time
import firebase_admin
from firebase_admin import credentials, db


def save_session(SESSION_DB_PATH, app1, session_data):
    """Salva os dados da sessão no Firebase Realtime Database."""
    try:
        ref = db.reference(SESSION_DB_PATH, app=app1)
        ref.set(session_data)
        print("Sessão salva com sucesso!")
    except Exception as e:
        print("Erro ao salvar sessão:", e)

def load_session(app1, SESSION_DB_PATH):
    """Carrega os dados da sessão do Firebase Realtime Database."""
    try:
        ref = db.reference(SESSION_DB_PATH, app=app1)
        session_data = ref.get()
        return session_data
    except Exception as e:
        print("Erro ao carregar sessão:", e)
        return None

def is_session_valid(session_data):
    """
    Verifica se a sessão é válida.
    Considera que session_data possui a chave 'expires_at', com o timestamp de expiração.
    """
    if session_data is None:
        return False
    return time.time() < session_data.get("expires_at", 0)
