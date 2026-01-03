from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select

from utils.constants import MESSAGE_CREATE_10_USERS_SUCCESS_TEXT, MESSAGE_CREATE_USER_ERROR_REQUIRED_FIELDS_TEXT, MESSAGE_CREATE_USER_SUCCESS_TEXT
from utils.selenium_utils import SeleniumUtils

class CreateUsersPage():
    """
    Page object for the Create Users page.
    """
    
    def __init__(self, driver: WebDriver, logger):
        self.page_path = "/create-user"
        self.driver = driver
        self.logger = logger
        self.selenium_utils = SeleniumUtils(self.driver, self.logger)
        self.wait_for_page_load()
        
    # Locators        
    BUTTON_CREATE_USER = (By.XPATH, "//button[text()='Create User']")
    BUTTON_CREATE_10_USERS = (By.XPATH, "//button[text()='Create 10 Users']")
    MESSAGE_GENERIC_LOCATOR = lambda self, msg: (By.XPATH, f"//div[text()='{msg}']")
    INPUT_NAME = (By.ID, "name")
    INPUT_EMAIL = (By.ID, "email")
    SELECT_ROLE = (By.ID, "role")
    SELECT_STATUS = (By.ID, "status")
    INPUT_PROFILE_PHOTO = (By.XPATH, "//input[@type='file']")
    
    # Page Object Methods
    def wait_for_page_load(self, timeout=5) -> None: 
        """
        Wait for the Create Users page to load by checking the presence of the uri.
        
        Args:
            timeout: Maximum time to wait in seconds
        """
        self.logger.info("Waiting for Create Users page to load")
        WebDriverWait(self.driver, timeout).until(
            lambda d: self.page_path in d.current_url 
        )    

    def is_at(self) -> bool:
        """
        Verify that we are on the Create Users page by checking for the presence of a mandatory element.
        
        Returns:
            bool: True if on Create Users page, False otherwise
        """
        return self.selenium_utils.is_element_present(self.BUTTON_CREATE_10_USERS)
    
    def click_create_user_button(self) -> 'CreateUsersPage':
        """
        Click the Create User button.
        """
        self.logger.info("Clicking create user button")
        self.driver.find_element(*self.BUTTON_CREATE_USER).click()
        
        return self
        
    def create_10_users(self) -> 'CreateUsersPage':
        """
        Click the Create 10 Users button.
        """
        self.logger.info("Clicking create 10 users button")
        self.driver.find_element(*self.BUTTON_CREATE_10_USERS).click()
        
        return self

    def is_required_fields_error_displayed(self) -> bool:
        """
        Check if the required fields error message is displayed.
        
        Returns:
            bool: True if the error message is displayed, False otherwise.
        """
        return self.selenium_utils.is_element_present(self.MESSAGE_GENERIC_LOCATOR(MESSAGE_CREATE_USER_ERROR_REQUIRED_FIELDS_TEXT))
    
    def fill_user_form(self, name, email, role, status, profile_photo_path=None) -> 'CreateUsersPage':
        """
        Fill the user creation form with provided details.
        
        Args:
            name: User's name
            email: User's email
            role: User's role
            status: User's status
            profile_photo_path: Path to the profile photo file (optional)
        """
        self.logger.info("Filling user creation form")
        self.logger.info(f"Name: {name}")
        self.driver.find_element(*self.INPUT_NAME).send_keys(name)
        self.logger.info(f"Email: {email}")
        self.driver.find_element(*self.INPUT_EMAIL).send_keys(email)
        
        # Select role and status
        self.logger.info(f"Role: {role}")
        role_element = self.driver.find_element(*self.SELECT_ROLE)
        select_role = Select(role_element)
        select_role.select_by_visible_text(role)

        self.logger.info(f"Status: {status}")
        status_element = self.driver.find_element(*self.SELECT_STATUS)
        select_status = Select(status_element)
        select_status.select_by_visible_text(status)

        if profile_photo_path:
            self.logger.info(f"Uploading profile picture: {profile_photo_path}")
            self.driver.find_element(*self.INPUT_PROFILE_PHOTO).send_keys(profile_photo_path)   
            
        return self

    def is_user_created(self) -> bool:
        """
        Check if the user creation success message is displayed.
        
        Returns:
            bool: True if the success message is displayed, False otherwise.
        """
        return self.selenium_utils.is_element_present(self.MESSAGE_GENERIC_LOCATOR(MESSAGE_CREATE_USER_SUCCESS_TEXT))
    
    def are_10_users_created(self) -> bool:
        """
        Check if the user creation success message for 10 users is displayed.
        
        Returns:
            bool: True if the success message is displayed, False otherwise.
        """
        return self.selenium_utils.is_element_present(self.MESSAGE_GENERIC_LOCATOR(MESSAGE_CREATE_10_USERS_SUCCESS_TEXT))