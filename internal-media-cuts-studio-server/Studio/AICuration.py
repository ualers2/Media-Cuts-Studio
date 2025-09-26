from agents import Agent,  ItemHelpers, Runner,RunHooks, handoff, ModelSettings , RunConfig, RunContextWrapper, Usage
import requests
import asyncio
import subprocess
import logging
import os
import cv2
from firebase_admin import db
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from pydantic import BaseModel
from openai.types.responses import ResponseCompletedEvent, ResponseTextDeltaEvent
import yt_dlp
import time
import unicodedata
import json
import re
import textwrap
import hashlib
from pathlib import Path
from difflib import SequenceMatcher
from datetime import datetime, timedelta
import requests
import srt
import pytz
from typing import List
from termcolor import cprint
from dotenv import load_dotenv
import math
# import pysubs2
import textwrap
from werkzeug.utils import secure_filename


diretorio_script = os.path.dirname(os.path.abspath(__file__)) 
os.makedirs(os.path.join(diretorio_script, 'Logs'), exist_ok=True)

# Cria o logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Formato dos logs
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Handler para o arquivo
file_handler = logging.FileHandler(os.path.join(diretorio_script, 'Logs', 'AICuration.log'))
file_handler.setFormatter(formatter)

# Handler para o console
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Adiciona ambos ao logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# os.chdir(diretorio_script)

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "Keys", "env.env"))

PRODUCTION_ENV = os.getenv("PRODUCTION_ENV", "True")

if PRODUCTION_ENV == "True":
    # Production
    from Studio.Modules.__init__ import *
    from Studio.AudioTranscriber import Audio_Transcriber
    from Studio.Studio import MediaCutsStudio
    MediaCutsStudio_instance = MediaCutsStudio(dockerffmpegCPU=False,dockerffmpegGPU=True)
    from Studio.TiktokAutoUploader_TESTEE.tiktok_uploader import tiktok
    from Studio.AutoReframe import AutoReframe, YOLO

    Audio_Transcriber_model = "faster-whisper-local-tiny"
    Audio_Transcriber_model_Cuts = "faster-whisper-local-small"
    Audio_Transcriber_webhook=False
    Audio_Transcriber_api_key=None
    Audio_Transcriber_WEBHOOK_URL=None
    dockerffmpegGPU = True
    show_preview = False
    path_ffmpegnotexe = 'ffmpeg'

    
elif PRODUCTION_ENV == "False":
    # Local test
    from Modules.__init__ import *
    from AudioTranscriber import Audio_Transcriber
    from Studio import MediaCutsStudio
    MediaCutsStudio_instance = MediaCutsStudio(dockerffmpegGPU=False,dockerffmpegCPU=True)
    from AutoReframe import AutoReframe, YOLO
    dockerffmpegGPU = False
    show_preview = False
    path_ffmpeg = os.path.join(diretorio_script, 'Utils', 'ffmpeg', 'ffmpeg.exe')
    
    path_ffmpegnotexe = os.path.join(diretorio_script, 'Utils', 'ffmpeg')
    os.environ['PATH'] = path_ffmpegnotexe + os.pathsep + os.environ['PATH']
    Audio_Transcriber_model = "faster-whisper-local-tiny"
    Audio_Transcriber_model_Cuts = "faster-whisper-local-tiny"
    Audio_Transcriber_webhook=False
    Audio_Transcriber_api_key=None
    Audio_Transcriber_WEBHOOK_URL=None
    # ########################################################################
    # # IMPORT FirebaseKeys
    # from Keys.FirebaseAppKeys import *
    # app_teste = init_firebase()
    ########################################################################
    path_keys_ = os.path.join(diretorio_script, 'Keys', 'keys.env')
    load_dotenv(dotenv_path=path_keys_)

class Corte_vertical(BaseModel):
    name_project: str
    titulo: str
    descricao: str
    hashtags: List[str]
    timestamp_inicio: str
    timestamp_fim: str
    name_score: float
    justificativa: str
    gancho_sugerido: str
    sentimento_principal: str
    potencial_de_viralizacao: int
    sugestao_de_titulo_curto: str

class AI_output_vertical(BaseModel):
    cortes: List[Corte_vertical]

class Corte_horizontal(BaseModel):
    name_project: str
    titulo: str
    descricao: str
    hashtags: List[str]
    timestamp_inicio: str
    timestamp_fim: str
    name_score: float
    justificativa: str
    gancho_sugerido: str
    sentimento_principal: str
    potencial_de_viralizacao: int
    sugestao_de_titulo_longo: str

class AI_output_horizontal(BaseModel):
    cortes: List[Corte_horizontal]

class AI_Curation:
    """
    A classe `AI_Curation` é responsável por automatizar o processo de curadoria, edição e publicação
    de cortes de vídeos longos para plataformas de vídeo curtos como TikTok, Reels e YouTube Shorts.
    Ela utiliza inteligência artificial para identificar os trechos mais impactantes e engajadores,
    realiza a transcrição de áudio, aplica legendas dinâmicas e efeitos visuais, e gerencia o upload
    ou o download dos vídeos finais.

    """
    def __init__(
        self, 
        includeHorizontal="",
        includeVertical="",
        StudioMode="Studio-Mini",
        linux_env=True,
        downloadToPanelEnabled='',
        secondsScheduleTiktokVideo='',
        TiktokAccount='',
        TiktokAccountCookies='',
        user_email='',
        user_email_origin='',
        canal_do_yt='',  
        lastlongvideotitle='',
        app_instance='',
        appdocs='',
        task_id='',
        title_origin='',
        pastedUrl='',
        Cutting_seconds='',

        SubtitleColor='white',
        SubtitleAnimation='Slow Fade-Out', 
        SubtitleFontName='Future',
        SubtitleEffects='Glow Effect',
        SubtitleFontsize='30',
        SubtitleVerticalReference='+20', 
        CaptionsAlignment = "5",
        CaptionsColor = "aqua",
        CaptionsFontName = "Future",
        CaptionsFontsize = 20,
        CaptionsPrimaryColour = "&HC0C0C0",
        CaptionsSecondaryColour = "&H8080",
        CaptionsOutlineColour = "&H0",
        CaptionsBackColour = "&H0",
        CaptionsBold = 1,
        CaptionsItalic = 0,
        CaptionsUnderline = 0,
        CaptionsOutline = 3,
        CaptionsShadow = 1,
        CaptionsRevealEffectInitialColor = "&HCCCC33&",
        CaptionsRevealEffectFinalColor = "&H0099FF&",
        legendstheme="Revelation Effect",
        editiontheme="Thumbnail Vertical Fusion",
        webhook=False,
        api_key="",
        max_caracter_to_see=10


        ):
        self.inicio = time.time() 
        self.includeHorizontal = includeHorizontal
        self.includeVertical = includeVertical
        self.Cutting_seconds = Cutting_seconds
        self.editiontheme = editiontheme
        self.title_origin = title_origin
        self.app_instance = app_instance
        self.appdocs = appdocs
        self.canal_do_yt = canal_do_yt
        self.lastlongvideotitle = lastlongvideotitle
        self.pastedUrl = pastedUrl
        self.StudioMode = StudioMode
                
        self.UPLOAD_URL = os.getenv("UPLOAD_URL")
        self.UPLOAD_URL_VIDEOMANAGER = os.getenv("UPLOAD_URL_VIDEOMANAGER")
        logger.info(f"UPLOAD_URL {self.UPLOAD_URL}")
        self.user_email = user_email
        self.user_email_origin = user_email_origin
        logger.info(f"user_email {self.user_email}")
        logger.info(f"user_email_origin {self.user_email_origin}")
        self.downloadToPanelEnabled = downloadToPanelEnabled
        self.legendstheme = legendstheme
        self.linux_env = linux_env
        self.api_key = api_key
        self.WEBHOOK_URL = os.getenv("WEBHOOK_URL")
        logger.info(f"WEBHOOK_URL {self.WEBHOOK_URL}")
        self.webhook = webhook
        self.secondsScheduleTiktokVideo = secondsScheduleTiktokVideo
        self.TiktokAccount = TiktokAccount
        self.TiktokAccountCookies = TiktokAccountCookies
        self.SubtitleColor = SubtitleColor 
        self.SubtitleAnimation = SubtitleAnimation
        self.SubtitleFontName = SubtitleFontName 
        self.SubtitleEffects = SubtitleEffects 
        self.SubtitleFontsize = SubtitleFontsize 
        self.SubtitleVerticalReference = SubtitleVerticalReference 
        self.CaptionsColor = CaptionsColor 
        self.CaptionsFontName = CaptionsFontName 
        self.CaptionsAlignment = CaptionsAlignment 
        self.CaptionsFontsize = CaptionsFontsize 
        self.CaptionsPrimaryColour = CaptionsPrimaryColour 
        self.CaptionsSecondaryColour = CaptionsSecondaryColour 
        self.CaptionsOutlineColour = CaptionsOutlineColour 
        self.CaptionsBackColour = CaptionsBackColour 
        self.CaptionsBold = CaptionsBold 
        self.CaptionsItalic = CaptionsItalic 
        self.CaptionsUnderline = CaptionsUnderline 
        self.CaptionsOutline = CaptionsOutline 
        self.CaptionsShadow = CaptionsShadow 
        self.CaptionsRevealEffectInitialColor = CaptionsRevealEffectInitialColor 
        self.CaptionsRevealEffectFinalColor = CaptionsRevealEffectFinalColor 
        self.MAX_INPUT_SIZE = 30000
        self.API_URL = os.getenv("API_URL")
        self.UPLOAD_URL = os.getenv("UPLOAD_URL")
        # if PRODUCTION_ENV == "True":
        #     self.transcriber = None
        # elif PRODUCTION_ENV == "False":
        self.transcriber = Audio_Transcriber(
                                        model_type=Audio_Transcriber_model_Cuts, 
                                        webhook=Audio_Transcriber_webhook,
                                        api_key=Audio_Transcriber_api_key,
                                        WEBHOOK_URL=Audio_Transcriber_WEBHOOK_URL
                                    )
        self.max_caracter_to_see = max_caracter_to_see
        self.base_dir = os.path.abspath(os.path.join(
                diretorio_script, 
                "WorkEnvironment", 
                "Process", 
                "MediaBase",  
                f'{canal_do_yt}'
            )
        )

        self.YOLO_MODEL = os.path.join(
            os.path.dirname(__file__), 
            "Models", "Yollo",
            "yolov11n-face.pt"#"yolov12n-face.pt"
        ) 
        self.task_id_db_str = f"{task_id}"
        logger.info("?????")
        self.ref_projects = db.reference(f'projects/{self.user_email}', app=self.appdocs)

        
        self.model = "gpt-4.1-nano"


        self.prompt_system_horizontal = """
        Você é uma IA especializada em identificar e extrair os trechos mais relevantes, informativos e narrativamente coerentes de vídeos, para a criação de cortes horizontais com foco em plataformas como YouTube e VOD. Seu objetivo é segmentar o conteúdo em blocos temáticos ou narrativos que mantenham a fluidez e ofereçam valor ao espectador, mesmo fora do contexto original.

        Baseie sua seleção nos seguintes critérios, priorizando a manutenção da coerência e o valor informativo:

        1.  **Coerência Narrativa:** Cada trecho deve apresentar um início, meio e fim claros, abordando um tópico ou subtópico de forma completa e compreensível, sem depender excessivamente do contexto anterior ou posterior.
        2.  **Profundidade do Conteúdo:** Priorize trechos que ofereçam insights detalhados, explicações aprofundadas, análises complexas ou discussões robustas sobre um determinado assunto.
        3.  **Transições Naturais:** Identifique pontos onde a transição entre assuntos é suave e lógica, permitindo que o corte se encaixe naturalmente em um novo vídeo sem parecer abrupto.
        4.  **Relevância para o Tema Principal:** Os trechos devem contribuir significativamente para o entendimento de um tema central ou para o desenvolvimento de uma ideia chave.
        5.  **Duração Adequada:** Cada trecho deve ter entre **3 a 10 minutos**, ideal para aprofundamento sem ser excessivamente longo.
        6.  **Valor Educacional ou Analítico:** Busque segmentos que expliquem conceitos, apresentem soluções, comparem ideias ou forneçam uma perspectiva única e bem fundamentada.
        7.  **Presença do Convidado:** Se houver um convidado, utilize seu nome (extraído da descrição) para indexação e categorização, mas a prioridade é sempre a qualidade e a coerência do conteúdo.

        ### Regras de Saída
        - `timestamp_inicio` e `timestamp_fim` devem estar dentro do escopo de duração do vídeo, obtido em `Duracao Total Do Video:`.
        - Cada objeto deve ter exatamente estas propriedades, sem texto adicional nem comentários:

        ```json
        {
            "name_project: "Nome Do Projeto Baseado no ``Título Original:``"
            "titulo": "Título curto e impactante do tema",
            "descricao": "Descrição sucinta do porquê este trecho é relevante",
            "hashtags": "lista de hashtags relevantes ao tema e ao convidado",
            "timestamp_inicio": "Inicio do Trecho relevante HH:MM:SS",
            "timestamp_fim": "Fim do Trecho relevante HH:MM:SS", 
            "justificativa": "Este trecho contém uma piada com um bom clímax e uma reação autêntica.",
            "gancho_sugerido": "Você não vai acreditar no que ele disse sobre...",
            "sentimento_principal": "humor",
            "potencial_de_viralizacao": "Uma nota de 1 a 10, baseada em critérios como humor, polêmica, informação útil ou emoção",
            "sugestao_de_titulo_longo": " Um título otimizado para plataformas de vídeos curtos, geralmente mais direto e chamativo que o titulo original.",
        }
        ````

        * `sugestao_de_titulo_longo`  Um título otimizado para plataformas de vídeos curtos, geralmente mais direto e chamativo que o titulo original.
        * `potencial_de_viralizacao`  Uma nota de 1 a 10, baseada em critérios como humor, polêmica, informação útil ou emoção. O seu name\_score já pode ser isso, mas vale a pena detalhar o critério no prompt.
        * `sentimento_principal`  Classifica a emoção do clipe (ex: "humor", "surpresa", "nostalgia").
        * `gancho_sugerido`  Uma sugestão de texto para os primeiros 2-3 segundos do vídeo (ex: "Você não vai acreditar no que ele disse sobre..."). Isso é crucial para prender a atenção.
        * `justificativa` (ex: "Este trecho contém uma piada com um bom clímax e uma reação autêntica.").
        * `name_project` deve ser um Nome Baseado no `Título Original:` o mesmo nome deve ser usado nos 3 a 5 objetos de cortes virais
        * `hashtags` deve usar o nome do convidado e palavras-chave do trecho.
        * Use dois-pontos e aspas duplas exatamente como no exemplo.
        * Garanta que os timestamps estejam no formato HH\:MM\:SS e que nao ultrapassem a minutagem de fim do video obtida atraves de "Duracao Total Do Video:"

        ### Restrições adicionais para títulos (NOVIDADE)

        * `titulo` deve ser **curto e impactante**, com no máximo **6 palavras**, forte e memorável.
        * `sugestao_de_titulo_longo` deve ter entre **10 e 15 palavras**, otimizado para YouTube/VOD, mais explicativo mas ainda chamativo.
        * Evitar títulos genéricos ou descritivos demais; priorizar emoção, gancho e impacto imediato.

        ---

        """



        
        self.prompt_system = """
            Você é uma IA especializada em identificar e extrair os trechos mais impactantes, interessantes e com maior potencial de engajamento em vídeos, para criação de cortes verticais em redes sociais (Reels, TikTok, Shorts etc.).  
            Baseie sua seleção nos seguintes critérios:
            1. **Gancho inicial forte**: fala direta que desperte curiosidade ou emoção.  
            2. **Conteúdo informativo ou inesperado**: estatísticas, curiosidades, revelações.  
            3. **Relevância para o público-alvo**: linguagem, tema ou humor alinhados às tendências.  
            4. **Duração ideal**: cada trecho deve seguir o limite imposto pelo usuario expecificamente em `Range de Limite de timestamp para cada Corte (em segundos):` 
            6. **Pico de emoção**: risadas, assuntos interressantes. 
            7. **Uso do nome do convidado**: utilize o nome do convidado (extraído da descrição) para potencializar hashtags, titulos e avaliar virality.
            8. **Nao corte a fala do speaker**: evite cortar a fala do speaker espere-o terminar o raciocinio 
            9. * Garanta que os timestamps estejam no formato HH:MM:SS e que nao ultrapassem a minutagem de fim do video obtida atraves do prompt do usuario expecificamente em "Duracao Total Do Video:"

            **Regras de saída**  

            - timestamp_inicio e timestamp_fim devem estar dentro do escopo de duracao do video que é obtido em `Duracao Total Do Video:` 
            - Cada objeto deve ter exatamente estas propriedades, sem texto adicional nem comentários:
            ```json
            {
                "name_project: "Nome Do Projeto Baseado no ``Título Original:``"
                "titulo": "Título curto e impactante do tema (máx. 100 caracteres). **periodicamente em forma de pergunta para gerar curiosidade e engajamento**",
                "sugestao_de_titulo_curto": "Título otimizado para vídeos curtos (máx. 100 caracteres). **periodicamente em forma de pergunta para gerar curiosidade e engajamento**"

                "descricao": "Descrição sucinta do porquê este trecho é relevante",
                "hashtags": "lista de hashtags relevantes ao tema e ao convidado",
                "timestamp_inicio": "Inicio do Trecho relevante HH:MM:SS",
                "timestamp_fim": "Fim do Trecho relevante HH:MM:SS", 
                "justificativa": "Este trecho contém uma piada com um bom clímax e uma reação autêntica.",
                "gancho_sugerido": "Você não vai acreditar no que ele disse sobre...",
                "sentimento_principal": "humor",
                "potencial_de_viralizacao": "Uma nota de 1 a 10, baseada em critérios como humor, polêmica, informação útil ou emoção",
            }
            ````

            * `timestamp_inicio e timestamp_fim` devem ser obrigatoriamente no formato HORA:MINUTO:SEGUNDO (HH:MM:SS) nunca retorne timestamp_inicio e timestamp_fim fora do formato contendo algo alem exemplo (00:01:01,400) 
            * `sugestao_de_titulo_curto`  Um título otimizado para plataformas de vídeos curtos, geralmente mais direto e chamativo que o titulo original.
            * `potencial_de_viralizacao`  Uma nota de 1 a 10, baseada em critérios como humor, polêmica, informação útil ou emoção. O seu name_score já pode ser isso, mas vale a pena detalhar o critério no prompt.
            * `sentimento_principal`  Classifica a emoção do clipe (ex: "humor", "surpresa", "nostalgia").
            * `gancho_sugerido`  Uma sugestão de texto para os primeiros 2-3 segundos do vídeo (ex: "Você não vai acreditar no que ele disse sobre..."). Isso é crucial para prender a atenção.
            * `justificativa` (ex: "Este trecho contém uma piada com um bom clímax e uma reação autêntica.").
            * `name_project` deve ser um nome gerado por voce com base na analise da transcricao o mesmo nome deve ser usado nos 3 a 5 objetos de cortes virais
            * `hashtags` deve usar o nome do convidado e palavras-chave do trecho.
            * Use dois-pontos e aspas duplas exatamente como no exemplo.
            * Garanta que os timestamps estejam no formato HH:MM:SS e que nao ultrapassem a minutagem de fim do video obtida atraves de "Duracao Total Do Video:"
            * O `titulo` e a `sugestao_de_titulo_curto` **devem periodicamente ser perguntas**, formuladas para gerar curiosidade, retenção e aumentar a probabilidade de viralização, mantendo o limite de 100 caracteres.

            Regras estritas para geração de **hashtags** :

                * **Priorize sempre o nome do convidado**: inclua variações comuns — nome completo, primeiro nome, sobrenome, apelido conhecido, handle sem `@`, versão sem acentos e versão abreviada (ex.: João Silva → #JoaoSilva, #Joao, #Silva, #JoaoSilvaOficial).
                * Inclua apenas hashtags **relevantes ao conteúdo do trecho** — palavras-chave extraídas da transcrição que descrevem o tópico, ação ou referência direta do trecho.
                * Evite hashtags genéricas ou desconexas que não ajudem no SEO do corte (ex.: não use tags virais genéricas se não tiver relação com o conteúdo).
                * Preferência por hashtags SEO-friendly:
                    * termos compostos em camelcase ou unidos sem espaços (ex.: `#MarketingDigital`, `#Curiosidade`),
                    * termos locais ou de idioma quando relevantes (ex.: `#pt`, `#brasil`, use com parcimônia),
                * inclua 3–10 hashtags por corte (máximo 10) — menos é melhor quando for preciso.
                * Não repita hashtags que sejam sinônimos exatos; prefira variações que cubram grafia com/sem acento e possíveis apelidos.
                * Não inclua símbolos, emojis ou espaços dentro de uma hashtag — só letras e números.
                * Se a transcrição referencia pessoas ou marcas populares, verifique se a hashtag da marca/pessoa está diretamente ligada ao trecho (caso contrário, não usar).
                * Se existir menção a palavras que são termos de busca (ex.: “SEO”, “investimento”, “criptomoedas”), inclua-as como hashtags complementares, mas somente se aparecerem no trecho.
                * Ao montar a lista, ordene as hashtags por prioridade SEO: 1) nome do convidado (variações), 2) keyword central do trecho, 3) tags de nicho/plataforma/localidade.
                
            Limite de caracteres para titulo e sugestao_de_titulo_curto:
                * titulo e sugestao_de_titulo_curto não podem ultrapassar 100 caracteres. Ajuste palavras e abreviações se necessário para respeitar o limite.
            
            Regras para Emotes / Emojis nos títulos (adicionado):
            * É permitido usar emojis/emotes em titulo e sugestao_de_titulo_curto para aumentar apelo visual e engajamento.
            * Use no máximo 2 emojis por título (recomendado 0–1 quando possível). Emojis contam para o limite de 100 caracteres.
            * Prefira emojis que complementem o sentimento principal do clipe (ex.: 😂 para humor, 😮 para surpresa, 🔥 para algo impactante).
            * Não use emojis dentro das hashtags; emojis são permitidos apenas nos campos titulo e sugestao_de_titulo_curto.
            * Evite emojis ambíguos ou potencialmente ofensivos; prefira emojis de uso comum e neutro.
            * Emojis não substituem palavras-chave essenciais — eles devem reforçar o título, não torná-lo menos descritivo.
            * Não use combinações de emojis que pareçam spam ou clickbait excessivo.
            * Se a plataforma alvo tem limitações conhecidas (ex.: caracteres contados diferente), priorize a conformidade com o limite de 100 caracteres.

            Siga rigorosamente todas as regras acima ao gerar cada objeto de saída.


        """
            
        logger.info(f"StudioMode? {StudioMode}")
        if self.StudioMode == "Studio-Startup":
            self.model = "gpt-4.1-nano"
        elif self.StudioMode == "Studio-Mini":
            self.model = "gpt-5-mini"
        elif self.StudioMode == "Studio-Deep-Think":
            self.model = "o3-mini"

                                

    def shedule_process_subclip(self, 
                                VIDEO_ID, 
                                output_filename,
                                start_time,
                                end_time,
                                date_time,
                                timezone,
                                user_email,
                                projectName,
                                API_KEY
                            ):

        payload = {
            "VIDEO_ID": VIDEO_ID,
            "start_time": start_time,          
            "end_time":   end_time,
            "date_time":  date_time,
            "timezone":   timezone,
            "user_email": user_email,
            "projectName": projectName,
            "output_filename": output_filename
        }

        resp = requests.post(
            f"{self.API_URL}/api/Media_Cuts_Studio/Process/Mode/generate_subclip_ai_curation",
            json=payload,
            headers={
                "X-User-Id": user_email,
                "X-API-KEY": API_KEY
            },
            timeout=10
        )

        if resp.status_code == 202:
            payload = resp.json()
            logger.info(f"Task agendada: {payload}")
            scheduled_time_task = payload["scheduled_time"]
            user_ = payload["user_email"]
            user_email_task = user_.replace(".", "_")
            process_queue_ref = db.reference('process_queue', app=self.app_instance)
            type_process = "generate_subclip_ai_curation"
            while True:
                all_items_process = process_queue_ref.get() or {}
                all_items = {**all_items_process}
                for key, item in all_items.items():
                    user = item['user_email']
                    user_email_db = user.replace(".", "_")
                    scheduled_time_db = item['scheduled_time']
                    type_process_db = item['type_process']
                    if str(user_email_db) == str(user_email_task):
                        if str(scheduled_time_db) == str(scheduled_time_task):
                            if str(type_process) == str(type_process_db):
                                logger.info(f"Tarefa encontrada esperando ser Completa para obter id")       
                                status_db = item['status']
                                logger.info(f"status_db? {status_db}")       
                                if status_db == 'Completed':
                                    video_id_db = item['video_id']
                                    logger.info(f"video_id_db? {video_id_db}")       

                                    # Deleta o nó da fila após obter os IDs
                                    process_queue_ref.child(key).delete()
                                    logger.info(f"Tarefa {key} removida da fila")
                                    return video_id_db
                                
                time.sleep(60)

        else:
            logger.error("Erro ao agendar:")
            logger.error(resp.status_code)
            logger.error(resp.text)
            
    def shedule_process_audio_transcriber(
                                self, 
                                VIDEO_ID, 
                                output_filename,
                                date_time,
                                timezone,
                                user_email,
                                projectName,
                                API_KEY
                            ):

        payload = {
            "VIDEO_ID": VIDEO_ID,
            "date_time":  date_time,
            "timezone":   timezone,
            "user_email": user_email,
            "projectName": projectName,
            "output_filename": output_filename
        }

        resp = requests.post(
            f"{self.API_URL}/api/Media_Cuts_Studio/Process/Mode/audio_transcriber",
            json=payload,
            headers={
                "X-User-Id": user_email,
                "X-API-KEY": API_KEY
            },
            timeout=10
        )


        if resp.status_code == 202:
            payload = resp.json()
            logger.info(f"Task agendada: {payload}")
            scheduled_time_task = payload["scheduled_time"]
            user_ = payload["user_email"]
            user_email_task = user_.replace(".", "_")
            process_queue_ref = db.reference('process_queue', app=self.app_instance)
            type_process = "audio_transcriber"
            while True:
                all_items_process = process_queue_ref.get() or {}
                all_items = {**all_items_process}
                for key, item in all_items.items():
                    user = item['user_email']
                    user_email_db = user.replace(".", "_")
                    scheduled_time_db = item['scheduled_time']
                    type_process_db = item['type_process']
                    if str(user_email_db) == str(user_email_task):
                        if str(scheduled_time_db) == str(scheduled_time_task):
                            if str(type_process) == str(type_process_db):
                                logger.info(f"Tarefa encontrada esperando ser Completa para obter id")       
                                status_db = item['status']
                                logger.info(f"status_db? {status_db}")       
                                if status_db == 'Completed':
                                    SRT_ID = item['SRT_ID']
                                    ASS_ID = item['ASS_ID']
                                    logger.info(f"SRT_ID? {SRT_ID}") 
                                    logger.info(f"ASS_ID? {ASS_ID}")  

                                    # Deleta o nó da fila após obter os IDs
                                    process_queue_ref.child(key).delete()
                                    logger.info(f"Tarefa {key} removida da fila")
                                    return SRT_ID, ASS_ID
                                
                time.sleep(60)

        else:
            logger.error("Erro ao agendar:")
            logger.error(resp.status_code)
            logger.error(resp.text)

    def shedule_process_theme_VerticalFusion(
                                self,
                                VIDEO_ID, 
                                IMAGE_ID,
                                ASS_ID,
                                texto_drawtext,
                                CaptionsAlignment,
                                SubtitleFontName,
                                SubtitleFontsize,
                                SubtitleColor,
                                SubtitleVerticalReference,
                                output_filename,
                                date_time,
                                timezone,
                                user_email,
                                projectName,
                                API_KEY
                            ):

        payload = {
            "VIDEO_ID": VIDEO_ID,
            "IMAGE_ID": IMAGE_ID,
            "ASS_ID": ASS_ID,
            "SubtitleFontName": SubtitleFontName,
            "texto_drawtext": texto_drawtext,
            "CaptionsAlignment": CaptionsAlignment,
            "SubtitleFontsize": SubtitleFontsize,
            "SubtitleColor": SubtitleColor,
            "SubtitleVerticalReference": SubtitleVerticalReference,
            "date_time":  date_time,
            "timezone":   timezone,
            "user_email": user_email,
            "projectName": projectName,
            "output_filename": output_filename
        }

        resp = requests.post(
            f"{self.API_URL}/api/Media_Cuts_Studio/Process/Mode/thumbnail_vertical_fusion",
            json=payload,
            headers={
                "X-User-Id": user_email,
                "X-API-KEY": API_KEY
            },
            timeout=10
        )


        if resp.status_code == 202:
            payload = resp.json()
            logger.info(f"Task agendada: {payload}")
            scheduled_time_task = payload["scheduled_time"]
            user_ = payload["user_email"]
            user_email_task = user_.replace(".", "_")
            process_queue_ref = db.reference('process_queue', app=self.app_instance)
            type_process = "thumbnail_vertical_fusion"
            while True:
                all_items_process = process_queue_ref.get() or {}
                all_items = {**all_items_process}
                for key, item in all_items.items():
                    user = item['user_email']
                    user_email_db = user.replace(".", "_")
                    scheduled_time_db = item['scheduled_time']
                    type_process_db = item['type_process']
                    if str(user_email_db) == str(user_email_task):
                        if str(scheduled_time_db) == str(scheduled_time_task):
                            if str(type_process) == str(type_process_db):
                                print(f"Tarefa encontrada esperando ser Completa para obter id")       
                                status_db = item['status']
                                print(f"status_db? {status_db}")       
                                if status_db == 'Completed':
                                    video_id_db = item['video_id']
                                    print(f"video_id_db? {video_id_db}")       

                                    # Deleta o nó da fila após obter os IDs
                                    process_queue_ref.child(key).delete()
                                    logger.info(f"Tarefa {key} removida da fila")
                                    return video_id_db
                            
                time.sleep(60)

        else:
            logger.error("Erro ao agendar:")
            logger.error(resp.status_code)
            logger.error(resp.text)

    def shedule_process_AutoReframe(    
                                self,
                                VIDEO_ID, 
                                ASS_ID,
                                CaptionsColor,
                                CaptionsFontsize,
                                CaptionsAlignment,
                                SubtitleFontName,
                                SubtitleFontsize,
                                SubtitleColor,
                                SubtitleVerticalReference,
                                output_filename,
                                date_time,
                                timezone,
                                user_email,
                                projectName,
                                API_KEY
                            ):

        payload = {
            "VIDEO_ID": VIDEO_ID,
            "ASS_ID": ASS_ID,
            "SubtitleFontName": SubtitleFontName,
            "CaptionsColor": CaptionsColor,
            "CaptionsFontsize": CaptionsFontsize,
            "CaptionsAlignment": CaptionsAlignment,
            "SubtitleFontsize": SubtitleFontsize,
            "SubtitleColor": SubtitleColor,
            "SubtitleVerticalReference": SubtitleVerticalReference,
            "date_time":  date_time,
            "timezone":   timezone,
            "user_email": user_email,
            "projectName": projectName,
            "output_filename": output_filename
        }

        resp = requests.post(
            f"{self.API_URL}/api/Media_Cuts_Studio/Process/Mode/AutoReframe",
            json=payload,
            headers={
                "X-User-Id": user_email,
                "X-API-KEY": API_KEY
            },
            timeout=10
        )

        if resp.status_code == 202:
            payload = resp.json()
            logger.info(f"Task agendada: {payload}")
            scheduled_time_task = payload["scheduled_time"]
            user_ = payload["user_email"]
            user_email_task = user_.replace(".", "_")
            process_queue_ref = db.reference('process_queue', app=self.app_instance)
            type_process = "AutoReframe"
            while True:
                all_items_process = process_queue_ref.get() or {}
                all_items = {**all_items_process}
                for key, item in all_items.items():
                    user = item['user_email']
                    user_email_db = user.replace(".", "_")
                    scheduled_time_db = item['scheduled_time']
                    type_process_db = item['type_process']
                    if str(user_email_db) == str(user_email_task):
                        if str(scheduled_time_db) == str(scheduled_time_task):
                            if str(type_process) == str(type_process_db):
                                logger.info(f"Tarefa encontrada esperando ser Completa para obter id")       
                                status_db = item['status']
                                logger.info(f"status_db? {status_db}")       
                                if status_db == 'Completed':
                                    video_id_db = item['video_id']
                                    logger.info(f"video_id_db? {video_id_db}")    
                                    
                                    # Deleta o nó da fila após obter os IDs
                                    process_queue_ref.child(key).delete()
                                    logger.info(f"Tarefa {key} removida da fila")
                                    return video_id_db
                                
                time.sleep(160)
        else:
            logger.error("Erro ao agendar:")
            logger.error(resp.status_code)
            logger.error(resp.text)
   
    def upload_(self, name_project, VIDEO_FILE_PATH, USER_ID_FOR_TEST):
            

        video_metadata = {
            "projectName": name_project,
            "type_project": "files",

        }

        if not os.path.exists(VIDEO_FILE_PATH):
            logger.error(f"Erro: O arquivo '{VIDEO_FILE_PATH}' não foi encontrado.")
            logger.error("Por favor, crie um arquivo MP4 com este nome ou ajuste o caminho.")
            exit()

        try:
            with open(VIDEO_FILE_PATH, 'rb') as video_file:
                files = {
                    'file': (os.path.basename(VIDEO_FILE_PATH), video_file, 'video/mp4')
                }
                data = {
                    'metadata': json.dumps(video_metadata) # Converte o dicionário de metadados para uma string JSON
                }
                headers = {
                    'X-User-Id': USER_ID_FOR_TEST 
                }
                logger.info(f"Tentando enviar '{VIDEO_FILE_PATH}' para {self.UPLOAD_URL}...")
                logger.info(f"Com metadados: {json.dumps(video_metadata, indent=2)}")
                response = requests.post(self.UPLOAD_URL, files=files, data=data, headers=headers)

                if response.status_code == 201:
                    logger.info("\nUpload bem-sucedido!")
                    logger.info("Resposta do servidor:")
                    logger.info(json.dumps(response.json(), indent=2))
                    payload = response.json()
                    VIDEO_ID = payload['video_id']
                    logger.info(f"video_id: {VIDEO_ID}")
                    return VIDEO_ID
                else:
                    logger.info(f"\nErro no upload: Código de status {response.status_code}")
                    logger.info("Resposta do servidor:")
                    try:
                        logger.info(json.dumps(response.json(), indent=2))
                    except json.JSONDecodeError:
                        logger.info(response.text) # Se a resposta não for JSON
                    logger.info("\nCertifique-se de que seu servidor Flask está rodando e o endpoint está acessível.")
                    logger.info("Verifique também se o 'USER_ID_FOR_TEST' e o 'UPLOAD_URL' estão corretos.")

        except FileNotFoundError:
            logger.error(f"Erro: O arquivo '{VIDEO_FILE_PATH}' não foi encontrado.")
        except requests.exceptions.ConnectionError:
            logger.error("Erro de conexão: O servidor não está acessível.")
            logger.error("Certifique-se de que o backend Flask está rodando em 'http://localhost:5000'.")
        except Exception as e:
            logger.error(f"Ocorreu um erro inesperado: {e}")

    def download_(self, save_path, USER_ID_FOR_TEST, VIDEO_ID) -> str:
        url = f"{self.UPLOAD_URL_VIDEOMANAGER}/api/videos/{VIDEO_ID}"
        headers={
            "X-User-Id": USER_ID_FOR_TEST,
            # "X-API-KEY": API_KEY
        }
        try:
            # 2) Faz a requisição em streaming
            with requests.get(url, headers=headers, stream=True, timeout=120) as resp:
                resp.raise_for_status()

                # 3) Grava em disco apenas chunks não vazios
                with open(save_path, "wb") as f:
                    for chunk in resp.iter_content(8192):
                        if chunk:
                            f.write(chunk)

        except requests.exceptions.RequestException as e:
            # 4) Tratamento de erro de rede/HTTP
            raise RuntimeError(f"Falha ao baixar vídeo: {e}") from e

        return save_path

    async def Autonomous_Analysis_Horizontal(self, 
                                resposta_ia, 
                                thumbnail_url, 
                                nome_rename_final,
                                project_key
                                ):
        self.inicio = time.time()
        logger.info("Inicializando a análise com o Agent...")
        self.debugg_webhook(self.api_key, "info", "Inicializando a análise com o Agent...")
        logger.info(f"Titulo do Vídeo: {self.lastlongvideotitle}")
        self.debugg_webhook(self.api_key, "info", f"Titulo do Vídeo: {self.lastlongvideotitle}")
        logger.info(f"Canal do Yt: {self.canal_do_yt}")
        self.debugg_webhook(self.api_key, "info", f"Canal do Yt: {self.canal_do_yt}")
        name_project = secure_filename(self.lastlongvideotitle).replace("-", "").replace("....", "").replace("...", "").replace("..", "").replace(".", "").replace("... - ", "").replace('"????????"', '').replace("...__", "_")

        self.configure_env()
        list_videos = []
        logger.info("🔑 Studio - Inicialize loop for cuts")
        self.debugg_webhook(self.api_key, "info", f"🎞️ Recortando os melhores trechos analisados por Curadoria de IA !")
        contador_de_Cortes_criados = 0 
        for idx, corte in enumerate(resposta_ia, start=1):
            title = corte["titulo"]
            desc = corte["descricao"]
            hashtags_origin = corte["hashtags"]
            ts_inicio = corte["timestamp_inicio"] 
            ts_fim    = corte["timestamp_fim"]    
            name_score = corte["name_score"]    
            justificativa = corte["justificativa"]
            gancho_sugerido = corte["gancho_sugerido"]
            sentimento_principal = corte["sentimento_principal"]
            potencial_de_viralizacao = corte["potencial_de_viralizacao"]
            sugestao_de_titulo_curto = corte["sugestao_de_titulo_longo"]
            self.debugg_webhook(self.api_key, "info", f"""🔍 Formatando Hashtags""")
            hashtags = MediaCutsStudio_instance.formatar_hashtags(hashtags_origin, formato="virgula")
            hashtags_for_sheduler = MediaCutsStudio_instance.formatar_hashtags(hashtags_origin, formato='virgula')
            
            self.send_to_webhook(self.api_key, "Mode", f"Shortify - Date - AI Curation", "yellow")
            self.send_to_webhook(self.api_key, "cuts_duration", f"{ts_inicio}/{ts_fim}", "green")
            self.send_to_webhook(self.api_key, "mediabase", f"{title}", "yellow")

            Informacoesdocorteviral = f"""
📝 Informacoes do corte viral                         
Name Project {name_project}
Titulo {title}
Descricao {desc}
Hashtags Origin {hashtags_origin}
Hashtags {hashtags}
Minutagem de Inicio {ts_inicio}
Minutagem de Fim {ts_fim}
Name Score: {name_score}
Justificativa: {justificativa}
Gancho Sugerido: {gancho_sugerido}
Sentimento Principal: {sentimento_principal}
Potencial De Viralizacao: {potencial_de_viralizacao}
Sugestao De Titulo Curto: {sugestao_de_titulo_curto}

            
                                
            """

            logger.info(Informacoesdocorteviral)

            texto_pra_titulo2 = f"{title}\n {hashtags}"
            texto_pra_titulo = f"{sugestao_de_titulo_curto}\n {hashtags}"
            
            texto_com_espacos = MediaCutsStudio_instance.add_line_breaks(f"{title}").replace(":", "") 

            if self.editiontheme == "AI Vertical Fusion":
                texto_pra_AI_Vertical_Fusion = f""



            logger.info("📝 Studio - Creating names for cuts")

            texto_sem_espacos = MediaCutsStudio_instance.normalize_find_mp4(sugestao_de_titulo_curto)
            sugestao_de_titulo_curto_sem_espacos = MediaCutsStudio_instance.normalize_find_mp4(sugestao_de_titulo_curto)

            path_create = os.path.abspath(os.path.join(diretorio_script, "WorkEnvironment", "Process", "Realtime_Cuts", 'Cuts', f'{texto_sem_espacos}'))
            path_create_2 = os.path.abspath(os.path.join(path_create, "CutsCreate"))
            VideosDirPath2 = os.path.abspath(os.path.join(path_create, "CutsDirPath"))
            output_video_converter = os.path.abspath(os.path.join(path_create, "CutsConverter"))
            output_folder = os.path.abspath(os.path.join(path_create, "CutsCreate"))


            os.makedirs(output_folder, exist_ok=True)
            os.makedirs(path_create, exist_ok=True)
            os.makedirs(path_create_2, exist_ok=True)
            os.makedirs(VideosDirPath2, exist_ok=True)
            os.makedirs(output_video_converter, exist_ok=True)

            
            audio_output = os.path.join(output_folder, f"audio_video_vertical_{contador_de_Cortes_criados + 1}.wav")
            audio_output_windows = os.path.join(output_folder,  f"audio_video_vertical_{contador_de_Cortes_criados + 1}.wav")
            trasncript_srt_windows = os.path.join(path_create,  f"audio_video_vertical_{contador_de_Cortes_criados + 1}.srt")
            audio_srt = os.path.join(output_folder, f"audio_video_vertical_{contador_de_Cortes_criados + 1}.srt")
            if self.linux_env == True:
                audio_ass_windows = f"/app/Studio/WorkEnvironment/Process/Realtime_Cuts/Cuts/{texto_sem_espacos}/CutsCreate/audio_video_vertical_{contador_de_Cortes_criados + 1}.ass"
                audio_srt_windows = f"/app/Studio/WorkEnvironment/Process/Realtime_Cuts/Cuts/{texto_sem_espacos}/CutsCreate/audio_video_vertical_{contador_de_Cortes_criados + 1}.srt"
            if self.linux_env == False:
                os.chdir(diretorio_script)
                audio_ass_windows = f"WorkEnvironment/Process/Realtime_Cuts/Cuts/{texto_sem_espacos}/CutsCreate/audio_video_vertical_{contador_de_Cortes_criados + 1}.ass"
                audio_srt_windows = f"WorkEnvironment/Process/Realtime_Cuts/Cuts/{texto_sem_espacos}/CutsCreate/audio_video_vertical_{contador_de_Cortes_criados + 1}.srt"

            audio_ass_windows2 = os.path.join(output_folder,  f"audio_video_vertical_{contador_de_Cortes_criados + 1}.ass")

            output_processar_video = os.path.join(output_folder, f"video_vertical_{contador_de_Cortes_criados + 1}.mp4")
            output_video_subtittle = f"{texto_sem_espacos}.mp4"
            output_video_subtittle_final = os.path.join(output_folder, f"{texto_sem_espacos}.mp4")
            output_video_subtittle_final_2 = os.path.join(output_folder, f"{texto_sem_espacos}_.mp4")

            output_video_subtittle_watermask = os.path.join(output_folder, f"{sugestao_de_titulo_curto_sem_espacos}_media_cuts.mp4")
            output_video_subtittle_ad = os.path.join(output_folder, f"video_vertical_{contador_de_Cortes_criados + 1}_subtitle_ad.mp4")
            output_video_convert = os.path.abspath(os.path.join(diretorio_script, "WorkEnvironment", "Process", "Realtime_Cuts", 'Cuts', f'{texto_sem_espacos}' ,  f"video_vertical_{contador_de_Cortes_criados + 1}_subtitles.mp4"))
            output_filename = f"subclip_vertical_{contador_de_Cortes_criados + 1}.mp4"

            timezone = "America/Sao_Paulo"
            date_time = (datetime.now(pytz.timezone(timezone)) + timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S")

            logger.info("✂️ Studio - Creating Subclip")

            subclip_filename = MediaCutsStudio_instance.generate_subclip_with_ffmpeg_ai_curation(
                                                                video_input=nome_rename_final,
                                                                start_time=ts_inicio,
                                                                end_time=ts_fim,
                                                                output_filename=output_video_subtittle_final
                                                                )

            self.debugg_webhook(self.api_key, "info", "🎵 Studio - Extracting Audio")


            try:
                audio_linux = audio_output_windows
                
                self.debugg_webhook(self.api_key, "info", "🗣️ Studio - Transcribing Audio")

                resultado, total_time_str = self.transcriber.main(
                    path_videofile=subclip_filename, 
                    path_file_audio=audio_linux
                                
                    )

            except Exception as err:
                audio_linux = audio_output_windows

            MediaCutsStudio_instance.adpte_srt_file(file_path=audio_srt_windows)

            flag = self.transcriber.convert_to_ass(subtitlesrt=audio_srt_windows, subtitleass=audio_ass_windows)
            cprint(flag, "green" if flag else "red")

            novo_estilo = {
                'Fontname': self.CaptionsFontName,
                'Fontsize': 20,
                'PrimaryColour': self.CaptionsPrimaryColour, 
                'SecondaryColour': self.CaptionsSecondaryColour, 
                'OutlineColour': self.CaptionsOutlineColour,  
                'BackColour': self.CaptionsBackColour, 
                'Bold': self.CaptionsBold, 
                'Italic': self.CaptionsItalic, 
                'Underline': self.CaptionsUnderline, 
                'Outline': self.CaptionsOutline,  
                'Shadow': self.CaptionsShadow, 
                'Alignment': self.CaptionsAlignment  
            }
            MediaCutsStudio_instance.modify_ass_styles(audio_ass_windows, novo_estilo)
            legendstheme_str = f"{self.legendstheme}"
            if legendstheme_str.startswith("Revelation Effect"):
                MediaCutsStudio_instance.apply_reveal_effect(
                    ass_file_path=audio_ass_windows,
                    initial_color=self.CaptionsRevealEffectInitialColor,
                    final_color=self.CaptionsRevealEffectFinalColor
                )
            elif legendstheme_str.startswith("Typewriter Effect"):
                MediaCutsStudio_instance.apply_typewriter_effect_fixed(
                    audio_ass_windows, 
                    char_reveal_time=75
                    )
            logger.info("\n Studio - Grouping Subtitles in Video")
            
            # self.download_(output_video_subtittle_final, self.user_email, VIDEO_ID_SUBCLIP)
            MediaCutsStudio_instance.embutir_legenda_ass(output_video_subtittle_final, audio_ass_windows, output_video_subtittle_final_2)
            if self.linux_env == True:
                watermark_image_path = f"/app/Studio/Utils/watermask2.png"
            elif self.linux_env == False:
                watermark_image_path = f"Utils/watermask2.png"
            
            api_key_str = str(self.api_key)
            if api_key_str.startswith("apikey-startup"):
                add_watermark(
                    input_video=output_video_subtittle_final_2,
                    output_video=output_video_subtittle_watermask,
                    watermark_image=watermark_image_path,
                    overlay_position="main_w-overlay_w-20:20",
                    watermark_width=140,  
                    start_time_seconds=10, 
                    gpu=dockerffmpegGPU
                )
            else:
                output_video_subtittle_watermask = output_video_subtittle_final_2

            tempo_final = time.time()
            minutos, segundos = divmod(int(tempo_final - self.inicio), 60)
            logger.info(f"\n ⏳ Time taken to create horizontal video: {minutos}m {segundos}")

            filename = os.path.basename(output_video_subtittle_watermask).replace(".mp4", "")
            safe_project_name = secure_filename(self.title_origin).replace("-", "")
            safe_project_name_filter = re.sub(r'[^0-9A-Za-z_-]', '', safe_project_name)
            ref_projects_metadata = db.reference(f'projects/{self.user_email}/{safe_project_name_filter}/metadata/{filename}', app=self.appdocs)
            video_metadata_sheduler = {
                "filename": os.path.basename(output_video_subtittle_watermask),
                "title": sugestao_de_titulo_curto,
                "description": desc,
                "tags": hashtags_for_sheduler,
                "schedule_time": "None",
                "social_networks": ["youtube", "tiktok"],
            }
            ref_projects_metadata.update(video_metadata_sheduler)
        
            VIDEO_FILE_PATH = output_video_subtittle_watermask
            USER_ID_FOR_TEST = self.user_email

            video_metadata = {
                "projectName": name_project,
                "title": sugestao_de_titulo_curto,
                "description": desc,
                "hashtags": hashtags_origin,
                "minutagemdeInicio": ts_inicio,
                "minutagemdeFim": ts_fim,
                "urltumbnail": thumbnail_url,
                "justificativa": justificativa,
                "sentimento_principal": sentimento_principal,
                "potencial_de_viralizacao": potencial_de_viralizacao
            }

            if not os.path.exists(VIDEO_FILE_PATH):
                logger.info(f"Erro: O arquivo '{VIDEO_FILE_PATH}' não foi encontrado.")
                logger.info("Por favor, crie um arquivo MP4 com este nome ou ajuste o caminho.")
                exit()
            try:
                with open(VIDEO_FILE_PATH, 'rb') as video_file:
                    files = {
                        'file': (os.path.basename(VIDEO_FILE_PATH), video_file, 'video/mp4')
                    }
                    data = {
                        'metadata': json.dumps(video_metadata) 
                    }
                    headers = {
                        'X-User-Id': USER_ID_FOR_TEST 
                        # 'Authorization': 'Bearer seu_token_firebase_aqui' 
                    }

                    logger.info(f"Tentando enviar '{VIDEO_FILE_PATH}' para {self.UPLOAD_URL}...")
                    logger.info(f"Com metadados: {json.dumps(video_metadata, indent=2)}")
                    response = requests.post(self.UPLOAD_URL, files=files, data=data, headers=headers)
                    if response.status_code == 201:
                        logger.info("\nUpload bem-sucedido!")
                        logger.info("Resposta do servidor:")
                        logger.info(json.dumps(response.json(), indent=2))
                    else:
                        logger.info(f"\nErro no upload: Código de status {response.status_code}")
                        logger.info("Resposta do servidor:")
                        try:
                            logger.info(json.dumps(response.json(), indent=2))
                        except json.JSONDecodeError:
                            logger.info(response.text) # Se a resposta não for JSON
                        logger.info("\nCertifique-se de que seu servidor Flask está rodando e o endpoint está acessível.")
                        logger.info("Verifique também se o 'USER_ID_FOR_TEST' e o 'UPLOAD_URL' estão corretos.")

            except FileNotFoundError:
                logger.info(f"Erro: O arquivo '{VIDEO_FILE_PATH}' não foi encontrado.")
            except requests.exceptions.ConnectionError:
                logger.info("Erro de conexão: O servidor não está acessível.")
                logger.info("Certifique-se de que o backend Flask está rodando em 'http://localhost:5000'.")
            except Exception as e:
                logger.info(f"Ocorreu um erro inesperado: {e}")



            # Monta o dicionário com caminho e metadados
            video_info = {
                "id": idx,
                "titulo": title,
                "descricao": desc,
                "hashtags": hashtags_origin,
                "timestamp_inicio": ts_inicio,
                "timestamp_fim": ts_fim,
                "filename": output_video_subtittle_watermask,
                "name_score": name_score,
                "projectName": name_project,
                "justificativa": justificativa,
                "gancho_sugerido": gancho_sugerido,
                "sentimento_principal": sentimento_principal,
                "potencial_de_viralizacao": potencial_de_viralizacao,
                "sugestao_de_titulo_curto": sugestao_de_titulo_curto
            }

            list_videos.append(video_info)

            logger.info(f"list_videos {list_videos}")
            # contador_de_Cortes_criados += 1
        
        logger.info(f"Todos os cortes foram criados")

        tempo_final = time.time()
        minutos, segundos = divmod(int(tempo_final - self.inicio), 60)
        cprint(f"\n ⏳ Todos os cortes foram criados: {minutos}m {segundos}")
        self.debugg_webhook(self.api_key, "info", f"⏳ Todos os cortes foram criados {minutos}m {segundos}")
        
        # self.update_status_progress(100, project_key)

        logger.info(f"list_videos {list_videos}")
        # self.Update_To_Status_Completed(self.inicio)
        return list_videos

    async def Autonomous_Analysis(self, 
                                resposta_ia, 
                                thumbnail_url, 
                                nome_rename_final,
                                output_miniatura
                                ):

        logger.info("Inicializando a análise com o Agent...")
        self.debugg_webhook(self.api_key, "info", "Inicializando a análise com o Agent...")
        logger.info(f"Titulo do Vídeo: {self.lastlongvideotitle}")
        self.debugg_webhook(self.api_key, "info", f"Titulo do Vídeo: {self.lastlongvideotitle}")
        logger.info(f"Canal do Yt: {self.canal_do_yt}")
        self.debugg_webhook(self.api_key, "info", f"Canal do Yt: {self.canal_do_yt}")

        self.configure_env()
        list_videos = []
        logger.info("🔑 Studio - Inicialize loop for cuts")
        self.debugg_webhook(self.api_key, "info", f"🎞️ Recortando os melhores trechos analisados por Curadoria de IA !")
        contador_de_Cortes_criados = 0 
        for idx, corte in enumerate(resposta_ia, start=1):
            title = corte["titulo"]
            desc = corte["descricao"]
            hashtags_origin = corte["hashtags"]
            ts_inicio = corte["timestamp_inicio"] 
            ts_fim    = corte["timestamp_fim"]    
            name_score = corte["name_score"]    
            name_project = corte["name_project"]    
            justificativa = corte["justificativa"]
            gancho_sugerido = corte["gancho_sugerido"]
            sentimento_principal = corte["sentimento_principal"]
            potencial_de_viralizacao = corte["potencial_de_viralizacao"]
            sugestao_de_titulo_curto = corte["sugestao_de_titulo_curto"]
            self.debugg_webhook(self.api_key, "info", f"""🔍 Formatando Hashtags""")
            hashtags = MediaCutsStudio_instance.formatar_hashtags(hashtags_origin)
            
            self.send_to_webhook(self.api_key, "Mode", f"Shortify - Date - AI Curation", "yellow")
            self.send_to_webhook(self.api_key, "cuts_duration", f"{ts_inicio}/{ts_fim}", "green")
            self.send_to_webhook(self.api_key, "mediabase", f"{title}", "yellow")

            Informacoesdocorteviral = f"""
📝 Informacoes do corte viral                         
Name Project {name_project}
Titulo {title}
Descricao {desc}
Hashtags Origin {hashtags_origin}
Hashtags {hashtags}
Minutagem de Inicio {ts_inicio}
Minutagem de Fim {ts_fim}
Name Score: {name_score}
Justificativa: {justificativa}
Gancho Sugerido: {gancho_sugerido}
Sentimento Principal: {sentimento_principal}
Potencial De Viralizacao: {potencial_de_viralizacao}
Sugestao De Titulo Curto: {sugestao_de_titulo_curto}

            
                                
            """

            logger.info(Informacoesdocorteviral)

            texto_pra_titulo2 = f"{title}\n {hashtags}"
            texto_pra_titulo = f"{sugestao_de_titulo_curto}\n {hashtags}"
            
            texto_com_espacos = MediaCutsStudio_instance.add_line_breaks(f"{title}").replace(":", "") 

            if self.editiontheme == "AI Vertical Fusion":
                texto_pra_AI_Vertical_Fusion = f""



            logger.info("📝 Studio - Creating names for cuts")

            texto_sem_espacos = MediaCutsStudio_instance.normalize_find_mp4(title)
            path_create = os.path.abspath(os.path.join(diretorio_script, "WorkEnvironment", "Process", "Realtime_Cuts", 'Cuts', f'{texto_sem_espacos}'))
            path_create_2 = os.path.abspath(os.path.join(path_create, "CutsCreate"))
            VideosDirPath2 = os.path.abspath(os.path.join(path_create, "CutsDirPath"))
            output_video_converter = os.path.abspath(os.path.join(path_create, "CutsConverter"))
            output_folder = os.path.abspath(os.path.join(path_create, "CutsCreate"))


            os.makedirs(output_folder, exist_ok=True)
            os.makedirs(path_create, exist_ok=True)
            os.makedirs(path_create_2, exist_ok=True)
            os.makedirs(VideosDirPath2, exist_ok=True)
            os.makedirs(output_video_converter, exist_ok=True)

            
            audio_output = os.path.join(output_folder, f"audio_video_vertical_{contador_de_Cortes_criados + 1}.wav")
            audio_output_windows = os.path.join(output_folder,  f"audio_video_vertical_{contador_de_Cortes_criados + 1}.wav")
            trasncript_srt_windows = os.path.join(path_create,  f"audio_video_vertical_{contador_de_Cortes_criados + 1}.srt")
            audio_srt = os.path.join(output_folder, f"audio_video_vertical_{contador_de_Cortes_criados + 1}.srt")
            if self.linux_env == True:
                audio_ass_windows = f"/app/Studio/WorkEnvironment/Process/Realtime_Cuts/Cuts/{texto_sem_espacos}/CutsCreate/audio_video_vertical_{contador_de_Cortes_criados + 1}.ass"
                audio_srt_windows = f"/app/Studio/WorkEnvironment/Process/Realtime_Cuts/Cuts/{texto_sem_espacos}/CutsCreate/audio_video_vertical_{contador_de_Cortes_criados + 1}.srt"
            if self.linux_env == False:
                os.chdir(diretorio_script)
                audio_ass_windows = f"WorkEnvironment/Process/Realtime_Cuts/Cuts/{texto_sem_espacos}/CutsCreate/audio_video_vertical_{contador_de_Cortes_criados + 1}.ass"
                audio_srt_windows = f"WorkEnvironment/Process/Realtime_Cuts/Cuts/{texto_sem_espacos}/CutsCreate/audio_video_vertical_{contador_de_Cortes_criados + 1}.srt"

            audio_ass_windows2 = os.path.join(output_folder,  f"audio_video_vertical_{contador_de_Cortes_criados + 1}.ass")

            output_processar_video = os.path.join(output_folder, f"video_vertical_{contador_de_Cortes_criados + 1}.mp4")
            output_video_subtittle = f"{texto_sem_espacos}.mp4"
            output_video_subtittle_final = os.path.join(output_folder, f"{texto_sem_espacos}.mp4")

            output_video_subtittle_watermask = os.path.join(output_folder, f"video_vertical_{contador_de_Cortes_criados + 1}_subtitle_and_watermask.mp4")
            output_video_subtittle_ad = os.path.join(output_folder, f"video_vertical_{contador_de_Cortes_criados + 1}_subtitle_ad.mp4")
            output_video_convert = os.path.abspath(os.path.join(diretorio_script, "WorkEnvironment", "Process", "Realtime_Cuts", 'Cuts', f'{texto_sem_espacos}' ,  f"video_vertical_{contador_de_Cortes_criados + 1}_subtitles.mp4"))
            output_filename = f"subclip_vertical_{contador_de_Cortes_criados + 1}.mp4"

            timezone = "America/Sao_Paulo"
            date_time = (datetime.now(pytz.timezone(timezone)) + timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S")

            logger.info("✂️ Studio - Creating Subclip")

            VIDEO_ID = self.upload_(name_project, nome_rename_final, self.user_email)

            VIDEO_ID_SUBCLIP = self.shedule_process_subclip(
                                    VIDEO_ID, 
                                    output_filename,
                                    ts_inicio,
                                    ts_fim,
                                    date_time,
                                    timezone,
                                    self.user_email,
                                    texto_sem_espacos,
                                    self.api_key
                                )
   
            SRT_ID, ASS_ID = self.shedule_process_audio_transcriber(
                                            VIDEO_ID_SUBCLIP, 
                                            output_filename,
                                            date_time,
                                            timezone,
                                            self.user_email,
                                            texto_sem_espacos,
                                            self.api_key
                                        )
            
            self.download_(audio_srt_windows, self.user_email, SRT_ID)

            self.download_(audio_ass_windows, self.user_email, ASS_ID)

            novo_estilo = {
                'Fontname': self.CaptionsFontName,
                'Fontsize': self.CaptionsFontsize,
                'PrimaryColour': self.CaptionsPrimaryColour, 
                'SecondaryColour': self.CaptionsSecondaryColour, 
                'OutlineColour': self.CaptionsOutlineColour,  
                'BackColour': self.CaptionsBackColour, 
                'Bold': self.CaptionsBold, 
                'Italic': self.CaptionsItalic, 
                'Underline': self.CaptionsUnderline, 
                'Outline': self.CaptionsOutline,  
                'Shadow': self.CaptionsShadow, 
                'Alignment': self.CaptionsAlignment  
            }
            MediaCutsStudio_instance.modify_ass_styles(audio_ass_windows, novo_estilo)
            legendstheme_str = f"{self.legendstheme}"
            if legendstheme_str.startswith("Revelation Effect"):
                MediaCutsStudio_instance.apply_reveal_effect(
                    ass_file_path=audio_ass_windows,
                    initial_color=self.CaptionsRevealEffectInitialColor,
                    final_color=self.CaptionsRevealEffectFinalColor
                )
            elif legendstheme_str.startswith("Typewriter Effect"):
                MediaCutsStudio_instance.apply_typewriter_effect_fixed(
                    audio_ass_windows, 
                    char_reveal_time=75
                    )
            logger.info("\n Studio - Grouping Subtitles in Video")

            if self.editiontheme == "Thumbnail Vertical Fusion":
                IMAGE_ID = self.upload_(name_project, output_miniatura, self.user_email)
                VIDEO_ID_SUBTITLE = self.shedule_process_theme_VerticalFusion(
                                        VIDEO_ID_SUBCLIP, 
                                        IMAGE_ID,
                                        ASS_ID,
                                        texto_pra_titulo,
                                        self.CaptionsAlignment,
                                        self.SubtitleFontName,
                                        self.SubtitleFontsize,
                                        self.SubtitleColor,
                                        self.SubtitleVerticalReference,
                                        output_video_subtittle,
                                        date_time,
                                        timezone,
                                        self.user_email,
                                        texto_sem_espacos,
                                        self.api_key
                                    )

            elif self.editiontheme == "AI Vertical Fusion":
                VIDEO_ID_SUBTITLE = self.shedule_process_AutoReframe(    
                        VIDEO_ID_SUBCLIP, 
                        ASS_ID,
                        self.CaptionsColor,
                        self.CaptionsFontsize,
                        self.CaptionsAlignment,
                        self.SubtitleFontName,
                        self.SubtitleFontsize,
                        self.SubtitleColor,
                        self.SubtitleVerticalReference,
                        output_video_subtittle,
                        date_time,
                        timezone,
                        self.user_email,
                        texto_sem_espacos,
                        self.api_key
                    )

            self.download_(output_video_subtittle_final, self.user_email, VIDEO_ID_SUBTITLE)

            # cprint("\n🔄 Converting video to MP4")


            # flag = MediaCutsStudio_instance.convert_to_mp4_codec_with_ffmpeg(
            #         input_video=output_video_subtittle,
            #         output_video_mkv=output_video_convert
            #         )

            # cprint("\n🎉 Conversion Complete!", "green")

            tempo_final = time.time()
            minutos, segundos = divmod(int(tempo_final - self.inicio), 60)
            logger.info(f"\n ⏳ Time taken to create vertical video: {minutos}m {segundos}")
            
            
            if self.downloadToPanelEnabled == True or self.downloadToPanelEnabled == "True" or self.downloadToPanelEnabled == "true":
     
                VIDEO_FILE_PATH = output_video_subtittle_final
                USER_ID_FOR_TEST = self.user_email_origin

                video_metadata = {
                    "projectName": name_project,
                    "type_project": "video",
                    "title": sugestao_de_titulo_curto,
                    "description": desc,
                    "hashtags": hashtags_origin,
                    "minutagemdeInicio": ts_inicio,
                    "minutagemdeFim": ts_fim,
                    "urltumbnail": thumbnail_url,
                    "justificativa": justificativa,
                    "sentimento_principal": sentimento_principal,
                    "potencial_de_viralizacao": potencial_de_viralizacao
                }

                # --- Verificações Iniciais ---
                if not os.path.exists(VIDEO_FILE_PATH):
                    logger.info(f"Erro: O arquivo '{VIDEO_FILE_PATH}' não foi encontrado.")
                    logger.info("Por favor, crie um arquivo MP4 com este nome ou ajuste o caminho.")
                    exit()

                # --- Preparação da Requisição ---

                # Abre o arquivo de vídeo em modo binário
                try:
                    with open(VIDEO_FILE_PATH, 'rb') as video_file:
                        # 'files' é para o arquivo, 'data' é para os outros campos (incluindo o JSON de metadados)
                        # O 'files' espera um dicionário onde a chave é o nome do campo ('file') e o valor é uma tupla
                        # (nome_do_arquivo, objeto_arquivo_aberto, content_type)
                        files = {
                            'file': (os.path.basename(VIDEO_FILE_PATH), video_file, 'video/mp4')
                        }
                        
                        # 'data' é para campos de formulário, onde o 'metadata' é uma string JSON
                        data = {
                            'metadata': json.dumps(video_metadata) # Converte o dicionário de metadados para uma string JSON
                        }
                        
                        # Cabeçalhos para autenticação (para o mock, use 'X-User-Id')
                        # EM PRODUÇÃO, VOCÊ USARIA 'Authorization': 'Bearer SEU_TOKEN_JWT'
                        headers = {
                            'X-User-Id': USER_ID_FOR_TEST 
                            # 'Authorization': 'Bearer seu_token_firebase_aqui' 
                        }

                        logger.info(f"Tentando enviar '{VIDEO_FILE_PATH}' para {self.UPLOAD_URL}...")
                        logger.info(f"Com metadados: {json.dumps(video_metadata, indent=2)}")

                        # Faz a requisição POST
                        response = requests.post(self.UPLOAD_URL, files=files, data=data, headers=headers)

                        # --- Tratamento da Resposta ---
                        if response.status_code == 200:
                            logger.info("\nUpload bem-sucedido!")
                            logger.info("Resposta do servidor:")
                            logger.info(json.dumps(response.json(), indent=2))
                        else:
                            logger.info(f"\nErro no upload: Código de status {response.status_code}")
                            logger.info("Resposta do servidor:")
                            try:
                                logger.info(json.dumps(response.json(), indent=2))
                            except json.JSONDecodeError:
                                logger.info(response.text) # Se a resposta não for JSON
                            logger.info("\nCertifique-se de que seu servidor Flask está rodando e o endpoint está acessível.")
                            logger.info("Verifique também se o 'USER_ID_FOR_TEST' e o 'UPLOAD_URL' estão corretos.")

                except FileNotFoundError:
                    logger.info(f"Erro: O arquivo '{VIDEO_FILE_PATH}' não foi encontrado.")
                except requests.exceptions.ConnectionError:
                    logger.info("Erro de conexão: O servidor não está acessível.")
                    logger.info("Certifique-se de que o backend Flask está rodando em 'http://localhost:5000'.")
                except Exception as e:
                    logger.info(f"Ocorreu um erro inesperado: {e}")



            elif self.downloadToPanelEnabled == False or self.downloadToPanelEnabled == "False" or self.downloadToPanelEnabled == "false":

                VIDEO_FILE_PATH = output_video_subtittle_final
                USER_ID_FOR_TEST = self.user_email

                video_metadata = {
                    "projectName": name_project,
                    "title": sugestao_de_titulo_curto,
                    "description": desc,
                    "hashtags": hashtags_origin,
                    "minutagemdeInicio": ts_inicio,
                    "minutagemdeFim": ts_fim,
                    "urltumbnail": thumbnail_url,
                    "justificativa": justificativa,
                    "sentimento_principal": sentimento_principal,
                    "potencial_de_viralizacao": potencial_de_viralizacao
                }

                # --- Verificações Iniciais ---
                if not os.path.exists(VIDEO_FILE_PATH):
                    logger.info(f"Erro: O arquivo '{VIDEO_FILE_PATH}' não foi encontrado.")
                    logger.info("Por favor, crie um arquivo MP4 com este nome ou ajuste o caminho.")
                    exit()

                # --- Preparação da Requisição ---

                # Abre o arquivo de vídeo em modo binário
                try:
                    with open(VIDEO_FILE_PATH, 'rb') as video_file:
                        # 'files' é para o arquivo, 'data' é para os outros campos (incluindo o JSON de metadados)
                        # O 'files' espera um dicionário onde a chave é o nome do campo ('file') e o valor é uma tupla
                        # (nome_do_arquivo, objeto_arquivo_aberto, content_type)
                        files = {
                            'file': (os.path.basename(VIDEO_FILE_PATH), video_file, 'video/mp4')
                        }
                        
                        # 'data' é para campos de formulário, onde o 'metadata' é uma string JSON
                        data = {
                            'metadata': json.dumps(video_metadata) # Converte o dicionário de metadados para uma string JSON
                        }
                        
                        # Cabeçalhos para autenticação (para o mock, use 'X-User-Id')
                        # EM PRODUÇÃO, VOCÊ USARIA 'Authorization': 'Bearer SEU_TOKEN_JWT'
                        headers = {
                            'X-User-Id': USER_ID_FOR_TEST 
                            # 'Authorization': 'Bearer seu_token_firebase_aqui' 
                        }

                        logger.info(f"Tentando enviar '{VIDEO_FILE_PATH}' para {self.UPLOAD_URL}...")
                        logger.info(f"Com metadados: {json.dumps(video_metadata, indent=2)}")

                        # Faz a requisição POST
                        response = requests.post(self.UPLOAD_URL, files=files, data=data, headers=headers)

                        # --- Tratamento da Resposta ---
                        if response.status_code == 201:
                            logger.info("\nUpload bem-sucedido!")
                            logger.info("Resposta do servidor:")
                            logger.info(json.dumps(response.json(), indent=2))
                        else:
                            logger.info(f"\nErro no upload: Código de status {response.status_code}")
                            logger.info("Resposta do servidor:")
                            try:
                                logger.info(json.dumps(response.json(), indent=2))
                            except json.JSONDecodeError:
                                logger.info(response.text) # Se a resposta não for JSON
                            logger.info("\nCertifique-se de que seu servidor Flask está rodando e o endpoint está acessível.")
                            logger.info("Verifique também se o 'USER_ID_FOR_TEST' e o 'UPLOAD_URL' estão corretos.")

                except FileNotFoundError:
                    logger.info(f"Erro: O arquivo '{VIDEO_FILE_PATH}' não foi encontrado.")
                except requests.exceptions.ConnectionError:
                    logger.info("Erro de conexão: O servidor não está acessível.")
                    logger.info("Certifique-se de que o backend Flask está rodando em 'http://localhost:5000'.")
                except Exception as e:
                    logger.info(f"Ocorreu um erro inesperado: {e}")


                for i in range(10):

                    self.debugg_webhook(self.api_key, "info", f"🎥 Inicializando Upload de video vertical para Tiktok")
                    # os.chdir(os.path.join(os.path.dirname(__file__), "TiktokAutoUploader_TESTEE"))        
                    logger.info(f"secondsScheduleTiktokVideo? {self.secondsScheduleTiktokVideo}")
                    schedule_time_tiktok = int(self.secondsScheduleTiktokVideo)
                    logger.info(f"schedule_time_tiktok? {schedule_time_tiktok}")
                    try: 

                        flag = tiktok.upload_video(WEBHOOK_URL=self.WEBHOOK_URL, 
                                            api_key=self.api_key, 
                                            session_user_cookie=self.TiktokAccountCookies, 
                                            video=output_video_convert, 
                                            title=texto_pra_titulo, 
                                            schedule_time=schedule_time_tiktok, 
                                            webhook=True
                                        )
                        if flag == True:

                            self.debugg_webhook(self.api_key, "info", f"✅ Upload de {title} para tiktok foi um sucesso !")

                            break


                        # time.sleep(3)  

                    except Exception as errupload1:
                        logger.info(f"errupload1 {errupload1}")


            # Monta o dicionário com caminho e metadados
            video_info = {
                "id": idx,
                "titulo": title,
                "descricao": desc,
                "hashtags": hashtags_origin,
                "timestamp_inicio": ts_inicio,
                "timestamp_fim": ts_fim,
                "caminho_arquivo": output_video_subtittle_final,
                "name_score": name_score,
                "name_project": name_project,
                "justificativa": justificativa,
                "gancho_sugerido": gancho_sugerido,
                "sentimento_principal": sentimento_principal,
                "potencial_de_viralizacao": potencial_de_viralizacao,
                "sugestao_de_titulo_curto": sugestao_de_titulo_curto
            }

            list_videos.append(video_info)

            logger.info(f"list_videos {list_videos}")
            # contador_de_Cortes_criados += 1
        
        logger.info(f"Todos os cortes foram criados")

        logger.info(f"list_videos {list_videos}")
        # self.Update_To_Status_Completed(self.inicio)
        return list_videos

    async def Autonomous_Analysis_Test(self):

        list_videos = [{'id': 1, 'titulo': 'Impacto das Taxas na Geração de Empregos', 'descricao': 'Este trecho destaca a importância do equilíbrio na tributação para manter empregos e a justiça fiscal, abordando temas atuais de política econômica.', 'hashtags': ['LuizaHelenaTrajano', 'impostos', 'empregos', 'justiça fiscal', 'Brasil'], 'timestamp_inicio': '00:01:30', 'timestamp_fim': '00:02:10', 'caminho_arquivo': 'c:\\Users\\Media Cuts DeV\\Downloads\\HomeServer\\HomeServer\\internalserver\\Studio\\WorkEnvironment\\Process\\Realtime_Cuts\\Cuts\\Impacto_das_Taxas_na_Geracao_de_Empregos\\CutsCreate\\Impacto_das_Taxas_na_Geracao_de_Empregos.mp4', 'name_score': 8.0, 'name_project': 'A VERDADE sobre a TAXAÇÃO do Governo Lula com Luiza Helena Trajano', 'justificativa': 'Este trecho apresenta uma discussão clara e relevante sobre educação fiscal e impacto na geração de empregos, com uma linguagem acessível.', 'gancho_sugerido': 'Você sabe como a taxação pode estar impactando seus empregos?', 'sentimento_principal': 'informativo', 'potencial_de_viralizacao': 8, 'sugestao_de_titulo_curto': 'Como impostos afetam seu emprego'}, {'id': 2, 'titulo': 'A importância das pequenas empresas na economia brasileira', 'descricao': 'Luiza Trajano enfatiza o papel das pequenas e médias empresas na sustentação do emprego e na economia, destacando a responsabilidade social do setor.', 'hashtags': ['LuizaHelenaTrajano', 'pequenasempresas', 'empregos', 'economiaBrasil'], 'timestamp_inicio': '00:02:20', 'timestamp_fim': '00:03:00', 'caminho_arquivo': 'c:\\Users\\Media Cuts DeV\\Downloads\\HomeServer\\HomeServer\\internalserver\\Studio\\WorkEnvironment\\Process\\Realtime_Cuts\\Cuts\\A_importancia_das_pequenas_empresas_na_economia_brasileira\\CutsCreate\\A_importancia_das_pequenas_empresas_na_economia_brasileira.mp4', 'name_score': 9.0, 'name_project': 'A VERDADE sobre a TAXAÇÃO do Governo Lula com Luiza Helena Trajano', 'justificativa': 'Este trecho reforça uma perspectiva crucial sobre o papel das pequenas empresas, gerando empatia e conscientização.', 'gancho_sugerido': 'Você conhece o verdadeiro motor da economia brasileira?', 'sentimento_principal': 'relevância', 'potencial_de_viralizacao': 9, 'sugestao_de_titulo_curto': 'Pequenas empresas: os verdadeiros motores do Brasil'}, {'id': 3, 'titulo': 'A luta contra a desigualdade e o papel do Brasil', 'descricao': 'Trajano discute a responsabilidade de todos na luta contra a desigualdade social, com foco na história de injustiça e na necessidade de oportunidades para todos.', 'hashtags': ['LuizaHelenaTrajano', 'desigualdade', 'oportunidades', 'justiça social'], 'timestamp_inicio': '00:03:40', 'timestamp_fim': '00:04:20', 'caminho_arquivo': 'c:\\Users\\Media Cuts DeV\\Downloads\\HomeServer\\HomeServer\\internalserver\\Studio\\WorkEnvironment\\Process\\Realtime_Cuts\\Cuts\\A_luta_contra_a_desigualdade_e_o_papel_do_Brasil\\CutsCreate\\A_luta_contra_a_desigualdade_e_o_papel_do_Brasil.mp4', 'name_score': 7.0, 'name_project': 'A VERDADE sobre a TAXAÇÃO do Governo Lula com Luiza Helena Trajano', 'justificativa': 'Um momento de reflexão importante, com potencial de engajamento emocional e de conscientização social.', 'gancho_sugerido': 'Você sabia que a história do Brasil ainda carrega desigualdades profundas?', 'sentimento_principal': 'comovente', 'potencial_de_viralizacao': 7, 'sugestao_de_titulo_curto': 'Desigualdade no Brasil: uma batalha por justiça'}]
     
        logger.info(f"list_videos {list_videos}")
        return list_videos


    async def Analyse_Vertical_and_Horizontal(
                    self, 
                    nome_rename_final,
                    output_miniatura,
                    video_id,
                    thumbnail_url,
                    project_key
                ):

            srt_file_content = await self.Analyse_Vertical(
                nome_rename_final,
                output_miniatura,
                video_id,
                thumbnail_url,
                project_key
            )

            await self.Analyse_Horizontal(
                nome_rename_final,
                output_miniatura,
                video_id,
                thumbnail_url,
                project_key,
                srt_file_content
            )
            
    async def Analyse_Horizontal(self, 
                      nome_rename_final,
                      output_miniatura,
                      video_id,
                      thumbnail_url,
                      project_key,
                      srt_file_content=""
                    ):
        print("Inicializando a análise com o Agent...")
        self.debugg_webhook(self.api_key, "info", "Inicializando a análise com o Agent...")
        if srt_file_content == "":

            print(f"nome_rename_final: {nome_rename_final}\n")
            trasncript_srt, audio_ = self.transcrever_audio(nome_rename_final, linux_env_flag=self.linux_env)
            print(f"trasncript_srt: {trasncript_srt}\n")

            try:
                with open(trasncript_srt, encoding='utf-8') as f:
                    srt_file_content = f.read()
            except UnicodeDecodeError:
                with open(trasncript_srt, encoding='latin1') as f:
                    srt_file_content = f.read()


        url = f'https://www.youtube.com/watch?v={video_id}'
        decription_content = obter_descricao(url)
        tags_do_video = obter_tags(url)
        # 
        try:
            duracao_total_seconds = get_duration_video(video_path=nome_rename_final)
            duracao_total = format_seconds(seconds=duracao_total_seconds)
        except Exception as e:
            print(f"e: {e}")
        resposta_ia = await self.Curation_Horizontal(
                range_array="2 a 5",
                range_seconds=(300, 240, 480),
                nome_do_canal=self.canal_do_yt,
                titulo_original=self.lastlongvideotitle,
                tags_do_video=tags_do_video,
                duracao_total=duracao_total,
                srt_file_content=srt_file_content,
                decription_content=decription_content,
            
            )

        lista_de_videos_horizontais = await self.Autonomous_Analysis_Horizontal(
                resposta_ia,  
                thumbnail_url,
                nome_rename_final,
                project_key
                )
        print(f"lista_de_videos_horizontais {lista_de_videos_horizontais}")

    async def Analyse_Vertical(self, 
                      nome_rename_final,
                      output_miniatura,
                      video_id,
                      thumbnail_url,
                      project_key
                    ):
        logger.info("Inicializando a análise com o Agent...")
        self.debugg_webhook(self.api_key, "info", "Inicializando a análise com o Agent...")
        self.update_status_progress(5, project_key)
        logger.info(f"nome_rename_final: {nome_rename_final}\n")
        trasncript_srt, audio_ = self.transcrever_audio(nome_rename_final, linux_env_flag=self.linux_env)
        logger.info(f"trasncript_srt: {trasncript_srt}\n")

        try:
            with open(trasncript_srt, encoding='utf-8') as f:
                srt_file_content = f.read()
        except UnicodeDecodeError:
            with open(trasncript_srt, encoding='latin1') as f:
                srt_file_content = f.read()


        url = f'https://www.youtube.com/watch?v={video_id}'
        decription_content = obter_descricao(url)
        tags_do_video = obter_tags(url)
        self.update_status_progress(15, project_key)
        try:
            duracao_total_seconds = get_duration_video(video_path=nome_rename_final)
            duracao_total = format_seconds(seconds=duracao_total_seconds)
        except Exception as e:
            print(f"e: {e}")
        resposta_ia = await self.Curation(
                # range_array="3 a 6",
                range_seconds=self.Cutting_seconds,
                nome_do_canal=self.canal_do_yt,
                titulo_original=self.lastlongvideotitle,
                tags_do_video=tags_do_video,
                duracao_total=duracao_total,
                srt_file_content=srt_file_content,
                decription_content=decription_content,
            )
        self.update_status_progress(25, project_key)
        cprint("🔑 Studio - Inicialize loop for cuts")
        self.debugg_webhook(self.api_key, "info", f"🎞️ Recortando os melhores trechos analisados por Curadoria de IA !")
        contador_de_Cortes_criados = 0 
        contador_de_status_progress = 25
        for idx, corte in enumerate(resposta_ia, start=1):
            title = corte["titulo"]
            desc = corte["descricao"]
            hashtags_origin = corte["hashtags"]
            ts_inicio = corte["timestamp_inicio"] 
            ts_fim    = corte["timestamp_fim"]    
            name_score = corte["name_score"]    
            name_project = corte["name_project"]    
            justificativa = corte["justificativa"]
            gancho_sugerido = corte["gancho_sugerido"]
            sentimento_principal = corte["sentimento_principal"]
            potencial_de_viralizacao = corte["potencial_de_viralizacao"]
            sugestao_de_titulo_curto = corte["sugestao_de_titulo_curto"]
            self.debugg_webhook(self.api_key, "info", f"""🔍 Formatando Hashtags""")
            hashtags = MediaCutsStudio_instance.formatar_hashtags(hashtags_origin)
            hashtags_for_sheduler = MediaCutsStudio_instance.formatar_hashtags(hashtags_origin, formato='virgula')
            
            self.send_to_webhook(self.api_key, "Mode", f"Shortify - Date - AI Curation", "yellow")
            self.send_to_webhook(self.api_key, "cuts_duration", f"{ts_inicio}/{ts_fim}", "green")
            self.send_to_webhook(self.api_key, "mediabase", f"{title}", "yellow")

            Informacoesdocorteviral = f"""
📝 Informacoes do corte viral                         
Name Project {name_project}
Titulo {title}
Descricao {desc}
Hashtags Origin {hashtags_origin}
Hashtags {hashtags}
Minutagem de Inicio {ts_inicio}
Minutagem de Fim {ts_fim}
Name Score: {name_score}
Justificativa: {justificativa}
Gancho Sugerido: {gancho_sugerido}
Sentimento Principal: {sentimento_principal}
Potencial De Viralizacao: {potencial_de_viralizacao}
Sugestao De Titulo Curto: {sugestao_de_titulo_curto}

            
                                
            """

            cprint(Informacoesdocorteviral, "green")
            self.debugg_webhook(self.api_key, "info", Informacoesdocorteviral)

            texto_com_espacos = MediaCutsStudio_instance.add_line_breaks(f"{title}").replace(":", "") 
            texto_pra_titulo2 = f"{title}\n {hashtags}"
            
            texto_pra_titulo = f" "

            # if self.editiontheme == "Thumbnail Vertical Fusion":
            #     texto_pra_titulo = f"{sugestao_de_titulo_curto}\n {hashtags}"



            cprint("📝 Studio - Creating names for cuts")
            self.debugg_webhook(self.api_key, "info", "📂 Inicializando Pastas")

            texto_sem_espacos = MediaCutsStudio_instance.normalize_find_mp4(title)
            texto_sem_espacos_shortest = MediaCutsStudio_instance.normalize_find_mp4(sugestao_de_titulo_curto)
            path_create = os.path.abspath(os.path.join(diretorio_script, "WorkEnvironment", "Process", "Realtime_Cuts", 'Cuts', f'{texto_sem_espacos}'))
            path_create_2 = os.path.abspath(os.path.join(path_create, "CutsCreate"))
            VideosDirPath2 = os.path.abspath(os.path.join(path_create, "CutsDirPath"))
            output_video_converter = os.path.abspath(os.path.join(path_create, "CutsConverter"))
            output_folder = os.path.abspath(os.path.join(path_create, "CutsCreate"))


            os.makedirs(output_folder, exist_ok=True)
            os.makedirs(path_create, exist_ok=True)
            os.makedirs(path_create_2, exist_ok=True)
            os.makedirs(VideosDirPath2, exist_ok=True)
            os.makedirs(output_video_converter, exist_ok=True)

            
            audio_output = os.path.join(output_folder, f"audio_video_vertical_{contador_de_Cortes_criados + 1}.wav")
            audio_output_windows = os.path.join(output_folder,  f"audio_video_vertical_{contador_de_Cortes_criados + 1}.wav")
            trasncript_srt_windows = os.path.join(path_create,  f"audio_video_vertical_{contador_de_Cortes_criados + 1}.srt")
            audio_srt = os.path.join(output_folder, f"audio_video_vertical_{contador_de_Cortes_criados + 1}.srt")
            if self.linux_env == True:
                watermark_image_path = f"/app/Studio/Utils/watermask2.png"
                audio_ass_windows = f"/app/Studio/WorkEnvironment/Process/Realtime_Cuts/Cuts/{texto_sem_espacos}/CutsCreate/audio_video_vertical_{contador_de_Cortes_criados + 1}.ass"
            if self.linux_env == False:
                watermark_image_path = f"Utils/watermask2.png"
                audio_ass_windows = f"WorkEnvironment/Process/Realtime_Cuts/Cuts/{texto_sem_espacos}/CutsCreate/audio_video_vertical_{contador_de_Cortes_criados + 1}.ass"
            
            audio_ass_windows2 = os.path.join(output_folder,  f"audio_video_vertical_{contador_de_Cortes_criados + 1}.ass")

            output_processar_video = os.path.join(output_folder, f"video_vertical_{contador_de_Cortes_criados + 1}.mp4")
            output_video_subtittle = os.path.join(output_folder, f"{texto_sem_espacos_shortest}_subtitle.mp4")
            output_video_subtittle_watermask = os.path.join(output_folder, f"{texto_sem_espacos_shortest}.mp4")
            output_video_subtittle_ad = os.path.join(output_folder, f"video_vertical_{contador_de_Cortes_criados + 1}_subtitle_ad.mp4")
            output_video_convert = os.path.abspath(os.path.join(diretorio_script, "WorkEnvironment", "Process", "Realtime_Cuts", 'Cuts', f'{texto_sem_espacos}' ,  f"video_vertical_{contador_de_Cortes_criados + 1}_subtitles.mp4"))
            output_filename = os.path.join(output_folder, f"subclip_vertical_{contador_de_Cortes_criados + 1}.mp4")


            cprint("✂️ Studio - Creating Subclip")
            self.debugg_webhook(self.api_key, "info", "✂️ Studio - Creating Subclip")

            subclip_filename = MediaCutsStudio_instance.generate_subclip_with_ffmpeg_ai_curation(
                                                                video_input=nome_rename_final,
                                                                start_time=ts_inicio,
                                                                end_time=ts_fim,
                                                                output_filename=output_filename
                                                                )

            self.debugg_webhook(self.api_key, "info", "🎵 Studio - Extracting Audio")


            for i in range(5):

                try:
                    audio_linux = audio_output_windows
                    
                    self.debugg_webhook(self.api_key, "info", "🗣️ Studio - Transcribing Audio")

                    resultado, total_time_str = self.transcriber.main(
                        path_videofile=subclip_filename, 
                        path_file_audio=audio_linux
                                    
                        )

                    break
                except Exception as err:
                    audio_linux = audio_output_windows
                    continue
        
            self.debugg_webhook(self.api_key, "info", "📐 Adaptando o arquivo de transcricao")

            MediaCutsStudio_instance.adpte_srt_file(file_path=audio_srt)

            self.debugg_webhook(self.api_key, "info", "📐 Convertendo o arquivo de transcricao para modo profissional")

            flag = self.transcriber.convert_to_ass(subtitlesrt=audio_srt, subtitleass=audio_ass_windows2)
            cprint(flag, "green" if flag else "red")

            self.debugg_webhook(self.api_key, "info", "📐 Definindo o estilo da legenda do corte")

            novo_estilo = {
                'Fontname': self.CaptionsFontName,
                'Fontsize': self.CaptionsFontsize,
                'PrimaryColour': self.CaptionsPrimaryColour, 
                'SecondaryColour': self.CaptionsSecondaryColour, 
                'OutlineColour': self.CaptionsOutlineColour,  
                'BackColour': self.CaptionsBackColour, 
                'Bold': self.CaptionsBold, 
                'Italic': self.CaptionsItalic, 
                'Underline': self.CaptionsUnderline, 
                'Outline': self.CaptionsOutline,  
                'Shadow': self.CaptionsShadow, 
                'Alignment': self.CaptionsAlignment  
            }

        

            cprint("\n💾 Studio - Saving new subtitles")
            self.transcriber.modify_ass_styles(audio_ass_windows, novo_estilo)
            
            
            self.debugg_webhook(self.api_key, "info", "📐 Aplicando efeitos de edicao de legenda")

            legendstheme_str = f"{self.legendstheme}"
            if legendstheme_str.startswith("Revelation Effect"):
                
                self.debugg_webhook(self.api_key, "info", "📐 Aplicando efeito Revelation Effect")

                MediaCutsStudio_instance.apply_reveal_effect(
                    ass_file_path=audio_ass_windows,
                    initial_color=self.CaptionsRevealEffectInitialColor,
                    final_color=self.CaptionsRevealEffectFinalColor
                )

            elif legendstheme_str.startswith("Typewriter Effect"):
                
                self.debugg_webhook(self.api_key, "info", "📐 Aplicando efeito Typewriter Effect")

                MediaCutsStudio_instance.apply_typewriter_effect_fixed(
                    audio_ass_windows, 
                    char_reveal_time=37
                    )

            cprint("\n Studio - Grouping Subtitles in Video")
            self.debugg_webhook(self.api_key, "info", "🎥 Aplicando o efeito de edicao Vertical Fusion")


            if self.editiontheme == "Thumbnail Vertical Fusion":
                
                MediaCutsStudio_instance.theme_VerticalFusion(
                    video_cima=subclip_filename,
                    imagem_baixo=output_miniatura,
                    fonte=self.SubtitleFontName,
                    texto_drawtext=texto_com_espacos,
                    ass_file=audio_ass_windows,
                    saida=output_video_subtittle,
                    CaptionsAlignment=self.CaptionsAlignment,
                    SubtitleFontsize=self.SubtitleFontsize,
                    SubtitleColor=self.SubtitleColor,
                    SubtitleVerticalReference=self.SubtitleVerticalReference
                )

            elif self.editiontheme == "AI Vertical Fusion":


                if not Path(self.YOLO_MODEL).exists():
                    print(f"AVISO: O modelo YOLO '{self.YOLO_MODEL}' não foi encontrado.")
                    print(f"Tentando baixar '{self.YOLO_MODEL}'...")
                    try:
                        YOLO(self.YOLO_MODEL) 
                        print(f"Modelo '{self.YOLO_MODEL}' baixado com sucesso.")
                    except Exception as e:
                        print(f"ERRO: Falha ao baixar o modelo YOLO '{self.YOLO_MODEL}'. Por favor, baixe-o manualmente.")
                        print(f"Você pode tentar 'pip install ultralytics --upgrade' e depois executar 'python -c \"from ultralytics import YOLO; YOLO(\'{self.YOLO_MODEL}\')\"'")
                        exit()
                try:
                    reframe_processor = AutoReframe(
                        ass_file_path=audio_ass_windows,
                        input_video_path=subclip_filename,
                        output_video_mp4=output_video_subtittle,
                        text_overlay=texto_pra_titulo,
                        CONF_MIN=0.77,
                        min_move_pixels=5000,
                        stability_threshold_frames=30,
                        padding_x_ratio_left = 0.0,   
                        padding_x_ratio_right = 0.0, 
                        padding_y_ratio_top = 0.0,   
                        padding_y_ratio_bottom = 0.0,
                        # fixed_padding_x_left = 70,   
                        # fixed_padding_x_right = 70,    
                        # fixed_padding_y_top = 150, 
                        # fixed_padding_y_bottom = 15,
                        font_path=self.SubtitleFontName,
                        captions_alignment=self.CaptionsAlignment,
                        captions_fontsize=self.CaptionsFontsize,
                        captions_color=self.CaptionsColor,
                        subtitle_fontsize=self.SubtitleFontsize,
                        subtitle_fontcolor=self.SubtitleColor,
                        SubtitleVerticalReference=self.SubtitleVerticalReference,

                        yolo_model_path=self.YOLO_MODEL,
                        show_preview=show_preview,
                        dockerffmpegGPU=dockerffmpegGPU,
                        task_id_db_str=self.task_id_db_str,

                    )
                    reframe_processor.run()
                except Exception as e:
                    print(f"Um erro inesperado ocorreu: {e}")

            api_key_str = str(self.api_key)
            if api_key_str.startswith("apikey-startup"):
                add_watermark(
                    input_video=output_video_subtittle,
                    output_video=output_video_subtittle_watermask,
                    watermark_image=watermark_image_path,
                    overlay_position="150:150", 
                    watermark_width=350,  
                    start_time_seconds=5, # A marca d'água aparecerá após 5 segundos
                    gpu=dockerffmpegGPU
                )
            else:
                output_video_subtittle_watermask = output_video_subtittle

            # cprint("\n🔄 Converting video to MP4")
            # self.debugg_webhook(self.api_key, "info", "🎥 Convertendo para codec mp4")


            # flag = MediaCutsStudio_instance.convert_to_mp4_codec_with_ffmpeg(
            #         input_video=output_video_subtittle,
            #         output_video_mkv=output_video_convert
            #         )

            # cprint("\n🎉 Conversion Complete!", "green")
            # self.debugg_webhook(self.api_key, "info", "🎉 Conversao para mp4 Completa !")

            tempo_final = time.time()
            minutos, segundos = divmod(int(tempo_final - self.inicio), 60)
            cprint(f"\n ⏳ Time taken to create vertical video: {minutos}m {segundos}")
            self.debugg_webhook(self.api_key, "info", f"⏳ Tempo para criar video vertical {minutos}m {segundos}")
            filename = os.path.basename(output_video_subtittle_watermask).replace(".mp4", "")
            safe_project_name = secure_filename(self.title_origin).replace("-", "")
            safe_project_name_filter = re.sub(r'[^0-9A-Za-z_-]', '', safe_project_name)
            ref_projects_metadata = db.reference(f'projects/{self.user_email}/{safe_project_name_filter}/metadata/{filename}', app=self.appdocs)
            # 
            video_metadata_sheduler = {
                "filename": os.path.basename(output_video_subtittle_watermask),
                "title": sugestao_de_titulo_curto,
                "description": desc,
                "tags": hashtags_for_sheduler,
                "schedule_time": "None",
                "social_networks": ["youtube", "tiktok"],
            }
            ref_projects_metadata.update(video_metadata_sheduler)
        
            VIDEO_FILE_PATH = output_video_subtittle_watermask
            USER_ID_FOR_TEST = self.user_email

            video_metadata = {
                "projectName": self.title_origin,
                "title": sugestao_de_titulo_curto,
                "description": desc,
                "hashtags": hashtags_origin,
                "minutagemdeInicio": ts_inicio,
                "minutagemdeFim": ts_fim,
                "urltumbnail": thumbnail_url,
                "justificativa": justificativa,
                "sentimento_principal": sentimento_principal,
                "potencial_de_viralizacao": potencial_de_viralizacao
            }

            # --- Verificações Iniciais ---
            if not os.path.exists(VIDEO_FILE_PATH):
                cprint(f"Erro: O arquivo '{VIDEO_FILE_PATH}' não foi encontrado.")
                cprint("Por favor, crie um arquivo MP4 com este nome ou ajuste o caminho.")
                exit()

            # --- Preparação da Requisição ---

            # Abre o arquivo de vídeo em modo binário
            try:
                with open(VIDEO_FILE_PATH, 'rb') as video_file:
                    # 'files' é para o arquivo, 'data' é para os outros campos (incluindo o JSON de metadados)
                    # O 'files' espera um dicionário onde a chave é o nome do campo ('file') e o valor é uma tupla
                    # (nome_do_arquivo, objeto_arquivo_aberto, content_type)
                    files = {
                        'file': (os.path.basename(VIDEO_FILE_PATH), video_file, 'video/mp4')
                    }
                    
                    # 'data' é para campos de formulário, onde o 'metadata' é uma string JSON
                    data = {
                        'metadata': json.dumps(video_metadata) # Converte o dicionário de metadados para uma string JSON
                    }
                    
                    # Cabeçalhos para autenticação (para o mock, use 'X-User-Id')
                    # EM PRODUÇÃO, VOCÊ USARIA 'Authorization': 'Bearer SEU_TOKEN_JWT'
                    headers = {
                        'X-User-Id': USER_ID_FOR_TEST 
                        # 'Authorization': 'Bearer seu_token_firebase_aqui' 
                    }

                    cprint(f"Tentando enviar '{VIDEO_FILE_PATH}' para {self.UPLOAD_URL}...")
                    cprint(f"Com metadados: {json.dumps(video_metadata, indent=2)}")

                    # Faz a requisição POST
                    response = requests.post(self.UPLOAD_URL, files=files, data=data, headers=headers)

                    # --- Tratamento da Resposta ---
                    if response.status_code == 201:
                        cprint("\nUpload bem-sucedido!")
                        cprint("Resposta do servidor:")
                        print(json.dumps(response.json(), indent=2))
                    else:
                        cprint(f"\nErro no upload: Código de status {response.status_code}")
                        cprint("Resposta do servidor:")
                        try:
                            print(json.dumps(response.json(), indent=2))
                        except json.JSONDecodeError:
                            print(response.text) # Se a resposta não for JSON
                        cprint("\nCertifique-se de que seu servidor Flask está rodando e o endpoint está acessível.")
                        cprint("Verifique também se o 'USER_ID_FOR_TEST' e o 'UPLOAD_URL' estão corretos.")

            except FileNotFoundError:
                print(f"Erro: O arquivo '{VIDEO_FILE_PATH}' não foi encontrado.")
            except requests.exceptions.ConnectionError:
                print("Erro de conexão: O servidor não está acessível.")
                print("Certifique-se de que o backend Flask está rodando em 'http://localhost:5000'.")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")



            contador_de_status_progress += 3
            self.update_status_progress(contador_de_status_progress, project_key)
            # break

        tempo_final = time.time()
        minutos, segundos = divmod(int(tempo_final - self.inicio), 60)
        cprint(f"\n ⏳ Todos os cortes foram criados: {minutos}m {segundos}")
        self.debugg_webhook(self.api_key, "info", f"⏳ Todos os cortes foram criados {minutos}m {segundos}")
        self.update_status_progress(100, project_key)

        return srt_file_content
        # self.Update_To_Status_Completed(self.inicio)


    async def Analyse_TEST(
                self,
                canal_do_yt, 
                lastlongvideotitle,
                new_video_ids,
                output_miniatura,
                nome_rename_final,
                srt_file_path
                
                

                
                ):

        print("Inicializando a análise com o Agent...")
        self.debugg_webhook(self.api_key, "info", "Inicializando a análise com o Agent...")
        print(f"Titulo do Vídeo: {lastlongvideotitle}")
        self.debugg_webhook(self.api_key, "info", f"Titulo do Vídeo: {lastlongvideotitle}")
        print(f"Canal do Yt: {canal_do_yt}")
        self.debugg_webhook(self.api_key, "info", f"Canal do Yt: {canal_do_yt}")

        self.configure_env()


        # nome_rename_final, output_miniatura, new_video_ids = self.download_yt_video_by_title(
        #         canal_do_yt, 
        #         lastlongvideotitle
        #         )
        
        # print(f"nome_rename_final: {nome_rename_final}\n")
        # trasncript_srt = self.transcrever_audio(nome_rename_final, linux_env_flag=self.linux_env)
        # print(f"trasncript_srt: {trasncript_srt}\n")
    #    try:
    #         with open(trasncript_srt, encoding='utf-8') as f:
    #             srt_file_content = f.read()
    #     except UnicodeDecodeError:
    #         with open(trasncript_srt, encoding='latin1') as f:
    #             srt_file_content = f.read()

        with open(srt_file_path, "r", encoding='utf-8') as srt_file:
            srt_file_content = srt_file.read()

        url = f'https://www.youtube.com/watch?v={new_video_ids}'
        decription_content = obter_descricao(url)
        tags_do_video = obter_tags(url)


        try:
            duracao_total_seconds = get_duration_video(video_path=nome_rename_final)
        except Exception as e:
            print(f"e: {e}")
        cprint(f"🔑 Studio - {duracao_total_seconds}")
        duracao_total = format_seconds(seconds=duracao_total_seconds)
        cprint(f"🔑 Studio - {duracao_total}")


        resposta_ia = await self.Curation(
                nome_do_canal=canal_do_yt,
                titulo_original=lastlongvideotitle,
                tags_do_video=tags_do_video,
                duracao_total=duracao_total,
                srt_file_content=srt_file_content,
                decription_content=decription_content,
            )
        
        cprint("🔑 Studio - Inicialize loop for cuts")
        self.debugg_webhook(self.api_key, "info", f"🎞️ Recortando os melhores trechos analisados por Curadoria de IA !")
        contador_de_Cortes_criados = 0
        for idx, corte in enumerate(resposta_ia, start=1):
            title = corte["titulo"]
            desc = corte["descricao"]
            hashtags_origin = corte["hashtags"]
            ts_inicio = corte["timestamp_inicio"] 
            ts_fim    = corte["timestamp_fim"]    
            name_score = corte["name_score"]    
            name_project = corte["name_project"]    
            justificativa = corte["justificativa"]
            gancho_sugerido = corte["gancho_sugerido"]
            sentimento_principal = corte["sentimento_principal"]
            potencial_de_viralizacao = corte["potencial_de_viralizacao"]
            sugestao_de_titulo_curto = corte["sugestao_de_titulo_curto"]
            self.debugg_webhook(self.api_key, "info", f"""🔍 Formatando Hashtags""")
            hashtags = MediaCutsStudio_instance.formatar_hashtags(hashtags_origin)
            
            Informacoes= f"""
📝 Informacoes do corte viral                         
Name Project {name_project}
Titulo {title}
Descricao {desc}
Hashtags Origin {hashtags_origin}
Hashtags {hashtags}
Minutagem de Inicio {ts_inicio}
Minutagem de Fim {ts_fim}
Name Score: {name_score}
Justificativa: {justificativa}
Gancho Sugerido: {gancho_sugerido}
Sentimento Principal: {sentimento_principal}
Potencial De Viralizacao: {potencial_de_viralizacao}
Sugestao De Titulo Curto: {sugestao_de_titulo_curto}

            
            """
            cprint(Informacoes, "green")
            self.debugg_webhook(self.api_key, "info", Informacoes)

            texto_com_espacos = MediaCutsStudio_instance.add_line_breaks(f"{title}").replace(":", "") 
            texto_pra_titulo = f"{title}\n {hashtags}"
            texto_pra_titulo2 = f"{sugestao_de_titulo_curto}\n {hashtags}"


            cprint(F"🔍 texto_pra_titulo - {texto_pra_titulo}")
            cprint(F"🔍 texto_pra_titulo2 - {texto_pra_titulo2}")

            # self.debugg_webhook(self.api_key, "info", "📂 Inicializando Pastas")

            # texto_sem_espacos = MediaCutsStudio_instance.normalize_find_mp4(title)
            # path_create = os.path.abspath(os.path.join(diretorio_script, "WorkEnvironment", "Process", "Realtime_Cuts", 'Cuts', f'{texto_sem_espacos}'))
            # path_create_2 = os.path.abspath(os.path.join(path_create, "CutsCreate"))
            # VideosDirPath2 = os.path.abspath(os.path.join(path_create, "CutsDirPath"))
            # output_video_converter = os.path.abspath(os.path.join(path_create, "CutsConverter"))
            # output_folder = os.path.abspath(os.path.join(path_create, "CutsCreate"))


            # os.makedirs(output_folder, exist_ok=True)
            # os.makedirs(path_create, exist_ok=True)
            # os.makedirs(path_create_2, exist_ok=True)
            # os.makedirs(VideosDirPath2, exist_ok=True)
            # os.makedirs(output_video_converter, exist_ok=True)



            # audio_output = os.path.join(output_folder, f"audio_video_vertical_{contador_de_Cortes_criados + 1}.wav")
            # audio_output_windows = os.path.join(output_folder,  f"audio_video_vertical_{contador_de_Cortes_criados + 1}.wav")
            # trasncript_srt_windows = os.path.join(path_create,  f"audio_video_vertical_{contador_de_Cortes_criados + 1}.srt")
            # audio_srt = os.path.join(output_folder, f"audio_video_vertical_{contador_de_Cortes_criados + 1}.srt")
            # if self.linux_env == True:
            #     audio_ass_windows = f"/app/Studio/WorkEnvironment/Process/Realtime_Cuts/Cuts/{texto_sem_espacos}/CutsCreate/audio_video_vertical_{contador_de_Cortes_criados + 1}.ass"
            # if self.linux_env == False:
            #     audio_ass_windows = f"WorkEnvironment/Process/Realtime_Cuts/Cuts/{texto_sem_espacos}/CutsCreate/audio_video_vertical_{contador_de_Cortes_criados + 1}.ass"
            
            # audio_ass_windows2 = os.path.join(output_folder,  f"audio_video_vertical_{contador_de_Cortes_criados + 1}.ass")

            # output_processar_video = os.path.join(output_folder, f"video_vertical_{contador_de_Cortes_criados + 1}.mp4")
            # output_video_subtittle = os.path.join(output_folder, f"video_vertical_{contador_de_Cortes_criados + 1}_subtitle.mp4")
            # output_video_subtittle_watermask = os.path.join(output_folder, f"video_vertical_{contador_de_Cortes_criados + 1}_subtitle_and_watermask.mp4")
            # output_video_subtittle_ad = os.path.join(output_folder, f"video_vertical_{contador_de_Cortes_criados + 1}_subtitle_ad.mp4")
            # output_video_convert = os.path.abspath(os.path.join(diretorio_script, "WorkEnvironment", "Process", "Realtime_Cuts", 'Cuts', f'{texto_sem_espacos}' ,  f"video_vertical_{contador_de_Cortes_criados + 1}_subtitles.mp4"))
            # output_filename = os.path.join(output_folder, f"subclip_vertical_{contador_de_Cortes_criados + 1}.mp4")


            # cprint("✂️ Studio - Creating Subclip")
            # self.debugg_webhook(self.api_key, "info", "✂️ Studio - Creating Subclip")

            # subclip_filename = MediaCutsStudio_instance.generate_subclip_with_ffmpeg(
            #                                                     video_input=nome_rename_final,
            #                                                     start_time=ts_inicio,
            #                                                     duration=ts_fim,
            #                                                     output_filename=output_filename
            #                                                     )

            # self.debugg_webhook(self.api_key, "info", "🎵 Studio - Extracting Audio")

            # transcriber = Audio_Transcriber(
            #                                 model_type="medium", 
            #                                 hash_thread="hash_do_dia",
            #                                 dockerffmpeg=True,
            #                                 webhook=False
            #                             )

            # for i in range(5):

            #     # os.makedirs(path_create, exist_ok=True)
            #     # trasncript_srt_linux = f"/app/Studio/WorkEnvironment/Process/AICuration/Transcript/audio_video_vertical.srt"
            #     try:
            #         audio_linux = audio_output_windows
                    
            #         transcriber.extract_audio_with_ffmpeg(video_input=subclip_filename,
            #                                                         audio_output=audio_linux)

            #         self.debugg_webhook(self.api_key, "info", "🗣️ Studio - Transcribing Audio")

            #         resultado, total_time_str = transcriber.transcrever_audio(
            #             arquivo_audio=audio_linux, 
            #             audio_sliced_path="path_create_2",
            #             vertical_id="hash_do_dia"
            #         )
            #         # return trasncript_srt_windows
            #         break
            #     except Exception as err:
            #         audio_linux = audio_output_windows
            #         continue
        
            # self.debugg_webhook(self.api_key, "info", "📐 Adaptando o arquivo de transcricao")

            # MediaCutsStudio_instance.adpte_srt_file(audio_srt)

            # self.debugg_webhook(self.api_key, "info", "📐 Convertendo o arquivo de transcricao para modo profissional")

            # flag = transcriber.convert_to_ass(path_ffmpeg, audio_srt, audio_ass_windows2)
            # cprint(flag, "green" if flag else "red")

            # self.debugg_webhook(self.api_key, "info", "📐 Definindo o estilo da legenda do corte")

            # novo_estilo = {
            #     'Fontname': self.CaptionsFontName,
            #     'Fontsize': self.CaptionsFontsize,
            #     'PrimaryColour': self.CaptionsPrimaryColour, 
            #     'SecondaryColour': self.CaptionsSecondaryColour, 
            #     'OutlineColour': self.CaptionsOutlineColour,  
            #     'BackColour': self.CaptionsBackColour, 
            #     'Bold': self.CaptionsBold, 
            #     'Italic': self.CaptionsItalic, 
            #     'Underline': self.CaptionsUnderline, 
            #     'Outline': self.CaptionsOutline,  
            #     'Shadow': self.CaptionsShadow, 
            #     'Alignment': self.CaptionsAlignment  
            # }

        
            # cprint("\n💾 Studio - Saving new subtitles")
    
            # transcriber.modify_ass_styles(audio_ass_windows, novo_estilo)
            
            
            # self.debugg_webhook(self.api_key, "info", "📐 Aplicando efeitos de edicao de legenda")


            # if self.legendstheme == "Revelation Effect":
                
            #     self.debugg_webhook(self.api_key, "info", "📐 Aplicando efeito Revelation Effect")

            #     MediaCutsStudio_instance.apply_reveal_effect(
            #         ass_file_path=audio_ass_windows,
            #         initial_color=self.CaptionsRevealEffectInitialColor,
            #         final_color=self.CaptionsRevealEffectFinalColor
            #     )

            # elif self.legendstheme == "Typewriter Effect":
                
            #     self.debugg_webhook(self.api_key, "info", "📐 Aplicando efeito Typewriter Effect")

            #     MediaCutsStudio_instance.apply_typewriter_effect_fixed(
            #         audio_ass_windows, 
            #         char_reveal_time=37
            #         )

            # cprint("\n Studio - Grouping Subtitles in Video")
            # self.debugg_webhook(self.api_key, "info", "🎥 Aplicando o efeito de edicao Vertical Fusion")

            # MediaCutsStudio_instance.theme_VerticalFusion(
            #     video_cima=subclip_filename,
            #     imagem_baixo=output_miniatura,
            #     fonte=self.SubtitleFontName,
            #     texto_drawtext=texto_com_espacos,
            #     ass_file=audio_ass_windows,
            #     saida=output_video_subtittle,
            #     CaptionsAlignment=self.CaptionsAlignment,
            #     SubtitleFontsize=self.SubtitleFontsize,
            #     SubtitleColor=self.SubtitleColor,
            #     SubtitleVerticalReference=self.SubtitleVerticalReference
            # )

            # cprint("\n🔄 Converting video to MP4")
            # self.debugg_webhook(self.api_key, "info", "🎥 Convertendo para codec mp4")


            # flag = MediaCutsStudio_instance.convert_to_mp4_codec_with_ffmpeg(
            #         input_video=output_video_subtittle,
            #         output_video_mkv=output_video_convert
            #         )

            # cprint("\n🎉 Conversion Complete!", "green")
            # self.debugg_webhook(self.api_key, "info", "🎉 Conversao para mp4 Completa !")

            # tempo_final = time.time()
            # minutos, segundos = divmod(int(tempo_final - self.inicio), 60)
            # cprint(f"\n ⏳ Time taken to create vertical video: {minutos}m {segundos}")
            # self.debugg_webhook(self.api_key, "info", f"⏳ Tempo para criar video vertical {minutos}m {segundos}")

            # # Abra em modo binário e leia os bytes puros
            # with open(output_video_convert, "rb") as f:
            #     file_bytes = f.read()

            # # Converte para Base64 (string)
            # b64 = base64.b64encode(file_bytes).decode("utf-8")
            # filename = os.path.basename(output_video_convert)
            # video_payload = {
            #     "title": texto_pra_titulo,
            #     "urltumbnail": output_miniatura,
            #     "descricao": desc,
            #     "hashtags": hashtags_origin,
            #     "minutagemdeInicio": ts_inicio,
            #     "minutagemdeFim": ts_fim,
            #     "filename": filename,
            #     "message": b64 # This is the actual Base64 string
            # }
            # self.send_video_bytes_to_webhook(
            #     self.api_key, 
            #     "video", 
            #     video_payload, 
            #     "yellow"
            # )



                
            # contador_de_Cortes_criados += 1
            # # break
    
    async def download_video_yt(self):
            
        if self.pastedUrl and self.pastedUrl != "":
            logger.info("Modo URL detectado.") 
            title_ = get_video_title_by_url(self.pastedUrl)
            project_key = secure_filename(title_).replace("-", "").replace("....", "").replace("...", "").replace("..", "").replace(".", "").replace("... - ", "").replace('"????????"', '').replace("...__", "_") 
            # self.update_status_progress(10, project_key)
            self.configure_env()

            nome_rename_final, output_miniatura, video_id, thumbnail_url = await self.download_yt_video_by_url(
                self.pastedUrl,
                self.canal_do_yt
            )
            return nome_rename_final, output_miniatura, video_id, thumbnail_url, project_key
        else:
            logger.info("Modo TÍTULO detectado.")
            logger.info(f"self.title_origin {self.title_origin}")
            project_key = secure_filename(self.title_origin).replace("-", "").replace("....", "").replace("...", "").replace("..", "").replace(".", "").replace("... - ", "").replace('"????????"', '').replace("...__", "_") 
            title_origin_db  = self.title_origin
            if title_origin_db == None:
                logger.info(f"erro ? title_origin_db {title_origin_db}")
            logger.info(title_origin_db)

            # self.update_status_progress(10, project_key)

            print(f"Titulo do Vídeo: {self.lastlongvideotitle}")
            self.debugg_webhook(self.api_key, "info", f"Titulo do Vídeo: {self.lastlongvideotitle}")
            print(f"Canal do Yt: {self.canal_do_yt}")
            self.debugg_webhook(self.api_key, "info", f"Canal do Yt: {self.canal_do_yt}")

            self.configure_env()
            
            nome_rename_final, output_miniatura, video_id, thumbnail_url = await self.download_yt_video_by_title(
                    self.canal_do_yt, 
                    self.lastlongvideotitle
                    )
                
            return nome_rename_final, output_miniatura, video_id, thumbnail_url, project_key
        
        return "", "", "", ""
    
    async def download_yt_video_by_url(
        self,
        video_url: str,
        canal_do_yt: str,
    ):
        
        """
        Baixa um único vídeo passado pela URL, renomeia, gera thumbnail
        e retorna os mesmos valores que download_yt_video_by_title.
        """
        from urllib.parse import urlparse, parse_qs



        self.debugg_webhook(self.api_key, "info", f"Iniciando download via URL direta: {video_url}")

        # 1) Extrair o video_id direto da URL (suporta ?v=ID e youtu.be/ID)
        def extract_id(url: str) -> str:
            # https://www.youtube.com/watch?v=ID ou https://youtu.be/ID
            parsed = urlparse(url)
            if parsed.hostname and 'youtu.be' in parsed.hostname:
                return parsed.path.lstrip('/')
            qs = parse_qs(parsed.query)
            return qs.get('v', [None])[0]

        video_id = extract_id(video_url)
        if not video_id:
            raise ValueError(f"Não foi possível extrair o ID da URL: {video_url}")

        # 2) Montar objeto compatível com download_new_videos
        videos = [{'id': video_id}]

        # 3) Chamar download_new_videos diretamente
        new_downloads, new_video_ids, titulo, output_miniatura, thumbnail_url = download_new_videos(
            videos=videos,
            output_dir=self.base_dir,
            channel=canal_do_yt,
            path_ffmpegnotexe=path_ffmpegnotexe,
            linux_env=self.linux_env,
            output_path_=os.path.join(os.path.dirname(__file__),
                                    "WorkEnvironment",
                                    "Process",
                                    "MediaBase"),
            downloaded_videos=[]  # assume nenhum já baixado
        )

        if new_downloads == 0:
            raise Exception(f"Nenhum vídeo novo foi baixado para a URL: {video_url}")

        # 4) Pega o único ID baixado (set com 1 item)
        video_id = next(iter(new_video_ids))

        # 5) Renomeia e retorna exatamente como o download_yt_video_by_title
        nome_rename_final = self.rename_file_mp4(canal_do_yt, titulo)

        self.debugg_webhook(self.api_key, "info", f"Download completo: {titulo}")

        return nome_rename_final, output_miniatura, video_id, thumbnail_url

        

    def update_status_progress(self, number, key):
        self.ref_projects.child(key).update({"progress_percent": f"{number}"})
 
    def send_video_bytes_to_webhook(self, user, type, message_content, cor):
        """Envia uma mensagem para o webhook."""
        try:
            # Construct the payload data correctly
            # For 'video' type, message_content should already be an object: {'filename': '...', 'message': 'base64_string'}
            # For other types, message_content is a string.
            payload_data = {
                "type": type,
                "message": message_content
            }
            
            # The top-level key should be the user (API_KEY)
            requests.post(self.WEBHOOK_URL, json={str(user): payload_data})

        except Exception as e:
            print("Erro ao enviar mensagem para webhook:", e)

    def configure_env(self):
        path_env = os.path.join(diretorio_script, 'Keys', 'keys.env')
        load_dotenv(path_env)

    def debugg_webhook(self, user, type_event, message, cor=None):

        if self.webhook == True:

            tempo_formatado, tempo_total_por_corte = self.get_total_current_time(self.inicio)
            self.send_to_webhook(self.api_key, "timestamp", tempo_formatado)
        
            self.send_to_webhook(user, type_event, message)

    def send_to_webhook(self, user, type, message, cor=None):
        """Envia uma mensagem para o webhook."""
        try:
            requests.post(self.WEBHOOK_URL, json={str(user): {"type": type, "message": message}})
        except Exception as e:
            logger.info(f"Erro ao enviar mensagem para webhook: {e}")

    def get_total_current_time(self, tempo_inicial):
        tempo_final = time.time()
        tempo_gasto = tempo_final - tempo_inicial
        
        tempo_total_por_corte = tempo_gasto
        horas_corte = int(tempo_total_por_corte // 3600)
        minutos_corte = int((tempo_total_por_corte % 3600) // 60)
        segundos_corte = int(tempo_total_por_corte % 60)
        tempo_formatado = f"{horas_corte:02d}:{minutos_corte:02d}:{segundos_corte:02d}"
        return tempo_formatado, tempo_total_por_corte
    
    def formatar_saida(self, texto):
        """Formata o texto de saída para melhor legibilidade no terminal."""
        texto_formatado = textwrap.indent(texto, '> ', predicate=lambda _: True)
        # Em um ambiente como Jupyter Notebook ou Google Colab, a linha abaixo renderizaria o Markdown.
        # No terminal, apenas exibirá o texto.
        # return Markdown(texto_formatado) 
        return texto_formatado

    def transcrever_audio(self, output_processar_video, linux_env_flag: bool):
        # path_ = os.path.join(os.path.dirname(__file__), "WorkEnvironment", "Process", "AICuration", "Transcript")
        # path_create = os.path.abspath(path_)
        # audio_output = os.path.join(path_create, f"audio_video_vertical.wav")
        primeiros_5 = self.task_id_db_str[:5]
        if self.linux_env == True:
            trasncript_srt_linux = f"/app/Studio/WorkEnvironment/Process/AICuration/{self.canal_do_yt}/Transcript/audio_video_vertical_{primeiros_5}.srt"
        elif self.linux_env == False:
            trasncript_srt_linux = f"Studio/WorkEnvironment/Process/AICuration/{self.canal_do_yt}/Transcript/audio_video_vertical_{primeiros_5}.srt"

        path_AIcuration = os.path.abspath(os.path.join(os.path.dirname(__file__), "WorkEnvironment", "Process", "AICuration", f"{self.canal_do_yt}", 'Transcript'))
        os.makedirs(path_AIcuration, exist_ok=True)

        counter_ = 0

        try:
            self.debugg_webhook(self.api_key, "info", f"🗣️ Inicializando Transcritor de Audio")
            if self.linux_env == True:
                audio_2 = f"/app/Studio/WorkEnvironment/Process/AICuration/{self.canal_do_yt}/Transcript/audio_video_vertical_{primeiros_5}.wav"
            elif self.linux_env == False:
                audio_2 = f"Studio/WorkEnvironment/Process/AICuration/{self.canal_do_yt}/Transcript/audio_video_vertical_{primeiros_5}.wav"

            logger.info(f"audio_2 {audio_2}")
            # logger.info("\n Studio - Extracting Audio")
            # self.debugg_webhook(self.api_key, "info", f"🎵 Extraindo Audio do Video")
            # transcriber.extract_audio_with_ffmpeg(video_input=output_processar_video,
            #                                audio_output=audio_2)
            logger.info("\n Studio - Transcribing Audio")

            resultado, total_time_str = self.transcriber.main(
                path_videofile=output_processar_video, 
                path_file_audio=audio_2
                            
                )

            # self.debugg_webhook(self.api_key, "info", f"🗣️ Transcrevendo Audio do video")
            # resultado, total_time_str = transcriber.transcrever_audio(
            #     arquivo_audio=audio_2, 
            # )
            return trasncript_srt_linux, audio_2

        except Exception as err:
            logger.info(f"?????{err}")
            # try:
            #     if os.path.exists(audio_2):
            #         print("O arquivo existe.")
            #         logger.info("\n Studio - Transcribing Audio")
            #         self.debugg_webhook(self.api_key, "info", f"🗣️ Transcrevendo Audio do video")
            #         resultado, total_time_str = transcriber.transcrever_audio(
            #             arquivo_audio=audio_2, 
            #         )
            #         return trasncript_srt_linux

            #     else:
            #         print("O arquivo NÃO existe.")
            # except Exception as e:
            #     print(f"Erro ao verificar o arquivo: {e}")
            # audio_2 = audio_output
            # continue


 
    def create_download_directory(self, base_dir):
        """Cria um diretório para os downloads com base no nome do canal"""
        channel_dir = os.path.join(base_dir)
        if not os.path.exists(channel_dir):
            cprint(f"AI Curation V1 - Criando diretório: {channel_dir}")
            os.makedirs(channel_dir)
        return channel_dir



    def normalize_find_mp4(self, name: str) -> str:
        # Remove acentos
        nfkd = unicodedata.normalize('NFKD', name)
        only_ascii = nfkd.encode('ASCII', 'ignore').decode('ASCII')
        # Remove pontuação e unifica espaços/underscores
        cleaned = re.sub(r'[\W]+', '_', only_ascii)
        return cleaned.strip('_').upper()

    def clear_file_name_to_rename(self, filename):
        """
        Limpa o nome do arquivo para buscar corretamente, na pasta mediabase
        """
        p = Path(filename)
        stem = p.stem   # parte sem a extensão
        extension = p.suffix  # inclui o ponto, ex.: ".mp4"

        # 1. Substituições explícitas para tratar casos específicos
        substitutions = {
            "z'": "z",
            "ft.": "ft",
            "À": "A",
            "Á": "A",
            "Ó": "O",
            "Ç": "C",
            "Í": "I",
            "É": "E",
            "é": "e",
            "Ã": "A",
            "Ô": "O",
            "Õ": "O",
            "｜": "",
            ",": "",
            "...": "",
            "'": "",
            "?": "",
            "!": "",
            " - ": " ",
            "(+": "_", 
            ")": "_", 
        }
        for key, value in substitutions.items():
            stem = stem.replace(key, value)

        # 2. Normaliza o texto (remove acentos e converte para ASCII)
        stem = unicodedata.normalize('NFKD', stem).encode('ASCII', 'ignore').decode('ASCII')

        # 3. Remove caracteres ilegais para nomes de arquivo no Windows: < > : " / \ | ? *
        stem = re.sub(r'[<>:"/\\|?*]', '', stem)

        # 4. Remove qualquer outro caractere indesejado, mantendo apenas letras, números, espaços, hífens e underscores
        stem = re.sub(r'[^\w\s-]', '', stem)

        # 5. Consolida múltiplos espaços ou hífens e aparar os extremos
        stem = re.sub(r'[-\s]+', ' ', stem).strip()

        # 6. (Opcional) Se o ffmpeg preferir nomes sem espaços, converte para underscore
        stem = stem.replace(' ', '_')

        # 7. Verifica se o 'stem' já termina com o nome da extensão (sem o ponto) e remove se necessário
        ext_without_dot = extension.lower()[1:]
        if stem.lower().endswith(ext_without_dot):
            stem = stem[:-len(ext_without_dot)]
            stem = stem.rstrip('_')  # remove underscore final se existir

        stem = stem.replace(' ', '_')

        stem = stem.replace('-', '')

        return f"{stem}{extension}"

    def safe_rename(self,original, new):
        os.rename(original, new)

    def find_mp4(
        self,
        base_dir: str,
        original_name: str,
        threshold: float = 0.8
    ) -> str:
        """
        Percorre base_dir procurando arquivos .mp4 cuja similaridade com original_name seja >= threshold.
        Se encontrar, renomeia para new_name e retorna o caminho final.
        """
        original_norm = self.normalize_find_mp4(original_name)
        for root, _, files in os.walk(base_dir):
            for fname in files:
                if not fname.lower().endswith('.mp4'):
                    continue
                orig_path = os.path.join(root, fname)
                fname_norm = self.normalize_find_mp4(fname)
                sim = SequenceMatcher(None, fname_norm, original_norm).ratio()
                print(f"similaridade?: {sim}")
                if sim >= threshold:
                    final_path = os.path.join(root, original_name)
                    return final_path

        return None
    
    def find_and_rename_mp4(
        self,
        base_dir: str,
        original_name: str,
        new_name: str,
        threshold: float = 0.8
    ) -> str:
        """
        Percorre base_dir procurando arquivos .mp4 cuja similaridade com original_name seja >= threshold.
        Se encontrar, renomeia para new_name e retorna o caminho final.
        """
        original_norm = self.normalize_find_mp4(original_name)
        for root, _, files in os.walk(base_dir):
            for fname in files:
                if not fname.lower().endswith('.mp4'):
                    continue

                orig_path = os.path.join(root, fname)
                fname_norm = self.normalize_find_mp4(fname)

                # Calcula similaridade entre fname_norm e original_norm
                sim = SequenceMatcher(None, fname_norm, original_norm).ratio()
                print(f"similaridade?: {sim}")
                if sim >= threshold:
                    final_path = os.path.join(root, new_name)
                    os.rename(orig_path, final_path)
                    return final_path

        return None

    def rename_file_mp4(
        self,
        canal_do_yt = "BisteconeLive",
        downloaded_filenames = "O QUE ESTÁ ACONTECENDO NESSA LANCHONETE À NOITE？ - BurgerPiz'",

        ):
        self.debugg_webhook(self.api_key, "info", f"Renomeando video baixado")


        nome_original = Path(self.base_dir) / f"{downloaded_filenames}.mp4"
        # remove_accents_nome = clear_file_name_to_search_correctly(nome_original.name) #remove_accents()
        # logger.info(f"remove_accents_nome: {remove_accents_nome}")

        novo_nome = self.clear_file_name_to_rename(nome_original.name)
        print(f"novo_nome: {novo_nome}")
        nome_rename_final = nome_original.parent / novo_nome
        rename_final = nome_original.parent / novo_nome
        print(f"nome_rename_final: {nome_rename_final}")

        try:
            self.safe_rename(nome_original, nome_rename_final)
        except Exception as fallback:
            print(f"fallback: {fallback}")
            try:
                candidate = self.loop_threshold(self.base_dir, nome_original, nome_original.name)
                nome_rename_final = Path(candidate)
                self.safe_rename(nome_original, nome_rename_final)
            except Exception as fallback:
                print(f"fallback 3 talvez foi renomeado mas deu erro de nao econtrado : {fallback}")
                nome_rename_final = Path(nome_rename_final)
                if nome_rename_final.exists():
                    print(f"O arquivo {nome_rename_final} existe. Retornando.")
                    return nome_rename_final
                else:
                    print(f"O arquivo {nome_rename_final} NÃO existe. Tentando similaridade.")
                    
                    nome_rename_final = self.find_mp4(
                        self.base_dir,
                        nome_original.name,
                        threshold= 0.7
                    )
                    if nome_rename_final == None:
                        print(f"sem similaridade com fallback 3: {nome_rename_final}")

                            
        print(f"Arquivo renomeado para: {nome_rename_final}")
        return nome_rename_final

    def loop_threshold(self, base_dir, nome_original, novo_nome):
        # Lista de thresholds decrescentes de 0.8 até 0.3
        thresholds = [0.8, 0.62]

        for threshold in thresholds:
            nome_rename_final = self.find_and_rename_mp4(
                base_dir, 
                str(nome_original), 
                novo_nome, 
                threshold=threshold
            )
            if nome_rename_final is not None:
                print(f"Arquivo encontrado com threshold {threshold}")
                return nome_rename_final
            else:
                print(f"Nenhum arquivo encontrado com threshold {threshold}")

        # Se chegou aqui, nada foi encontrado
        print("Nenhum arquivo encontrado após todas as tentativas.")
        return None
    
    def _is_true(self, x) -> bool:
        return str(x).strip().lower() in ("true", "1", "yes", "y", "on")

    async def main_TEST(self, 
            canal_do_yt, 
            lastlongvideotitle,
            new_video_ids,
            output_miniatura,
            nome_rename_final,
            srt_file_path
            
        ):

        await self.Analyse_TEST(
                    canal_do_yt,  
                    lastlongvideotitle,
                    new_video_ids,
                    output_miniatura,
                    nome_rename_final,
                    srt_file_path
                    )

    async def main_Horizontal_TEST(
            self, 
            nome_rename_final,
            srt_file_path,
            video_id,
            thumbnail_url,
            project_key

            
        ):

        print(f"nome_rename_final: {nome_rename_final}\n")
        trasncript_srt = srt_file_path#, audio_ = self.transcrever_audio(nome_rename_final, linux_env_flag=self.linux_env)
        print(f"trasncript_srt: {trasncript_srt}\n")

        try:
            with open(trasncript_srt, encoding='utf-8') as f:
                srt_file_content = f.read()
        except UnicodeDecodeError:
            with open(trasncript_srt, encoding='latin1') as f:
                srt_file_content = f.read()

        url = f'https://www.youtube.com/watch?v={video_id}'
        decription_content = obter_descricao(url)
        tags_do_video = obter_tags(url)
        try:
            duracao_total_seconds = get_duration_video(video_path=nome_rename_final)
            duracao_total = format_seconds(seconds=duracao_total_seconds)
        except Exception as e:
            print(f"e: {e}")
        resposta_ia =await self.Curation_Horizontal(
                range_array="1 a 2",
                range_seconds=(300, 240, 480),
                nome_do_canal=self.canal_do_yt,
                titulo_original=self.lastlongvideotitle,
                tags_do_video=tags_do_video,
                duracao_total=duracao_total,
                srt_file_content=srt_file_content,
                decription_content=decription_content,
            
            )

        lista_de_videos_horizontais = await self.Autonomous_Analysis_Horizontal(
                resposta_ia,  
                thumbnail_url,
                nome_rename_final,
                project_key
                )
        print(f"lista_de_videos_horizontais {lista_de_videos_horizontais}")
        
    async def download_yt_video_by_title(
            self,
            canal_do_yt, 
            lastlongvideotitle
            ):
        
        self.debugg_webhook(self.api_key, "info", f"Baixando: {lastlongvideotitle}")

        canal_nome, videos = await get_video_by_title(
            canal_url=f"https://www.youtube.com/@{canal_do_yt}",
            title_target=lastlongvideotitle,
            path_ffmpegnotexe=path_ffmpegnotexe,
            linux_env=self.linux_env,
            logger=logger
            
            
            )
        if not videos:
            print("AI Curation V1 - Nenhum vídeo encontrado no canal")

        
        output_dir = self.create_download_directory(self.base_dir)

        canal_nome_str = f"{canal_nome}"
        canal_nome = canal_nome_str.replace("- Videos", "").replace(" ", "")

        new_downloads, new_video_ids, downloaded_filenames, output_miniatura, thumbnail_url = download_new_videos(
                                                videos=videos, 
                                                output_dir=self.base_dir, 
                                                channel=canal_do_yt, 
                                                path_ffmpegnotexe=path_ffmpegnotexe,
                                                linux_env=self.linux_env, 
                                                output_path_ = os.path.join(os.path.dirname(__file__), 
                                               "WorkEnvironment",  
                                               "Process", 
                                               "MediaBase"))

        print(f"New videos downloaded: {new_downloads}")

        print(f"New id downloaded: {new_video_ids}")

        new_video_ids_str = str(new_video_ids)
        video_id = new_video_ids_str.strip("{}").strip("'\"").replace("{'", "").replace("'}", "")      

        self.debugg_webhook(self.api_key, "info", f"Video foi baixado: {lastlongvideotitle}")

        nome_rename_final = self.rename_file_mp4(canal_do_yt, downloaded_filenames)
        
        print(f"nome_rename_final? {nome_rename_final}")
        return nome_rename_final, output_miniatura, video_id, thumbnail_url

    async def Curation_Horizontal(
            self,
            range_array,
            range_seconds,
            nome_do_canal: str,
            titulo_original: str,
            tags_do_video: List[str],
            duracao_total: str,
            srt_file_content: str,
            decription_content: str,
            model: str = "gpt-4.1-nano"
        ):
        self.debugg_webhook(self.api_key, "info", "🔍 Inicializando Curadoria de IA Para Selecao De Melhores Cortes")
        content_ = f"""
Retorne apenas um **array** JSON contendo minimo de {range_array} os objetos
Range de Limite de timestamp para cada Corte (em segundos) {range_seconds}\n 
Duracao Total Do Video: {duracao_total}\n
Nome Do Canal {nome_do_canal}\n
Título Original: {titulo_original}\n
Tags: {', '.join(tags_do_video)}\n
Descrição: {decription_content}\n
Transcrição:
{srt_file_content}
        """
        # Tamanho real em bytes
        input_size = len(content_.encode("utf-8"))
        print(f"Tamanho em bytes: {input_size}")

        # Se ultrapassar o limite, dividimos em 2
        if input_size > self.MAX_INPUT_SIZE:
            self.debugg_webhook(self.api_key, "warning",
                f"Conteúdo ({input_size} bytes) acima do limite ({self.MAX_INPUT_SIZE} bytes). Dividindo em 2 chunks.")

            # Divide por linhas para manter cortes coerentes
            linhas = content_.splitlines(keepends=True)
            meio = math.ceil(len(linhas) / 2)
            chunk1 = "".join(linhas[:meio])
            chunk2 = "".join(linhas[meio:])

            # Cria dois agentes (podem ser iguais)
            agent1 = Agent(name="AI Horizontal CurationPt1", instructions=self.prompt_system_horizontal, model=model, output_type=AI_output_horizontal)
            agent2 = Agent(name="AI Horizontal CurationPt2", instructions=self.prompt_system_horizontal, model=model, output_type=AI_output_horizontal)

            # Executa cada parte
            result1 = await Runner.run(agent1, chunk1, max_turns=300)
            final_output1 = result1.final_output
            logger.info(f"RAW OUTPUT: {final_output1}")
            list1 = final_output1.cortes
      
            result2 = await Runner.run(agent2, chunk2, max_turns=300)
            final_output2 = result2.final_output
            logger.info(f"RAW OUTPUT: {final_output2}")
            list2 = final_output2.cortes
        

            # Une as duas listas
            merged = list1 + list2
            logger.info(f"📜 Curadoria dividida em 2 partes e unida com sucesso! Total de itens: {len(merged)}")

            # Padroniza saída para JSON igual chamada única
            cortes_dict = [corte.dict() for corte in merged]
            cortes_json = json.dumps(cortes_dict, indent=2, ensure_ascii=False)
            logger.info(f"RAW cortes_json (merged): {cortes_json}")

            try:
                cortes_json_list = json.loads(cortes_json)
                return cortes_json_list
            except Exception as err1:
                logger.info(f"err1: {err1}")
                return cortes_dict   # fallback em dict
            
        # Se não ultrapassar, faz chamada única normal
        agent = Agent(name="AI Horizontal Curation", instructions=self.prompt_system_horizontal, model=model, output_type=AI_output_horizontal)
        result = await Runner.run(agent, content_, max_turns=300)
        final_output = result.final_output
        logger.info(f"RAW OUTPUT: {result.final_output}")
        cortes = final_output.cortes
        logger.info(f"RAW cortes: {cortes}")
        cortes_dict = [corte.dict() for corte in cortes]
        cortes_json = json.dumps(cortes_dict, indent=2, ensure_ascii=False)
        logger.info(f"RAW cortes_json: {cortes_json}")
        
        try:
            cortes_json_list = json.loads(cortes_json)
            return cortes_json_list
        except Exception as err1:
            logger.info(f"err1: {err1}")

    async def Curation(
            self,
            range_seconds,
            nome_do_canal: str,
            titulo_original: str,
            tags_do_video: List[str],
            duracao_total: str,
            srt_file_content: str,
            decription_content: str,
            
        ):
        self.debugg_webhook(self.api_key, "info", "🔍 Inicializando Curadoria de IA Para Selecao De Melhores Cortes")
        
        content_ = f"""
    Retorne apenas um **array** JSON contendo minimo de 10 os objetos, lembre-se que voce pode escolher quantos objetos quer retornar mas o MINIMO É 10
    Range de Limite de timestamp para cada Corte (em segundos): {range_seconds}\n 
    Duracao Total Do Video: {duracao_total}\n
    Nome Do Canal {nome_do_canal}\n
    Título Original: {titulo_original}\n
    Tags Original: {', '.join(tags_do_video)}\n
    Descrição: {decription_content}\n
    Transcrição do Video:
    {srt_file_content}
        """
        
        # Tamanho real em bytes
        input_size = len(content_.encode("utf-8"))
        logger.info(f"Tamanho em bytes: {input_size}")

        # Se ultrapassar o limite, dividimos em chunks e processamos sequencialmente
        if input_size > self.MAX_INPUT_SIZE:
            logger.info(f"Conteúdo ({input_size} bytes) acima do limite ({self.MAX_INPUT_SIZE} bytes). Processando em chunks sequenciais.")

            # Divide por linhas para manter cortes coerentes
            linhas = content_.splitlines(keepends=True)
            
            # Calcula quantos chunks precisamos
            num_chunks = math.ceil(input_size / self.MAX_INPUT_SIZE)
            chunk_size = math.ceil(len(linhas) / num_chunks)
            
            logger.info(f"Dividindo em {num_chunks} chunks de aproximadamente {chunk_size} linhas cada.")

            # Cria um único agente para processar todos os chunks
            agent = Agent(
                name="AI Vertical Curation Sequential", 
                instructions=self.prompt_system, 
                model=self.model, 
                output_type=AI_output_vertical
            )
            
            accumulated_results = []
            conversation_context = ""
            
            # Processa cada chunk sequencialmente
            for i in range(num_chunks):
                start_idx = i * chunk_size
                end_idx = min((i + 1) * chunk_size, len(linhas))
                chunk = "".join(linhas[start_idx:end_idx])
                
                logger.info(f"Processando chunk {i+1}/{num_chunks}")
                
                # Monta o input com contexto acumulado
                if i == 0:
                    # Primeiro chunk - input normal
                    chunk_input = f"""
    Parte {i+1} de {num_chunks} chunks. Processe esta parte e retorne os cortes encontrados.
    Informações gerais:
    Range de Limite de timestamp para cada Corte (em segundos): {range_seconds}
    Duracao Total Do Video: {duracao_total}
    Nome Do Canal {nome_do_canal}
    Título Original: {titulo_original}
    Tags Original: {', '.join(tags_do_video)}
    Descrição: {decription_content}

    Transcrição desta parte:
    {chunk}
                    """
                else:
                    # Chunks subsequentes - inclui contexto dos anteriores
                    chunk_input = f"""
    Parte {i+1} de {num_chunks} chunks. Continue a análise considerando os cortes já encontrados.

    Cortes já identificados nas partes anteriores:
    {conversation_context}

    Agora processe esta nova parte da transcrição:
    {chunk}

    Retorne apenas os novos cortes desta parte.
                    """
                
                try:
                    # Aguarda um pouco entre as chamadas para evitar rate limit
                    if i > 0:
                        await asyncio.sleep(2)  # 2 segundos entre chunks
                    
                    result = await Runner.run(agent, chunk_input, max_turns=300)
                    final_output = result.final_output
                    chunk_cortes = final_output.cortes
                    
                    logger.info(f"Chunk {i+1} processado com {len(chunk_cortes)} cortes")
                    
                    # Acumula os resultados
                    accumulated_results.extend(chunk_cortes)
                    
                    # Atualiza o contexto para o próximo chunk (apenas um resumo)
                    if len(chunk_cortes) > 0:
                        context_summary = f"Chunk {i+1}: {len(chunk_cortes)} cortes encontrados. "
                        conversation_context += context_summary
                        
                except Exception as e:
                    logger.error(f"Erro ao processar chunk {i+1}: {e}")
                    # Em caso de erro, aguarda mais tempo antes de tentar o próximo
                    await asyncio.sleep(5)
            
            logger.info(f"📜 Processamento sequencial concluído! Total de cortes coletados: {len(accumulated_results)}")
            
            # Agora cria um agente de sumarização para consolidar e otimizar os resultados
            if len(accumulated_results) > 0:
                logger.info("🔄 Iniciando sumarização e otimização dos cortes...")
                
                # Converte para dict para facilitar a manipulação
                cortes_dict = [corte.dict() for corte in accumulated_results]
                cortes_json_raw = json.dumps(cortes_dict, indent=2, ensure_ascii=False)
                
                # Cria agente de sumarização
                summary_agent = Agent(
                    name="AI Curation Summarizer",
                    instructions=f"""
    Você receberá uma lista de cortes de vídeo identificados por chunks sequenciais.
    Sua tarefa é:
    1. Remover duplicatas baseadas em timestamps similares (diferença < 5 segundos)
    2. Manter apenas os melhores cortes (mínimo 10, máximo 20)
    3. Priorizar cortes com maior potencial viral
    4. Garantir diversidade de conteúdo
    5. Retornar no mesmo formato JSON

    Informações do vídeo:
    - Canal: {nome_do_canal}
    - Título: {titulo_original}  
    - Duração: {duracao_total}
    - Range por corte: {range_seconds} segundos
                    """,
                    model=self.model,
                    output_type=AI_output_vertical
                )
                
                summary_input = f"""
    Otimize e consolide esta lista de cortes, removendo duplicatas e mantendo apenas os melhores:

    {cortes_json_raw}
                """
                
                try:
                    # Aguarda antes da sumarização
                    await asyncio.sleep(3)
                    
                    summary_result = await Runner.run(summary_agent, summary_input, max_turns=300)
                    final_summary = summary_result.final_output
                    final_cortes = final_summary.cortes
                    
                    logger.info(f"✅ Sumarização concluída! Cortes finais: {len(final_cortes)}")
                    
                    # Retorna resultado final otimizado
                    final_cortes_dict = [corte.dict() for corte in final_cortes]
                    final_cortes_json = json.dumps(final_cortes_dict, indent=2, ensure_ascii=False)
                    logger.info(f"RAW final_cortes_json: {final_cortes_json}")
                    
                    try:
                        return json.loads(final_cortes_json)
                    except Exception as err:
                        logger.info(f"Erro na conversão final: {err}")
                        return final_cortes_dict
                        
                except Exception as summary_error:
                    logger.error(f"Erro na sumarização: {summary_error}")
                    # Fallback: retorna os resultados não sumarizados
                    logger.info("Usando resultados não sumarizados como fallback")
                    final_cortes_dict = [corte.dict() for corte in accumulated_results]
                    return final_cortes_dict
            
            else:
                logger.warning("Nenhum corte foi encontrado nos chunks processados")
                return []

        # Se não ultrapassar o limite, faz chamada única normal
        agent = Agent(
            name="AI Vertical Curation", 
            instructions=self.prompt_system, 
            model=self.model, 
            output_type=AI_output_vertical
        )
        
        result = await Runner.run(agent, content_, max_turns=300)
        final_output = result.final_output
        logger.info(f"RAW OUTPUT: {result.final_output}")
        cortes = final_output.cortes
        logger.info(f"RAW cortes: {cortes}")
        
        cortes_dict = [corte.dict() for corte in cortes]
        cortes_json = json.dumps(cortes_dict, indent=2, ensure_ascii=False)
        logger.info(f"RAW cortes_json: {cortes_json}")
        
        try:
            cortes_json_list = json.loads(cortes_json)
            return cortes_json_list
        except Exception as err1:
            logger.info(f"err1: {err1}")
            return cortes_dict

    async def main(self):
        nome_rename_final, output_miniatura, video_id, thumbnail_url, project_key = await self.download_video_yt()
        self.update_status_progress(3, project_key)    
        includeV = self._is_true(self.includeVertical) 
        includeH = self._is_true(self.includeHorizontal)

        if includeV and includeH:
            await self.Analyse_Vertical_and_Horizontal(
                nome_rename_final, output_miniatura, video_id, thumbnail_url, project_key
            )
            self.update_status_progress(100, project_key)
            
        elif includeV:
            await self.Analyse_Vertical(
                nome_rename_final, output_miniatura, video_id, thumbnail_url, project_key
            )
            self.update_status_progress(100, project_key)
        elif includeH:
            self.update_status_progress(50, project_key)
            await self.Analyse_Horizontal(
                nome_rename_final, output_miniatura, video_id, thumbnail_url, project_key
            )
            self.update_status_progress(100, project_key)
        else:
            # tratar caso nenhum esteja marcado
            logger.info("Nenhum formato selecionado: includeVertical e includeHorizontal são falsos")
            await self.Analyse_Vertical(
                nome_rename_final, output_miniatura, video_id, thumbnail_url, project_key
            )
            self.update_status_progress(100, project_key)

# if __name__ == "__main__":
#     api_key = "apikey-startup-YEubhuzU8iasgxbExFMAJrWbf8NFd_sq4okm9b-OEDw"
#     user_email = "freitasalexandre810@gmail_com"
#     canal_do_yt = "cortesdoflow"
    
#     lastlongvideotitle = "O que NÃO TE CONTAM sobre LULA: Brasil deveria ROMPER RELAÇÕES com Israel?"
#     project_key = secure_filename(lastlongvideotitle).replace("-", "").replace("....", "").replace("...", "").replace("..", "").replace(".", "").replace("... - ", "").replace('"????????"', '').replace("...__", "_") 
#     new_video_ids = "CO3LC8ub2_g"
#     output_miniatura = r"C:\Users\Media Cuts DeV\Downloads\HomeServer\HomeServer\internalserver\Studio\WorkEnvironment\Process\MediaBase\cortesdoflow\CO3LC8ub2_g.jpg"
#     nome_rename_final = r"C:\Users\Media Cuts DeV\Downloads\HomeServer\HomeServer\internalserver\Studio\WorkEnvironment\Process\MediaBase\cortesdoflow\O_que_NAO_TE_CONTAM_sobre_LULA_Brasil_deveria_ROMPER_RELACOES_com_Israel.mp4"
#     srt_file_path = r"C:\Users\Media Cuts DeV\Downloads\HomeServer\HomeServer\internalserver\Studio\WorkEnvironment\Process\AICuration\Transcript\audio_video_vertical.srt"
#     video_id = "CO3LC8ub2_g"
#     thumbnail_url = ""
#     AI_Curation_instance = AI_Curation(
#         linux_env=False, 
#         downloadToPanelEnabled=True,
#         secondsScheduleTiktokVideo="",
#         TiktokAccount="",
#         TiktokAccountCookies="",
#         user_email=user_email,
#         app_instance=app_teste,
#         canal_do_yt=canal_do_yt,
#         api_key=api_key,
#         CaptionsAlignment="2"
#         )
#     asyncio.run(AI_Curation_instance.main_Horizontal_TEST(
#             nome_rename_final,
#             srt_file_path,
#             video_id,
#             thumbnail_url,
#             project_key
            
            
            
#         ))

    # asyncio.run(AI_Curation_instance.main_TEST(
    #         canal_do_yt, 
    #         lastlongvideotitle,
    #         new_video_ids,
    #         output_miniatura,
    #         nome_rename_final,
    #         srt_file_path
            
    #     ))


