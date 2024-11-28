from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class SynchronizationMethods:
    @staticmethod
    def implicit_wait(driver, time_in_seconds):
        """Set an implicit wait for the WebDriver."""
        driver.implicitly_wait(time_in_seconds)

    @staticmethod
    def explicit_wait_visibility(driver, by, locator, time_in_seconds):
        """Wait explicitly for an element to be visible."""
        return WebDriverWait(driver, time_in_seconds).until(
            EC.visibility_of_element_located((by, locator))
        )

    @staticmethod
    def explicit_wait_clickable(driver, by, locator, time_in_seconds):
        """Wait explicitly for an element to be clickable."""
        return WebDriverWait(driver, time_in_seconds).until(
            EC.element_to_be_clickable((by, locator))
        )

    @staticmethod
    def fluent_wait(driver, by, locator, timeout=30, poll_frequency=5):
        """Implement a fluent wait for an element."""
        wait = WebDriverWait(driver, timeout, poll_frequency=poll_frequency,
                             ignored_exceptions=[Exception])
        return wait.until(EC.presence_of_element_located((by, locator)))

# Example usage:
if __name__ == "__main__":
    # Initialize WebDriver (e.g., Chrome)
    driver = webdriver.Chrome()

    # Example usage of synchronization methods
    SynchronizationMethods.implicit_wait(driver, 10)

    driver.get("http://example.com")

    try:
        # Wait for an element to be visible
        element = SynchronizationMethods.explicit_wait_visibility(
            driver,
            By.ID,
            "exampleElementId",
            10
        )
        print("Element is visible:", element)

        # Wait for an element to be clickable
        clickable_element = SynchronizationMethods.explicit_wait_clickable(
            driver,
            By.ID,
            "clickableElementId",
            10
        )
        print("Element is clickable:", clickable_element)

    finally:
        driver.quit()
