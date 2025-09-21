import base64
import os
from datetime import datetime

def encode_files_to_base64(file_paths, output_dir="encoded_files"):
    """
    Recebe uma lista de caminhos de arquivos, converte cada um para base64
    e salva em um .txt com o nome do arquivo e seu conteúdo em base64.

    Args:
        file_paths (list): Lista de caminhos dos arquivos a codificar.
        output_dir (str): Pasta onde os arquivos .txt serão salvos.

    Returns:
        list: Lista com os caminhos dos arquivos .txt gerados.
    """
    # Cria diretório de saída se não existir
    os.makedirs(output_dir, exist_ok=True)

    output_files = []

    for file_path in file_paths:
        if not os.path.isfile(file_path):
            print(f"[AVISO] Arquivo não encontrado: {file_path}")
            continue

        try:
            with open(file_path, "rb") as f:
                encoded = base64.b64encode(f.read()).decode("utf-8")

            filename = os.path.basename(file_path)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = os.path.join(output_dir, f"{filename}_{timestamp}.txt")

            with open(output_file, "w", encoding="utf-8") as f:
                f.write(f"Arquivo original: {filename}\n\n")
                f.write(encoded)

            output_files.append(output_file)
            print(f"[OK] Arquivo convertido: {output_file}")

        except Exception as e:
            print(f"[ERRO] Falha ao processar {file_path}: {e}")

    return output_files


if __name__ == "__main__":
    # Exemplo de uso
    path_dir = os.path.join(os.path.dirname(__file__))
    landingapiFirebase = os.path.join(
        path_dir, 
        'internal-landing-api',
        'Keys',
        'Firebase.json'
        )

   
   
    yt_json = os.path.join(
        path_dir, 
        'internal-media-cuts-studio-server',
        'Studio',
        'Cookies',
        'yt.json'
                           
        )
    firebase_json = os.path.join(
        path_dir, 
        'internal-media-cuts-studio-server',
        'Studio',
        'Keys',
        'Firebase.json'
        )
    client_secret_1 = os.path.join(
        path_dir, 
        'internal-sheduler-server',
        'Internal-server',
        'Keys',
        'client_secret_1.json'
        )
    shedulerserverFirebase = os.path.join(
        path_dir, 
        'internal-sheduler-server',
        'Internal-server',
        'Keys',
        'Firebase.json'
        )
    sheduleruploaderserverFirebase = os.path.join(
        path_dir, 
        'internal-sheduler-uploader-server',
        'Keys',
        'Firebase.json'
        )
    uptimeserverFirebase = os.path.join(
        path_dir, 
        'internal-uptime-server',
        'Keys',
        'Firebase.json'
        )
    shortifyapiFirebase = os.path.join(
        path_dir, 
        'internal-shortify-api',
        'Keys',
        'Firebase.json'
        )
    shortifyapiyt = os.path.join(
        path_dir, 
        'internal-shortify-api',
        'Cookies',
        'yt.json'
        )

    vps_compose = os.path.join(
        path_dir, 
        'ProductionFiles',
        'VPS',
        'docker-compose.yml'
        )


    arquivos = [
        vps_compose,
        # yt_json,
        # firebase_json,
        # client_secret_1,
        # shedulerserverFirebase,
        # sheduleruploaderserverFirebase,
        # uptimeserverFirebase,
        # shortifyapiFirebase,
        # shortifyapiyt



    ]
    saidas = encode_files_to_base64(arquivos)

    print("\nArquivos gerados:")
    for s in saidas:
        print(s)
