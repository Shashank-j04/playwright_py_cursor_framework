Feature: User Login
    As a user
    I want to log in to the application
    So that I can access my account

    Background:
        Given I am on the "login" page

    Scenario: Successful login with valid credentials
        When I enter "testuser" in the "username" field
        And I enter "testpass" in the "password" field
        And I click on the "login button" element
        Then I should be on the "dashboard" page
        And I should see "Welcome, testuser"

    Scenario: Failed login with invalid credentials
        When I enter "wronguser" in the "username" field
        And I enter "wrongpass" in the "password" field
        And I click on the "login button" element
        Then I should see "Invalid credentials"
        And I should be on the "login" page

    Scenario: Login with empty credentials
        When I enter "" in the "username" field
        And I enter "" in the "password" field
        And I click on the "login button" element
        Then I should see "Username and password are required"
        And I should be on the "login" page 