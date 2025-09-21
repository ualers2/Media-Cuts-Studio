import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def extract_preserved_block(lines, identifier):
    """
    Extrai o bloco preservado de 'lines' delimitado pelos marcadores
    # PRESERVE: <identifier> start e # PRESERVE: <identifier> end.
    Retorna o bloco (lista de linhas) ou None se não encontrado.
    """
    start_marker = f"# PRESERVE: {identifier} start"
    end_marker = f"# PRESERVE: {identifier} end"
    block = []
    recording = False
    for line in lines:
        if start_marker in line:
            recording = True
            block.append(line)
            continue
        if recording:
            block.append(line)
            if end_marker in line:
                break
    return block if block else None

def replace_or_insert_preserved_block(dev_lines, identifier, preserved_block, fallback_keyword=None):
    """
    Procura no dev_lines um bloco delimitado pelos marcadores de <identifier>.
    Se encontrado, substitui esse bloco pelo preserved_block.
    Se não encontrado e fallback_keyword for informado, insere o bloco logo após
    a linha que contenha esse fallback.
    Retorna as linhas modificadas.
    """
    start_marker = f"# PRESERVE: {identifier} start"
    end_marker = f"# PRESERVE: {identifier} end"
    new_lines = []
    replaced = False
    i = 0
    while i < len(dev_lines):
        line = dev_lines[i]
        if start_marker in line:
            # Pula as linhas até encontrar o marcador final
            while i < len(dev_lines) and end_marker not in dev_lines[i]:
                i += 1
            if i < len(dev_lines):  # pula também a linha do end_marker
                i += 1
            new_lines.extend(preserved_block)
            replaced = True
        else:
            new_lines.append(line)
            i += 1

    # Se não foi substituído, tenta inserir após a linha com fallback_keyword
    if not replaced and fallback_keyword:
        inserted = False
        for j, line in enumerate(new_lines):
            if fallback_keyword in line:
                new_lines = new_lines[:j+1] + preserved_block + new_lines[j+1:]
                inserted = True
                break
        if not inserted:
            new_lines.extend(preserved_block)
    return new_lines

def remove_conflicting_blocks(dev_lines):
    """
    Remove do conteúdo proveniente do dev os blocos que definem os estilos de
    json_style_control_panel e json_style_Splash sem estarem marcados com # PRESERVE.
    Esses blocos normalmente são compostos de duas linhas:
      - A linha que define a variável com os caminhos (ex: json_style_control_panel = os.path.abspath(...))
      - A linha que chama loadJsonStyle(...)
    """
    new_lines = []
    skip_next = False
    for line in dev_lines:
        stripped = line.strip()
        # Se a linha contém uma definição de estilo sem marcador de preservação, pulamos
        if ("json_style_control_panel =" in stripped or "json_style_Splash =" in stripped) and "PRESERVE:" not in stripped:
            skip_next = True  # pula também a próxima linha (assumindo que seja a loadJsonStyle)
            continue
        if skip_next:
            # Se a linha contém loadJsonStyle para os mesmos identificadores, pula-a
            if "loadJsonStyle" in stripped and ("json_style_control_panel" in stripped or "json_style_Splash" in stripped):
                skip_next = False
                continue
            skip_next = False
        new_lines.append(line)
    return new_lines

def update_production_file(dev_file, prod_file):
    """
    Atualiza o arquivo de produção com base no conteúdo do arquivo de desenvolvimento,
    mas preservando os blocos marcados no arquivo de produção.
    
    - O bloco de 'json_style_Splash' deverá ser mantido onde está (por exemplo, dentro de LoadingScreen).
    - O bloco de 'json_style_control_panel' deverá ser posicionado logo após a linha com 'self.liveCompileQss'.
    - As definições “cruas” no dev (sem os marcadores) serão removidas para evitar conflitos.
    """
    try:
        with open(dev_file, 'r', encoding='utf-8') as f:
            dev_lines = f.readlines()
    except Exception as e:
        print("Erro ao ler o arquivo de desenvolvimento:", e)
        return

    # Remove os blocos conflitantes do dev
    dev_lines = remove_conflicting_blocks(dev_lines)

    prod_lines = []
    if os.path.exists(prod_file):
        try:
            with open(prod_file, 'r', encoding='utf-8') as f:
                prod_lines = f.readlines()
        except Exception as e:
            print("Erro ao ler o arquivo de produção:", e)

    # Extrai os blocos preservados do arquivo de produção
    preserved_splash = extract_preserved_block(prod_lines, "json_style_Splash")
    preserved_control = extract_preserved_block(prod_lines, "json_style_control_panel")
    preserved_syspath = extract_preserved_block(prod_lines, "sys_path")

    # Se os blocos forem encontrados, atualiza o conteúdo do dev
    if preserved_splash:
        # Fallback: inserir logo após a linha que contenha 'self.ui.setupUi(self)'
        dev_lines = replace_or_insert_preserved_block(dev_lines, "json_style_Splash", preserved_splash,
                                                        fallback_keyword="self.ui.setupUi(self)")
    if preserved_control:
        # Fallback: inserir logo após a linha que contenha 'self.liveCompileQss'
        dev_lines = replace_or_insert_preserved_block(dev_lines, "json_style_control_panel", preserved_control,
                                                        fallback_keyword="self.liveCompileQss")
    if preserved_syspath:
        # Fallback: inserir logo após a linha que contenha 'import sys'
        dev_lines = replace_or_insert_preserved_block(dev_lines, "sys_path", preserved_syspath,
                                                        fallback_keyword="import sys")
        
    try:
        with open(prod_file, 'w', encoding='utf-8') as f:
            f.writelines(dev_lines)
        print(f"Arquivo de produção '{prod_file}' atualizado com sucesso.")
    except Exception as e:
        print("Erro ao escrever o arquivo de produção:", e)

class DevFileEventHandler(FileSystemEventHandler):
    def __init__(self, dev_file, prod_file):
        super().__init__()
        self.dev_file = dev_file
        self.prod_file = prod_file

    def on_modified(self, event):
        if event.src_path.endswith(os.path.basename(self.dev_file)):
            print(f"Detectada modificação em: {event.src_path}")
            update_production_file(self.dev_file, self.prod_file)

if __name__ == '__main__':
    # Defina os caminhos absolutos dos arquivos de desenvolvimento e produção
    dev_file = os.path.abspath('main_control_panel_TESTE.py')
    prod_file = os.path.abspath('main_control_panel.py')

    event_handler = DevFileEventHandler(dev_file, prod_file)
    observer = Observer()
    observer.schedule(event_handler, os.path.dirname(dev_file), recursive=False)
    observer.start()
    print(f"Monitorando alterações em {dev_file}. Pressione Ctrl+C para sair.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Encerrando monitoramento...")
        observer.stop()
    observer.join()
