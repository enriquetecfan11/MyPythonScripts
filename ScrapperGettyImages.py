from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import urllib.request
from urllib.error import HTTPError
import time

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)

URL = 'https://www.instagram.com/melissajimenezgp'


driver.get(URL)
time.sleep(5)
print("Pagina Cargada")

# Aceptamos las cookies button id = onetrust-accept-btn-handler
driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
print("Cookies aceptadas")
time.sleep(5)

# Now scroll to down the page slower
print("Scrool Down Page")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)

# Encuentra todos los elementos de imagen en la página
image_elements = driver.find_elements(By.TAG_NAME, "img")
print("Imagenes encontradas: ", len(image_elements))



# Close the driver
driver.quit()
