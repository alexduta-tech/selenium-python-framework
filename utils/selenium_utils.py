from utils.config import IMPLICIT_WAIT


class SeleniumUtils:
    """Utility class for common Selenium operations.
    """
    
    def __init__(self, driver, logger=None):
        self.driver = driver
        self.logger = logger

    def is_element_present(self, locator):
        """Check if an element is present on the page.
        Args:
            locator: Tuple of (By, locator) to find the element.
        Returns:
            bool: True if the element is present, False otherwise.
        """

        self.logger.info(f"Checking if element is present: {locator}")
        try:
            # Temporarily set implicit wait to 1 second for quick check
            self.driver.implicitly_wait(1)
            # Attempt to find the element
            self.driver.find_element(*locator)
            # scroll to the element (useful for taking screenshots)
            self.scroll_to_element(locator)
            self.logger.info("Element is present")
            return True 
        except:
            self.logger.info("Element is not present")
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