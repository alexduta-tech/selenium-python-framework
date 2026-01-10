from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver

from utils.config import IMPLICIT_WAIT
from utils.selenium_utils import SeleniumUtils

class UserSearchOverlapPage:
    """
    Page object for the User Search Overlap page (the get random user button is overlapped by another element).
    """
    
    def __init__(self, driver: WebDriver, logger):
        self.page_path = "/user-search-overlap"
        self.driver = driver
        self.logger = logger
        self.selenium_utils = SeleniumUtils(self.driver, self.logger)
        self.wait_for_page_load()
    
    # Locators  
    BUTTON_BACK_TO_DASHBOARD = (By.XPATH, "//button[contains(.,'Back')]")  
    BUTTON_GET_RANDOM_USER = (By.ID, "getRandomUserBtn")  
    MESSAGE_SUCCESS = (By.CSS_SELECTOR, ".message.success")
    MESSAGE_ERROR = (By.CSS_SELECTOR, ".message.error")    
    LOADING_SPINNER = (By.CSS_SELECTOR, ".spinner")
    
    # Page Object Methods
    def wait_for_page_load(self, timeout=5) -> None:
        """
        Wait for the User Search Overlap page to load by checking the presence of the uri.
        
        Args:
            timeout: Maximum time to wait in seconds
        """
        self.logger.info("Waiting for User Search Overlap page to load")
        WebDriverWait(self.driver, timeout).until(
            lambda d: self.page_path in d.current_url 
        )
        
    def go_back_to_dashboard(self) -> None:
        """
        Go back to the Dashboard page.
        """
        self.logger.info("Clicking back to dashboard button")
        self.selenium_utils.scroll_to_element(self.BUTTON_BACK_TO_DASHBOARD)
        self.driver.find_element(*self.BUTTON_BACK_TO_DASHBOARD).click()   
        
    def is_at(self) -> bool:
        """
        Verify that we are on the User Search Overlap page by checking for the presence of a mandatory element.
        
        Returns:
            bool: True if on User Search    Overlap page, False otherwise
        """
        return self.selenium_utils.is_element_present(self.BUTTON_GET_RANDOM_USER)
    
    def click_get_random_user_button(self) -> 'UserSearchOverlapPage':
        """
        Click the Get Random User button.
        """
        self.logger.info("Clicking get random user button")
        # The button is overlapped by another element, so we need to scroll to it first
        self.selenium_utils.scroll_to_element(self.BUTTON_GET_RANDOM_USER)
        # Then click the button
        self.driver.find_element(*self.BUTTON_GET_RANDOM_USER).click()
        self.selenium_utils.wait_for_element_to_disappear(self.LOADING_SPINNER)           
        
        return self
    
    def get_result_message(self) -> str:
        """
        Get the text of the result message (after interacting with the overlapped element).

        Returns:
            str: The text of the success message or error message if present
        """
        
        if self.selenium_utils.is_element_present(self.MESSAGE_ERROR):
            self.logger.error("Error message present on the page, no success message available")
            return self.driver.find_element(*self.MESSAGE_ERROR).text
        
        if not self.selenium_utils.is_element_present(self.MESSAGE_SUCCESS):
            self.logger.error("Success message not present on the page")
            return "Success message not present on the page"
        
        success_message = self.driver.find_element(*self.MESSAGE_SUCCESS).text
        self.logger.info(f"Success message is present on the page, text: {success_message}")
        
        return success_message    