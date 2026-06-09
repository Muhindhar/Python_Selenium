from selenium import webdriver
from selenium.webdriver.common.by import By
from read_config import get_config

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get(get_config("basic info", "url"))


def test_valid():
    driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(get_config("search term", "valid"))
    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
    assert driver.find_element(By.XPATH, "//a[normalize-space()='HP LP3065']").is_displayed()


def test_invalid():
    driver.get(get_config("basic info", "url"))
    driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(get_config("search term", "invalid"))
    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
    exp = "There is no product that matches the search criteria."
    actual = driver.find_element(By.XPATH, "//p[contains(text(),'There is no product')]").text
    assert actual == exp


def test_noproduct():
    driver.get(get_config("basic info", "url"))
    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
    exp = "There is no product that matches the search criteria."
    actual = driver.find_element(By.XPATH, "//p[contains(text(),'There is no product')]").text
    assert actual == exp
    
driver.quit()