import pytest_check as check
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://tutorialsninja.com/demo/")

def test_invalid():
    driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("honda")
    driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
    exp = "There is no product" 
    actual = driver.find_element(By.XPATH,"//p[contains(text(),'There is no product')]").text
    #check.equal(actual, exp, "Message validation failed")
    #print("Execution continues after failure")
    driver.quit()
    check.not_equal(actual, exp, "Message validation failed")
    print("Execution continues after failure")
    
    check.is_true(actual, exp, "Message validation failed")
    print("istrue is passed")
    
    check.is_false(actual, exp, "Message validation failed")
    print("IS false is passed")
    