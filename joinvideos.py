from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import VideoFileClip

def unir_videos(video1_path, video2_path, output_path):
    video1 = VideoFileClip(video1_path)
    video2 = VideoFileClip(video2_path)
    
    final_video = video1.set_duration(video1.duration + video2.duration)
    final_video = final_video.crossfadein(video2, duration=2)  # Agregar un fundido entre los videos
    
    final_video.write_videofile(output_path, codec="libx264")

if __name__ == "__main__":
    video1_path = "ruta_al_video1.mp4"
    video2_path = "ruta_al_video2.mp4"
    output_path = "ruta_del_video_salida.mp4"
    
    unir_videos(video1_path, video2_path, output_path)
