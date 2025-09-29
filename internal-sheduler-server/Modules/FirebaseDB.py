import firebase_admin
from firebase_admin import db
from datetime import datetime
import pytz

class FirebaseDB:
    def __init__(self, firebase_app, config):
        """
        Inicializa a classe FirebaseDB.

        Args:
            firebase_app: A instância do Firebase app inicializada.
            config: Objeto de configuração contendo 'FIREBASE_DB_URL'.
        """
        self.app = firebase_app
        self.db_url = config.FIREBASE_DB_URL
        if not self.db_url:
            raise ValueError("FIREBASE_DB_URL não configurado. Por favor, forneça a URL do seu Realtime Database.")
        firebase_admin.db.reference('/').set_url(self.db_url)

    def get_ref(self, path):
        """
        Obtém uma referência para um caminho específico no banco de dados.

        Args:
            path (str): O caminho para o nó no banco de dados (ex: 'canais', 'shorts/short_id').

        Returns:
            firebase_admin.db.Reference: Uma referência ao nó especificado.
        """
        return db.reference(path, app=self.app)

    def get(self, path):
        """
        Recupera dados de um caminho específico.

        Args:
            path (str): O caminho para o nó no banco de dados.

        Returns:
            dict or None: Os dados recuperados, ou None se não forem encontrados.
        """
        return self.get_ref(path).get()

    def create(self, path, data):
        """
        Cria um novo registro em um caminho específico com um ID gerado automaticamente.

        Args:
            path (str): O caminho base para o nó (ex: 'canais', 'shorts').
            data (dict): Os dados a serem salvos.

        Returns:
            dict: Os dados salvos, incluindo o ID gerado.
        """
        ref = self.get_ref(path).push(data)
        data['id'] = ref.key
        self.update(f"{path}/{ref.key}", {'id': ref.key}) # Salva o ID dentro do próprio nó
        return data

    def update(self, path, data):
        """
        Atualiza dados em um caminho específico.

        Args:
            path (str): O caminho para o nó a ser atualizado.
            data (dict): Os dados a serem atualizados.
        """
        self.get_ref(path).update(data)

    def delete(self, path):
        """
        Exclui dados de um caminho específico.

        Args:
            path (str): O caminho para o nó a ser excluído.
        """
        self.get_ref(path).delete()

    def get_all(self, path):
        """
        Recupera todos os registros de um caminho específico.

        Args:
            path (str): O caminho para o nó que contém os registros.

        Returns:
            list: Uma lista de dicionários, onde cada dicionário representa um registro.
        """
        all_data = self.get_ref(path).get()
        if not all_data:
            return []
        
        # O Firebase retorna um dicionário de dicionários com as chaves sendo os IDs.
        # Convertemos para uma lista de dicionários, adicionando o ID como um campo 'id'
        # se ainda não estiver presente (idealmente, o método create já faz isso).
        return [{**data, 'id': key} for key, data in all_data.items()]
    


class Canal:
    def __init__(self, db_instance):
        self.db = db_instance
        self.collection_name = 'canais'

    def create(self, nome, client_secrets_path, token_path, scopes):
        canal_data = {
            'nome': nome,
            'client_secrets_path': client_secrets_path,
            'token_path': token_path,
            'scopes': scopes,
            'data_criacao': datetime.now(pytz.utc).isoformat()
        }
        return self.db.create(self.collection_name, canal_data)

    def get(self, canal_id):
        return self.db.get(f"{self.collection_name}/{canal_id}")

    def update(self, canal_id, data):
        self.db.update(f"{self.collection_name}/{canal_id}", data)

    def delete(self, canal_id):
        self.db.delete(f"{self.collection_name}/{canal_id}")

    def get_all(self):
        return self.db.get_all(self.collection_name)


class Short:
    def __init__(self, db_instance):
        self.db = db_instance
        self.collection_name = 'shorts'

    def create(self, canal_id, caminho_arquivo, titulo, descricao, tags, categoria_id, status_privacidade, data_agendamento):
        short_data = {
            'canal_id': canal_id,
            'caminho_arquivo': caminho_arquivo,
            'titulo': titulo,
            'descricao': descricao,
            'tags': tags,
            'categoria_id': categoria_id,
            'status_privacidade': status_privacidade,
            'data_agendamento': data_agendamento.isoformat() if data_agendamento else None,
            'status': 'AGENDADO',  # Status inicial
            'data_criacao': datetime.now(pytz.utc).isoformat(),
            'data_upload_real': None,
            'youtube_video_id': None,
            'youtube_url': None,
            'erro_mensagem': None
        }
        return self.db.create(self.collection_name, short_data)

    def get(self, short_id):
        return self.db.get(f"{self.collection_name}/{short_id}")

    def update(self, short_id, data):
        # Converte datetime para ISO format string se presente
        if 'data_agendamento' in data and isinstance(data['data_agendamento'], datetime):
            data['data_agendamento'] = data['data_agendamento'].isoformat()
        if 'data_upload_real' in data and isinstance(data['data_upload_real'], datetime):
            data['data_upload_real'] = data['data_upload_real'].isoformat()

        self.db.update(f"{self.collection_name}/{short_id}", data)

    def delete(self, short_id):
        self.db.delete(f"{self.collection_name}/{short_id}")

    def get_all(self):
        return self.db.get_all(self.collection_name)