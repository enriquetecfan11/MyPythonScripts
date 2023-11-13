import time, os
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv

load_dotenv()

texts = "paraphrase thirty times the following sentence where is the movie theater?"
email = os.getenv('email')
password = os.getenv('password')

driver = uc.Chrome()
url = "https://chat.openai.com/chat"

driver.get(url)
driver.maximize_window()

# Wait 10 seconds for page to load
driver.wait = WebDriverWait(driver, 10)

# Click on the login button '//button[@data-testid='login-button']
login_button = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='login-button']")))

login_button.click()




