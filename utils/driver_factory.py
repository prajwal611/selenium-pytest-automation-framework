from selenium import webdriver
class DriverFactory:
    @staticmethod
    def create_driver(browser):
        browser=browser.lower()
        if browser=="chrome":
            driver=webdriver.Chrome()
        elif browser=="edge":
            driver=webdriver.Edge()
        elif browser=="firefox":
            driver=webdriver.Firefox()
        else:
            raise ValueError(
                f"Unsupported browser: {browser}"
            )
        driver.maximize_window()
        return driver