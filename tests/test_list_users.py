import pytest
from pages.dashboard_page import DashboardPage
from utils.config import BASE_URL


@pytest.mark.parametrize("name,email,role,status", [
    ("Test User", "test@example.com", "Admin", "Active")
],ids=["Create user to filter by name"])
@pytest.mark.smoke
def test_filter_users_by_name(driver, logger, name, email, role, status):
    """
    Test filtering users by name
    """
    result = is_user_in_list(driver, logger, name, email, role, status, search_term=name)
    
    assert result, f"User with name {name} not found in the filtered list"
    
@pytest.mark.parametrize("name,email,role,status", [
    ("Test User", "test@example.com", "Admin", "Active")
],ids=["Create user to filter by email"])
@pytest.mark.smoke
def test_filter_users_by_email(driver, logger, name, email, role, status):
    """
    Test filtering users by email
    """
    result = is_user_in_list(driver, logger, name, email, role, status, search_term=email)
    assert result, f"User with email {email} not found in the filtered list"
  
def is_user_in_list(driver, logger, name, email, role, status, search_term: str) -> bool:
    """
    Test filtering users by email
    """
    logger.info(f"Opening URL: {BASE_URL}")
    driver.get(BASE_URL)
    
    dashboard_page = DashboardPage(driver, logger)
    
    # make sure users are created before filtering
    create_users_page = dashboard_page.open_create_users_page()
    create_users_page.create_10_users()
    
    create_users_page.fill_user_form(
        name=name,
        email=email,
        role=role,
        status=status
    )
    
    create_users_page.click_create_user_button()
    create_users_page.go_back_to_dashboard()

    # filter users by name or email
    list_all_users_page = dashboard_page.open_list_all_users_page()
    list_all_users_page.filter_users_by_name_or_email(search_term)

    return list_all_users_page.is_user_in_list(search_term)