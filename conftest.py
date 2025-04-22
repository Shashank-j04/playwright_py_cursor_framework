import pytest
from playwright.sync_api import Page
from pytest_bdd import given, when, then, parsers
from pages.base_page import BasePage
from api.api_client import APIClient
from config.config import Config

# Load configuration
config = Config()
config.setup_directories()

# Shared fixtures
@pytest.fixture
def base_page(page: Page):
    return BasePage(page)

@pytest.fixture
def api_client():
    return APIClient()

# Shared step definitions
@given(parsers.parse('I am on the "{page_name}" page'))
def navigate_to_page(base_page, page_name):
    """Navigate to a specific page"""
    page_url = f"/{page_name.lower().replace(' ', '-')}"
    base_page.navigate(page_url)

@given(parsers.parse('I am logged in as "{username}"'))
def logged_in_user(base_page, username):
    """Log in as a specific user"""
    base_page.navigate("/login")
    base_page.fill("#username", username)
    base_page.fill("#password", "password123")  # In real scenario, use secure password
    base_page.click("#login-button")

@when(parsers.parse('I click on the "{element}" element'))
def click_element(base_page, element):
    """Click on a specific element"""
    element_id = f"#{element.lower().replace(' ', '-')}"
    base_page.click(element_id)

@when(parsers.parse('I enter "{text}" in the "{field}" field'))
def enter_text(base_page, text, field):
    """Enter text in a specific field"""
    field_id = f"#{field.lower().replace(' ', '-')}"
    base_page.fill(field_id, text)

@then(parsers.parse('I should see "{text}"'))
def verify_text(base_page, text):
    """Verify text is visible on the page"""
    assert text in base_page.page.content()

@then(parsers.parse('I should be on the "{page_name}" page'))
def verify_page(base_page, page_name):
    """Verify current page"""
    expected_url = f"/{page_name.lower().replace(' ', '-')}"
    assert expected_url in base_page.page.url

# API step definitions
@given(parsers.parse('I have the following data:'))
def parse_data(request):
    """Parse data from Gherkin table"""
    table = request.getfixturevalue('table')
    return {row['key']: row['value'] for row in table}

@then(parsers.parse('the response should contain:'))
def verify_response_data(response, request):
    """Verify response data from Gherkin table"""
    table = request.getfixturevalue('table')
    response_data = response.json()
    for row in table:
        assert row['key'] in response_data
        assert str(response_data[row['key']]) == row['value'] 