########################################################################
## IMPORTAÇÃO DE BIBLIOTECAS
########################################################################

# Bibliotecas padrão do Python

import os
import random

# Bibliotecas de terceiros
try:

    import glob

    from firebase_admin import credentials, initialize_app, storage, db, delete_app

except ImportError as e:
    print(f"Erro ao importar bibliotecas: {e}")
    

class FirebaseThread:
    def __init__(self, app1):
        #self.ref = db.reference('Thread', app=app1)
        #self.thread_id = thread_id
        #self.thread_ref = self.ref.child(self.thread_id)
        self.pastas_usadas_ref = db.reference('PastasUsadas', app=app1) 
        self.ref_pastas_perfil = db.reference('PastasPorPerfil', app=app1) 
        self.ref = db.reference('Thread_media_cuts', app=app1)
        self.arquivos_usados_ref = db.reference('ArquivosUsados_media_cuts', app=app1) 

    def choose_subfolder_media_base(self, app1):
        """
        Escolhe uma subpasta aleatória da pasta MediaBase que ainda não foi utilizada.

        Esta função acessa uma referência do banco de dados Firebase que contém informações sobre as subpastas
        que já foram utilizadas em processos anteriores. Em seguida, ela verifica a pasta MediaBase local para 
        identificar todas as subpastas disponíveis. A função filtra as subpastas, removendo aquelas que já estão 
        registradas como usadas no banco de dados. Se houver subpastas disponíveis, uma delas é escolhida aleatoriamente 
        e seu caminho é armazenado no banco de dados para garantir que não será selecionada novamente em execuções futuras.

        Parâmetros:
        app1 (firebase_admin.App): A instância do aplicativo Firebase que é utilizada para acessar o banco de dados.
        
        Retorno:
        str: O caminho da subpasta escolhida, ou None se não houver subpastas disponíveis.

        Exemplo de uso:
        >>> app_instance = firebase_admin.initialize_app(credentials)
        >>> folder_path = escolher_subpasta_media_base(app_instance)
        >>> if folder_path is None:
        ...     print("Nenhuma pasta disponível para escolha.")
        ... else:
        ...     print(f"Pasta escolhida: {folder_path}")

        Considerações:
        - O funcionamento correto desta função depende da configuração apropriada do Firebase e do acesso à 
        referência do banco de dados. É importante que a estrutura de pastas na MediaBase esteja devidamente 
        organizada e que as permissões de acesso ao banco de dados estejam configuradas corretamente.
        - Se todas as subpastas na MediaBase já foram utilizadas, a função retornará None, o que pode ser 
        tratado pelo código chamador para evitar erros ou comportamentos inesperados.
        - A escolha aleatória de uma subpasta pode resultar em diferentes comportamentos a cada execução, 
        tornando a função útil para balancear a utilização de recursos.

        """
        arquivos_usados_ref = db.reference('Subpastas_utilizadas_em_algov1', app=app1)
        cuts_base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'CoreApp', 'Process', 'MediaBase')
        subpastas = [f.path for f in os.scandir(cuts_base_path) if f.is_dir()]
        pastas_usadas = arquivos_usados_ref.get() or {}
        pastas_usadas_set = set(path for path in pastas_usadas.values())
        subpastas_disponiveis = [pasta for pasta in subpastas if pasta not in pastas_usadas_set]
        if not subpastas_disponiveis:
            return None
        folder_path = random.choice(subpastas_disponiveis)
        arquivos_usados_ref.push(folder_path)
        return folder_path

    def is_file_in_use(self, file_path):
        """
        Verifica se o caminho do arquivo já está em uso, consultando o nó 'ArquivosUsados_media_cuts'.
        
        :param file_path: Caminho do arquivo a ser verificado.
        :return: True se o arquivo estiver em uso, False caso contrário.
        """
        arquivos_usados = self.arquivos_usados_ref.get()
        if file_path in arquivos_usados.values():
            return True
        return False
    
    # def create_metrics(self, thread_id, folder_path, created_at, android_name, Acc_namex, folows, likess):
    #     self.ref_metrics.child(thread_id).set({
    #         'folows': folows,
    #         'likes': likess,
    #         'thread_id': thread_id,
    #         'created_at': created_at,
    #         'android': android_name,
    #         'Acc_name': Acc_namex,
    #         'folder_path': folder_path  
    #     })
    #     return True



    def escolher_pasta_por_perfil(self, perfil, path_cuts, diretorio_script):
        """
        Percorre todos os nós de 'Thread_media_cuts' no Firebase, verifica se o perfil
        contém o nome especificado e se o status está como 'not_use'.
        Retorna o 'file_path' da mídia, se disponível.

        :param perfil: O nome do perfil para verificar (ex: 'cortesdofelquinhass').
        :return: O caminho do arquivo ('file_path') se o status estiver como 'not_use', caso contrário None.
        """
        #ref = db.reference('Thread_media_cuts')
        todos_os_nos = self.ref.get()
        if not todos_os_nos:
            print("Nenhum nó encontrado em 'Thread_media_cuts'.")
            return None, None
        for chave, dados in todos_os_nos.items():

            if 'profile_Tiktok' in dados and dados['profile_Tiktok'] == perfil and 'profile_Kwai' in dados and dados['profile_Kwai'] == perfil:
                print(f"Nó Tiktok encontrado para o perfil '{perfil}'.")
                if 'status' in dados and dados['status'] == 'not_use':
                    replacearcg = dados.get('file_path')
                    basenamefilepath =  os.path.basename(replacearcg)
                    pasta_analize = basenamefilepath.replace(".mp4", "").replace(" ", "")
                    path_cuts_dir = os.listdir(path_cuts)
                    for name_cuts in path_cuts_dir:
                        print(name_cuts)
                        print(pasta_analize)
                        if str(name_cuts) == str(pasta_analize):
                            print(f"Pasta encontrada {name_cuts}")
                            pasta_analize_Dir = os.path.join(diretorio_script, "src_", "CoreApp", "Process", "Cuts", pasta_analize)
                            print(pasta_analize_Dir)
                            mp4_files = glob.glob(os.path.join(pasta_analize_Dir, '*.mp4'))
                            if mp4_files:
                                print(f"Encontrados {len(mp4_files)} arquivo(s) MP4 na pasta.")
                                filepath_return = os.path.join(diretorio_script,  "src_", "CoreApp", "Process", "Cuts", pasta_analize)
                                #return filepath_return, descricao
                                return filepath_return
                            else:
                                print(f"Delete")
                                self.ref.child(chave).delete()    
                  
        

                        
                        

    def finalize_thread(self, folder_path, profile_Kwai, profile_Tiktok):
        
        
        todos_os_nos = self.ref.get()
        if not todos_os_nos:
            print("Nenhum nó encontrado em 'Thread_media_cuts'.")
            return None

        for chave, dados in todos_os_nos.items():
            #self.thread_ref_profile = db.reference(chave, app=app1)
            if 'profile_Kwai' in dados and dados['profile_Kwai'] == profile_Kwai:
                print(f"Nó encontrado para o profile_Kwai '{profile_Kwai}'.")

                if 'status' in dados and dados['status'] == 'not_use':
                    replacearcg = dados.get('file_path')
                    created_at = dados.get('created_at')
                    filepath = replacearcg.replace(".mp4", "")
                    if str(filepath) == str(folder_path):
                        status = "used"
                        self.ref.child(chave).set({
                            'thread_id': chave,
                            'created_at': created_at,
                            'file_path': filepath,
                            'status': status,
                            'profile_Kwai': profile_Kwai
                        })

                    return filepath
           
            elif 'profile_Tiktok' in dados and dados['profile_Tiktok'] == profile_Tiktok:
                print(f"Nó encontrado para o profile_Tiktok '{profile_Tiktok}'.")

                if 'status' in dados and dados['status'] == 'not_use':
                    replacearcg = dados.get('file_path')
                    created_at = dados.get('created_at')
                    filepath = replacearcg.replace(".mp4", "")
                    if str(filepath) == str(folder_path):
                        status = "used"
                        self.ref.child(chave).set({
                            'thread_id': chave,
                            'created_at': created_at,
                            'file_path': filepath,
                            'status': status,
                            'profile_Tiktok': profile_Tiktok
                        })

                    return filepath
                
            elif 'profile_Tiktok' in dados and dados['profile_Tiktok'] == profile_Tiktok and 'profile_Kwai' in dados and dados['profile_Kwai'] == profile_Kwai:
                print(f"Nó encontrado para o profile_Tiktok {profile_Tiktok} e profile_Kwai {profile_Kwai}")

                if 'status' in dados and dados['status'] == 'not_use':
                    replacearcg = dados.get('file_path')
                    created_at = dados.get('created_at')
                    filepath = replacearcg.replace(".mp4", "")
                    if str(filepath) == str(folder_path):
                        status = "used"
                        self.ref.child(chave).set({
                            'thread_id': chave,
                            'created_at': created_at,
                            'file_path': filepath,
                            'status': status,
                            'profile_Tiktok': profile_Tiktok,
                            'profile_Kwai': profile_Kwai
                        })

                    return filepath
        print(f'Thread {chave} Foi utilizada.')

        # Remover o caminho da pasta usada em PastasUsadas no Firebase
        #pastas_usadas = self.pastas_usadas_ref.get()
        #if pastas_usadas:
        #    for key, value in pastas_usadas.items():
        #        if value == folder_path:
        #            self.pastas_usadas_ref.child(key).delete()
        #            print(f'A pasta "{folder_path}" foi removida da lista de pastas usadas.')
