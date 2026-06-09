import pytest
from selenium import webdriver

@pytest.fixture()
def test_setup_teardown(request):

    browser = getattr(request, "param", "chrome")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()

    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo/")

    request.cls.driver = driver

    yield

    driver.quit()