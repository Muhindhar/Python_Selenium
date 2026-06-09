import pytest_check as check
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://tutorialsninja.com/demo/")

def test_invalid():

    driver.find_element(
        By.XPATH,
        "//input[@placeholder='Search']"
    ).send_keys("honda")

    driver.find_element(
        By.XPATH,
        "//button[@class='btn btn-default btn-lg']"
    ).click()

    exp = "There is no product"

    actual = driver.find_element(
        By.XPATH,
        "//p[contains(text(),'There is no product')]"
    ).text

    check.not_equal(actual, exp, "not_equal validation")
    print("not_equal passed")

    check.is_true(actual != exp, "is_true validation")
    print("is_true passed")

    check.is_false(actual == exp, "is_false validation")
    print("is_false passed")

    driver.quit()