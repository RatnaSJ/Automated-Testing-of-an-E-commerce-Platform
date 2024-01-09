import pytest
from selenium import webdriver

from Utilities import ReadConfig


@pytest.fixture()
def setup_browser(request):
    print("before reading configuration")
    browser = ReadConfig.read_configuration('basic info', 'browser')
    print("after reading configuration")
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Provide a valid browser")
    driver.maximize_window()
    app_url = ReadConfig.read_configuration("basic info", "url")
    driver.get(app_url)
    request.cls.driver = driver
    yield driver
    driver.quit()

