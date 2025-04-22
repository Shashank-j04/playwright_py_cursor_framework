# Playwright Python Test Framework

A modern test automation framework using Playwright, pytest, and pytest-bdd for UI and API testing.

## Project Structure

```
playwright_py_cursor_framework/
├── features/                    # BDD feature files
│   ├── ui/                     # UI feature files
│   └── api/                    # API feature files
├── tests/                      # Test implementation
│   ├── ui/                     # UI test files
│   ├── api/                    # API test files
│   └── steps/                  # Step definitions
├── pages/                      # Page objects
├── api/                        # API client and models
├── utils/                      # Utility functions
├── config/                     # Configuration files
│   └── config.py               # Main configuration
├── reports/                    # Test reports
├── .env                        # Environment variables
├── pyproject.toml              # Poetry configuration
└── README.md                   # Project documentation
```

## Setup

1. Install Poetry (if not already installed):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

3. Install Playwright browsers:
   ```bash
   poetry run playwright install
   ```

## Running Tests

- Run all tests:
  ```bash
  poetry run pytest
  ```

- Run UI tests:
  ```bash
  poetry run pytest -m ui
  ```

- Run API tests:
  ```bash
  poetry run pytest -m api
  ```

- Run BDD tests:
  ```bash
  poetry run pytest -m bdd
  ```

## Features

- UI testing with Playwright
- API testing with requests
- BDD syntax with pytest-bdd
- Parallel test execution
- HTML test reports
- Environment configuration
- Page Object Model
- API client abstraction