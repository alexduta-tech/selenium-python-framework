from selenium.webdriver.remote.webdriver import WebDriver

class GenericAlertDialog:
    """
    Page object for the Generic Alert Dialog: alert, confirm, prompt.
    """

    def __init__(self, driver: WebDriver, logger):
        self.driver = driver
        self.logger = logger

    def get_generic_dialog_text(self) -> str:
        """
        Get the text of the alert dialog.

        Returns:
            str: The text of the alert dialog
        """
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        self.logger.info(f"Dialog text: {alert_text}")
        
        return alert_text   
    
    def accept_generic_alert_dialog(self) -> 'GenericAlertDialog':
        """
        Accept the alert/confirm dialog.
        """
        self.logger.info("Accepting dialog")
        alert = self.driver.switch_to.alert
        alert.accept()
        
        return self 
    
    def cancel_confirm_or_prompt_dialog(self) -> 'GenericAlertDialog':
        """
        Cancel the confirm/prompt dialog.
        """
        self.logger.info("Cancelling confirm dialog")
        alert = self.driver.switch_to.alert
        alert.dismiss()
        
        return self   
    
    def send_text_to_prompt_dialog(self, text: str) -> 'GenericAlertDialog':
        """
        Send text to the prompt dialog.

        Args:
            text (str): The text to send to the prompt dialog
        """
        self.logger.info(f"Sending text to prompt dialog: {text}")
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        
        return self