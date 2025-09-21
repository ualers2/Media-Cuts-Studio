

import os
PRODUCTION_ENV = os.getenv("PRODUCTION_ENV", "True")

if PRODUCTION_ENV == "True":
    # Production
    from Studio.Modules.__init_libs__ import *

elif PRODUCTION_ENV == "False":
    # Local test
    from Modules.__init_libs__ import *

def loop_threshold_norm_target(norm, target):
    # Lista de thresholds decrescentes de 0.8 até 0.5
    thresholds = [0.8, 0.62]

    for threshold in thresholds:

        # Calcula similaridade entre fname_norm e original_norm
        sim = SequenceMatcher(None, norm, target).ratio()
        print(f"similaridade?: {sim}")
        if sim >= threshold:
            return True
    
    # Se chegou aqui, nada foi encontrado
    print("Nenhuma similaridade encontrado após todas as tentativas.")
    return False