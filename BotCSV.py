import csv
import tkinter as tk
from tkinter import ttk

def cargar_respuestas(nombre_archivo):
    respuestas = {}
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo)
        for fila in lector_csv:
            pregunta = fila[0]
            respuesta = fila[1]
            respuestas[pregunta] = respuesta
    return respuestas

def buscar_respuesta(respuestas, pregunta):
    if pregunta in respuestas:
        return respuestas[pregunta]
    else:
        return "Lo siento, no tengo una respuesta para eso. ¿Puedes hacer otra pregunta?"

def obtener_respuesta():
    pregunta = entrada.get()  # Obtener la pregunta ingresada por el usuario
    respuesta = buscar_respuesta(respuestas, pregunta)  # Buscar la respuesta
    texto_respuesta.delete("1.0", tk.END)  # Borrar el contenido anterior en el campo de texto de respuesta
    texto_respuesta.insert(tk.END, respuesta)  # Mostrar la respuesta en el campo de texto de respuesta

# Nombre del archivo CSV
nombre_archivo = 'PreguntasCSV.csv'

# Cargar las respuestas desde el archivo CSV
respuestas = cargar_respuestas(nombre_archivo)

# Crear la ventana de la interfaz
ventana = tk.Tk()
ventana.title("Chatbot de Python")

# Estilo ttk
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12))

# Etiqueta de pregunta
etiqueta_pregunta = ttk.Label(ventana, text="Pregunta:")
etiqueta_pregunta.pack(pady=10)

# Campo de texto para ingresar la pregunta
entrada = ttk.Entry(ventana, width=50)
entrada.pack(pady=5)

# Botón de enviar pregunta
boton_enviar = ttk.Button(ventana, text="Enviar", command=obtener_respuesta)
boton_enviar.pack(pady=5)

# Etiqueta de respuesta
etiqueta_respuesta = ttk.Label(ventana, text="Respuesta:")
etiqueta_respuesta.pack(pady=10)

# Campo de texto para mostrar la respuesta
texto_respuesta = tk.Text(ventana, width=50, height=10)
texto_respuesta.pack(pady=5)

# Iniciar el bucle de eventos de la interfaz
ventana.mainloop()
