

import os
PRODUCTION_ENV = os.getenv("PRODUCTION_ENV", "True")

if PRODUCTION_ENV == "True":
    # Production
    from Studio.Modules.__init_libs__ import *

elif PRODUCTION_ENV == "False":
    # Local test
    from Modules.__init_libs__ import *

def normalize_title(s: str) -> str:
    """
    - Remove espaços extras
    - Normaliza Unicode e casefold
    - Remove pontuação (tudo que não for letra, número ou espaço)
    """
    # colapsa múltiplos espaços
    s = " ".join(s.split())
    # normalização Unicode e lowercase
    s = unicodedata.normalize("NFC", s).casefold()
    # remove pontuação
    return re.sub(r"[^0-9a-zçáâãéêíóôõúü ]+", "", s)
