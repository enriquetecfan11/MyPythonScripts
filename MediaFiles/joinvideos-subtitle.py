from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import TextClip
from moviepy.editor import concatenate_videoclips

def agregar_subtitulos(video_clip, subtitulo, tiempo_inicio):
    duracion = video_clip.duration
    txt_clip = TextClip(subtitulo, fontsize=24, color='white', bg_color='black', size=(video_clip.w, None))
    txt_clip = txt_clip.set_duration(duracion).set_position(("center", "bottom"))
    video_con_subtitulo = concatenate_videoclips([video_clip, txt_clip.crossfadein(1).set_start(tiempo_inicio)])
    return video_con_subtitulo

def unir_videos_con_subtitulos(video1_path, video2_path, output_path):
    video1 = VideoFileClip(video1_path)
    video2 = VideoFileClip(video2_path)

    video1_nombre = video1_path.split("/")[-1].split(".")[0]  # Obtén el nombre del archivo sin extensión
    video2_nombre = video2_path.split("/")[-1].split(".")[0]  # Obtén el nombre del archivo sin extensión

    print("Nombre Video 1: ", video1_nombre)
    print("Nombre Video 2: ", video2_nombre)

    video_con_subtitulos1 = agregar_subtitulos(video1, video1_nombre, 0)
    video_con_subtitulos2 = agregar_subtitulos(video2, video2_nombre, video1.duration)

    final_clip = concatenate_videoclips([video_con_subtitulos1, video_con_subtitulos2])
    final_clip.write_videofile("./videos/" + output_path, codec="libx264")

if __name__ == "__main__":
    video1_path = "./videos/DJI_0157.mp4"
    video2_path = "./videos/DJI_0158-009.mp4"
    output_path = "puente01_con_subtitulos.mp4"
    
    unir_videos_con_subtitulos(video1_path, video2_path, output_path)
    print("Videos Unidos con Subtítulos")
