import requests
from bs4 import BeautifulSoup
import time
import random
import csv

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
}

bucket_list = [
    'https://amzn.eu/d/eEtfD8Y',
    'https://amzn.eu/d/2iNz9um',
    'https://amzn.eu/d/8R2Z9Y0',
    ]


def get_price(soup):
    # Encuentra el elemento que contiene el precio
    price_element = soup.find('span', {'class': 'a-offscreen'})
    # Si se encuentra el elemento del precio
    if price_element:
        # Extrae el texto del precio y elimina caracteres no deseados
        price_text = price_element.get_text().strip().replace('€', '').replace('.', '').replace(',', '.')
        # Convierte el precio a un número flotante
        price_float = float(price_text)
        
        return price_float
    else:
        return 'Precio no encontrado'


def get_product_name(soup):
    try:
        name_element = soup.find('span', {'id': 'productTitle'})
        if name_element:
            # Obtener el texto completo del nombre del producto
            full_product_name = name_element.get_text().strip()
            # Obtener la parte del texto antes de la coma (,)
            product_name = full_product_name.split(',')[0]
            return product_name
        else:
            return 'Nombre no encontrado'
    except Exception as e:
        return 'Not Available'



# Escribir datos en un archivo CSV
with open('master_data.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['product name', 'price', 'url'])

    for url in bucket_list:
        response = requests.get(url, headers=header)
        soup = BeautifulSoup(response.content, 'html.parser')
        product_name = get_product_name(soup)
        product_price = get_price(soup)
        print("El nombre del producto es:", product_name)
        print("El precio del producto es:", product_price)
        time.sleep(random.randint(2, 10))
        writer.writerow([product_name, product_price, url])
