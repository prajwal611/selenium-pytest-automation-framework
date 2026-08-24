import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

from utils.config_reader import load_config
from utils.logger import get_logger
logger=get_logger(__name__)
config=load_config()

@pytest.mark.smoke
def test_add_product_to_cart(driver):
    logger.info("Starting add-to-cart test")
    driver.get(config["base_url"])
    login_page=LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    products_page=ProductsPage(driver)
    products_page.add_backpack_to_cart()
    products_page.open_cart()
    cart_page=CartPage(driver)
    product_name=cart_page.get_backpack_name()
    logger.info(f"Product found in cart:{product_name}")
    assert product_name=="Sauce Labs Backpack"
    logger.info("Add-to-cart test completed successfully")
