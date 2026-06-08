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
logged_in = driver.find_element(By.XPATH,"//a[contains(text(),'Logged in as')]").is_displayed()
print("Login Successful:", logged_in)
driver.find_element(By.XPATH, "//a[normalize-space()='Delete Account']").click()
time.sleep(3)
account_deleted = driver.find_element(By.XPATH,"//h2[contains(text(),'Account Deleted!')]").is_displayed()
print("Account Deleted:", account_deleted)
driver.quit()

