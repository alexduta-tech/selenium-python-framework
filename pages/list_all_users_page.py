from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utils.config import IMPLICIT_WAIT
from utils.selenium_utils import SeleniumUtils

class ListAllUsersPage():
    """Page object for the List All Users page.
    """
    
    def __init__(self, driver: WebDriver, logger):
        self.page_path = "/users"
        self.driver = driver
        self.logger = logger
        self.selenium_utils = SeleniumUtils(self.driver, self.logger)
        self.wait_for_page_load()
        
    # Locators
    BUTTON_BACK_TO_DASHBOARD = (By.XPATH, "//button[contains(.,'Back')]")
    INPUT_SEARCH = (By.ID, "searchInput")
    SELECT_ROLE = (By.ID, "filterRole")
    SELECT_STATUS = (By.ID, "filterStatus")
    BUTTON_RESET_FILTERS = (By.XPATH, "//button[text()='Reset Filters']")    
    TABLE_USERS = (By.TAG_NAME, "table")
    TABLE_USERS_HEADERS = (By.XPATH, "//table/thead/tr/th")
    TABLE_USERS_ROWS = (By.XPATH, "//table/tbody/tr")
    TABLE_NO_USERS_FOUND_MESSAGE = (By.ID, "noUsersCell")
    TABLE_NEXT_PAGE_BUTTON = (By.ID, "nextPage")
    TABLE_PREVIOUS_PAGE_BUTTON = (By.ID, "prevPage")
    LOADING_SPINNER = (By.ID, "spinner")
        
    # Page Object Methods
    def wait_for_page_load(self, timeout=5) -> None:
        """
        Wait for the List All Users page to load by checking the presence of the uri.
        
        Args:
            timeout: Maximum time to wait in seconds
        """
        if self.logger:
            self.logger.info("Waiting for List All Users page to load")
        WebDriverWait(self.driver, timeout).until(
            lambda d: self.page_path in d.current_url 
        )   
        
    def is_at(self) -> bool:
        """
        Verify that we are on the List All Users page by checking for the presence of a mandatory element.
        
        Returns:
            bool: True if on List All Users page, False otherwise
        """
        return self.selenium_utils.is_element_present(self.INPUT_SEARCH)
        
    def go_back_to_dashboard(self) -> None:
        """
        Go back to the Dashboard page.
        """
        if self.logger:
            self.logger.info("Clicking back to dashboard button")
        self.driver.find_element(*self.BUTTON_BACK_TO_DASHBOARD).click()

    def filter_users(self, **kwargs) -> 'ListAllUsersPage':
        """
        Filter users by name, email, role, or status.
        
        Args:
            name: User's name
            email: User's email
            role: User's role
            status: User's status
        
        Args:
            kwargs: Key-value pairs representing user attributes 
                to search for. Examples:
                filter_users_by_name_or_email_by_kwargs(name="John")
                filter_users_by_name_or_email_by_kwargs(email="john@example.com")
                filter_users_by_name_or_email_by_kwargs(name="John", role="Admin", status="Active")
        """
        if kwargs.get('name'):
            self.logger.info(f"Filtering users by name: {kwargs['name']}")
            search_input = self.driver.find_element(*self.INPUT_SEARCH)
            search_input.clear()
            search_input.send_keys(kwargs['name'])
        elif kwargs.get('email'):
            self.logger.info(f"Filtering users by email: {kwargs['email']}")
            search_input = self.driver.find_element(*self.INPUT_SEARCH)
            search_input.clear()
            search_input.send_keys(kwargs['email'])
        if kwargs.get('role'):
            self.logger.info(f"Filtering users by role: {kwargs['role']}")
            role_element = self.driver.find_element(*self.SELECT_ROLE)
            select_role = Select(role_element)
            select_role.select_by_visible_text(kwargs['role'])
        if kwargs.get('status'):
            self.logger.info(f"Filtering users by status: {kwargs['status']}")  
            status_element = self.driver.find_element(*self.SELECT_STATUS)
            select_status = Select(status_element)
            select_status.select_by_visible_text(kwargs['status'])
        if not any(k in kwargs for k in ['name', 'email', 'role', 'status']):
            self.logger.warning("No valid keyword argument provided for filtering by name or email. Please use 'name' or 'email'.")
        
        # wait for possible loading spinner to disappear
        if self.selenium_utils.is_element_present(self.LOADING_SPINNER):
            WebDriverWait(self.driver, IMPLICIT_WAIT).until(
                lambda d: not d.find_element(*self.LOADING_SPINNER).is_displayed()
            )
        
        return self
    
    def is_user_in_list(self, **kwargs) -> bool:
        """
        Check if a user with the given attributes is present in the users list.
        
        Args:
            kwargs: Key-value pairs representing user attributes 
                to search for. Examples:
                is_user_in_list(name="John", email="john@example.com")
                is_user_in_list(role="Admin")
        
        Returns:
            bool: True if the user is found, False otherwise.
        """
        is_user_found = True
        
        self.logger.info(f"Checking if user with attributes {kwargs} is in the list of users")  
        rows = self.driver.find_elements(*self.TABLE_USERS_ROWS)
        for row in rows:
            # check all provided attributes, ignore case when searching for values
            for key, value in kwargs.items():
                if value.lower() in row.text.lower():
                    self.logger.info(f"User attribute '{key}: {value}' was found for row: {row.text}") 
                else:
                    self.logger.error(f"User attribute '{key}: {value}' was not found for row: {row.text}")
                    is_user_found = False
        return is_user_found
    
    def is_no_users_found_message_displayed(self) -> bool:
        """
        Check if the 'No users found' message is displayed.
        
        Returns:
            bool: True if the message is displayed, False otherwise.
        """
        self.logger.info("Checking if 'No users found' message is displayed")
        return self.selenium_utils.is_element_present(self.TABLE_NO_USERS_FOUND_MESSAGE)
    
    def go_to_next_page(self) -> 'ListAllUsersPage':
        """
        Go to the next page of the users list.
        """
        self.logger.info("Clicking next page button")
        self.driver.find_element(*self.TABLE_NEXT_PAGE_BUTTON).click()
 
        # wait for possible loading spinner to disappear
        if self.selenium_utils.is_element_present(self.LOADING_SPINNER):
            WebDriverWait(self.driver, IMPLICIT_WAIT).until(
                lambda d: not d.find_element(*self.LOADING_SPINNER).is_displayed()
            )
 
        return self
    
    def go_to_previous_page(self) -> 'ListAllUsersPage':
        """
        Go to the previous page of the users list.
        """
        self.logger.info("Clicking previous page button")
        self.driver.find_element(*self.TABLE_PREVIOUS_PAGE_BUTTON).click()
        
        # wait for possible loading spinner to disappear
        if self.selenium_utils.is_element_present(self.LOADING_SPINNER):
            WebDriverWait(self.driver, IMPLICIT_WAIT).until(
                lambda d: not d.find_element(*self.LOADING_SPINNER).is_displayed()
            )
                
        return self

    def get_displayed_users_rows(self) -> list:
        """
        Get all user rows from the users table.

        Returns:
            list: List of strings representing user row texts.
        """
        self.logger.info("Getting all user rows from the users table")
        result = [row.text for row in self.driver.find_elements(*self.TABLE_USERS_ROWS)]
        self.logger.info(f"User rows: {result}")
        return result
    
    def reset_filters(self) -> 'ListAllUsersPage':
        """
        Reset all applied filters.
        """
        self.logger.info("Clicking reset filters button")
        self.driver.find_element(*self.BUTTON_RESET_FILTERS).click()
        
        # wait for possible loading spinner to disappear
        if self.selenium_utils.is_element_present(self.LOADING_SPINNER):
            WebDriverWait(self.driver, IMPLICIT_WAIT).until(
                lambda d: not d.find_element(*self.LOADING_SPINNER).is_displayed()
            )
        
        return self