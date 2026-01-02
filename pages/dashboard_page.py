from selenium.webdriver.common.by import By
from pages.create_users_page import CreateUsersPage

class DashboardPage():
    """Page object for the Dashboard page.
    """
    
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
    
    # Locators
    CREATE_USER_LINK = (By.XPATH, "//a[@href='/create-user']")

    # Page Object Methods
    def open_create_users_page(self):
        """
        Open the Create Users page.
        
        Returns:
            CreateUsersPage: Page object for the Create Users page.
        """
        self.logger.info("Clicking create users link")
        self.driver.find_element(*self.CREATE_USER_LINK).click()
        
        return CreateUsersPage(self.driver, self.logger)
    
