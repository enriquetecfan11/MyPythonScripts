from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import TextClip
from moviepy.editor import concatenate_videoclips
import glob


def unir_videos(videopath):
  # Leer los videos de una carpeta de manera recursiva 
  videopath = videopath

  # Añadir los videos a la lista de videos
  videos = []

  # Recorrer los videos de la carpeta
  for video in glob.glob(videopath):
    # Leer el video
    video = VideoFileClip(video)
    # Añadir el video a la lista
    videos.append(video)

  # Unir los videos de la lista
  final_clip = concatenate_videoclips(videos)

  # Crear un video con los videos de la lista
  final_clip.write_videofile("final.mp4")

if __name__ == "__main__":
  # Aqui estamos llamando a la funcion unir_videos
  videopath = r""
  
  # Llamamos a la funcion y unir los videos
  unir_videos()
  print("Videos unidos")

