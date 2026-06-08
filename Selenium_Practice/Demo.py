from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window
URL=("https://www.google.co.in")
driver.get(URL)
print(driver.title)
time.sleep(5)
driver.close()