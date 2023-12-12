import os
import requests
from PIL import Image
from io import BytesIO
from datetime import datetime
from dotenv import load_dotenv
from selenium import webdriver
import time
from datetime import datetime
load_dotenv()


options = webdriver.ChromeOptions()
# Make window size 1920x1080
options.add_argument('--window-size=1920,1080')
options.add_argument('--headless')


def capture_screenshot(url):
    capture_time = datetime.now().strftime("%Y%m%d%H%M%S")

    try:
        # Create a new Chrome session
        browser = webdriver.Chrome(options=options)
        # Open the URL
        browser.get(url)
        # Wait 10 seconds for page to load
        time.sleep(10)
        browser.execute_script("window.scrollTo(0, 500)")
        time.sleep(5)
        
        # Get the screenshot of the full page and name it screenshot_<page_title>.png
        page_title = browser.title
        screenshot_name = f"screenshot_{page_title}_{capture_time}.png"

        # Save the screenshot
        browser.save_screenshot(os.path.join("export", screenshot_name))
        
        # Close the browser
        browser.close()
        return {"message": f"Screenshot saved successfully: {screenshot_name}"}

    except Exception as e:
        return {"message": f"Failed to capture screenshot: {e}"}

if __name__ == "__main__":
    url = "https://www.metromadrid.es/es"
    capture_screenshot(url)
    url = "https://sondehub.org/#!mt=Mapnik&mz=10&qm=1h&mc=40.33137,-3.22655"
    capture_screenshot(url)