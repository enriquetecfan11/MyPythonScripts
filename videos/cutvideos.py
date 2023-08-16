from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.compositing.concatenate import concatenate_videoclips
import pandas as pd
import os

def time_to_seconds(time_str):
  """
  Convierte una cadena de tiempo en formato "0:00:00" a segundos.

  Args:
    time_str (str): Cadena de tiempo en formato "0:00:00".

  Returns:
    int: La cantidad de segundos correspondiente a la cadena de tiempo.
  """
  hours, minutes, seconds = map(int, time_str.split(':'))
  return hours * 3600 + minutes * 60 + seconds

def cut_and_save_segment(begins, ends, output_path):
  """
  Corta un segmento del video original y lo guarda en un archivo.

  Args:
    begins (int): Tiempo de inicio del segmento en segundos.
    ends (int): Tiempo de fin del segmento en segundos.
    output_path (str): Ruta donde se guardará el archivo de salida.
  """
  ffmpeg_extract_subclip(video_path, begins, ends, targetname=output_path)

# Cargar el archivo CSV
csv_path = "DJI_0123.csv"
data = pd.read_csv(csv_path)

#Ruta del video original para cortarlo
video_path = "DJI_0123.mp4"

from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.compositing.concatenate import concatenate_videoclips
import pandas as pd
import os

def time_to_seconds(time_str):
  """
  Convierte una cadena de tiempo en formato "0:00:00" a segundos.

  Args:
    time_str (str): Cadena de tiempo en formato "0:00:00".

  Returns:
    int: La cantidad de segundos correspondiente a la cadena de tiempo.
  """
  hours, minutes, seconds = map(int, time_str.split(':'))
  return hours * 3600 + minutes * 60 + seconds

def cut_and_save_segment(begins, ends, output_path):
  """
  Corta un segmento del video original y lo guarda en un archivo.

  Args:
    begins (int): Tiempo de inicio del segmento en segundos.
    ends (int): Tiempo de fin del segmento en segundos.
    output_path (str): Ruta donde se guardará el archivo de salida.
  """
  ffmpeg_extract_subclip(video_path, begins, ends, targetname=output_path)

# Cargar el archivo CSV
csv_path = "DJI_0123.csv"
data = pd.read_csv(csv_path)

#Ruta del video original para cortarlo
video_path = "DJI_0123.mp4"

# Iterar a través de los datos y cortar los segmentos no descartados
for index, row in data.iterrows():
  if row['type'] != "DISCARD":
    output_filename = f"segment_{index}.mp4"
    begins = time_to_seconds(row['begins'])
    ends = time_to_seconds(row['ends'])
    cut_and_save_segment(begins, ends, output_filename)

# Cargar y combinar todos los segmentos no descartados
segment_filenames = [f"segment_{index}.mp4" for index, row in data.iterrows() if row['type'] != "DISCARD"]
video_clips = [VideoFileClip(filename) for filename in segment_filenames]
final_video = concatenate_videoclips(video_clips)

# Guardar el video final
final_video_filename = "video_final.mp4"
final_video.write_videofile(final_video_filename, codec="libx264")

# Limpiar los archivos temporales de los segmentos

# Iterar a través de los datos y cortar los segmentos no descartados
for index, row in data.iterrows():
  if row['type'] != "DISCARD":
    output_filename = f"segment_{index}.mp4"
    begins = time_to_seconds(row['begins'])
    ends = time_to_seconds(row['ends'])
    cut_and_save_segment(begins, ends, output_filename)

# Cargar y combinar todos los segmentos no descartados
segment_filenames = [f"segment_{index}.mp4" for index, row in data.iterrows() if row['type'] != "DISCARD"]
video_clips = [VideoFileClip(filename) for filename in segment_filenames]
final_video = concatenate_videoclips(video_clips)

# Guardar el video final
final_video_filename = "video_final.mp4"
final_video.write_videofile(final_video_filename, codec="libx264")

# Limpiar los archivos temporales de los segmentos
for filename in segment_filenames:
  os.remove(filename)
