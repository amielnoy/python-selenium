import pytest
import requests as requests

from pages.base_page import BasePage
from utils.log import LoggerSingleton


class WeatherApi:
    def get_api(self,zip_code, api_key):
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={zip_code}"
        try:
            response = requests.get(url)
            data = response.json()
            temp = data['current']['temp_f']
        except Exception as e:
            BasePage.logger.error(f"Error fetching data from weatherapi.com: {e}")
            return None
        return temp