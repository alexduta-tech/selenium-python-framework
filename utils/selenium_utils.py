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
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False