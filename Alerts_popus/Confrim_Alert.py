import time
from selenium import webdriver
import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

driver = webdriver.Chrome()
driver.maximize_window()
wait =WebDriverWait(driver,10)
driver.get("https://demoqa.com/alerts")

#confrim alert
confmalert = driver.find_element(By.XPATH,"//button[@id='confirmButton']").click()
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
time.sleep(4)
alert.accept()
print("alert accpeted")

#confirm-dismiss
confmalert = driver.find_element(By.XPATH,"//button[@id='confirmButton']").click()
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
time.sleep(4)
alert.dismiss()
print("Alert dismissed")
