Feature: User API
    As an API consumer
    I want to manage user data through the API
    So that I can perform CRUD operations on user resources

    Scenario: Create a new user
        Given I have valid user data
        When I send a POST request to "/users" with the user data
        Then the response status code should be 201
        And the response should contain the created user data

    Scenario: Get user details
        Given a user exists with ID "123"
        When I send a GET request to "/users/123"
        Then the response status code should be 200
        And the response should contain the user details

    Scenario: Update user details
        Given a user exists with ID "123"
        When I send a PUT request to "/users/123" with updated data
        Then the response status code should be 200
        And the response should contain the updated user data 