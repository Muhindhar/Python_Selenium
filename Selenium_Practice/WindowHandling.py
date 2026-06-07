from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/browser-windows")
parent = driver.current_window_handle
print("Parent window : ",driver.current_window_handle)
driver.find_element(By.XPATH,"//button[@id='tabButton']").click()
print("Switched to child window")
driver.switch_to.window(parent)
print("Switched to parent window")