import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from datetime import datetime

def get_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "USD",
        "ids": "bitcoin,ethereum,cardano",
        "order": "market_cap_desc"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

def create_crypto_image(data):
    # Assuming each section is 100 pixels high and there's a 10 pixel margin
    image_height = 100 * len(data) + 15
    image = Image.new("RGB", (500, image_height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", size=15)

    # Get current date and time
    now = datetime.now()
    current_time = now.strftime("%d/%m/%Y %H:%M:%S")
    x_text = 10
    y_text = 10
    draw.text((x_text, y_text), f"Last updated: {current_time}", fill=(0, 0, 0), font=font)

    y = 35  # Start 10 pixels from the top
    for crypto in data:
        # Draw image logo of the crypto
        response = requests.get(crypto['image'])
        logo = Image.open(BytesIO(response.content))
        logo = logo.resize((50, 50))  # Resize image logo
        image.paste(logo, (10, y))

        # Calculate x position for text, 10 pixels to the right of the logo
        x_text = 70
        
        draw.text((x_text, y), f"Symbol: {crypto['symbol'].upper()}", fill=(0, 0, 0), font=font)
        draw.text((x_text, y + 20), f"Name: {crypto['name']}", fill=(0, 0, 0), font=font)
        draw.text((x_text, y + 40), f"Price: ${crypto['current_price']:.2f}", fill=(0, 0, 0), font=font)
        draw.text((x_text, y + 60), f"Price Change 24H: {crypto['price_change_percentage_24h']:.2f}%", fill=(0, 0, 0), font=font)

        y += 100  # Move to the next section

    # Save image with name crypto_data_currentime.png
    image_name = f"./export/crypto_data_{now.strftime('%Y%m%d%H%M%S')}.png"
    image.save(image_name)
    return image_name

if __name__ == "__main__":
    crypto_data = get_crypto_data()
    create_crypto_image(crypto_data)
