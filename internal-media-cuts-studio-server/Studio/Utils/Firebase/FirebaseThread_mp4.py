########################################################################
## IMPORTAÇÃO DE BIBLIOTECAS
########################################################################

# Bibliotecas padrão do Python
import os
import time

# Bibliotecas de terceiros
try:

    from firebase_admin import credentials, initialize_app, storage, db, delete_app

except ImportError as e:
    print(f"Erro ao importar bibliotecas: {e}")
    


class FirebaseThread_mp4:
    def __init__(self, thread_id, app1):
        self.ref = db.reference('Thread_media_cuts', app=app1)
        self.thread_id = thread_id
        self.thread_ref = self.ref.child(self.thread_id)
        self.arquivos_usados_ref = db.reference('ArquivosUsados_media_cuts', app=app1) 
        self.ref_pastas_perfil = db.reference('PastasPorPerfil', app=app1) 
        self.ref_metrics = db.reference('metrics', app=app1)

    def is_file_in_use(self, file_path):
        """
        Verifica se o caminho do arquivo MP4 já está em uso, consultando o nó 'ArquivosUsados_media_cuts'.
        
        :param file_path: Caminho do arquivo a ser verificado.
        :return: True se o arquivo estiver em uso, False caso contrário.
        """
        arquivos_usados = self.arquivos_usados_ref.get()
        if file_path in arquivos_usados.values():
            return True
        return False
    
    def create_thread(self, file_path):
        """
        Cria um nó no Firebase com as informações da thread, incluindo o caminho de um arquivo MP4,
        se o caminho do arquivo não estiver em uso. Se o nome da pasta contiver 'felca' ou 'Felca',
        a thread é associada ao perfil 'cortesdofelquinhasss'.

        :param file_path: O caminho do arquivo MP4.
        :return: Mensagem de sucesso ou falha.
        """
        if self.is_file_in_use(file_path):
            return None
        folder_name2 = os.path.basename(file_path)
        folder_name = folder_name2.replace(".mp4", "")
        print(folder_name)
        profile1 = "default_profile"
        profile2 = "default_profile"
        if 'felca' in folder_name.lower():
            profile1 = "cortesdofelquinhasss"
            profile2 = "cortesdofelquinhasss"

        elif 'brino' in folder_name.lower():
            profile1 = "brunimcortes"
            profile2 = "brunimcortes"

        elif 'novela' in folder_name.lower():
            profile1 = "NovelasCine"
            profile2 = "novelascine1"

        elif 'desenho' in folder_name.lower():
            profile1 = "desenhocine"
            profile2 = "desenhocine1"


        new_used_key = self.arquivos_usados_ref.push().key
        self.arquivos_usados_ref.child(new_used_key).set(file_path)
        file_path = file_path.replace(".mp4", "")
        created_at = time.strftime("%Y-%m-%d %H:%M:%S")
        status = "not_use"
        self.thread_ref.set({
            'thread_id': self.thread_id,
            'created_at': created_at,
            'file_path': file_path,
            'status': status,
            'profile_Kwai': profile1,
            'profile_Tiktok': profile2
        })
        # profile_folder_ref = self.ref_pastas_perfil.child(profile1)
        # profile_folder_ref.push().set(folder_name)
        return self.thread_id, file_path, created_at,status, profile1, profile2

