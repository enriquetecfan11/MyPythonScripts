import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import requests
from bs4 import BeautifulSoup


scope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file("client_secret.json", scopes=scope)
client = gspread.authorize(creds)
google_sh = client.open("Prueba")
sheet1 = google_sh.get_worksheet(0)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

ciudad = input("Enter the name of the city: ")
# Get the weather of the city you want to search
def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    print("Searching wheather request...\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    
    # Separate time strip with comma and get the first part
    time = soup.select('#wob_dts')[0].getText().strip().split(",")[0]
    day = soup.select('#wob_dts')[0].getText().strip().split(",")[1]
    
    
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()

    # sheet1.update("A3:D3", [[location, time, info, weather]])

    # Create a list of lists for the sheet
    values = [[location, time, day, info, weather]]
    # Create a for loop to iterate through the list of lists
    for row in values:
        # Append the row to the sheet
        sheet1.append_row(row)
    # print(location)
    # print(time)
    # print(info)
    # print(weather+"°C")



city = ciudad +" weather"
weather(city)

df = pd.DataFrame(data=sheet1.get_all_records())
print("Google Sheet Updated with the Weather Data \n")
print(df)
