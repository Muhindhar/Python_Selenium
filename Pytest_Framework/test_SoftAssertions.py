import pytest_check as check
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

def test_invalid():

    driver.get("https://tutorialsninja.com/demo/")

    driver.find_element(
        By.XPATH,
        "//input[@placeholder='Search']"
    ).send_keys("honda")

    driver.find_element(
        By.XPATH,
        "//button[@class='btn btn-default btn-lg']"
    ).click()

    actual = driver.find_element(
        By.XPATH,
        "//p[contains(text(),'There is no product')]"
    ).text

    expected = "There is no product that matches the search criteria."

    check.equal(actual, expected, "Text validation")
    print("Validation 1 completed")

    check.is_true("search criteria" in actual, "Contains validation")
    print("Validation 2 completed")

    check.is_false(actual == "Honda", "Honda validation")
    print("Validation 3 completed")

    driver.quit()
