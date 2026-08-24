from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class CheckoutPage(BasePage):
    checkout_button=(By.ID,"checkout")
    first_name=(By.ID,"first-name")
    last_name=(By.ID,"last-name")
    postal_code=(By.ID,"postal-code")
    continue_button=(By.ID,"continue")
    finish_button=(By.ID,"finish")
    success_message=(By.CSS_SELECTOR,"[data-test='complete-header']")
    def click_checkout(self):
        self.click(self.checkout_button)
    def enter_first_name(self,first_name):
        self.type_text(self.first_name,first_name)
    def enter_last_name(self,last_name):
        self.type_text(self.last_name,last_name)
    def enter_postal_code(self,postal_code):
        self.type_text(self.postal_code,postal_code)
    def click_continue(self):
        self.click(self.continue_button)
    def click_finish(self):
        self.click(self.finish_button)
    def get_success_message(self):
        return self.get_text(self.success_message)
    
