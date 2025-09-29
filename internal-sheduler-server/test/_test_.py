


import requests
import json

API_BASE = "https://accepted-poorly-maggot.ngrok-free.app/"  # onde seu Flask está rodando

def test_upload():
    # Substitua pelo open_id salvo no Firebase e pelo caminho real do vídeo
    open_id = "-000hBTtvK5U5gP3A_xjHYnze98OfBeZYNK9"
    filepath = r"C:\Users\Media Cuts DeV\Downloads\HomeServer\HomeServer\internal-sheduler-server\Internal-server\Danilo_acabou_o_ciclo.mp4"
    title = "Meu primeiro upload via API 🚀"

    payload = {
        "open_id": open_id,
        "filepath": filepath,
        "title": title
    }

    resp = requests.post(f"{API_BASE}/upload_video", json=payload)
    print("Status:", resp.status_code)
    try:
        print(json.dumps(resp.json(), indent=2, ensure_ascii=False))
    except Exception:
        print(resp.text)


if __name__ == "__main__":
    test_upload()











