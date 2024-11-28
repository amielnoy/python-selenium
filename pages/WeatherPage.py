from datetime import datetime

import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.synchronization import SynchronizationMethods

class WeatherPage(BasePage):
    def __init__(self, zip_code):
        super().__init__()
        self.zip_code = zip_code

    def take_screenshot(self,driver, name):
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_name = f"{name}_{timestamp}.png"
        driver.save_screenshot(screenshot_name)
        print(f"Screenshot saved as {screenshot_name}")

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(item, call):
        # Execute all other hooks to obtain the report object
        outcome = yield
        report = outcome.get_result()

        # Check if the test failed
        if report.when == "call" and report.failed:
            driver = item.funcargs['driver']
            driver.take_screenshot(driver, item.name)

    def get_temp_using_web_ui(self):
        try:
            self.driver.get(f"http://www.weather.com/weather/today/l/{self.zip_code}")

            element=SynchronizationMethods.explicit_wait_visibility(
                self.driver,
                By.CSS_SELECTOR,
                'span[data-testid="TemperatureValue"]',
                10
            )

            # Extract and convert the temperature value
            temp = float(element.text.replace('°', ''))

        except Exception as e:
            BasePage.logger.error(f"Error scraping weather.com: {e}")
            temp = None

        finally:
            super().close()

        return temp
