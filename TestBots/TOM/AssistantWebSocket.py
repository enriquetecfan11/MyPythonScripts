import socketio
import pyttsx3
from gtts import gTTS
from moviepy.editor import VideoFileClip, AudioFileClip

# Configura el cliente Socket.IO
sio = socketio.Client()

# Define la función para manejar el evento 'connect'
@sio.on('connect')
def on_connect():
    print('Conectado al servidor WebSocket')

# Define la función para manejar el evento 'chat message'
@sio.on('chat message')
def on_chat_message(msg):
    print('Mensaje del servidor:', msg)
    process_audio_video(msg)

# Conéctate al servidor WebSocket
sio.connect('http://192.168.1.38:3000')  # Cambia esto con la dirección de tu servidor

def process_audio_video(frase):
    # Configurar el motor de síntesis de voz
    engine = pyttsx3.init()

    # Obtener las voces disponibles
    voices = engine.getProperty('voices')

    # Seleccionar una voz (puedes ajustar esto)
    # selected_voice_id = 'your_selected_voice_id'
    selected_voice_id = "spanish-latin-am"
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

    # Ajustar la duración del video para que coincida con la duración del audio
    video = video.set_duration(audio.duration)

    # Combinar el audio con el video
    video = video.set_audio(audio)

    # Guardar el nuevo video con el audio combinado y la duración ajustada
    output_path = 'video_con_audio.mp4'
    video.write_videofile(output_path, codec='libx264')

try:
    while True:
        pass  # Mantén la conexión activa

except KeyboardInterrupt:
    sio.disconnect()  # Desconéctate cuando se presiona Ctrl+C
