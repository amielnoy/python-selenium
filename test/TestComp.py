import pytest
from Api.WeatherApi import WeatherApi
from pages.WeatherPage import WeatherPage
from pages.base_page import BasePage


class TestComp:

    @pytest.mark.parametrize("zip_code, api_key", [
        ("20852", "93f8f223148f4db7abc182516242611")
    ])
    def test_compare_temps(self, zip_code, api_key):
        # Get temperatures from API and WebUI
        weatherApi = WeatherApi()
        temp_api = weatherApi.get_api(zip_code, api_key)
        weatherWebui=WeatherPage(zip_code)
        webui_temp = weatherWebui.get_temp_using_web_ui()

        # Assert that both temperatures are not None
        assert temp_api is not None, "API temperature is None"
        assert webui_temp is not None, "WebUI temperature is None"

        # Calculate the gap
        gap = abs(webui_temp - temp_api) / webui_temp * 100

        # Print temperatures and gap for debugging
        BasePage.logger.info(f"API Temperature: {temp_api}°F")
        BasePage.logger.info(f"WebUI Temperature: {webui_temp}°F")
        BasePage.logger.info(f"Temperature Gap: {gap:.2f}%")

        # Assert that the gap is within acceptable range
        assert gap <= 10, f"Test Failed: Gap temp is {gap:.2f}%, which exceeds 10%"
