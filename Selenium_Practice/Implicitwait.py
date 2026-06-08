from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://automationexercise.com")
driver.find_element(By.XPATH, "//a[normalize-space()='Signup / Login']").click()
driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("muhi2701@gmail.com")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("1234567890")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()