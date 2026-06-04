from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com")
print("Current URL:", driver.current_url)
driver.find_element(By.XPATH, "//a[normalize-space()='Signup / Login']").click()
driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("muhindhar27@gmail.com")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("12345678")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
time.sleep(3)
check = driver.find_element(By.XPATH,"//p[normalize-space()='Your email or password is incorrect!']").text
checkstr = "Your email or password is incorrect!"
print(check)
assert check == checkstr,"error msg not shown"