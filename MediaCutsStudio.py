import subprocess    
import sys
import os
import sys
import os

# Caminho correto para `CoreApp`
coreapp_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "MediaCutsStudio", "Versions", "Version_2")
)

# Adiciona ao sys.path para que o Python possa encontrá-lo
if coreapp_path not in sys.path:
    sys.path.append(coreapp_path)
    import CoreApp
    print("CoreApp importado com sucesso!")
    
subprocess.run(["MediaCutsStudio/Python/pythonw", f"MediaCutsStudio/Update_Update.py"])

subprocess.run(["MediaCutsStudio/Python/python", f"MediaCutsStudio/Update.py"])

# subprocess.run(["MediaCutsStudio/Python/python", f"MediaCutsStudio/Vesions/Vesion_2/main_control_panel.py"])


# comando_terminal = ['start', 'MediaCutsStudio/Python/python', f'MediaCutsStudio/Versions/Version_2/main_control_panel.py']
# subprocess.Popen(comando_terminal, shell=True)
