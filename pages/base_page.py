from selenium.webdriver.support.ui import WebDriverWait
from utils.config_reader import load_config
from selenium.webdriver.support import expected_conditions as EC
class BasePage:
    def __init__(self,driver):
        self.driver=driver
        config=load_config()
        timeout=config["timeout"]
        self.wait=WebDriverWait(driver,timeout)
    def click(self,locator):
        element=self.wait.until(lambda driver:driver.find_element(*locator))
        self.wait.until(
            lambda driver:element.is_displayed() and element.is_enabled()
        )
        element.click()
        
                    
    def type_text(self,locator,text):
        element=self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.click()
        element.clear
        element.send_keys(text)

    def get_text(self,locator):
        element=self.wait.until(lambda driver:driver.find_element(*locator))
        return element.text
    def find_element(self,locator):
        return self.wait.until(
            lambda driver:
            driver.find_element(*locator)
        )
    
