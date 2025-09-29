import requests
import os
from datetime import datetime, timedelta
import pytz # Para manipulação de fuso horário

# --- Configurações do Cliente ---
SERVER_URL = "http://127.0.0.1:5029/api/shorts/agendar"
# Caminho para um arquivo de vídeo de teste
# Certifique-se de que este arquivo exista no seu ambiente local para o teste!
VIDEO_FILE_PATH = r"C:\Users\Media Cuts DeV\Downloads\HomeServer\HomeServer\internalserver\Studio\WorkEnvironment\Process\Realtime_Cuts\Cuts\Alim_do_Poder_da_ONU_e_a_Realidade_das_Relacoes_Internacionais\CutsCreate\subclip_vertical_1.mp4"
# --- Fim Configurações do Cliente ---

def schedule_short(
    video_path,
    canal_id,
    title,
    description,
    category_id="22", # Padrão para "Pessoas e blogs"
    video_tags=None,
    privacy_status="private", # 'public', 'private', 'unlisted'
    scheduled_publish_at=None, # Objeto datetime com fuso horário
):
    """
    Envia uma requisição para agendar o upload de um Short.

    Args:
        video_path (str): Caminho local para o arquivo de vídeo.
        canal_id (str): ID do canal do YouTube associado no Firebase.
        title (str): Título do vídeo.
        description (str): Descrição do vídeo.
        category_id (str): ID da categoria do YouTube (ex: '22' para Pessoas e blogs).
        video_tags (list): Lista de tags para o vídeo.
        privacy_status (str): Status de privacidade do vídeo ('public', 'private', 'unlisted').
        scheduled_publish_at (datetime, optional): Data e hora de agendamento. Deve ser um objeto datetime
                                                    com fuso horário (UTC é recomendado).
        ia_gen_title (bool): Indica se o título foi gerado por IA.

    Returns:
        requests.Response: Objeto de resposta da requisição.
    """
    if not os.path.exists(video_path):
        print(f"Erro: O arquivo de vídeo não foi encontrado em '{video_path}'")
        return None

    # Prepara os dados do formulário
    data = {
        'canal_id': canal_id,
        'title': title,
        'description': description,
        'category_id': category_id,
        'video_tags': ','.join(video_tags) if video_tags else '',
        'privacy_status': privacy_status,
    }

    # Adiciona a data de agendamento se fornecida
    if scheduled_publish_at:
        # Garante que o datetime esteja em UTC e formatado para ISO 8601
        # if scheduled_publish_at.tzinfo is None:
        # Se não tiver fuso horário, assume que é para o fuso horário de São Paulo
        # e converte para UTC para o envio.
        local_tz = pytz.timezone('America/Sao_Paulo')
        scheduled_publish_at = local_tz.localize(scheduled_publish_at).astimezone(pytz.utc)
        # else:
        #     scheduled_publish_at = scheduled_publish_at.astimezone(pytz.utc)
        data['scheduled_publish_at'] = scheduled_publish_at.isoformat()
        print(f"Agendando para: {data['scheduled_publish_at']}")
    else:
        print("Agendando para upload imediato (se privacy_status for 'public' ou 'unlisted' e não houver scheduled_publish_at).")


    # Abre o arquivo de vídeo em modo binário
    files = {'video_file': (os.path.basename(video_path), open(video_path, 'rb'), 'video/mp4')}

    print(f"Enviando Short para {SERVER_URL}...")
    try:
        response = requests.post(SERVER_URL, data=data, files=files)
        return response
    except requests.exceptions.ConnectionError:
        print(f"Erro de conexão: O servidor Flask não está rodando em {SERVER_URL}. Certifique-se de que o servidor está ativo.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao enviar a requisição: {e}")
        return None
    finally:
        # Garante que o arquivo seja fechado após o envio
        files['video_file'][1].close()


if __name__ == "__main__":
    # --- Passo 1: Opcional - Crie um Canal de Teste no Firebase (se ainda não tiver um) ---
    # Você pode fazer isso manualmente no console do Firebase ou usando um endpoint API temporário
    # para criar canais, se tiver um. Para este exemplo, vou assumir que você tem um CANAL_ID existente.
    # Exemplo de payload para criar um canal via POST para /api/canais:
    # {
    #     "nome": "Meu Canal de Teste",
    #     "client_secrets_path": "/app/client_secrets/client_secrets_canal1.json",
    #     "token_path": "/app/tokens/token_canal1.pickle",
    #     "scopes": ["https://www.googleapis.com/auth/youtube.upload"]
    # }
    # Substitua pelo ID de um canal existente no seu Firebase Realtime Database
    # Você pode criar um acessando http://localhost:8080/api/canais com um POST request (ex: via Postman)
    TEST_CANAL_ID = "-OV0E5_HsjpAwXCX1Jlh" # <<-- MUDE ESTE VALOR!
    if TEST_CANAL_ID == "YOUR_EXISTING_CANAL_ID_FROM_FIREBASE":
        print("\nATENÇÃO: Por favor, substitua 'YOUR_EXISTING_CANAL_ID_FROM_FIREBASE' pelo ID de um canal real no seu Firebase Realtime Database.")
        print("Você pode criar um canal enviando um POST request para http://localhost:8080/api/canais com os dados do canal (veja o comentário no código).")
        print("Após criar, copie o 'canal_id' retornado e cole aqui.")
        exit()

    # --- Passo 2: Configure o caminho para o seu arquivo de vídeo de teste ---
    if not os.path.exists(VIDEO_FILE_PATH) or VIDEO_FILE_PATH == "caminho/para/seu/video_exemplo.mp4":
        print(f"\nERRO: Por favor, substitua '{VIDEO_FILE_PATH}' por um caminho válido para um arquivo de vídeo MP4 existente no seu computador.")
        print("Exemplo: VIDEO_FILE_PATH = 'C:/Users/SeuUsuario/Videos/meu_short.mp4'")
        exit()

    print(f"\n--- Iniciando o teste de agendamento de Short ---")

    # # Exemplo 1: Agendar um Short para upload imediato (ou 'public' se não agendado)
    # print("\nAttempting to schedule a short for immediate upload...")
    # response_immediate = schedule_short(
    #     video_path=VIDEO_FILE_PATH,
    #     canal_id=TEST_CANAL_ID,
    #     title=f"Meu Short de Teste Imediato - {datetime.now().strftime('%Y%m%d%H%M%S')}",
    #     description="Este é um Short de teste enviado para upload imediato.",
    #     video_tags=["teste", "short", "python"],
    #     privacy_status="private" # Use 'private' para evitar publicar acidentalmente
    # )

    # if response_immediate:
    #     print(f"Status da Resposta (Imediato): {response_immediate.status_code}")
    #     print("Corpo da Resposta (Imediato):", response_immediate.json())
    #     if response_immediate.status_code == 202:
    #         print("Short agendado com sucesso para upload imediato!")
    #     else:
    #         print("Falha ao agendar o Short para upload imediato.")
    # print("-" * 50)

    # Exemplo 2: Agendar um Short para o futuro
    print("\nAttempting to schedule a short for a future date/time...")
    # Agende para 5 minutos no futuro (fuso horário de São Paulo)
    sao_paulo_tz = pytz.timezone('America/Sao_Paulo')
    future_time_local = datetime.now(sao_paulo_tz) + timedelta(minutes=1)

    response_scheduled = schedule_short(
        video_path=VIDEO_FILE_PATH,
        canal_id=TEST_CANAL_ID,
        title=f"Meu Short de Teste Agendado - {future_time_local.strftime('%Y%m%d%H%M%S')}",
        description=f"Este é um Short de teste agendado para {future_time_local.strftime('%Y-%m-%d %H:%M:%S')}.",
        video_tags=["teste", "agendado", "celery"],
        privacy_status="private", # Para agendamento, 'private' ou 'unlisted' são comuns
        scheduled_publish_at=future_time_local
    )

    if response_scheduled:
        print(f"Status da Resposta (Agendado): {response_scheduled.status_code}")
        print("Corpo da Resposta (Agendado):", response_scheduled.json())
        if response_scheduled.status_code == 202:
            print("Short agendado com sucesso para o futuro!")
        else:
            print("Falha ao agendar o Short para o futuro.")
    print("-" * 50)

    print("\n--- Teste de agendamento de Short concluído ---")