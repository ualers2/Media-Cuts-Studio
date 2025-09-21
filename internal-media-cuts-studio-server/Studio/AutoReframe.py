# python3 /app/Studio/AutoReframe.py
import cv2
import subprocess
import os
from ultralytics import YOLO
import numpy as np
import math
from pathlib import Path
import time
from dotenv import load_dotenv
diretorio_script = os.path.dirname(os.path.abspath(__file__)) 
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "Keys", "env.env"))
PRODUCTION_ENV = os.getenv("PRODUCTION_ENV", "True")
if PRODUCTION_ENV == "True":
    # Production
    dockerffmpegGPU = True
    show_preview = False
elif PRODUCTION_ENV == "False":
    # Local test
    dockerffmpegGPU = False
    path_ffmpeg = os.path.join(diretorio_script, 'Utils', 'ffmpeg', 'ffmpeg.exe')
    path_ffmpegnotexe = os.path.join(diretorio_script, 'Utils', 'ffmpeg')
    os.environ['PATH'] = path_ffmpegnotexe + os.pathsep + os.environ['PATH']
    show_preview = True

class AutoReframe:
    """
    Automatiza o reframing de vídeos de podcast para um formato vertical (9:16),
    focando em rostos detectados por YOLOv8/YOLOv11 e utilizando FFmpeg para processamento.
    """

    def __init__(self, 
                ass_file_path,
                input_video_path, 
                output_video_mp4="output.mp4", 
                yolo_model_path='yolov11n-face.pt',
                CONF_MIN=0.75,
                CONF_MAX=0.99,
                stability_threshold_frames=30, # NOVO: Limite de frames para estabilidade
                min_move_pixels   = 550,     # mínimo de deslocamento (px) para reposicionar
                padding_x_ratio_left=0.2, 
                padding_x_ratio_right=0.2,
                padding_y_ratio_top=0.3, 
                padding_y_ratio_bottom=0.3, 
                fixed_padding_x_left=70, 
                fixed_padding_x_right=70,  
                fixed_padding_y_top=150, 
                fixed_padding_y_bottom=150, 
                target_width=1080, 
                target_aspect_ratio=(9, 16),
                text_overlay="Seu Texto Aqui", 
                font_path="Future",
                captions_alignment=2,
                captions_fontsize=6,
                captions_color="white",
                subtitle_fontsize=20,
                subtitle_fontcolor="white",
                SubtitleVerticalReference="+20",
                show_preview=True,
                dockerffmpegGPU=True, 
                task_id_db_str="",
                video_type="podcast" # NOVO PARÂMETRO
                ):
        self.video_type = video_type # Armazenar o tipo de vídeo
        self.output_video_mp4 =output_video_mp4
        self.dockerffmpegGPU = dockerffmpegGPU
        self.inicio = time.time()
        self.padding_x_ratio_left = padding_x_ratio_left
        self.padding_x_ratio_right = padding_x_ratio_right
        self.padding_y_ratio_top = padding_y_ratio_top
        self.padding_y_ratio_bottom = padding_y_ratio_bottom
        self.fixed_padding_x_left = fixed_padding_x_left
        self.fixed_padding_x_right = fixed_padding_x_right
        self.fixed_padding_y_top = fixed_padding_y_top
        self.fixed_padding_y_bottom = fixed_padding_y_bottom
        self.padding_x_ratio = padding_x_ratio_left
        self.padding_y_ratio = padding_y_ratio_top
        self.fixed_padding_x = fixed_padding_x_left
        self.fixed_padding_y = fixed_padding_y_top
        self.ass_file_path = ass_file_path 
        self.font_path = font_path# "Future" 
        self.captions_alignment = captions_alignment #  # 2 = Centro inferior. Veja documentação ASS/FFmpeg para outros valores
        self.captions_fontsize = captions_fontsize # # Tamanho da fonte para as legendas
        self.captions_color = captions_color # # Cor das legendas
        self.subtitle_fontsize = subtitle_fontsize #
        self.subtitle_fontcolor = subtitle_fontcolor #
        self.SubtitleVerticalReference = SubtitleVerticalReference
        print(f"Padding de recorte: Proporcional X_Left={self.padding_x_ratio_left}, X_Right={self.padding_x_ratio_right}, Y_Top={self.padding_y_ratio_top}, Y_Bottom={self.padding_y_ratio_bottom} | Fixo X_Left={self.fixed_padding_x_left}px, X_Right={self.fixed_padding_x_right}px, Y_Top={self.fixed_padding_y_top}px, Y_Bottom={self.fixed_padding_y_bottom}px")
        self.input_video_path = Path(input_video_path)
        if not self.input_video_path.exists():
            raise FileNotFoundError(f"Vídeo de entrada não encontrado: {input_video_path}")
        output_video = os.path.join(os.path.dirname(__file__), "WorkEnvironment", "Process", "AIReframe")
        self.output_dir = Path(output_video)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.yolo_model_path = yolo_model_path
        self.model = self._load_yolo_model()
        self.target_aspect_ratio = target_aspect_ratio
        self.target_width = target_width
        self.target_height = int(target_width * target_aspect_ratio[1] / target_aspect_ratio[0])
        self.text_overlay = text_overlay
        self.show_preview = show_preview
        primeiros_5 = task_id_db_str[:5]
        self.video_cima_temp_path = self.output_dir / f"video_cima_temp_{primeiros_5}.mp4"
        self.video_baixo_temp_path = self.output_dir / f"video_baixo_temp_{primeiros_5}.mp4"
        self.video_single_temp_path = self.output_dir / f"video_single_temp_{primeiros_5}.mp4"
        self.audio_original_path = self.output_dir / f"audio_original_{primeiros_5}.aac"
        self.final_output_path = output_video_mp4 #self.output_dir / f"{self.input_video_path.stem}_reframe.mp4"
        self.min_move_pixels   = min_move_pixels     # mínimo de deslocamento (px) para reposicionar
        self.p1_assigned_to_top_slot = None # True if P1 is top, False if P1 is bottom, None if not yet determined or only one person
        self.person_id_p1 = -1 # ID da Pessoa 1
        self.person_id_p2 = -1 # ID da Pessoa 2
        self.last_bbox_p1 = None # Última bbox conhecida para Pessoa 1
        self.last_bbox_p2 = None # Última bbox conhecida para Pessoa 2
        self.last_crop_p1 = None # Último recorte usado para Pessoa 1 (x, y, w, h)
        self.last_crop_p2 = None # Último recorte usado para Pessoa 2
        self.last_center_p1    = None   # centro usado no frame anterior (Pessoa 1)
        self.last_center_p2    = None   # centro usado no frame anterior (Pessoa 2)
        self.last_gamer_face_stable_crop = None # Novo: Armazena o último recorte estável do gamer
        self.move_threshold_pixels = min_move_pixels
        
        self.CONF_MIN = CONF_MIN 
        self.CONF_MAX = CONF_MAX 
        # NOVO: Variáveis para controle de estabilidade
        self.stability_threshold_frames = stability_threshold_frames 
        self.face_stability_counters = {} # {track_id: consecutive_detection_count}

        print(f"AutoReframe inicializado para: {self.input_video_path.name}")
        print(f"Saída será salva em: {self.output_dir}")

    def _load_yolo_model(self):
        """Carrega o modelo YOLO."""
        print(f"Carregando modelo YOLO: {self.yolo_model_path}...")
        try:
            model = YOLO(self.yolo_model_path, task='detect')
            return model
        except Exception as e:
            raise RuntimeError(f"Erro ao carregar o modelo YOLO: {e}")

    def _run_ffmpeg_command(self, command, description="FFmpeg"):
        """Executa um comando FFmpeg e lida com erros."""
        print(f"Executando {description}...")
        try:
            subprocess.run(command, check=True, capture_output=True, text=True) # Added check=True, capture_output, text
            print(f"{description} concluído com sucesso.")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar {description}:")
            print(f"Comando: {' '.join(e.cmd)}")
            print(f"Stdout: {e.stdout}")
            print(f"Stderr: {e.stderr}")
            raise RuntimeError(f"FFmpeg command failed: {e}")
        except FileNotFoundError:
            raise RuntimeError("FFmpeg não encontrado. Certifique-se de que está instalado e no PATH.")

    def _get_video_properties(self, video_path):
        """Obtém as propriedades de largura, altura e FPS de um vídeo usando OpenCV."""
        cap = cv2.VideoCapture(str(video_path))
        if not cap.isOpened():
            raise IOError(f"Não foi possível abrir o vídeo: {video_path}")
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        cap.release()
        return width, height, fps
    

    def analyze_and_get_crop_coords(self):
        """
        Analisa o vídeo frame a frame, detecta e rastreia rostos com YOLO e calcula
        as coordenadas de recorte para os dois rostos principais, aplicando padding fixo e proporcional.
        Retorna as coordenadas e o número de pessoas detectadas por frame.
        """
        print("Iniciando análise de vídeo para detecção e rastreamento de rostos...")
        cap = cv2.VideoCapture(str(self.input_video_path))
        if not cap.isOpened():
            raise IOError(f"Não foi possível abrir o vídeo: {self.input_video_path}")

        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        all_crop_data = [] # Armazena (coords_p1_for_output, coords_p2_for_output, num_detected_faces)
        
        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            results = self.model.track(frame, persist=True, conf=self.CONF_MIN, iou=0.5)
            
            if self.video_type == "podcast":
                    
                current_frame_tracked_faces = [] # Faces detectadas no frame atual, com IDs
                if results[0].boxes.id is not None:
                    for box in results[0].boxes:
                        confidence = float(box.conf[0])
                        if box.id is not None and self.CONF_MIN <= confidence <= self.CONF_MAX:
                            x1, y1, x2, y2 = map(int, box.xyxy[0])
                            track_id = int(box.id[0])
                            current_frame_tracked_faces.append({
                                'bbox': (x1, y1, x2, y2),
                                'confidence': confidence,
                                'id': track_id
                            })
                
                # NOVO: Atualizar contadores de estabilidade e filtrar faces estáveis
                current_frame_ids = {f['id'] for f in current_frame_tracked_faces}
                stable_faces = []
                
                # Incrementar contadores para IDs presentes no frame atual
                for face in current_frame_tracked_faces:
                    track_id = face['id']
                    self.face_stability_counters[track_id] = self.face_stability_counters.get(track_id, 0) + 1
                    if self.face_stability_counters[track_id] >= self.stability_threshold_frames:
                        stable_faces.append(face)
                
                # Resetar contadores para IDs que não estão mais presentes no frame atual
                ids_to_remove = [tid for tid in self.face_stability_counters if tid not in current_frame_ids]
                for tid in ids_to_remove:
                    self.face_stability_counters[tid] = 0 # Reinicia o contador para 0
                    # Opcional: del self.face_stability_counters[tid] se quiser remover completamente

                # A partir daqui, toda a lógica de recorte e atribuição usará 'stable_faces'
                # em vez de 'tracked_faces' ou 'current_frame_tracked_faces'.
                current_faces_by_id = {f['id']: f['bbox'] for f in stable_faces}
                num_detected_faces_current_frame = len(stable_faces)

                # --- Logic for 3 or more people (Comprehensive Bounding Box) ---
                if num_detected_faces_current_frame >= 3:
                    min_x = frame_width
                    min_y = frame_height
                    max_x = 0
                    max_y = 0

                    for face in stable_faces: # Alterado de tracked_faces para stable_faces
                        x1, y1, x2, y2 = face['bbox']
                        min_x = min(min_x, x1)
                        min_y = min(min_y, y1)
                        max_x = max(max_x, x2)
                        max_y = max(max_y, y2)
                    
                    comprehensive_bbox = (min_x, min_y, max_x, max_y)
                    coords_single_slot_raw = self._calculate_padded_coords(comprehensive_bbox, frame_width, frame_height)
                    coords_single_slot = self._adjust_coords_to_aspect_ratio(coords_single_slot_raw, frame_width, frame_height, self.target_aspect_ratio)

                    # Store as last_crop_p1 (since it's the single main crop for all)
                    self.last_crop_p1 = coords_single_slot
                    coords_top_slot = coords_single_slot
                    coords_bottom_slot = coords_single_slot # Will be ignored
                    num_people_in_frame_for_output = 3

                    self.person_id_p1 = -1
                    self.person_id_p2 = -1
                    self.last_bbox_p1 = None
                    self.last_bbox_p2 = None
                    self.p1_assigned_to_top_slot = None

                # --- Logic to assign and persist P1 and P2 IDs (for 1 or 2 people) ---
                else: # num_detected_faces_current_frame < 3
                    found_p1_current = False
                    found_p2_current = False

                    if self.person_id_p1 != -1 and self.person_id_p1 in current_faces_by_id:
                        self.last_bbox_p1 = current_faces_by_id[self.person_id_p1]
                        found_p1_current = True
                    
                    if self.person_id_p2 != -1 and self.person_id_p2 in current_faces_by_id:
                        self.last_bbox_p2 = current_faces_by_id[self.person_id_p2]
                        found_p2_current = True

                    # NOVO: Filtra 'available_faces' para incluir apenas faces estáveis
                    available_faces = [f for f in stable_faces if f['id'] != self.person_id_p1 and f['id'] != self.person_id_p2]
                    available_faces.sort(key=lambda f: f['bbox'][0]) 

                    if not found_p1_current and len(available_faces) > 0:
                        self.person_id_p1 = available_faces[0]['id']
                        self.last_bbox_p1 = available_faces[0]['bbox']
                        found_p1_current = True
                        available_faces = [f for f in available_faces if f['id'] != self.person_id_p1]

                    if not found_p2_current and len(available_faces) > 0:
                        self.person_id_p2 = available_faces[0]['id']
                        self.last_bbox_p2 = available_faces[0]['bbox']
                        found_p2_current = True
                    
                    if not found_p1_current:
                        self.person_id_p1 = -1
                        self.last_bbox_p1 = None
                        self.p1_assigned_to_top_slot = None
                        self.last_crop_p1 = None # Reset last crop for P1
                    if not found_p2_current:
                        self.person_id_p2 = -1
                        self.last_bbox_p2 = None
                        self.p1_assigned_to_top_slot = None
                        self.last_crop_p2 = None # Reset last crop for P2


                    # --- Calculate crop coordinates based on who is present ---
                    coords_top_slot = None
                    coords_bottom_slot = None
                    num_people_in_frame_for_output = 0

                    if self.last_bbox_p1 is not None and self.last_bbox_p2 is not None:
                        num_people_in_frame_for_output = 2
                        
                        # Logic to determine if P1's crop should be updated
                        if self.last_crop_p1 is None or not self._is_bbox_within_crop(self.last_bbox_p1, self.last_crop_p1, frame_width, frame_height):
                            coords_for_p1_id_raw = self._calculate_padded_coords(self.last_bbox_p1, frame_width, frame_height)
                            adjusted_coords_p1_id_ar = self._adjust_coords_to_aspect_ratio(coords_for_p1_id_raw, frame_width, frame_height, (self.target_aspect_ratio[0], self.target_aspect_ratio[1] / 2))
                            self.last_crop_p1 = adjusted_coords_p1_id_ar
                        
                        # Logic to determine if P2's crop should be updated
                        if self.last_crop_p2 is None or not self._is_bbox_within_crop(self.last_bbox_p2, self.last_crop_p2, frame_width, frame_height):
                            coords_for_p2_id_raw = self._calculate_padded_coords(self.last_bbox_p2, frame_width, frame_height)
                            adjusted_coords_p2_id_ar = self._adjust_coords_to_aspect_ratio(coords_for_p2_id_raw, frame_width, frame_height, (self.target_aspect_ratio[0], self.target_aspect_ratio[1] / 2))
                            self.last_crop_p2 = adjusted_coords_p2_id_ar
                        
                        # Ensure both crops are not None before assigning
                        if self.last_crop_p1 and self.last_crop_p2:
                            # NEW LOGIC: Persist top/bottom assignment
                            if self.p1_assigned_to_top_slot is None:
                                if self.last_crop_p1[1] < self.last_crop_p2[1]:
                                    self.p1_assigned_to_top_slot = True
                                else:
                                    self.p1_assigned_to_top_slot = False
                            
                            if self.p1_assigned_to_top_slot:
                                coords_top_slot = self.last_crop_p1
                                coords_bottom_slot = self.last_crop_p2
                            else:
                                coords_top_slot = self.last_crop_p2
                                coords_bottom_slot = self.last_crop_p1
                        else:
                            # Fallback if one crop is somehow not determined, treat as single person or default
                            num_people_in_frame_for_output = 0
                            coords_top_slot = self._get_default_crop(frame_width, frame_height)
                            coords_bottom_slot = coords_top_slot
                            self.p1_assigned_to_top_slot = None


                    elif self.last_bbox_p1 is not None: # Only P1's ID is being tracked
                        num_people_in_frame_for_output = 1
                        if self.last_crop_p1 is None or not self._is_bbox_within_crop(self.last_bbox_p1, self.last_crop_p1, frame_width, frame_height):
                            coords_for_p1_id_raw = self._calculate_padded_coords(self.last_bbox_p1, frame_width, frame_height)
                            self.last_crop_p1 = self._adjust_coords_to_aspect_ratio(coords_for_p1_id_raw, frame_width, frame_height, self.target_aspect_ratio)
                        
                        coords_top_slot = self.last_crop_p1
                        coords_bottom_slot = coords_top_slot
                        self.p1_assigned_to_top_slot = None

                    elif self.last_bbox_p2 is not None: # Only P2's ID is being tracked (promote to P1 for single slot)
                        num_people_in_frame_for_output = 1
                        if self.last_crop_p2 is None or not self._is_bbox_within_crop(self.last_bbox_p2, self.last_crop_p2, frame_width, frame_height):
                            coords_for_p2_id_raw = self._calculate_padded_coords(self.last_bbox_p2, frame_width, frame_height)
                            self.last_crop_p2 = self._adjust_coords_to_aspect_ratio(coords_for_p2_id_raw, frame_width, frame_height, self.target_aspect_ratio)
                        
                        coords_top_slot = self.last_crop_p2 # Use P2's crop as the main one
                        coords_bottom_slot = coords_top_slot
                        self.p1_assigned_to_top_slot = None

                    else: # Zero rostos detectados ou rastreados
                        num_people_in_frame_for_output = 0
                        coords_top_slot = self._get_default_crop(frame_width, frame_height)
                        coords_bottom_slot = coords_top_slot
                        self.p1_assigned_to_top_slot = None
                        self.last_crop_p1 = None # Reset if no people
                        self.last_crop_p2 = None # Reset if no people

                # Determine which person's ID is in the top/bottom slot for display purposes
                id_top_slot = -1
                id_bottom_slot = -1
                if num_people_in_frame_for_output == 2:
                    if self.p1_assigned_to_top_slot:
                        id_top_slot = self.person_id_p1
                        id_bottom_slot = self.person_id_p2
                    else:
                        id_top_slot = self.person_id_p2
                        id_bottom_slot = self.person_id_p1
                elif num_people_in_frame_for_output == 1:
                    id_top_slot = self.person_id_p1 if self.person_id_p1 != -1 else self.person_id_p2
                elif num_people_in_frame_for_output >= 3:
                    id_top_slot = "ALL" # Special ID for comprehensive view
                    id_bottom_slot = "ALL"


                all_crop_data.append({
                    'person1_coords': coords_top_slot,  # This will be the top visual crop (or the comprehensive crop)
                    'person2_coords': coords_bottom_slot, # This will be the bottom visual crop (or ignored for single/all)
                    'num_faces': num_people_in_frame_for_output, # Crucial for deciding rendering logic
                    'person_id_top': id_top_slot, # ID of the person in the top slot for display
                    'person_id_bottom': id_bottom_slot # ID of the person in the bottom slot for display
                })

                # --- Pré-visualização dos frames ---
                if self.show_preview:
                    display_frame = frame.copy()

                    # Draw the YOLO detected bounding boxes (all of them)
                    for face in current_frame_tracked_faces: # Exibe todas as detecções YOLO, antes do filtro de estabilidade
                        x1_orig, y1_orig, x2_orig, y2_orig = face['bbox']
                        color = (0, 255, 0) # Green for YOLO detections
                        label = f'ID: {face["id"]} Conf: {face["confidence"]:.2f}'
                        
                        if face['id'] == self.person_id_p1:
                            color = (255, 0, 0) # Blue for Persona 1 (tracked ID)
                            label = f"Pessoa 1 Conf: {face['confidence']:.2f}"
                        elif face['id'] == self.person_id_p2:
                            color = (0, 0, 255) # Red for Persona 2 (tracked ID)
                            label = f"Pessoa 2 Conf: {face['confidence']:.2f}"

                        # NOVO: Indicar se a face é estável ou não na pré-visualização
                        if face['id'] in self.face_stability_counters and self.face_stability_counters[face['id']] >= self.stability_threshold_frames:
                            label += f" (Estavel {self.face_stability_counters[face['id']]})"
                            color = (0, 255, 255) # Amarelo para faces estáveis
                        else:
                            label += f" (Instavel {self.face_stability_counters.get(face['id'], 0)})"
                            color = (0, 165, 255) # Laranja para faces instáveis

                        cv2.rectangle(display_frame, (x1_orig, y1_orig), (x2_orig, y2_orig), color, 2)
                        cv2.putText(display_frame, label, (x1_orig, y1_orig - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

                    if num_people_in_frame_for_output >= 3:
                        # Draw the comprehensive bounding box
                        x, y, w, h = coords_top_slot # coords_top_slot holds the comprehensive bbox
                        cv2.rectangle(display_frame, (x, y), (x + w, y + h), (255, 255, 0), 2) # Yellow for comprehensive
                        cv2.putText(display_frame, "Todas as Pessoas (Bounding Box Abrangente)", (x, y - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
                    elif num_people_in_frame_for_output == 2:
                        # Draw the calculated crop areas for the two persons
                        colors = [(255, 0, 0), (0, 0, 255)] # Blue for top crop, Red for bottom crop
                        
                        id_top_slot_display = all_crop_data[-1]['person_id_top']
                        id_bottom_slot_display = all_crop_data[-1]['person_id_bottom']

                        label_top = f"Recorte Cima (ID:{id_top_slot_display})"
                        label_bottom = f"Recorte Baixo (ID:{id_bottom_slot_display})"

                        x, y, w, h = coords_top_slot
                        cv2.rectangle(display_frame, (x, y), (x + w, y + h), colors[0], 2)
                        cv2.putText(display_frame, label_top, (x, y - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, colors[0], 2)

                        x, y, w, h = coords_bottom_slot
                        cv2.rectangle(display_frame, (x, y), (x + w, y + h), colors[1], 2)
                        cv2.putText(display_frame, label_bottom, (x, y - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, colors[1], 2)

                    elif num_people_in_frame_for_output == 1:
                        # Draw the calculated crop area for the single person occupying full height
                        x, y, w, h = coords_top_slot
                        cv2.rectangle(display_frame, (x, y), (x + w, y + h), (255, 255, 0), 2) # Yellow for single person
                        cv2.putText(display_frame, f"Pessoa unica (ID:{id_top_slot})", (x, y - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
                    else: # 0 faces
                        x, y, w, h = coords_top_slot # Using top_slot as placeholder for default full frame crop
                        cv2.rectangle(display_frame, (x, y), (x + w, y + h), (128, 128, 128), 2) # Gray for no faces
                        cv2.putText(display_frame, "Nenhuma Pessoa (Default)", (x, y - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (128, 128, 128), 2)
                    
                    max_display_width = 1280
                    max_display_height = 720
                    if display_frame.shape[1] > max_display_width or display_frame.shape[0] > max_display_height:
                        scale = min(max_display_width / display_frame.shape[1], max_display_height / display_frame.shape[0])
                        display_frame = cv2.resize(display_frame, (int(display_frame.shape[1] * scale), int(display_frame.shape[0] * scale)))
                    cv2.imshow("Pré-visualização do YOLO e Recortes", display_frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        print("Pré-visualização interrompida pelo usuário.")
                        break
                frame_count += 1
                if frame_count % 100 == 0:
                    print(f"Processando frame {frame_count}/{total_frames}...")

            elif self.video_type == "game":
                gamer_face_bbox = None
                if results[0].boxes.id is not None:
                    tracked_faces_in_frame = []
                    for i in range(len(results[0].boxes.id)):
                        confidence = float(results[0].boxes.conf[i])
                        if self.CONF_MIN <= confidence <= self.CONF_MAX:
                            x1, y1, x2, y2 = map(int, results[0].boxes.xyxy[i])
                            track_id = int(results[0].boxes.id[i])
                            tracked_faces_in_frame.append({'bbox': (x1, y1, x2, y2), 'confidence': confidence, 'id': track_id})

                    if self.person_id_p1 != -1 and self.person_id_p1 in {f['id'] for f in tracked_faces_in_frame}:
                        gamer_face_bbox = next(f['bbox'] for f in tracked_faces_in_frame if f['id'] == self.person_id_p1)
                    elif tracked_faces_in_frame:
                        tracked_faces_in_frame.sort(key=lambda f: f['confidence'], reverse=True)
                        gamer_face_bbox = tracked_faces_in_frame[0]['bbox']
                        self.person_id_p1 = tracked_faces_in_frame[0]['id']

                coords_gamer_face_adjusted = None # Inicializa como None

                if gamer_face_bbox:
                    # Calcula o recorte com padding para a detecção atual
                    current_padded_crop = self._calculate_padded_coords(gamer_face_bbox, frame_width, frame_height)
                    
                    # Lógica para "grudar" o recorte da face do gamer
                    if self.last_gamer_face_stable_crop is None:
                        # Se não há um recorte estável anterior, use o atual
                        self.last_gamer_face_stable_crop = current_padded_crop
                    else:
                        # Calcula a distância do centro da detecção atual para o centro do último recorte estável
                        # Nota: Poderíamos usar _is_bbox_within_crop aqui também, mas uma simples distância é suficiente para o movimento do centro.
                        x_curr_center = gamer_face_bbox[0] + (gamer_face_bbox[2] - gamer_face_bbox[0]) / 2
                        y_curr_center = gamer_face_bbox[1] + (gamer_face_bbox[3] - gamer_face_bbox[1]) / 2

                        x_stable_center = self.last_gamer_face_stable_crop[0] + self.last_gamer_face_stable_crop[2] / 2
                        y_stable_center = self.last_gamer_face_stable_crop[1] + self.last_gamer_face_stable_crop[3] / 2

                        distance = np.sqrt((x_curr_center - x_stable_center)**2 + (y_curr_center - y_stable_center)**2)

                        if distance > self.move_threshold_pixels:
                            # Se a face se moveu significativamente, atualize o recorte estável
                            self.last_gamer_face_stable_crop = current_padded_crop
                    
                    # Usa o recorte estável como o recorte final para o gamer
                    coords_gamer_face_adjusted = self.last_gamer_face_stable_crop
                else:
                    # Se não detectou a face, pode-se decidir manter o último recorte estável
                    # ou deixar como None para gerar uma tela preta se não houver detecção por muito tempo.
                    # Para evitar tremedeira em ausências momentâneas, é melhor manter o último.
                    coords_gamer_face_adjusted = self.last_gamer_face_stable_crop # Mantém o último recorte estável
                    # Você pode adicionar um contador aqui para zerar last_gamer_face_stable_crop se a face estiver ausente por X frames.

                # Lógica para o recorte da tela do jogo (continua a mesma)
                game_slot_height_target = self.target_height - (self.target_height // 3)
                target_game_slot_aspect = self.target_width / game_slot_height_target

                current_game_aspect = frame_width / frame_height
                
                # Coordenadas do recorte da tela do jogo (originalmente 'person2_coords')
                # Por padrão, vamos centralizar horizontalmente e recortar verticalmente, se necessário
                # ou manter a largura total e calcular a altura necessária.

                coords_game_screen_crop = (0, 0, frame_width, frame_height) # Início: usa o frame inteiro
                
                # Ajustar para a proporção alvo do slot do jogo
                actual_crop_width_game = frame_width
                actual_crop_height_game = int(frame_width / target_game_slot_aspect)

                if actual_crop_height_game > frame_height:
                    # Se a altura necessária for maior que a altura do frame, ajuste pela altura do frame
                    actual_crop_height_game = frame_height
                    actual_crop_width_game = int(frame_height * target_game_slot_aspect)
                
                # Centralizar o recorte do jogo
                x_game_crop = max(0, (frame_width - actual_crop_width_game) // 2)
                y_game_crop = max(0, (frame_height - actual_crop_height_game) // 2)

                coords_game_screen_crop = (x_game_crop, y_game_crop, actual_crop_width_game, actual_crop_height_game)


                all_crop_data.append({
                    'person1_coords': coords_gamer_face_adjusted if coords_gamer_face_adjusted else self._get_default_crop(frame_width, frame_height), # Recorte da face do gamer
                    'person2_coords': coords_game_screen_crop, # Recorte da tela do jogo
                    'num_faces': 1 if gamer_face_bbox else 0, # Indica se detectou o gamer
                    'person_id_top': self.person_id_p1,
                    'person_id_bottom': None # Não aplicável para o slot do jogo
                })

                # --- Pré-visualização para o tipo "game" ---
                if self.show_preview:
                    display_frame = frame.copy()

                    # Desenhar a bounding box da detecção YOLO original (verde)
                    for face in tracked_faces_in_frame:
                        x1_orig, y1_orig, x2_orig, y2_orig = face['bbox']
                        cv2.rectangle(display_frame, (x1_orig, y1_orig), (x2_orig, y2_orig), (0, 255, 0), 2)
                        cv2.putText(display_frame, f"YOLO ID:{face['id']} Conf:{face['confidence']:.2f}", (x1_orig, y1_orig - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

                    # Desenhar o recorte ESTÁVEL da face do gamer (azul)
                    if self.last_gamer_face_stable_crop:
                        x, y, w, h = self.last_gamer_face_stable_crop
                        cv2.rectangle(display_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        cv2.putText(display_frame, "Face Gamer (Estavel)", (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
                    
                    # Desenhar o recorte da tela do jogo (vermelho)
                    x_g, y_g, w_g, h_g = coords_game_screen_crop
                    cv2.rectangle(display_frame, (x_g, y_g), (x_g + w_g, y_g + h_g), (0, 0, 255), 2)
                    cv2.putText(display_frame, "Tela Jogo", (x_g, y_g - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

                    max_display_width = 1280
                    max_display_height = 720
                    if display_frame.shape[1] > max_display_width or display_frame.shape[0] > max_display_height:
                        scale = min(max_display_width / display_frame.shape[1], max_display_height / display_frame.shape[0])
                        display_frame = cv2.resize(display_frame, (int(display_frame.shape[1] * scale), int(display_frame.shape[0] * scale)))
                    cv2.imshow("Pré-visualização do YOLO e Recortes (Game)", display_frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        print("Pré-visualização interrompida pelo usuário.")
                        break
                frame_count += 1
                if frame_count % 100 == 0:
                    print(f"Processando frame {frame_count}/{total_frames}...")

        # ESTAS LINHAS DEVEM ESTAR AQUI, FORA DO LOOP WHILE
        cap.release()
        if self.show_preview:
            cv2.destroyAllWindows()
        print("Análise de vídeo concluída.")
        return all_crop_data


    def generate_final_composite_video(self, all_crop_data):
        """
        Gera um único vídeo temporário já no formato final vertical (9:16),
        aplicando a lógica de recorte para 1, 2 ou mais pessoas.
        """
        input_width, input_height, input_fps = self._get_video_properties(self.input_video_path)

        print("Gerando vídeo composto final com lógica de 1, 2 ou mais pessoas...")

        cap = cv2.VideoCapture(str(self.input_video_path))
        if not cap.isOpened():
            raise IOError(f"Não foi possível abrir o vídeo: {self.input_video_path}")

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        
        out_stream = cv2.VideoWriter(str(self.video_single_temp_path), fourcc, input_fps, (self.target_width, self.target_height))

        frame_idx = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            current_frame_data = all_crop_data[frame_idx]
            num_faces = current_frame_data['num_faces']
            
            final_composite_frame = np.zeros((self.target_height, self.target_width, 3), dtype=np.uint8) # Frame preto inicial
           
            if self.video_type == "podcast":
                if num_faces >= 3:

                    # Três ou mais pessoas: usar a bounding box abrangente para preencher a tela toda

                    x_comp, y_comp, w_comp, h_comp = current_frame_data['person1_coords'] # This holds the comprehensive bbox

                    # Ensure coordinates are within frame bounds

                    x_comp = max(0, x_comp)

                    y_comp = max(0, y_comp)

                    w_comp = min(w_comp, input_width - x_comp)

                    h_comp = min(h_comp, input_height - y_comp)





                    if w_comp > 0 and h_comp > 0: # Check if crop dimensions are valid

                        cropped_frame_comprehensive = frame[y_comp : y_comp + h_comp, x_comp : x_comp + w_comp]

                        resized_comprehensive = cv2.resize(cropped_frame_comprehensive, (self.target_width, self.target_height))

                        final_composite_frame = resized_comprehensive

                    else:

                        print(f"Warning: Invalid comprehensive crop dimensions at frame {frame_idx}. Using black frame.")

                    # final_composite_frame remains black

                elif num_faces == 2:

                    # Duas pessoas: cortar e empilhar

                    x_top, y_top, w_top, h_top = current_frame_data['person1_coords'] # These are already sorted by Y (or consistently assigned)

                    x_bottom, y_bottom, w_bottom, h_bottom = current_frame_data['person2_coords']



                    # Garantir que as coordenadas são válidas para recorte

                    x_top = max(0, x_top)

                    y_top = max(0, y_top)

                    w_top = min(w_top, input_width - x_top)

                    h_top = min(h_top, input_height - y_top)



                    x_bottom = max(0, x_bottom)

                    y_bottom = max(0, y_bottom)

                    w_bottom = min(w_bottom, input_width - x_bottom)

                    h_bottom = min(h_bottom, input_height - y_bottom)





                    cropped_frame_top = np.zeros((h_top, w_top, 3), dtype=np.uint8)

                    cropped_frame_bottom = np.zeros((h_bottom, w_bottom, 3), dtype=np.uint8)



                    if w_top > 0 and h_top > 0:

                        cropped_frame_top = frame[y_top : y_top + h_top, x_top : x_top + w_top]

                    else:

                        print(f"Warning: Invalid top crop dimensions at frame {frame_idx}. Using black frame for top.")



                    if w_bottom > 0 and h_bottom > 0:

                        cropped_frame_bottom = frame[y_bottom : y_bottom + h_bottom, x_bottom : x_bottom + w_bottom]

                    else:

                        print(f"Warning: Invalid bottom crop dimensions at frame {frame_idx}. Using black frame for bottom.")



                    # Redimensionar para metade da altura total

                    resized_top = self._resize_and_crop_to_fit(cropped_frame_top, self.target_width, self.target_height // 2)
                    resized_bottom = self._resize_and_crop_to_fit(cropped_frame_bottom, self.target_width, self.target_height // 2)


                    # Empilhar os dois vídeos

                    final_composite_frame[:self.target_height // 2, :] = resized_top

                    final_composite_frame[self.target_height // 2:, :] = resized_bottom


                elif num_faces == 1:
                    # Uma pessoa: cortar e preencher a tela inteira
                    x_single, y_single, w_single, h_single = current_frame_data['person1_coords']
                    
                    x_single = max(0, x_single)
                    y_single = max(0, y_single)
                    w_single = min(w_single, input_width - x_single)
                    h_single = min(h_single, input_height - y_single)

                    if w_single > 0 and h_single > 0:
                        cropped_frame_single = frame[y_single : y_single + h_single, x_single : x_single + w_single]
                                        
                        # *** MUDANÇA AQUI: Usar _resize_and_crop_to_fit ***
                        resized_single = self._resize_and_crop_to_fit(cropped_frame_single, self.target_width, self.target_height)
                        final_composite_frame = resized_single
                    else:
                        print(f"Warning: Invalid single crop dimensions at frame {frame_idx}. Using black frame.")
                        # final_composite_frame remains black
                else:
                    # Zero pessoas: fallback, use person1_coords (which is the default full frame crop)
                    x_default, y_default, w_default, h_default = current_frame_data['person1_coords']
                    
                    x_default = max(0, x_default)
                    y_default = max(0, y_default)
                    w_default = min(w_default, input_width - x_default)
                    h_default = min(h_default, input_height - y_default)

                    if w_default > 0 and h_default > 0:
                        cropped_frame_default = frame[y_default : y_default + h_default, x_default : x_default + w_default]
                        resized_default = cv2.resize(cropped_frame_default, (self.target_width, self.target_height))
                        final_composite_frame = resized_default
                    else:
                        print(f"Warning: Invalid default crop dimensions at frame {frame_idx}. Using black frame.")
                        # final_composite_frame remains black
            

            elif self.video_type == "game":
                x_gamer, y_gamer, w_gamer, h_gamer = current_frame_data['person1_coords']
                x_game, y_game, w_game, h_game = current_frame_data['person2_coords']

                # Garantir que as coordenadas são válidas para recorte para o gamer
                x_gamer = max(0, x_gamer)
                y_gamer = max(0, y_gamer)
                w_gamer = min(w_gamer, input_width - x_gamer)
                h_gamer = min(h_gamer, input_height - y_gamer)

                # Garantir que as coordenadas são válidas para recorte para o jogo
                x_game = max(0, x_game)
                y_game = max(0, y_game)
                w_game = min(w_game, input_width - x_game)
                h_game = min(h_game, input_height - y_game)


                cropped_gamer_face = np.zeros((h_gamer, w_gamer, 3), dtype=np.uint8)
                if w_gamer > 0 and h_gamer > 0:
                    cropped_gamer_face = frame[y_gamer : y_gamer + h_gamer, x_gamer : x_gamer + w_gamer]
                else:
                    print(f"Warning: Invalid gamer face crop dimensions at frame {frame_idx}. Using black frame for gamer.")

                cropped_game_screen = np.zeros((h_game, w_game, 3), dtype=np.uint8)
                if w_game > 0 and h_game > 0:
                    cropped_game_screen = frame[y_game : y_game + h_game, x_game : x_game + w_game]
                else:
                    print(f"Warning: Invalid game screen crop dimensions at frame {frame_idx}. Using black frame for game.")

                # Dimensões dos slots no vídeo final
                target_face_slot_height = self.target_height // 3
                target_game_slot_height = self.target_height - target_face_slot_height

                # Redimensionar a face do gamer para preencher o slot superior (irá esticar se as proporções forem diferentes)
                resized_gamer_face = cv2.resize(cropped_gamer_face, (self.target_width, target_face_slot_height))

                # Redimensionar e preencher a tela do jogo no slot inferior
                resized_game_screen_padded = self._resize_and_pad_to_fit(cropped_game_screen, self.target_width, target_game_slot_height)

                # Empilhar verticalmente
                final_composite_frame[:target_face_slot_height, :] = resized_gamer_face
                final_composite_frame[target_face_slot_height:, :] = resized_game_screen_padded



            out_stream.write(final_composite_frame)
            frame_idx += 1
            if frame_idx % 100 == 0:
                print(f"Gerando frame composto {frame_idx}...")

        cap.release()
        out_stream.release()
        print("Vídeo composto final gerado via OpenCV.")




    def _resize_and_pad_to_fit(self, image, target_width, target_height):
        """
        Redimensiona uma imagem para caber dentro de uma largura e altura alvo,
        mantendo sua proporção original. Adiciona barras pretas (padding)
        se a proporção da imagem não corresponder à do alvo.

        Args:
            image (np.array): A imagem de entrada (recorte).
            target_width (int): A largura desejada para a imagem de saída.
            target_height (int): A altura desejada para a imagem de saída.

        Returns:
            np.array: A imagem redimensionada e com padding, no tamanho alvo.
        """
        h, w = image.shape[:2]
        target_aspect = target_width / target_height
        image_aspect = w / h

        if image_aspect > target_aspect:
            # Imagem é mais larga que o slot alvo -> ajustar pela largura
            new_w = target_width
            new_h = int(new_w / image_aspect)
            pad_y = (target_height - new_h) // 2
            pad_x = 0
        else:
            # Imagem é mais alta que o slot alvo ou proporção igual -> ajustar pela altura
            new_h = target_height
            new_w = int(new_h * image_aspect)
            pad_x = (target_width - new_w) // 2
            pad_y = 0

        resized_image = cv2.resize(image, (new_w, new_h))

        # Criar uma tela preta para o resultado
        padded_image = np.zeros((target_height, target_width, 3), dtype=np.uint8)
        padded_image[pad_y:pad_y + new_h, pad_x:pad_x + new_w] = resized_image
        
        return padded_image

    def should_update_bbox(self, track_id, bbox, last_center):
        x1, y1, x2, y2 = bbox
        cx, cy = (x1 + x2)/2, (y1 + y2)/2
        if last_center is None:
            return True, (cx, cy)
        dx = abs(cx - last_center[0])
        dy = abs(cy - last_center[1])
        if dx < self.min_move_pixels and dy < self.min_move_pixels:
            return False, last_center
        return True, (cx, cy)
    

    def _is_bbox_within_crop(self, bbox_face, crop_area, frame_width, frame_height, margin_ratio=0.05):
        """ Verifica se a bbox do rosto está dentro da área de recorte, com uma margem de tolerância. Retorna True se estiver dentro, False caso contrário. """
        fx1, fy1, fx2, fy2 = bbox_face[0], bbox_face[1], bbox_face[2], bbox_face[3]
        cx, cy, cw, ch = crop_area[0], crop_area[1], crop_area[2], crop_area[3]
        # Calculate a slightly larger crop area to allow for a margin
        margin_x = int(cw * margin_ratio)
        margin_y = int(ch * margin_ratio)
        expanded_cx1 = cx - margin_x
        expanded_cy1 = cy - margin_y
        expanded_cx2 = cx + cw + margin_x
        expanded_cy2 = cy + ch + margin_y
        # Check if face bbox is entirely within the expanded crop area
        is_within = (fx1 >= expanded_cx1 and fx2 <= expanded_cx2 and fy1 >= expanded_cy1 and fy2 <= expanded_cy2)
        return is_within


    def _get_default_crop(self, frame_width, frame_height):
        """ Retorna uma área de recorte padrão (centro da tela, com a proporção alvo). """
        # Calculate target width and height for the default crop
        target_w = self.target_width
        target_h = self.target_height
        # Ensure default crop respects original frame dimensions
        if target_w > frame_width:
            target_w = frame_width
            target_h = int(target_w * self.target_aspect_ratio[1] / self.target_aspect_ratio[0])
        if target_h > frame_height:
            target_h = frame_height
            target_w = int(target_h * self.target_aspect_ratio[0] / self.target_aspect_ratio[1])
        # Ensure even dimensions
        target_w = target_w - (target_w % 2)
        target_h = target_h - (target_h % 2)
        default_x = (frame_width - target_w) // 2
        default_y = (frame_height - target_h) // 2
        # Ensure even coordinates
        default_x = default_x - (default_x % 2)
        default_y = default_y - (default_y % 2)
        return (default_x, default_y, target_w, target_h)
    

    def _calculate_padded_coords(self, bbox, frame_width, frame_height):
        x1, y1, x2, y2 = bbox
        face_width = x2 - x1
        face_height = y2 - y1

        # Proportional padding based on face size
        prop_x_pad = face_width * (self.padding_x_ratio_left + self.padding_x_ratio_right) / 2 # Using average for simplicity in symmetric padding
        prop_y_pad_top = face_height * self.padding_y_ratio_top
        prop_y_pad_bottom = face_height * self.padding_y_ratio_bottom

        # Combined padding (proportional + fixed)
        pad_left = int(prop_x_pad + self.fixed_padding_x_left)
        pad_right = int(prop_x_pad + self.fixed_padding_x_right)
        pad_top = int(prop_y_pad_top + self.fixed_padding_y_top)
        pad_bottom = int(prop_y_pad_bottom + self.fixed_padding_y_bottom)

        crop_x1 = max(0, int(x1 - pad_left))
        crop_y1 = max(0, int(y1 - pad_top))
        crop_x2 = min(frame_width, int(x2 + pad_right))
        crop_y2 = min(frame_height, int(y2 + pad_bottom))

        return (crop_x1, crop_y1, crop_x2 - crop_x1, crop_y2 - crop_y1)

    def _adjust_coords_to_aspect_ratio(self, coords_raw, frame_width, frame_height, target_aspect_ratio_tuple):
        x, y, w, h = coords_raw
        target_ratio_w, target_ratio_h = target_aspect_ratio_tuple
        target_aspect_ratio = target_ratio_w / target_ratio_h
        # Calculate ideal dimensions based on target aspect ratio
        if (w / h) < target_aspect_ratio:   # Current crop is too tall
            new_w = int(h * target_aspect_ratio)
            new_h = h
        else:   # Current crop is too wide or perfect
            new_h = int(w / target_aspect_ratio)
            new_w = w

        # Calculate how much to expand and distribute
        # Horizontal centering
        expand_x = new_w - w
        final_x = x - expand_x // 2
        final_w = new_w

        # Vertical expansion with bias (e.g., 30% above, 70% below)
        expand_y = new_h - h
        final_y = y - int(expand_y * 0.3)
        final_h = new_h

        # Clamp to frame boundaries
        final_x = max(0, final_x)
        final_y = max(0, final_y)

        # Adjust dimensions if clamping occurred, to maintain aspect ratio
        if final_x + final_w > frame_width:
            final_x = frame_width - final_w # Shift left if overflowing right
            final_x = max(0, final_x) # Ensure it doesn't go negative
        if final_y + final_h > frame_height:
            final_y = frame_height - final_h # Shift up if overflowing bottom
            final_y = max(0, final_y) # Ensure it doesn't go negative

        # Recalculate dimensions after clamping to ensure they are within bounds
        # and then adjust to preserve aspect ratio as best as possible
        final_w = min(final_w, frame_width - final_x)
        final_h = min(final_h, frame_height - final_y)

        # Final check and adjustment for aspect ratio after clamping
        # This part ensures that after clamping, the aspect ratio is still respected.
        # If one dimension was clamped, the other must be adjusted accordingly.
        if final_h > 0 and (final_w / final_h) < target_aspect_ratio:
            # If still too tall (constrained by width), adjust height
            final_h = int(final_w / target_aspect_ratio)
        elif final_w > 0 and (final_w / final_h) > target_aspect_ratio:
            # If still too wide (constrained by height), adjust width
            final_w = int(final_h * target_aspect_ratio)

        # Ensure even dimensions
        final_w = final_w - (final_w % 2)
        final_h = final_h - (final_h % 2)
        final_x = final_x - (final_x % 2)
        final_y = final_y - (final_y % 2)

        return (final_x, final_y, final_w, final_h)


    def _resize_and_crop_to_fit(self, image, target_width, target_height):
        """
        Redimensiona uma imagem para preencher completamente uma largura e altura alvo,
        mantendo sua proporção original. Partes da imagem que excedem a proporção
        do alvo serão cortadas (cropped).

        Args:
            image (np.array): A imagem de entrada (recorte).
            target_width (int): A largura desejada para a imagem de saída.
            target_height (int): A altura desejada para a imagem de saída.

        Returns:
            np.array: A imagem redimensionada e cortada, no tamanho alvo.
        """
        h_orig, w_orig = image.shape[:2]
        target_aspect = target_width / target_height
        image_aspect = w_orig / h_orig

        # Calcule as novas dimensões para preencher o slot, garantindo que
        # a proporção original seja mantida e a dimensão menor se ajuste.
        if image_aspect < target_aspect:
            # A imagem é mais 'alta' que o slot alvo (proporção menor).
            # Ajuste pela largura do slot e corte a altura.
            new_w = target_width
            new_h = int(new_w / image_aspect) # Altura maior que target_height
        else:
            # A imagem é mais 'larga' que o slot alvo (proporção maior) ou tem proporção igual.
            # Ajuste pela altura do slot e corte a largura.
            new_h = target_height
            new_w = int(new_h * image_aspect) # Largura maior que target_width

        # Redimensiona a imagem para as novas dimensões (maiores ou iguais ao alvo)
        resized_image = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)

        # Calcule as coordenadas de corte para centralizar a imagem redimensionada no alvo
        x_crop = (new_w - target_width) // 2
        y_crop = (new_h - target_height) // 2

        # Realize o corte
        cropped_image = resized_image[y_crop : y_crop + target_height, x_crop : x_crop + target_width]

        return cropped_image

    def extract_audio(self):
        """Extrai a trilha de áudio do vídeo original."""
        print("Extraindo áudio original...")
        command = [
            'ffmpeg',
            '-i', str(self.input_video_path),
            '-vn',        # No video
            '-acodec', 'aac',    # Audio codec
            '-q:a', '2',         # Audio quality (VBR, 2 is good)
            '-y', str(self.audio_original_path)
        ]
        self._run_ffmpeg_command(command, "extração de áudio")

    def combine_videos_and_add_text(self):
        """
        Combina o vídeo, adiciona legendas ASS e drawtext, e o áudio original,
        gerando o vídeo final.
        """
        print("Combinando vídeos e adicionando legendas/texto com lógica de alternância...")
        filter_chain_elements = []
        escaped_ass_path = str(self.ass_file_path).replace("\\", "\\\\").replace(":", "\\:").replace("'", "\\'")
        if self.ass_file_path and os.path.exists(self.ass_file_path):
            print(f"Adicionando legendas do arquivo ASS: {self.ass_file_path}")
            color_hex_bgr = self.color_name_to_ass_hex(self.captions_color) # Função auxiliar para converter
            filter_chain_elements.append(
                f"[0:v]subtitles='{escaped_ass_path}':"
                f"force_style='Alignment={self.captions_alignment},"
                f"Fontsize={self.captions_fontsize},"
                f"PrimaryColour={color_hex_bgr},"
                f"MarginV=20'[video_with_subtitles]" # Saída do filtro subtitles
            )
            drawtext_input = "[video_with_subtitles]"
        else:
            print("Nenhum arquivo ASS fornecido ou encontrado. Pulando adição de legendas ASS.")
            drawtext_input = "[0:v]" # Se não há subtitles, o drawtext usa o input original

        filter_chain_elements.append(
            f"{drawtext_input}drawtext=text='{self.text_overlay}':fontfile='{self.font_path}':"
            f"fontsize={self.subtitle_fontsize}:fontcolor={self.subtitle_fontcolor}:x=(w-text_w)/2:y=(h-text_h)/2{self.SubtitleVerticalReference}:"
            f"bordercolor=black:borderw=2[outv]" # Saída final do complex filter
        )

        # Junta todos os elementos da cadeia de filtros
        filter_complex_string = ";".join(filter_chain_elements)

        command = [
            'ffmpeg',
            '-y', # Sobrescrever arquivo de saída sem perguntar
        ]

        if self.dockerffmpegGPU:
            command.extend([
                '-hwaccel', "cuda",
                # '-hwaccel_output_format', 'cuda', 
            ])

        command.extend([
            '-i', str(self.video_single_temp_path), # Input de vídeo
            '-i', str(self.audio_original_path),   # Input de áudio
            '-filter_complex', filter_complex_string,
            '-map', '[outv]', # Mapeia o stream de vídeo da saída do filter_complex
            '-map', '1:a:0',  # Mapeia o stream de áudio do input 1 (original_audio_path)
        ])

        if self.dockerffmpegGPU:
            command.extend([
                '-s', '1080x1920',
                '-c:v', 'h264_nvenc', 
                '-rc', 'constqp',    
                '-qp', '18',      
            ])
        else:
            command.extend([
                '-s', '1080x1920',
                '-c:v', 'libx264',   # Encoder de vídeo CPU
                '-preset', 'fast',
                '-crf', '16',        # Qualidade (menor CRF = maior qualidade/arquivo)
            ])
        
        # Parâmetros comuns para ambos CPU/GPU
        command.extend([
            '-c:a', 'aac',       # Encoder de áudio
            '-b:a', '192k',      # Bitrate de áudio
            '-shortest',         # Encerra quando o input mais curto termina
            '-pix_fmt', 'yuv420p', # Formato de pixel (compatibilidade)
            str(self.final_output_path)
        ])

        self._run_ffmpeg_command(command, "combinação e adição de texto")


    def color_name_to_ass_hex(self, color_name):
        """Converte nomes de cores para o formato hexadecimal BGR usado pelo ASS/libass."""
        colors = {
            "white": "&H00FFFFFF",
            "black": "&H00000000",
            "red": "&H000000FF",
            "green": "&H0000FF00",
            "blue": "&H00FF0000",
            "yellow": "&H0000FFFF",
            "cyan": "&H00FFFF00",
            "magenta": "&H00FF00FF",
            # Adicione mais cores conforme necessário
        }
        return colors.get(color_name.lower(), "&H00FFFFFF") # Padrão para branco se não encontrada


    def cleanup(self):
        """Remove os arquivos temporários."""
        print("Realizando limpeza dos arquivos temporários...")
        for temp_file in [self.video_cima_temp_path, self.video_baixo_temp_path, self.video_single_temp_path, self.audio_original_path]:
            if temp_file.exists():
                temp_file.unlink()
                print(f"Arquivo temporário removido: {temp_file.name}")
        
        print("Limpeza concluída.")

    def run(self):
        """Executa o processo completo de Auto Reframe."""
        try:
            print("\n--- Iniciando processo Auto Reframe ---")
         
            # 1. Analisar vídeo e obter coordenadas de recorte e número de faces COM RASTREAMENTO
            all_crop_data = self.analyze_and_get_crop_coords()

            # 2. Gerar o vídeo composto final (já com a lógica de 1 ou 2 pessoas)
            self.generate_final_composite_video(all_crop_data)

            # 3. Extrair áudio original
            self.extract_audio()

            # 4. Adicionar texto ao vídeo composto final
            self.combine_videos_and_add_text() # all_crop_data não é estritamente necessário aqui, mas mantido

            print(f"\n--- Processo Auto Reframe concluído com sucesso! ---")
            print(f"Vídeo final salvo em: {self.final_output_path}")

            # Marca o fim
            fim = time.time()

            # Calcula o tempo gasto
            tempo_gasto = fim - self.inicio

            # Converter para horas, minutos e segundos
            horas, resto = divmod(tempo_gasto, 3600)
            minutos, segundos = divmod(resto, 60)

            print(f"Tempo gasto total: {tempo_gasto:.2f} segundos")
            print(f"Ou: {int(horas)} horas, {int(minutos)} minutos, {segundos:.2f} segundos")

        except Exception as e:
            print(f"\n--- Erro durante o processo Auto Reframe: {e} ---")
        finally:
            self.cleanup()

if __name__ == "__main__":
    INPUT_VIDEO_PODCASTS = r"C:\Users\Media Cuts DeV\Downloads\HomeServer\HomeServer\internalserver\Studio\WorkEnvironment\Process\subclip_vertical_1.mp4"
    INPUT_VIDEO_GAME = r"C:\Users\Media Cuts DeV\Downloads\HomeServer\HomeServer\internalserver\Studio\WorkEnvironment\Process\0818.mp4"
    ass_file_path = r"C:\Users\Media Cuts DeV\Downloads\HomeServer\HomeServer\internalserver\Studio\WorkEnvironment\Process\Realtime_Cuts\Cuts\Quem_realmente_sustenta_o_Brasil\CutsCreate\audio_video_vertical_1.ass"
    output_video_ = os.path.abspath(os.path.join(diretorio_script,
                    "WorkEnvironment", "Process", 
                    "Realtime_Cuts", 'Cuts', 
                    f"video_vertical_game.mp4"))

    OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 
                              "Models", "Yollo",
                                "reframe_output")
    YOLO_MODEL = os.path.join(
        os.path.dirname(__file__), 
        "Models", "Yollo",
        "yolov12n-face.pt"
    ) 

    if not Path(YOLO_MODEL).exists():
        print(f"AVISO: O modelo YOLO '{YOLO_MODEL}' não foi encontrado.")
        print(f"Tentando baixar '{YOLO_MODEL}'...")
        try:
            YOLO(YOLO_MODEL) 
            print(f"Modelo '{YOLO_MODEL}' baixado com sucesso.")
        except Exception as e:
            print(f"ERRO: Falha ao baixar o modelo YOLO '{YOLO_MODEL}'. Por favor, baixe-o manualmente.")
            print(f"Você pode tentar 'pip install ultralytics --upgrade' e depois executar 'python -c \"from ultralytics import YOLO; YOLO(\'{YOLO_MODEL}\')\"'")
            exit()
    try:
        
        reframe_processor = AutoReframe(
            video_type="game",
            ass_file_path=ass_file_path,
            input_video_path=INPUT_VIDEO_GAME,
            output_video_mp4=output_video_,
            CONF_MIN=0.70,
            min_move_pixels=1000,
            stability_threshold_frames=30,
            text_overlay="", # Personalize o texto aqui
            padding_x_ratio_left = 0.0,    # New
            padding_x_ratio_right = 0.0,   # New
            padding_y_ratio_top = 0.0,     # New
            padding_y_ratio_bottom = 0.0,  # New
            fixed_padding_x_left = 80,     # New
            fixed_padding_x_right = 80,    # New (assuming symmetric for now)
            fixed_padding_y_top = 80,     # New (adjust as needed for head)
            fixed_padding_y_bottom = 80,
            font_path="Future",
            captions_alignment=2,
            captions_fontsize=9,
            captions_color="white",
            subtitle_fontsize=20,
            subtitle_fontcolor="white",
            SubtitleVerticalReference="+20",

            yolo_model_path=YOLO_MODEL,
            show_preview=show_preview,
            dockerffmpegGPU=dockerffmpegGPU,
        )
        reframe_processor.run()
    except Exception as e:
        print(f"Um erro inesperado ocorreu: {e}")