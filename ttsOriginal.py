# -*- coding: utf-8 -*-
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
selected_voice_id = input("Selecciona el ID de la voz que deseas utilizar: ")

# Configurar la voz seleccionada
engine.setProperty('voice', selected_voice_id)

# Generar el archivo de audio con gTTS
tts = gTTS(text=frase, lang='es')
tts.save("audio.mp3")
