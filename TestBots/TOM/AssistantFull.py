from moviepy.editor import VideoFileClip, AudioFileClip
import pyttsx3
from gtts import gTTS
import os

def get_user_phrase():
    frase = input("Ingresa la frase que deseas convertir en audio: ")
    return frase

def configure_speech_engine():
    engine = pyttsx3.init()
    return engine

def get_available_voices(engine):
    voices = engine.getProperty('voices')
    return voices

def select_voice():
    selected_voice_id = "spanish-latin-am"
    return selected_voice_id

def configure_selected_voice(engine, selected_voice_id):
    engine.setProperty('voice', selected_voice_id)

def generate_audio_file(text, filename):
    tts = gTTS(text=text, lang='es')
    tts.save(filename)

def process_video_and_audio(video_path, audio_path):
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)
    print("Duración del video: ", video.duration)
    print("Duración del audio: ", audio.duration)
    video = video.set_duration(audio.duration)
    video = video.set_audio(audio)
    output_path = 'video_con_audio.mp4'
    video.write_videofile(output_path, codec='libx264')

def main():
    user_phrase = get_user_phrase()
    speech_engine = configure_speech_engine()
    selected_voice = select_voice()
    configure_selected_voice(speech_engine, selected_voice)

    audio_filename = "audio.mp3"
    generate_audio_file(user_phrase, audio_filename)

    video_path = './girl.mp4'
    process_video_and_audio(video_path, audio_filename)

if __name__ == "__main__":
    main()

