import subprocess
import time
import re 
from faster_whisper import WhisperModel
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import os
import whisper
from datetime import timedelta
import requests
import srt
from termcolor import cprint

class Audio_Transcriber:
    """
    A class for transcribing audio from video files using the Whisper model and managing
    the transcription process, including audio extraction, progress updates, and webhook
    notifications.

    This class supports extracting audio from video files using FFmpeg, transcribing
    the extracted audio using a specified Whisper model, and generating SRT subtitle files.
    It can also send progress updates and transcription results to a webhook and
    interface with UI signals for real-time feedback.

    | Modelo         | Parâmetros aprox. | Tamanho do arquivo  | Línguas suportadas | WER médio (en)¹  | Velocidade diária²    |
    | -------------- | ----------------- | ------------------- | ------------------ | ---------------- | --------------------- |
    | **tiny**       | \~39 M            | \~74 MB             | 99 idiomas         | \~31 %           | \~70× real-time (GPU) |
    | **base**       | \~74 M            | \~140 MB            | 99 idiomas         | \~24 %           | \~35× real-time (GPU) |
    | **small**      | \~244 M           | \~500 MB            | 99 idiomas         | \~15 %           | \~15× real-time (GPU) |
    | **medium**     | \~769 M           | \~1.5 GB            | 99 idiomas         | \~12 %           | \~5× real-time (GPU)  |
    | **large**      | \~1.55 B          | \~3.1 GB            | 99 idiomas         | \~10 %           | \~2× real-time (GPU)  |
    | **whisper-1**³ | \~1.55 B          | gerenciado pela API | 99 idiomas         | similar ao large | escalável via API     |


    Attributes:
        webhook (bool): Indicates if webhook notifications are enabled.
        model_type (str): The type of Whisper model to load (e.g., "small").
        WEBHOOK_URL (Optional[str]): The URL for sending webhook notifications.
        start_time (float): The timestamp when the transcription process started.
        model (whisper.model): The loaded Whisper transcription model.
        api_key (Optional[str]): The API key used for webhook authentication or other services.
    """
    def __init__(self,
                api_key=None,
                WEBHOOK_URL=None, 
                model_type="whisper-robust-small", 
                webhook=False,

                
                ):
        """
        Initializes the Audio_Transcriber with various configuration parameters.

        Args:
            api_key (str, optional): An API key for authentication, possibly for webhook or other services. Defaults to None.
            WEBHOOK_URL (str, optional): The URL endpoint for sending webhook notifications. Defaults to None.
            model_type (str, optional): Specifies the Whisper model to use for transcription (e.g., "small"). Defaults to "small".
            webhook (bool, optional): If True, enables sending notifications to the specified WEBHOOK_URL. Defaults to False.
        """
        self.start_time = time.time()
        print(f"Audio Transcriber")

        cache_dir = os.path.join(os.path.dirname(__file__), "Models", "Whisper")

        self.webhook = webhook
        self.model_type = model_type 
        self.whisperlocal_flag = False
        self.largev3turbo_flag = False
        self.faster_flag = False
        self.pipe = None
        WHISPER_MODELS = {
            "whisper-robust-tiny": "tiny",
            "whisper-robust-base": "base",
            "whisper-robust-small": "small",
            "whisper-robust-medium": "medium",
            "whisper-robust-large": "large",
            "whisper-robust-turbo": "turbo",
            "whisper-robust-large-v1": "large-v1",
            "whisper-robust-large-v2": "large-v2",
            "whisper-robust-large-v3": "large-v3",
            "whisper-robust-large-v3-turbo": "large-v3-turbo",
            "whisper-hugface-v3-turbo": "whisper-large-v3-turbo",
            "faster-whisper-local-tiny.en": "tiny.en",
            "faster-whisper-local-tiny": "tiny",
            "faster-whisper-local-base.en": "base.en",
            "faster-whisper-local-base": "base",
            "faster-whisper-local-small.en": "small.en",
            "faster-whisper-local-small": "small",
            "faster-whisper-local-medium.en": "medium.en",
            "faster-whisper-local-medium": "medium",
            "faster-whisper-local-large-v1": "large-v1",
            "faster-whisper-local-large-v2": "large-v2",
            "faster-whisper-local-large-v3": "large-v3",
            "faster-whisper-local-large": "large-v3",
            "faster-whisper-local-distil-large-v2": "distil-large-v2",
            "faster-whisper-local-distil-medium.en": "distil-medium.en",
            "faster-whisper-local-distil-small.en": "distil-small.en",
            "faster-whisper-local-distil-large-v3": "distil-large-v3",
            "faster-whisper-local-distil-large-v3.5": "distil-large-v3.5",
            "faster-whisper-local-large-v3-turbo": "large-v3-turbo",
            "faster-whisper-local-turbo": "turbo",

        }
        
        info = WHISPER_MODELS.get(self.model_type)
        if info:
            print(f"Modelo {self.model_type}: {info}")
            if self.model_type.startswith("whisper-robust"):
                self.whisperlocal_flag = True
                self.model = whisper.load_model(info, download_root=cache_dir) 
            
            elif self.model_type.startswith("whisper-hugface-v3-turbo"):  
                self.largev3turbo_flag = True

                device = "cuda:0" if torch.cuda.is_available() else "cpu"
                torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

                model_id = "openai/whisper-large-v3-turbo"

                self.model = AutoModelForSpeechSeq2Seq.from_pretrained(
                    model_id, torch_dtype=torch_dtype, cache_dir=cache_dir, low_cpu_mem_usage=True, use_safetensors=True
                )
                self.model.to(device)

                processor = AutoProcessor.from_pretrained(model_id, cache_dir=cache_dir)

                self.pipe = pipeline(
                    "automatic-speech-recognition",
                    model=self.model,
                    tokenizer=processor.tokenizer,
                    feature_extractor=processor.feature_extractor,
                    torch_dtype=torch_dtype,
                    device=device,
                )

            elif self.model_type.startswith("faster-whisper-local"):  
                self.faster_flag = True
                self.model = WhisperModel(info, download_root=cache_dir)

        else:
            print(f"Modelo {self.model_type} não reconhecido.")
            # return 
        self.text_edit_signal = None
        self.progress_signal = None
        self.hash_thread = "hash_thread"
        self.WEBHOOK_URL = WEBHOOK_URL

        #if self.model_type == "whisper":
        
        
        self.api_key = api_key
    
        # else:
        #     raise ValueError("Tipo de modelo desconhecido. Use 'whisper' ou 'whisper-large-v3-turbo'.")
    
    def main(self, path_videofile, path_file_audio):

        input_file_audio = self.extract_audio_with_ffmpeg(
            video_input=path_videofile,
            audio_output=path_file_audio
            )

        if self.whisperlocal_flag == True:
            resultado, total_time_str = self.transcrever_audio(input_file_audio)
            return resultado, total_time_str 

        elif self.largev3turbo_flag == True:
            resultado, total_time_str = self.transcrever_audio_large_v3_turbo(input_file_audio)
            return resultado, total_time_str 

        elif self.faster_flag == True:
            resultado, total_time_str = self.transcrever_audio_whisper_faster(input_file_audio)
            return resultado, total_time_str 

        


    def send_to_webhook(self, user, type, message, cor=None):
        """Envia uma mensagem para o webhook."""
        try:
            # Envia o conteúdo da mensagem como JSON; ajuste se necessário
            requests.post(self.WEBHOOK_URL, json={str(user): {"type": type, "message": message}})

        except Exception as e:
            # Evita erro recursivo chamando a função original de print
            print("Erro ao enviar mensagem para webhook:", e)


    def extract_audio_with_ffmpeg(self, video_input, audio_output):
        """
        Extrai o áudio do vídeo usando ffmpeg e salva como .wav.

        :param video_input: Caminho para o arquivo de vídeo de entrada
        :param audio_output: Caminho para o arquivo de saída do áudio (.wav)
        """
        command = [
            'ffmpeg',
            '-y',  # Forçar a sobreposição de arquivos
            '-i', video_input,  # Especifica o arquivo de entrada
            '-vn',  # Não processa vídeo
            '-acodec', 'pcm_s16le',  # Codec de áudio para .wav
            '-ar', '16000',  # Ajustar para uma taxa de amostragem mais comum
            '-ac', '1',  # Um canal (mono) pode ajudar na compatibilidade
            audio_output  # Arquivo de saída
        ]
        subprocess.run(command)
        return audio_output


    def finish(self):
        total = time.time() - self.start_time  # total em segundos (float)

        # converte em horas, minutos e segundos
        horas   = int(total // 3600)
        minutos = int((total % 3600) // 60)
        segundos = total % 60  # ainda float, para fração de segundo

        # monta string legível
        if horas:
            total_str = f"{horas}h {minutos}m {segundos:.2f}s"
        elif minutos:
            total_str = f"{minutos}m {segundos:.2f}s"
        else:
            total_str = f"{segundos:.2f}s"

        print(f"⏳ Tempo total de transcrição: {total_str}")
        return total_str

    def transcrever_audio_whisper_faster(self, arquivo_audio, audio_sliced_path="", vertical_id=""):
        segments, info = self.model.transcribe(arquivo_audio, word_timestamps=True)
        # for segment in segments:
        #     print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
        arquivo_audio_replace = f"{arquivo_audio}"
        arquivo_audio_sem_wav = arquivo_audio_replace.replace(".wav", "").replace(".mp4", "")
        self.write_captions(segments, arquivo_audio_sem_wav)


        total_time_str = self.finish()

        return segments, total_time_str

    def transcrever_audio_large_v3_turbo(self, arquivo_audio, audio_sliced_path="", vertical_id=""):
        resultado = self.transcrever_com_whisper_large_v3_turbo(arquivo_audio)
     
        arquivo_audio_replace = f"{arquivo_audio}"
        arquivo_audio_sem_wav = arquivo_audio_replace.replace(".wav", "").replace(".mp4", "")
        # self.write_captions(resultado, arquivo_audio_sem_wav)


        total_time_str = self.finish()

        return resultado, total_time_str

    def transcrever_audio(self, arquivo_audio, audio_sliced_path="", vertical_id=""):
        resultado = self.transcrever_com_whisper(arquivo_audio)

        arquivo_audio_replace = f"{arquivo_audio}"
        arquivo_audio_sem_wav = arquivo_audio_replace.replace(".wav", "").replace(".mp4", "")
        self.write_captions(resultado, arquivo_audio_sem_wav)


        total_time_str = self.finish()

        return resultado, total_time_str
    
    def transcrever_com_whisper_large_v3_turbo(self, arquivo_audio):
            try:
                
                print(f"⏳ Transcribe...")
           
                result = self.pipe(arquivo_audio)
                print(result["text"])
                del self.pipe
                del self.model
                # torch.cuda.empty_cache() 
                return result
            except Exception as e: 
                print(f"err {e}")       
                
    def transcrever_com_whisper(self, arquivo_audio):
        for i in range(5):
            try:
                    
                if self.text_edit_signal is not None:
                    self.text_edit_signal.emit(f"Transcribe...")
                else:
                    print(f"⏳ Transcribe...")
                    self.send_to_webhook(self.api_key, "info", f"⏳ Transcribe...")

                resultado = self.model.transcribe(arquivo_audio, word_timestamps=True)
                del self.model
                # torch.cuda.empty_cache() 
                return resultado
            except Exception as e: 
                print(f"err {e}")       



    def write_captions(self, segments, filename):
        """
        Gera arquivo .srt a partir de:
        - lista de objetos com atributos .start, .end, .text
        - dict {'segments': [ {'start':…, 'end':…, 'text':…}, … ]}
        """
        # Extraímos a lista de segmentos no formato homogêneo
        if isinstance(segments, dict) and 'segments' in segments:
            seg_list = segments['segments']
            # função de acesso para dicionários
            get = lambda seg, attr: seg[attr]
        else:
            seg_list = segments
            # função de acesso para objetos
            get = lambda seg, attr: getattr(seg, attr)

        captions = []
        for seg in seg_list:
            start = timedelta(seconds=float(get(seg, 'start')))
            end   = timedelta(seconds=float(get(seg, 'end')))
            text  = get(seg, 'text')
            captions.append(
                srt.Subtitle(
                    index  = len(captions) + 1,
                    start  = start,
                    end    = end,
                    content= text
                )
            )

        # Opcional: imprimir no console no estilo Whisper original
        for seg in seg_list:
            print("[%.2fs -> %.2fs] %s" % (
                float(get(seg, 'start')),
                float(get(seg, 'end')),
                get(seg, 'text')
            ))

        # Compondo e salvando o arquivo SRT
        srt_content = srt.compose(captions)
        srt_file = f"{filename}.srt"
        with open(srt_file, "w", encoding="utf-8") as f:
            f.write(srt_content)

        return srt_file
    
    def convert_to_ass(self, subtitlesrt, subtitleass):
        command = [
            'ffmpeg',
            '-y',
            '-i',
            subtitlesrt,
            subtitleass
        ]

        
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True,  encoding="utf-8")
        time_pattern = re.compile(r'time=(\d+:\d+:\d+\.\d+)')
        size_pattern = re.compile(r'size=\s*(\d+(\.\d+)?[A-Za-z]+)')
        counter = 0
        while True:
            output = process.stderr.readline()
            if output == "" and process.poll() is not None:
                break
            if output:
                time_match = time_pattern.search(output)
                size_match = size_pattern.search(output)
                

                if time_match and size_match:
                    time_value = time_match.group(1)
                    size_value = size_match.group(1)

                    log_message = f"⏳ Convert srt to ass... | Time: {time_value} | Size: {size_value}"
                    cprint(log_message)
                    # if self.text_edit_signal is not None:
                    #     self.text_edit_signal.emit(log_message)
                    # else:
                    #     cprint(log_message)
                    #     counter += 1
                    if self.webhook == True:
                        self.send_to_webhook(self.api_key, "info",  log_message)
        

        process.wait() 
        process.terminate() 
        return True
        
    def load_ass_styles(self, ass_file_path):
        """
        Loads subtitle styles from an ASS (Advanced SubStation Alpha) file.

        This function reads the `[V4+ Styles]` section of the ASS file and retrieves the first style found, typically 
        the default style. The style is returned as a dictionary containing various style properties.

        Args:
            ass_file_path (str): Path to the ASS file to read.

        Returns:
            dict: A dictionary containing the style properties if successfully loaded, or None in case of an error.

        Raises:
            Exception: If an error occurs while reading or parsing the ASS file.
        """
        styles = {}
        try:
            # Read the content of the .ass file
            with open(ass_file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            # Control variables
            inside_styles = False
            for line in lines:
                line = line.strip()

                # Detect the start of the styles section
                if line.startswith('[V4+ Styles]'):
                    inside_styles = True
                    continue

                # Detect the end of the styles section
                if inside_styles and line.startswith('[Events]'):
                    inside_styles = False
                    continue

                # If inside the styles section
                if inside_styles:
                    if line.startswith('Format:'):
                        # Ignore the format line
                        continue
                    elif line.startswith('Style:'):
                        # Extract the values of the default style
                        style_values = line.split(',')
                        styles = {
                            'Name': style_values[0],
                            'Fontname': style_values[1],
                            'Fontsize': int(style_values[2]),
                            'PrimaryColour': style_values[3],
                            'SecondaryColour': style_values[4],
                            'OutlineColour': style_values[5],
                            'BackColour': style_values[6],
                            'Bold': int(style_values[7]),
                            'Italic': int(style_values[8]),
                            'Underline': int(style_values[9]),
                            'StrikeOut': int(style_values[10]),
                            'ScaleX': int(style_values[11]),
                            'ScaleY': int(style_values[12]),
                            'Spacing': int(style_values[13]),
                            'Angle': int(style_values[14]),
                            'BorderStyle': int(style_values[15]),
                            'Outline': int(style_values[16]),
                            'Shadow': int(style_values[17]),
                            'Alignment': int(style_values[18]),
                            'MarginL': int(style_values[19]),
                            'MarginR': int(style_values[20]),
                            'MarginV': int(style_values[21]),
                            'Encoding': int(style_values[22])
                        }
                        break  # Stop after finding the default style
            return styles
        except Exception as e:
            print(f"An error occurred while reading the ASS file: {e}")
            return None

    def modify_ass_styles(self, ass_file_path, new_style):
        """
        Modifies the default subtitle style in an ASS (Advanced SubStation Alpha) file.

        This function updates the `[V4+ Styles]` section of the ASS file, specifically modifying the default style 
        with the properties provided in the `new_style` dictionary.

        Args:
            ass_file_path (str): Path to the ASS file to modify.
            new_style (dict): A dictionary containing the new style properties to apply.

        Returns:
            None

        Raises:
            Exception: If an error occurs while reading, modifying, or saving the ASS file.
        """
        try:
            # Read the content of the .ass file
            with open(ass_file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            # Control variables
            inside_styles = False
            new_lines = []
            for line in lines:
                line = line.strip()

                # Detect the start of the styles section
                if line.startswith('[V4+ Styles]'):
                    inside_styles = True
                    new_lines.append(line)
                    continue

                # Detect the end of the styles section
                if inside_styles and line.startswith('[Events]'):
                    inside_styles = False
                    new_lines.append(line)
                    continue

                # Modify the default style if found
                if inside_styles and line.startswith('Style: Default'):
                    # Split the components of the default style
                    style_values = line.split(',')

                    # Map new values to the correct positions
                    for key, value in new_style.items():
                        if key == 'Fontname':
                            style_values[1] = value
                        elif key == 'Fontsize':
                            style_values[2] = str(value)
                        elif key == 'PrimaryColour':
                            style_values[3] = value
                        elif key == 'SecondaryColour':
                            style_values[4] = value
                        elif key == 'OutlineColour':
                            style_values[5] = value
                        elif key == 'BackColour':
                            style_values[6] = value
                        elif key == 'Bold':
                            style_values[7] = str(value)
                        elif key == 'Italic':
                            style_values[8] = str(value)
                        elif key == 'Underline':
                            style_values[9] = str(value)
                        elif key == 'StrikeOut':
                            style_values[10] = str(value)
                        elif key == 'ScaleX':
                            style_values[11] = str(value)
                        elif key == 'ScaleY':
                            style_values[12] = str(value)
                        elif key == 'Spacing':
                            style_values[13] = str(value)
                        elif key == 'Angle':
                            style_values[14] = str(value)
                        elif key == 'BorderStyle':
                            style_values[15] = str(value)
                        elif key == 'Outline':
                            style_values[16] = str(value)
                        elif key == 'Shadow':
                            style_values[17] = str(value)
                        elif key == 'Alignment':
                            style_values[18] = str(value)
                        elif key == 'MarginL':
                            style_values[19] = str(value)
                        elif key == 'MarginR':
                            style_values[20] = str(value)
                        elif key == 'MarginV':
                            style_values[21] = str(value)
                        elif key == 'Encoding':
                            style_values[22] = str(value)

                    # Recreate the style line with the modified values
                    new_lines.append(','.join(style_values))
                else:
                    new_lines.append(line)

            # Save the modified content back to the .ass file
            with open(ass_file_path, 'w', encoding='utf-8') as file:
                file.writelines("\n".join(new_lines))

            print(f"Styles in the file {ass_file_path} were successfully modified!")

        except Exception as e:
            print(f"An error occurred while modifying the ASS file: {e}")

        # def write_captions(self, segments, filename):
        #     captions = []  # Lista de objetos Subtitle

        #     # Cabeçalho do arquivo .ass (Script Info)
        #     script_info_header = """
        #     [Script Info]
        #     Title: Example Subtitle File
        #     Original Script: Generated
        #     ScriptType: v4.00
        #     Collisions: Normal
        #     PlayDepth: 0
        #     """
            
        #     # Cabeçalho de estilo (V4+ Styles)
        #     styles_header = """
        #     [V4+ Styles]
        #     Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, BackColour, Bold, Italic, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
        #     Style: Default,Arial,24,&HFFFFFF,&H0000FF,&H000000,-1,0,1,1.0,0,2,10,10,10,1
        #     """
            
        #     # Adicionando o cabeçalho de script e estilos
        #     captions.append(script_info_header)
        #     captions.append(styles_header)
            
        #     # Adicionando as legendas
        #     for segment in segments['segments']:
        #         start = timedelta(seconds=segment['start'])
        #         end = timedelta(seconds=segment['end'])
        #         text = segment['text']

        #         # Convertendo os tempos para o formato ASS
        #         start_time = str(start).split('.')[0]  # Remover milissegundos
        #         end_time = str(end).split('.')[0]  # Remover milissegundos

        #         # Formatando a legenda no padrão ASS
        #         ass_subtitle = f"Dialogue: 0,{start_time},{end_time},Default,,0,0,0,,{text}"

        #         # Adicionando a legenda ao arquivo
        #         captions.append(ass_subtitle)

        #     # Salvando o conteúdo no arquivo .ass
        #     ass_file = f"{filename}.ass"
        #     with open(ass_file, "w", encoding="UTF-8") as file:
        #         file.writelines(captions)

        #     return ass_file

        def _format_timestamp(self, seconds):
            """Converte um timestamp em segundos para o formato SRT (hh:mm:ss,ms)."""
            hours = int(seconds // 3600)
            minutes = int((seconds % 3600) // 60)
            seconds = int(seconds % 60)
            milliseconds = int((seconds - int(seconds)) * 1000)
            return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"


if __name__ == "__main__":
    subclip_filename = r"C:\Users\Media Cuts DeV\Downloads\HomeServer\HomeServer\internalserver\Studio\WorkEnvironment\Process\MediaBase\cortesdoflow\O_que_NAO_TE_CONTAM_sobre_LULA_Brasil_deveria_ROMPER_RELACOES_com_Israel.mp4"
    audio_linux = r"C:\Users\Media Cuts DeV\Downloads\HomeServer\HomeServer\internalserver\Studio\WorkEnvironment\Process\Realtime_Cuts\Cuts\Alim_do_Poder_da_ONU_e_a_Realidade_das_Relacoes_Internacionais\CutsCreate\audio_video_vertical_1.wav"#r"C:\Users\Media Cuts DeV\Downloads\HomeServer\HomeServer\internalserver\Studio\WorkEnvironment\Process\MediaBase\cortesdoflow\audio.wav"
    Audio_Transcriber_webhook = False
    Audio_Transcriber_api_key = ""
    Audio_Transcriber_WEBHOOK_URL = ""

    diretorio_script = os.path.dirname(os.path.abspath(__file__)) 
    path_ffmpeg = os.path.join(diretorio_script, 'Utils', 'ffmpeg', 'ffmpeg.exe')
    path_ffmpegnotexe = os.path.join(diretorio_script, 'Utils', 'ffmpeg')
    os.environ['PATH'] = path_ffmpegnotexe + os.pathsep + os.environ['PATH']

    Audio_Transcriber_model = "whisper-robust-tiny"#"faster-whisper-local-tiny"

    transcriber = Audio_Transcriber(
                                    model_type=Audio_Transcriber_model, 
                                    webhook=Audio_Transcriber_webhook,
                                    api_key=Audio_Transcriber_api_key,
                                    WEBHOOK_URL=Audio_Transcriber_WEBHOOK_URL
                                )

    resultado, total_time_str = transcriber.main(
        path_videofile=subclip_filename, 
        path_file_audio=audio_linux
                    
        )
    # resultado = transcriber.transcrever_audio_whisper_faster(audio_linux)
    # resultado, total_time_str = transcriber.transcrever_audio_large_v3_turbo(audio_linux)
    print(total_time_str)
    # print(resultado)