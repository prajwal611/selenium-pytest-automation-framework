from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class CartPage(BasePage):
    backpack_item=(
        By.CSS_SELECTOR,
        "[data-test='inventory-item-name']"
    )
    def get_backpack_name(self):
        return self.get_text(self.backpack_item)
    