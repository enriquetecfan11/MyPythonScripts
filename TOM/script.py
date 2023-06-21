# -*- coding: utf-8 -*-
import speech_recognition as sr
from termcolor import colored
import openai

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
from langchain import ConversationChain

import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")



llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm, verbose=False)


def process_input(input_text):
    # Verificar si la entrada es 'salir' para salir del programa
    if input_text.lower() == "salir":
        return None
    else:
        # Generar respuesta utilizando ChatGPT
        response = generate_response(input_text)
        return response

def generate_response(input_text):
    response = conversation.run(input_text)
    return response


def getTokens(text):
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(text)
    return tokens



def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(colored("Dime algo:", "green"))
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="es-ES")
        print(colored("Entrada de voz:", "cyan"), text)
        response = process_input(text)
        if response == False:
            return False  # Salir del programa
        else:
            print(colored("Respuesta del asistente:", "yellow"), response)
    except sr.UnknownValueError:
        print(colored("No se pudo reconocer la entrada de voz", "red"))
    except sr.RequestError:
        print(colored("Error al realizar la solicitud de reconocimiento de voz", "red"))
    return True

def read_input():
    while True:
        input_text = input(colored("Escribe algo: ", "green"))
        response = process_input(input_text)
        if response == False:
            break  # Salir del programa
        else:
            print(colored("Respuesta del asistente:", "yellow"), response)

def main():
    print(colored("¡Bienvenido al asistente virtual!", "magenta"))
    while True:
        print(colored("¿Cómo te gustaría interactuar?", "blue"))
        print(colored("1. Voz", "cyan"))
        print(colored("2. Teclado", "cyan"))
        print(colored("3. Salir", "red"))
        option = input(colored("Elige una opción: ", "green"))
        if option == "1":
            should_continue = listen()
            if not should_continue:
                break  # Salir del programa
        elif option == "2":
            read_input()
            getTokens()
        elif option == "3":
            print(colored("¡Hasta luego!", "magenta"))
            break
        else:
            print(colored("Opción inválida. Por favor, elige una opción válida.", "red"))

if __name__ == "__main__":
    main()
