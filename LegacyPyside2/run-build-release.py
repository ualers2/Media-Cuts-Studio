import os
import zipfile
import time
from github import Github
from dotenv import load_dotenv

def zip_directory(folder_path, zip_name):
    """
    Compacta o conteúdo da pasta 'folder_path' em um arquivo ZIP com o nome 'zip_name'.
    """
    with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Cria um caminho relativo dentro do ZIP
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)
    print(f"Pasta '{folder_path}' compactada em '{zip_name}'.")

def create_github_release(token, repo_name, tag, release_name, release_body, asset_path):
    """
    Cria uma release no GitHub com a tag, nome e descrição informados, 
    e faz o upload do arquivo asset (por exemplo, o ZIP da nova versão).
    """
    g = Github(token)
    repo = g.get_repo(repo_name)
    try:
        # Cria a release (não é draft e nem pré-release)
        release = repo.create_git_release(tag=tag, name=release_name, message=release_body, draft=False, prerelease=False)
        print(f"Release '{release_name}' criada com sucesso!")
    except Exception as e:
        print(f"Erro ao criar a release: {e}")
        return

    try:
        # Faz o upload do arquivo asset para a release
        release.upload_asset(asset_path)
        print(f"Asset '{asset_path}' enviado para a release.")
    except Exception as e:
        print(f"Erro ao enviar o asset: {e}")

def get_new_version(token, repo_name):
    """
    Obtém a última release do repositório e define a nova versão incrementando o patch.
    Caso não exista nenhuma release, retorna a versão inicial v1.0.0.
    """
    g = Github(token)
    repo = g.get_repo(repo_name)
    try:
        latest_release = repo.get_latest_release()
        current_version = latest_release.tag_name  # Exemplo: v1.0.0
        # Remove o 'v' inicial e separa as partes
        version_parts = current_version.lstrip("v").split(".")
        major, minor, patch = map(int, version_parts)
        new_version = f"v{major}.{minor}.{patch+1}"
        print(f"Última versão encontrada: {current_version}. Nova versão: {new_version}")
    except Exception:
        print("Nenhuma release encontrada. Iniciando na versão v1.0.0")
        new_version = "v1.0.0"
    return new_version

def main():
    # Recupera o token do GitHub a partir da variável de ambiente

    load_dotenv("keys.env")

    token = os.getenv("token")
    repo_name = os.getenv("repo_name")
    build_number = os.getenv("build_number")
    if not token:
        print("A variável de ambiente GITHUB_TOKEN não está definida!")
        return

    # Determina a nova versão com base na última release
    new_version = get_new_version(token, repo_name)

    # Define o nome do arquivo ZIP que será criado
    zip_file_name = f"release_{new_version}.zip"
    # Pasta que será compactada (por exemplo, a pasta 'dist' com a build do software)
    folder_to_zip = "Build"
    
    # Compacta a pasta
    zip_directory(folder_to_zip, zip_file_name)
    
    # Define os detalhes da release
    release_title = f"Release {new_version}"

    with open(f"Release/{build_number}", "r") as file:
       content = file.read()

    release_body = content
    
    # Cria a release no GitHub e faz o upload do asset
    create_github_release(token, repo_name, new_version, release_title, release_body, zip_file_name)
    
    # Remove o arquivo ZIP local após o upload (opcional)
    try:
        os.remove(zip_file_name)
        print(f"Arquivo '{zip_file_name}' removido após o upload.")
    except Exception as e:
        print(f"Erro ao remover o arquivo ZIP: {e}")

if __name__ == "__main__":
    main()
