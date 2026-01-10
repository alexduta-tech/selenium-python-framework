from selenium.webdriver.support.ui import WebDriverWait
from utils.config import IMPLICIT_WAIT

class SeleniumUtils:
    """Utility class for common Selenium operations.
    """
    
    def __init__(self, driver, logger=None):
        self.driver = driver
        self.logger = logger

    def is_element_present(self, locator, timeout: int = 1):
        """Check if an element is present on the page.
        Args:
            locator: Tuple of (By, locator) to find the element.
            timeout: Maximum timeout in seconds for the check.
        Returns:
            bool: True if the element is present, False otherwise.
        """

        self.logger.debug(f"Checking if element is present: {locator}")
        try:
            # Temporarily set implicit wait to 1 second for quick check
            self.driver.implicitly_wait(timeout)
            # Attempt to find the element
            self.driver.find_element(*locator)
            # scroll to the element (useful for taking screenshots)
            self.scroll_to_element(locator)
            self.logger.debug("Element is present")
            return True 
        except:
            self.logger.debug("Element is not present")
            return False
        finally:
            # Restore the original implicit wait time
            self.driver.implicitly_wait(IMPLICIT_WAIT)
        
    def scroll_to_element(self, locator):
        """Scroll the page to bring the element into view.
        Args:
            locator: Tuple of (By, locator) to find the element.
        """
        self.logger.debug(f"Scrolling to element: {locator}")
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.logger.debug("Scrolled to element")
        
    def wait_for_element_to_disappear(self, locator, timeout: int = IMPLICIT_WAIT) -> None:    
        """
        Wait for the element to disappear (if present).
        """
        self.logger.debug(f"Waiting for element to disappear: {locator}")
        WebDriverWait(self.driver, timeout).until(
            lambda d: not self.is_element_present(locator)
        )          