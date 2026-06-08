from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/alerts")
driver.find_element(By.ID, "promtButton").click()
alert = driver.switch_to.alert
alert.send_keys("Muhindhar")
alert.accept()
res = driver.find_element(By.ID, "promptResult")
if res.is_displayed():
    print("Success")
    print(res.text)
else:
    print("Failed")