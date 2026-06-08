from selenium import webdriver 
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/")
driver.get_screenshot_as_file(r"D:\Python_Selenium\python_selenium\Screenshots\pngfile.png")