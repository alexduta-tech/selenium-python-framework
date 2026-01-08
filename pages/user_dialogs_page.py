from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from pages.common_widgets.generic_alert_dialog import GenericAlertDialog
from utils.selenium_utils import SeleniumUtils

class UserDialogsPage():
    """
    Page object for the Users Dialogs Page.
    """

    def __init__(self, driver: WebDriver, logger):
        self.page_path = "/user-dialogs"
        self.driver = driver
        self.logger = logger
        self.selenium_utils = SeleniumUtils(self.driver, self.logger)
        self.generic_alert_dialog = GenericAlertDialog(self.driver, self.logger)
        self.wait_for_page_load()

    # Locators
    BUTTON_BACK_TO_DASHBOARD = (By.XPATH, "//button[contains(.,'Back')]")
    BUTTON_SHOW_ALERT = (By.ID, "alertBtn")
    BUTTON_SHOW_CONFIRM = (By.ID, "confirmBtn")
    BUTTON_SHOW_PROMPT = (By.ID, "promptBtn")
    MESSAGE_SUCCESS = (By.CSS_SELECTOR, ".message.success")
    MESSAGE_ERROR = (By.CSS_SELECTOR, ".message.error")
    
    # Page Object Methods
    def wait_for_page_load(self, timeout=5) -> None:
        """
        Wait for the Users Dialogs page to load by checking the presence of the uri.

        Args:
            timeout: Maximum time to wait in seconds
        """
        self.logger.info("Waiting for Users Dialogs page to load")
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
        Verify that we are on the Users Dialogs page by checking for the presence of a mandatory element.

        Returns:
            bool: True if on Users Dialogs page, False otherwise
        """
        return self.selenium_utils.is_element_present(self.BUTTON_SHOW_ALERT)     
    
    def click_show_alert_button(self) -> 'UserDialogsPage':
        """ 
        Click the Show Alert button.
        """           
        self.logger.info("Clicking show alert button")
        self.driver.find_element(*self.BUTTON_SHOW_ALERT).click()
        
        return self

    def accept_alert_dialog(self) -> 'UserDialogsPage':
        """
        Accept the alert dialog.
        """
        self.generic_alert_dialog.accept_generic_alert_dialog()
        
        return self
    
    def get_dialog_result_message(self, is_error_expected=False) -> str:
        """
        Get the text of the dialog result message.

        Returns:
            str: The text of the success message or error message if present
        """
        
        if is_error_expected:
            error_message = self.driver.find_element(*self.MESSAGE_ERROR).text
            self.logger.info(f"Error message is present on the page, text: {error_message}")
            return error_message
            
        if self.selenium_utils.is_element_present(self.MESSAGE_ERROR):
            self.logger.error("Error message present on the page, no success message available")
            return self.driver.find_element(*self.MESSAGE_ERROR).text
        
        if not self.selenium_utils.is_element_present(self.MESSAGE_SUCCESS):
            self.logger.error("Success message not present on the page")
            return "Success message not present on the page"
        
        success_message = self.driver.find_element(*self.MESSAGE_SUCCESS).text
        self.logger.info(f"Success message is present on the page, text: {success_message}")
        
        return success_message
    
    def click_show_confirm_dialog_button(self) -> 'UserDialogsPage':
        """ 
        Click the Show Confirm button.
        """           
        self.logger.info("Clicking show confirm button")
        self.driver.find_element(*self.BUTTON_SHOW_CONFIRM).click()
        
        return self
    
    def accept_confirm_dialog(self) -> 'UserDialogsPage':
        """
        Accept the confirm dialog.
        """
        self.generic_alert_dialog.accept_generic_alert_dialog()
        
        return self
    
    def cancel_confirm_dialog(self) -> 'UserDialogsPage':
        """
        Cancel the confirm dialog.
        """
        self.generic_alert_dialog.cancel_confirm_or_prompt_dialog()
        
        return self
        
    def click_show_prompt_button(self) -> 'UserDialogsPage':
        """ 
        Click the Show Prompt button.
        """           
        self.logger.info("Clicking show prompt button")
        self.driver.find_element(*self.BUTTON_SHOW_PROMPT).click()
        
        return self
    
    def accept_prompt_dialog_with_text(self, text: str) -> 'UserDialogsPage':
        """
        Accept the prompt dialog with the provided text.

        Args:
            text (str): The text to send to the prompt dialog
        """
        self.generic_alert_dialog.send_text_to_prompt_dialog(text)
        self.generic_alert_dialog.accept_generic_alert_dialog()
        
        return self
    
    def cancel_prompt_dialog(self) -> 'UserDialogsPage':
        """
        Cancel the prompt dialog.
        """
        self.generic_alert_dialog.cancel_confirm_or_prompt_dialog()
        
        return self
    