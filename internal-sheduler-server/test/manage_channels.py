import requests
import json
from datetime import datetime, timedelta

# --- Configurações do Servidor ---
BASE_URL = "http://127.0.0.1:5029/api/canais"
# --- Fim Configurações do Servidor ---

def create_channel(name,  token_path, scopes):
    """
    Envia uma requisição POST para criar um novo canal no Firebase.
    """
    print(f"\n--- Criando um novo canal: '{name}' ---")
    headers = {'Content-Type': 'application/json'}
    payload = {
        "nome": name,
        "token_path": token_path,
        "scopes": scopes
    }
    try:
        response = requests.post(BASE_URL, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx/5xx
        print(f"Status da Resposta: {response.status_code}")
        print("Corpo da Resposta:", response.json())
        return response.json()
    except requests.exceptions.ConnectionError:
        print(f"Erro de conexão: O servidor Flask não está rodando em {BASE_URL}. Certifique-se de que o servidor está ativo.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"Erro HTTP ao criar canal: {e}")
        print("Corpo da Resposta de Erro:", e.response.json())
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao criar o canal: {e}")
        return None

def get_all_channels():
    """
    Envia uma requisição GET para listar todos os canais do Firebase.
    """
    print("\n--- Listando todos os canais ---")
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        print(f"Status da Resposta: {response.status_code}")
        channels = response.json()
        if channels:
            print("Canais encontrados:")
            for channel_id, channel_data in channels.items(): # Firebase retorna um dict de dicts
                # Se você estiver usando o 'id' salvo dentro do objeto, use channel_data.get('id', channel_id)
                print(f"  ID: {channel_data.get('id', channel_id)}, Nome: {channel_data.get('nome', 'N/A')}")
                # print(f"    Detalhes: {channel_data}") # Descomente para ver todos os detalhes
        else:
            print("Nenhum canal encontrado.")
        return channels
    except requests.exceptions.ConnectionError:
        print(f"Erro de conexão: O servidor Flask não está rodando em {BASE_URL}. Certifique-se de que o servidor está ativo.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"Erro HTTP ao listar canais: {e}")
        print("Corpo da Resposta de Erro:", e.response.json())
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao listar os canais: {e}")
        return None

def get_channel_details(channel_id):
    """
    Envia uma requisição GET para obter detalhes de um canal específico.
    """
    print(f"\n--- Obtendo detalhes do canal com ID: {channel_id} ---")
    try:
        response = requests.get(f"{BASE_URL}/{channel_id}")
        response.raise_for_status()
        print(f"Status da Resposta: {response.status_code}")
        channel_data = response.json()
        print(f"Detalhes do Canal: {channel_data}")
        return channel_data
    except requests.exceptions.ConnectionError:
        print(f"Erro de conexão: O servidor Flask não está rodando em {BASE_URL}. Certifique-se de que o servidor está ativo.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"Erro HTTP ao obter detalhes do canal: {e}")
        print("Corpo da Resposta de Erro:", e.response.json())
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao obter detalhes do canal: {e}")
        return None


if __name__ == "__main__":
    print("--- Iniciando testes para o endpoint /api/canais ---")

    # --- Exemplo 1: Listar todos os canais existentes ---
    print("\nTentando listar canais existentes...")
    get_all_channels()
    print("-" * 50)

    # --- Exemplo 2: Criar um novo canal ---
    # Altere estes valores para criar canais diferentes
    new_channel_name = f"Cuts podcasts {datetime.now().strftime('%Y%m%d%H%M%S')}"
    # Estes caminhos são fictícios e devem corresponder à estrutura esperada pelo seu servidor
    token_file = "/app/Tokens/token_1.pickle"
    scopes_list = ["https://www.googleapis.com/auth/youtube.upload"] # Escopo mínimo para upload

    created_channel_response = create_channel(
        name=new_channel_name,
        token_path=token_file,
        scopes=scopes_list
    )

    if created_channel_response:
        print(f"Novo canal criado com ID: {created_channel_response.get('canal_id')}")
        # --- Exemplo 3: Obter detalhes do canal recém-criado ---
        if created_channel_response.get('canal_id'):
            get_channel_details(created_channel_response['canal_id'])
    print("-" * 50)

    # --- Exemplo 4: Listar todos os canais novamente para ver o novo ---
    print("\nTentando listar canais novamente (incluindo o recém-criado)...")
    get_all_channels()
    print("-" * 50)

    print("\n--- Testes para o endpoint /api/canais concluídos ---")