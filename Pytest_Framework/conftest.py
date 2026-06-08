import pytest
from selenium import webdriver


@pytest.fixture()
def test_setup_teardown(request):
    #global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo/")
    request.cls.driver = driver
    yield
    driver.quit()
    