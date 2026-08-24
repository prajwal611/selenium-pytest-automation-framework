from selenium import webdriver
import pytest
from pages.login_page import LoginPage
from utils.logger import get_logger
from utils.test_data_reader import load_json_data
from utils.config_reader import load_config

logger=get_logger(__name__)
LOGIN_DATA=load_json_data("test_data/login_data.json")
config=load_config()

@pytest.mark.smoke
@pytest.mark.login
@pytest.mark.parametrize(
    "login_data",
    LOGIN_DATA
)
def test_valid_login(driver,login_data):
    username=login_data["username"]
    password=login_data["password"]
    logger.info(f"Testing login with user: {username}")
    driver.get(config["base_url"])
    login_page=LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    logger.info(f"Verifying login for user: {username}")
    assert "inventory" in driver.current_url
    logger.info(f"Login test completed successfully: {username}")

@pytest.mark.login
def test_invalid_login(driver):
    logger.info("Testing invalid login")
    driver.get(config["base_url"])
    login_page=LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("wrong_password")
    login_page.click_login()
    error_message=login_page.get_error_message()
    logger.info("Verifying login error message")
    assert "Username and password do not match" in error_message