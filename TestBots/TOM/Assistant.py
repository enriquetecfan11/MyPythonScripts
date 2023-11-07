from moviepy.editor import VideoFileClip, AudioFileClip

# Rutas de los archivos de video y audio
video_path = './personaje.mp4'
audio_path = './audio.mp3'

# Cargar el video y el audio
video = VideoFileClip(video_path)
audio = AudioFileClip(audio_path)

print("Duraccion del video: ", video.duration)
print("Duraccion del audio: ", audio.duration)

# Ajustar la duración del video para que coincida con la duración del audio
video = video.set_duration(audio.duration)

# Combinar el audio con el video
video = video.set_audio(audio)

# Guardar el nuevo video con el audio combinado y la duración ajustada
output_path = 'video_con_audio.mp4'
video.write_videofile(output_path, codec='libx264')
