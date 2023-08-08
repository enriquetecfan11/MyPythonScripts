from moviepy.editor import VideoFileClip, AudioFileClip
import pyttsx3
from gtts import gTTS
import os

# Obtener la frase del usuario
frase = input("Ingresa la frase que deseas convertir en audio: ")

# Configurar el motor de síntesis de voz
engine = pyttsx3.init()

# Obtener las voces disponibles
voices = engine.getProperty('voices')

# Imprimir las voces disponibles para que el usuario las vea
for voice in voices:
    print("ID:", voice.id)
    print("Name:", voice.name)
    print("Lang:", voice.languages)
    print("Gender:", voice.gender)
    print("--------------")

# Permitir al usuario seleccionar una voz
# selected_voice_id = input("Selecciona el ID de la voz que deseas utilizar: ")
selected_voice_id = "spanish-latin-am"

# Configurar la voz seleccionada
engine.setProperty('voice', selected_voice_id)

# Generar el archivo de audio con gTTS
tts = gTTS(text=frase, lang='es')
tts.save("audio.mp3")

# Rutas de los archivos de video y audio
video_path = './personaje.mp4'
audio_path = './audio.mp3'

# Cargar el video y el audio
video = VideoFileClip(video_path)
audio = AudioFileClip(audio_path)

print("Duración del video: ", video.duration)
print("Duración del audio: ", audio.duration)

# Ajustar la duración del video para que coincida con la duración del audio
video = video.set_duration(audio.duration)

# Combinar el audio con el video
video = video.set_audio(audio)

# Guardar el nuevo video con el audio combinado y la duración ajustada
output_path = 'video_con_audio.mp4'
video.write_videofile(output_path, codec='libx264')
