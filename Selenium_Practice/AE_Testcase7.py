from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://automationexercise.com")

wait = WebDriverWait(driver, 10)

testcase = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Test Cases')]")))
testcase.click()
visible = driver.find_element(By.XPATH, "//h2[@class='title text-center']")

if visible.is_displayed():
    print("Testcase page displayed")
else:
    print("Not displayed")
