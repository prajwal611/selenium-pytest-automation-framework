import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.config_reader import load_config 
from utils.logger import get_logger

logger=get_logger(__name__)
config=load_config()

@pytest.mark.smoke
def test_complete_checkout(driver):
    logger.info("Starting checkout test")
    driver.get(config["base_url"])
    login_page=LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    products_page=ProductsPage(driver)
    products_page.add_backpack_to_cart()
    products_page.open_cart()

    checkout_page=CheckoutPage(driver)
    checkout_page.click_checkout()
    checkout_page.enter_first_name("Prajwal")
    checkout_page.enter_last_name("Tester")
    checkout_page.enter_postal_code("226001")
    checkout_page.click_continue()
    checkout_page.click_finish()
    success_message=checkout_page.get_success_message()
    logger.info(f"Checkout result: {success_message}")
    assert success_message=="Thank you for your order!"
    logger.info("Checkout test completed successfully")
    
