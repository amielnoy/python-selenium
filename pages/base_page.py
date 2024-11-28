import pytest
from selenium import webdriver
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class BasePage:
    def __init__(self):
        options = Options()
        options.headless = False  # Set to True if you want headless mode
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def close(self):
        """Close the browser."""
        self.driver.quit()