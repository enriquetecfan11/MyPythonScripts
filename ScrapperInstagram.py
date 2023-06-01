from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import urllib.request
from urllib.error import HTTPError
import time

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)

URL = 'https://www.instagram.com/'

driver.get(URL)
time.sleep(5)
print("Pagina Cargada")


# Aceptamos las cookies button class = _a9-- _a9_0
driver.find_element(By.CLASS_NAME, "_a9--").click()
print("Cookies aceptadas")
time.sleep(5)

# Login into insstagram
username = 'tecfanai'
password = 'mondejar1996'

driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)
print("Credenciales Escritas")

time.sleep(5)

#click in a button with the name Entrar
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]").click()
print("Dentro")
time.sleep(10)

#click in a button with the name Ahora no
driver.find_element(By.CLASS_NAME, "_a9--").click()
print("Ahora no")
time.sleep(5)



# click in aria-label Búsqueda
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div/div[2]/div/div").click()

time.sleep(20)
