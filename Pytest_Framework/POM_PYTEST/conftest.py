import pytest
from selenium import webdriver
from read_config import get_config

@pytest.fixture()
def setup_teardown(request):
    browser = get_config("basic info", "browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(get_config("basic info", "url"))
    request.cls.driver = driver
    yield
    driver.quit()
