from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.create_users_page import CreateUsersPage
from pages.list_all_users_page import ListAllUsersPage
from pages.user_overlap_page import UserSearchOverlapPage
from pages.user_dialogs_page import UserDialogsPage
from utils.config import IMPLICIT_WAIT
from utils.selenium_utils import SeleniumUtils

class DashboardPage():
    """Page object for the Dashboard page.
    """
    
    def __init__(self, driver: WebDriver, logger):
        self.driver = driver
        self.logger = logger
        self.selenium_utils = SeleniumUtils(self.driver, self.logger)
    
    # Locators
    CREATE_USER_LINK = (By.XPATH, "//a[@href='/create-user']")
    LIST_ALL_USERS_LINK = (By.XPATH, "//a[@href='/users']")
    USER_DIALOGS_LINK = (By.XPATH, "//a[@href='/user-dialogs']")
    USER_SEARCH_OVERLAP_LINK = (By.XPATH, "//a[@href='/user-search-overlap']")  
    LOADING_SPINNER = (By.CSS_SELECTOR, ".spinner")

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
        self.selenium_utils.wait_for_element_to_disappear(self.LOADING_SPINNER)       
        
        return ListAllUsersPage(self.driver, self.logger)
    
    def open_user_dialogs_page(self) -> 'UserDialogsPage':
        """
        Open the User Dialogs page.
        
        Returns:
            UserDialogsPage: Page object for the User Dialogs page.
        """
        self.logger.info("Clicking user dialogs link")
        self.driver.find_element(*self.USER_DIALOGS_LINK).click()
        
        return UserDialogsPage(self.driver, self.logger)
    
    def open_user_search_overlap_page(self) -> 'UserSearchOverlapPage':
        """
        Open the User Search Overlap page.
        
        Returns:
            UserSearchOverlapPage: Page object for the User Search Overlap page.
        """
        self.logger.info("Clicking user search overlap link")
        self.driver.find_element(*self.USER_SEARCH_OVERLAP_LINK).click()
        
        return UserSearchOverlapPage(self.driver, self.logger)
        