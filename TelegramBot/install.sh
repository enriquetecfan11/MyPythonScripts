#!/bin/bash

# Actualizar el gestor de paquetes
sudo apt-get update

# Instalar el módulo 'dotenv' para cargar variables de entorno desde el archivo .env
pip3 install python-dotenv

# Instalar el módulo 'translate' para traducir texto
pip3 install translate

# Instalar el módulo 'python-telegram-bot' para interactuar con la API de Telegram
pip3 install python-telegram-bot

# Instalar el módulo 'langchain' para el procesamiento del lenguaje natural
pip3 install langchain

# Instalar el módulo 'chroma' para el almacenamiento de vectores
pip3 install chroma

# Instalar el módulo 'openai' para el modelo de lenguaje
pip3 install openai

# Instalar el módulo 'pyPDF2' para manipular archivos PDF
pip3 install pyPDF2

# Instalar el módulo 'requests' para realizar solicitudes HTTP
pip3 install requests

# Instalar el módulo 'numpy' para operaciones numéricas
pip3 install numpy

# Instalar el módulo 'pandas' para manipulación de datos
pip3 install pandas

# Instalar el módulo 'matplotlib' para visualización de datos
pip3 install matplotlib

echo "¡Las dependencias han sido instaladas con éxito!"