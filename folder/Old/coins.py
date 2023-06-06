from bs4 import BeautifulSoup
import requests
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import datetime


scope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file("client_secret.json", scopes=scope)
client = gspread.authorize(creds)
google_sh = client.open("Prueba")
sheet1 = google_sh.get_worksheet(1)

# Get the name of the coin you want to search
coin = input("Enter the name of the coin: ")

mainpage = requests.get('https://coinmarketcap.com/currencies/' + coin + '/')
soup = BeautifulSoup(mainpage.content, 'html.parser')

name = soup.find(class_='nameSymbol').get_text()

statsContainer = soup.find_all("div", {"class": "hide statsContainer"})

statsValues = statsContainer[0].find_all("div", {"class": "statsValue"})

statsValue_marketcap = statsValues[0].text.strip()

statsValue_fully_diluted_marketcap = statsValues[1].text.strip()

statsValue_volume = statsValues[2].text.strip()

statsValue_volume_per_marketcap = statsValues[3].text.strip()

statsValue_circulating_supply = statsValues[4].text.strip()

price_value = statsContainer[0].find_all("div", {"class": "priceValue "})
divTagContent = soup.find('div', {'class': 'priceValue'})
priceTag = divTagContent.select_one('span')

# Know hour and date
now = datetime.datetime.now()
hour = now.strftime("%H:%M")
date = now.strftime("%d/%m/%Y")

values = [[name, priceTag.text.strip(), statsValue_marketcap, hour, date]]

for row in values:
    sheet1.append_row(row)


# print("Coin Name: " + name + "\n")
# print("Market Cap: " + statsValue_marketcap + "\n")
# print("Fully Diluted Market Cap: " + statsValue_fully_diluted_marketcap + "\n")
# print("Volume: " + statsValue_volume + "\n")
# print("Volume Per Market Cap: " + statsValue_volume_per_marketcap + "\n")
# print("Circulating Supply: " + statsValue_circulating_supply + "\n")
# print("Price: " + priceTag.text.strip() + "\n")
print("Data has been written to the sheet")
