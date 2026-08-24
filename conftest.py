import os
import pytest
from selenium import webdriver
from utils.config_reader import load_config
from utils.driver_factory import DriverFactory
@pytest.fixture
def driver(request):
    config=load_config()
    browser=config["browser"]
    driver=DriverFactory.create_driver(browser)
    yield driver 
    if hasattr(request.node,"rep_call") and  request.node.rep_call.failed: os.makedirs("screenshots",exist_ok=True)
    screenshot_path= os.path.join("screenshots",f"{request.node.name}.png")
    driver.save_screenshot(screenshot_path)
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome=yield
    report=outcome.get_result()
    setattr(item,f"rep_{report.when}",report)