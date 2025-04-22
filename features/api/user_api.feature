Feature: User API
    As an API consumer
    I want to manage user data through the API
    So that I can perform CRUD operations on user resources

    Scenario: Create a new user
        Given I have the following data:
            | key      | value                |
            | name     | John Doe             |
            | email    | john.doe@example.com |
            | password | securepass123        |
        When I send a POST request to "/users" with the user data
        Then the response status code should be 201
        And the response should contain:
            | key   | value                |
            | name  | John Doe             |
            | email | john.doe@example.com |

    Scenario: Get user details
        Given a user exists with ID "123"
        When I send a GET request to "/users/123"
        Then the response status code should be 200
        And the response should contain:
            | key   | value                |
            | id    | 123                  |
            | name  | John Doe             |
            | email | john.doe@example.com |

    Scenario: Update user details
        Given a user exists with ID "123"
        And I have the following data:
            | key   | value                 |
            | name  | Jane Doe              |
            | email | jane.doe@example.com  |
        When I send a PUT request to "/users/123" with updated data
        Then the response status code should be 200
        And the response should contain:
            | key   | value                 |
            | name  | Jane Doe              |
            | email | jane.doe@example.com  |

    Scenario: Delete user
        Given a user exists with ID "123"
        When I send a DELETE request to "/users/123"
        Then the response status code should be 204
        And I send a GET request to "/users/123"
        Then the response status code should be 404 