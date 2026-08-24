# Selenium PyTest Automation Framework

A UI test automation framework built using Python, Selenium WebDriver, and PyTest. 
The framework follows the Page Object Model (POM) and includes reusable utilities 
for logging, screenshots, test data management, configuration, reporting, and 
multi-browser execution.

## Tech Stack

- Python 3.11
- Selenium WebDriver
- PyTest
- PyTest HTML
- Page Object Model (POM)
- JSON
- Git & GitHub

## Framework Features

- Page Object Model
- Reusable BasePage
- Selenium WebDriver
- PyTest fixtures
- Explicit waits
- Parameterized testing
- JSON-based test data
- Configuration management
- Driver Factory
- Logging
- Automatic screenshots on failure
- PyTest markers
- HTML test reports
- Chrome, Edge and Firefox support

## Project Structure

AutomationFramework/
│
├── config/
│   └── config.json
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── test_data/
│   └── login_data.json
│
├── utils/
│   ├── config_reader.py
│   ├── driver_factory.py
│   ├── logger.py
│   └── test_data_reader.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── .gitignore

## Test Scenarios

### Login

- Valid login with multiple users
- Invalid login with incorrect password

### Cart

- Login
- Add Sauce Labs Backpack to cart
- Verify product in cart

### Checkout

- Login
- Add product to cart
- Navigate to checkout
- Enter customer information
- Complete order
- Verify successful order message

## Installation

Clone the repository:

```bash
git clone https://github.com/prajwal611/selenium-pytest-automation-framework.git
