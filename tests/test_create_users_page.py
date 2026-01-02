"""
Test suite for the create users page
"""
import pytest
from utils.config import BASE_URL
from pages.dashboard_page import DashboardPage

# create venv: python -m venv .venv
# activate venv: .\.venv\Scripts\activate
# install dependencies: pip install -r requirements.txt
# run tests: pytest -m smoke --html=reports/report.html --self-contained-html
@pytest.mark.smoke
def test_access_create_users_page(driver, logger):
    """
    Test access to the create users page
    """
    logger.info(f"Opening URL: {BASE_URL}")
    driver.get(BASE_URL)
    
    dashboard_page = DashboardPage(driver, logger)
    create_users_page = dashboard_page.open_create_users_page()
    
    assert create_users_page.is_at(), "Failed to access create users page"
    
@pytest.mark.smoke
def test_create_user_required_fields(driver, logger):
    """
    Test negative flow for creating a user: name and email are required fields
    """
    logger.info(f"Opening URL: {BASE_URL}")
    driver.get(BASE_URL)
    
    dashboard_page = DashboardPage(driver, logger)
    create_users_page = dashboard_page.open_create_users_page()
    
    create_users_page.click_create_user_button()
    assert create_users_page.is_required_fields_error_displayed(), "Error message was not displayed for required fields: Name and Email"
    
