import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

link = 'https://www.eltiempo.es/en-provincia-almeria/abejuela.html'
driver = webdriver.Chrome()
driver.get(link)