from selenium.webdriver.common.by import By  
from pages.base_page import BasePage
from utils.logger import get_logger
class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.logger=get_logger(__name__)
        self.username=(By.ID,"user-name")
        self.password=(By.ID,"password")
        self.login_button=(By.ID,"login-button")
        self.error_message=(By.CSS_SELECTOR,"[data-test='error']")
    def enter_username(self,username):
        self.logger.info("Entering username")
        self.type_text(self.username,username)
    def enter_password(self,password):
        self.logger.info("Entering password")
        self.type_text(self.password,password)
    def click_login(self):
        self.logger.info("Clicking login button")
        self.click(self.login_button) 
    def get_error_message(self):
        return self.get_text(self.error_message)