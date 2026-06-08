import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/tool-tips")
textbox = driver.find_element(By.XPATH,"//input[@id='toolTipTextField']")
Action = ActionChains(driver)
time.sleep(5)
textbox = Action.move_to_element(textbox).perform()
time.sleep(5)
tooltip = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='tooltip-inner']")))
print(tooltip.text)