from pytest_bdd import given, when, then, parsers
from api.api_client import APIClient
import pytest

@pytest.fixture
def api_client():
    return APIClient()

@given("I have valid user data")
def valid_user_data():
    return {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "password": "securepass123"
    }

@given(parsers.parse('a user exists with ID "{user_id}"'))
def existing_user(api_client, user_id):
    # In a real scenario, you might want to create the user first
    # or ensure it exists in the test environment
    return user_id

@when(parsers.parse('I send a {method} request to "{endpoint}" with the user data'))
def send_request_with_data(api_client, method, endpoint, valid_user_data):
    method = method.lower()
    response = getattr(api_client, method)(endpoint, json=valid_user_data)
    return response

@when(parsers.parse('I send a {method} request to "{endpoint}"'))
def send_request(api_client, method, endpoint):
    method = method.lower()
    response = getattr(api_client, method)(endpoint)
    return response

@then(parsers.parse('the response status code should be {status_code}'))
def verify_status_code(response, status_code):
    assert response.status_code == int(status_code)

@then("the response should contain the created user data")
def verify_created_user_data(response, valid_user_data):
    response_data = response.json()
    assert response_data["name"] == valid_user_data["name"]
    assert response_data["email"] == valid_user_data["email"]
    # Note: Password should not be returned in the response

@then("the response should contain the user details")
def verify_user_details(response):
    response_data = response.json()
    assert "id" in response_data
    assert "name" in response_data
    assert "email" in response_data

@then("the response should contain the updated user data")
def verify_updated_user_data(response, valid_user_data):
    response_data = response.json()
    assert response_data["name"] == valid_user_data["name"]
    assert response_data["email"] == valid_user_data["email"] 