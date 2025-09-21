


import os
PRODUCTION_ENV = os.getenv("PRODUCTION_ENV", "True")

if PRODUCTION_ENV == "True":
    # Production
    from Studio.Modules.__init_libs__ import *

elif PRODUCTION_ENV == "False":
    # Local test
    from Modules.__init_libs__ import *


def add_watermark(
        input_video,
        output_video,
        watermark_image=None,
        overlay_position="10:10",
        watermark_width=100, 
        watermark_height=None,
        start_time_seconds=0,
        gpu=False
    ):
    """
    Adiciona uma marca d'água de imagem ao vídeo, com a opção de definir um tempo de início
    e controlar a qualidade de re-codificação do vídeo.

    :param input_video: str - Caminho para o vídeo de entrada.
    :param output_video: str - Caminho para salvar o vídeo de saída com a marca d'água.
    :param watermark_image: str - Caminho para a imagem de marca d'água a ser sobreposta no vídeo.
    :param overlay_position: str, opcional - Posição da imagem de marca d'água no vídeo,
        definida no formato `x:y`. Exemplo: "10:10".
        Valor padrão: "10:10" (canto superior esquerdo com margem de 10 pixels).
    :param watermark_width: int, opcional - Largura da imagem de marca d'água, em pixels.
        Valor padrão: 100.
    :param watermark_height: int, opcional - Altura da imagem de marca d'água, em pixels.
        Valor padrão: None (para auto-escala).
    :param start_time_seconds: int/float, opcional - O tempo em segundos a partir do qual a marca d'água
        deve começar a aparecer. Valor padrão: 0 (aparece desde o início).


    :return: None
        A função salva o vídeo processado no caminho especificado em `output_video`.
        Não há retorno direto de valor.
    """
    try:
        # Determine a altura para o filtro scale do FFmpeg
        # Se watermark_height for None, use -1 para auto-escala
        ffmpeg_watermark_height = watermark_height if watermark_height is not None else -1
        
        # Build the overlay string with enable condition
        # The 'enable' option uses 't' for current timestamp in seconds
        overlay_filter_string = f"overlay={overlay_position}:enable='gte(t,{start_time_seconds})'"

        # Consolidate the filter_complex for image overlay
        command_filter_complex = f"[1:v]format=rgba,scale={watermark_width}:{ffmpeg_watermark_height}[wm];" \
                                     f"[0:v][wm]{overlay_filter_string}"
        if gpu == False:
                
            command = [
                "ffmpeg",
                '-y',
                '-i', input_video,
                '-i', watermark_image,
                '-filter_complex', command_filter_complex,
                "-c:v", "libx264",
                "-crf", "17", # Use CRF for quality control
                "-preset", "slow", # Use the chosen preset
                "-threads", "0",
                "-c:a", "copy", # Audio can still be copied without re-encoding
                output_video
            ]
        else:
   
            command = [
                "ffmpeg",
                '-y',
                '-i', input_video,
                '-i', watermark_image,
                '-filter_complex', command_filter_complex,
                "-c:v", "h264_nvenc",
                "-preset", "p1", # Use the chosen preset
                "-rc", "vbr",
                "-cq", "18",
                "-c:a", "copy", # Audio can still be copied without re-encoding
                output_video
            ]

        subprocess.run(command, check=True)

    except subprocess.CalledProcessError as e:
        print(f"Erro ao adicionar a marca d'água: {e.stderr.decode('utf-8') if e.stderr else e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
