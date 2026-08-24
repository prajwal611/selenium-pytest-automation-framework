from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class ProductsPage(BasePage):
    backpack=(By.ID,"add-to-cart-sauce-labs-backpack")
    cart_icon=(By.CLASS_NAME,"shopping_cart_link")
    def add_backpack_to_cart(self):
        self.click(self.backpack)
    def open_cart(self):
        self.click(self.cart_icon)