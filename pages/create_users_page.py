from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from utils.selenium_utils import SeleniumUtils

class CreateUsersPage():
    """
    Page object for the Create Users page.
    """
    
    def __init__(self, driver, logger):
        self.page_path = "/create-user"
        self.driver = driver
        self.logger = logger
        self.selenium_utils = SeleniumUtils(self.driver, self.logger)
        self.wait_for_page_load()
        
    CREATE_10_USERS_BUTTON = (By.XPATH, "//button[text()='Create 10 Users']")
    
    def wait_for_page_load(self, timeout=5):
        """
        Wait for the Create Users page to load by checking the presence of the uri.
        
        Args:
            timeout: Maximum time to wait in seconds
        """
        self.logger.info("Waiting for Create Users page to load")
        WebDriverWait(self.driver, timeout).until(
            lambda d: self.page_path in d.current_url 
        )    

    def is_at(self):
        """
        Verify that we are on the Create Users page by checking for the presence of a mandatory element.
        
        Returns:
            bool: True if on Create Users page, False otherwise
        """
        return self.selenium_utils.is_element_present(self.CREATE_10_USERS_BUTTON)