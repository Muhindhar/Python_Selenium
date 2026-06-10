from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")
driver.implicitly_wait(10)

login = driver.find_element(locate_with(By.XPATH,"//a[text()='Register']")
                            .below((By.XPATH,"//a[normalize-space()='Login']")))
