from fastapi import FastAPI
import uvicorn
from telegram import Bot
from pydantic import BaseModel
from getCoins import get_crypto_data, create_crypto_image
from getWeather import get_weather_data, create_weather_image
from captureWEB import capture_screenshot

# Configura el token de tu bot de Telegram
bot_token = "1984896147:AAHPlXoRiVSqN8oWkieMz4GeFYfZzFUVxOw"

# Configura el chat_id de tu bot de Telegram
chat_id = "207196532"

bot = Bot(token=bot_token)

app = FastAPI()

# Lista de URLs para captura de pantalla
urls = [
    "https://www.metromadrid.es/es",
    "https://sondehub.org/#!mt=Mapnik&mz=10&qm=1h&mc=40.33137,-3.22655"
]

# Lista de ciudades para obtener datos meteorológicos
cities = ["Madrid", "Malaga", "Mondejar"]

@app.get("/")
def home():
    bot.send_message(chat_id=chat_id, text="Hola, soy un bot de Telegram. Envíame un comando para ejecutar una acción.")
    return {"message": "Hello World"}

@app.get("/crypto_image")
def get_crypto_image_endpoint():
    data = get_crypto_data()
    image_path = create_crypto_image(data)
    if image_path:
        with open(image_path, 'rb') as image_file:
            bot.send_photo(chat_id=chat_id, photo=image_file)
            return {"message": f"Image saved and sent: {image_path}"}
    else:
        return {"message": "Error al crear la imagen."}

@app.get("/weather_image/{city}")
def get_weather_image_endpoint(city: str):
    image_path = create_weather_image(city)
    if image_path:
        with open(image_path, 'rb') as image_file:
            bot.send_photo(chat_id=chat_id, photo=image_file)
            return {"message": f"Image saved and sent: {image_path}"}
    else:
        return {"message": "Error al crear la imagen."}

@app.get("/capture_screenshot")
def capture_screenshots_endpoint():
    screenshot_paths = []
    for url in urls:
        screenshot_path = capture_screenshot(url)
        screenshot_paths.append(screenshot_path)
        if screenshot_path:
            with open(screenshot_path, 'rb') as image_file:
                bot.send_photo(chat_id=chat_id, photo=image_file)
    return {"message": f"Screenshots saved and sent: {screenshot_paths}"}

@app.get("/capture_screenshot/{url}")
def capture_screenshot_endpoint(url: str):
    screenshot_path = capture_screenshot(url)
    if screenshot_path:
        with open(screenshot_path, 'rb') as image_file:
            bot.send_photo(chat_id=chat_id, photo=image_file)
            return {"message": f"Screenshot saved and sent: {screenshot_path}"}
    else:
        return {"message": "Error al crear la imagen."}

@app.get("/crypto_data")
def get_crypto_data_endpoint():
    data = get_crypto_data()
    return data

@app.get("/weather_data/{city}")
def get_weather_data_endpoint(city: str):
    weather_data = get_weather_data(city)
    return weather_data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
