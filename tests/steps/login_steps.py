from pytest_bdd import given, when, then, parsers
from playwright.sync_api import Page
from pages.base_page import BasePage
import pytest

@pytest.fixture
def base_page(page: Page):
    return BasePage(page)

@given("I am on the login page")
def navigate_to_login(base_page):
    base_page.navigate("/login")

@when(parsers.parse('I enter valid username "{username}" and password "{password}"'))
def enter_valid_credentials(base_page, username, password):
    base_page.fill("#username", username)
    base_page.fill("#password", password)

@when(parsers.parse('I enter invalid username "{username}" and password "{password}"'))
def enter_invalid_credentials(base_page, username, password):
    base_page.fill("#username", username)
    base_page.fill("#password", password)

@when("I click the login button")
def click_login_button(base_page):
    base_page.click("#login-button")

@then("I should be redirected to the dashboard")
def verify_dashboard_redirect(base_page):
    assert "/dashboard" in base_page.page.url

@then(parsers.parse('I should see the welcome message "{message}"'))
def verify_welcome_message(base_page, message):
    actual_message = base_page.get_text("#welcome-message")
    assert actual_message == message

@then(parsers.parse('I should see an error message "{message}"'))
def verify_error_message(base_page, message):
    actual_message = base_page.get_text("#error-message")
    assert actual_message == message 