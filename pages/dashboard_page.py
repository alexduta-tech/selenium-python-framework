from selenium.webdriver.common.by import By
from pages.create_users_page import CreateUsersPage
from pages.list_all_users_page import ListAllUsersPage

class DashboardPage():
    """Page object for the Dashboard page.
    """
    
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
    
    # Locators
    CREATE_USER_LINK = (By.XPATH, "//a[@href='/create-user']")
    LIST_ALL_USERS_LINK = (By.XPATH, "//a[@href='/users']")

    # Page Object Methods
    def open_create_users_page(self) -> CreateUsersPage:
        """
        Open the Create Users page.
        
        Returns:
            CreateUsersPage: Page object for the Create Users page.
        """
        self.logger.info("Clicking create users link")
        self.driver.find_element(*self.CREATE_USER_LINK).click()
        
        return CreateUsersPage(self.driver, self.logger)
    
    def open_list_all_users_page(self) -> ListAllUsersPage:
        """
        Open the List All Users page.
        
        Returns:
            ListAllUsersPage: Page object for the List All Users page.
        """
        self.logger.info("Clicking list all users link")
        self.driver.find_element(*self.LIST_ALL_USERS_LINK).click()
        
        return ListAllUsersPage(self.driver, self.logger)
    
