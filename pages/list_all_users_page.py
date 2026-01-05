from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class ListAllUsersPage:
    """Page object for the List All Users page.
    """
    
    def __init__(self, driver: WebDriver, logger):
        self.page_path = "/users"
        self.driver = driver
        self.logger = logger
        self.wait_for_page_load()
        
    # Locators
    BUTTON_BACK_TO_DASHBOARD = (By.XPATH, "//button[contains(.,'Back')]")
    INPUT_SEARCH = (By.ID, "searchInput")
    TABLE_USERS = (By.TAG_NAME, "table")
    TABLE_USERS_HEADERS = (By.XPATH, "//table/thead/tr/th")
    TABLE_USERS_ROWS = (By.XPATH, "//table/tbody/tr")
    TABLE_USERS_CELLS = (By.TAG_NAME, "td")
    TABLE_NO_USERS_FOUND = (By.ID, "noUsersCell")
        
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
        
    def go_back_to_dashboard(self) -> None:
        """
        Go back to the Dashboard page.
        """
        if self.logger:
            self.logger.info("Clicking back to dashboard button")
        self.driver.find_element(*self.BUTTON_BACK_TO_DASHBOARD).click()
        
    def filter_users_by_name_or_email(self, search_term: str) -> None:
        """
        Filter users by name or email.
        
        Args:
            search_term: The name or email to filter by.
        """
        self.logger.info(f"Filtering users by name or email: {search_term}")
        search_input = self.driver.find_element(*self.INPUT_SEARCH)
        search_input.clear()
        search_input.send_keys(search_term)
    
    def is_user_in_list(self, search_term: str) -> bool:
        """
        Check if a user with the given name or email is present in the users list.
        
        Args:
            search_term: The name or email to search for.
        
        Returns:
            bool: True if the user is found, False otherwise.
        """
        self.logger.info(f"Checking if user with name or email '{search_term}' is in the list")
        rows = self.driver.find_elements(*self.TABLE_USERS_ROWS)
        for row in rows:
            cells = row.find_elements(*self.TABLE_USERS_CELLS)
            for cell in cells:
                if search_term in cell.text:
                    return True
        return False
        
