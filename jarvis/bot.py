import logging
from telegram import Update, Bot
from telegram.ext import CallbackContext, CommandHandler, Updater, MessageHandler
from telegram.ext import Filters
from telegram.error import TimedOut
from telegram import Update, InputFile
import time
import requests
import dotenv
import os

dotenv.load_dotenv()


# Configura el logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Reemplaza 'TU_API_URL' con la URL de tu API web
API_URL = 'http://localhost:8000'

# Función para manejar el comando /start
def start(update: Update, context: CallbackContext):
    user_name = update.effective_user.username
    update.message.reply_text(f"Hola, {user_name}! Soy tu asistente personal. ¿En qué puedo ayudarte?")
    logger.info(f"El usuario {user_name} ha iniciado una conversación con el bot.")

# Función para manejar el comando /get_crypto_image
def get_crypto_image(update: Update, context: CallbackContext):
    response = requests.get(f"{API_URL}/crypto_image")
    if response.status_code == 200:
        update.message.reply_text("Aquí tienes la imagen de datos de criptomonedas:")
        update.message.reply_photo(photo=response.content)
    else:
        update.message.reply_text("Lo siento, hubo un error al obtener la imagen de datos de criptomonedas.")

# Función para manejar el comando /get_weather_image
def get_weather_image(update: Update, context: CallbackContext):
    # Solicita al usuario el nombre de la ciudad
    update.message.reply_text("Por favor, ingresa el nombre de la ciudad:")
    # Establece el estado de espera para la ciudad
    context.user_data['waiting_for_city'] = True

# Función para manejar la respuesta del nombre de la ciudad
def handle_city_response(update: Update, context: CallbackContext):
    user_text = update.message.text

    logger.info(f"El usuario {update.effective_user.username} espera el tiempo de la ciudad: {user_text}")

    # Si el usuario no está esperando una ciudad, ignora el mensaje
    if 'waiting_for_city' not in context.user_data:
        return
    
    # Si el usuario está esperando una ciudad, obtiene la respuesta de la API weather_data/{city}
    response = requests.get(f"{API_URL}/weather_data/{user_text}")

    if response.status_code == 200:
        weather_data = response.json()
        message = f"Datos meteorológicos para {user_text}:\n"
        message += f"Condición: {weather_data['condition']}\n"
        message += f"Temperatura: {weather_data['temp']}°C\n"
        message += f"Sensación térmica: {weather_data['temp_feel']}°C\n"
        message += f"Temperatura mínima: {weather_data['min_temp']}°C\n"
        message += f"Temperatura máxima: {weather_data['max_temp']}°C\n"
        update.message.reply_text(message)
    else:
        update.message.reply_text("Lo siento, hubo un error al obtener los datos meteorológicos.")

    # Limpia el estado de espera para futuras interacciones
    del context.user_data['waiting_for_city']


# Función para manejar el comando capturar_screenshot con argumentos de URL
def capture_screenshot(update: Update, context: CallbackContext):
    # Solicita al usuario la URL
    update.message.reply_text("Por favor, ingresa la URL (La url tiene que ser completa ejemplo: https://www.google.es):")
    # Establece el estado de espera para la URL
    context.user_data['waiting_for_url'] = True

# Función para manejar la respuesta de la URL
def handle_url_response(update: Update, context: CallbackContext):
    user_text = update.message.text
    logger.info(f"El usuario {update.effective_user.username} espera la URL: {user_text}")
    
    # Si el usuario no está esperando una URL, ignora el mensaje
    if 'waiting_for_url' not in context.user_data:
        return

    # Si el usuario está esperando una URL, obtiene la respuesta de la API weather_data/{city}
    response = requests.get(f"{API_URL}/capture_screenshot/{user_text}")

    if response.status_code == 200:
        update.message.reply_text("Aquí tienes la captura de pantalla:")
        update.message.reply_photo(photo=response.content)
    else:
        update.message.reply_text("Lo siento, hubo un error al obtener la captura de pantalla.")

    # Limpia el estado de espera para futuras interacciones
    del context.user_data['waiting_for_url']

# Función para ver todos los comandos disponibles
def help(update: Update, context: CallbackContext):
    help_text = """
    Los siguientes comandos están disponibles:
    /start - Inicia la conversación con el bot
    /crypto - Muestra una imagen de datos de criptomonedas
    /tiempo - Muestra una imagen de datos meteorológicos para una ciudad
    /screenshot - Captura una captura de pantalla de una URL
    /help - Muestra este mensaje de ayuda
    """
    update.message.reply_text(help_text)
    logger.info(f"El usuario {update.effective_user.username} ha solicitado ayuda.")

# Función para manejar el comando logger_handler
def logger_handler(update: Update, context: CallbackContext):
    user_name = update.effective_user.username
    user_message = update.message.text
    logger.info(f"El usuario {user_name} ha enviado el mensaje: {user_message}")

# Función ejecutar un comando a dos horas diferentes
# eL comando ejecuta hace una llamada a la API a dos endpoints diferentes uno es crypto_image y el otro es weather_image
# Se tiene que ejecutar a las 12:00 y a las 00:00
# def job(context: CallbackContext):


# Función principal para iniciar el bot
def main():
  # Crea una instancia de Bot con el token
  bot_token = os.getenv("BOT_TOKEN")  
  bot = Bot(token=bot_token)

  # Crea un Updater que manejará las actualizaciones del bot
  updater = Updater(bot=bot, use_context=True)
  
  # Obtén el despachador para registrar manejadores
  dispatcher = updater.dispatcher


  # Registra manejadores para comandos y mensajes de texto
  dispatcher.add_handler(CommandHandler("start", start))
  dispatcher.add_handler(CommandHandler("crypto", get_crypto_image))
  dispatcher.add_handler(CommandHandler("tiempo", get_weather_image, pass_args=True))
  dispatcher.add_handler(CommandHandler("screenshot", capture_screenshot, pass_args=True))
  dispatcher.add_handler(CommandHandler("help", help))
  dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_city_response))

  # Registro de lo que hace el usuario con logger
  dispatcher.add_handler(MessageHandler(None, logger_handler))

  # Inicia el bot
  updater.start_polling()
  updater.idle()

if __name__ == "__main__":
    logger.info("Iniciando el bot...")
    print("Iniciando el bot...")
    main()
