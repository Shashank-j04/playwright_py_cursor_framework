Feature: User Login
    As a user
    I want to log in to the application
    So that I can access my account

    Scenario: Successful login with valid credentials
        Given I am on the login page
        When I enter valid username "testuser" and password "testpass"
        And I click the login button
        Then I should be redirected to the dashboard
        And I should see the welcome message "Welcome, testuser"

    Scenario: Failed login with invalid credentials
        Given I am on the login page
        When I enter invalid username "wronguser" and password "wrongpass"
        And I click the login button
        Then I should see an error message "Invalid credentials" 