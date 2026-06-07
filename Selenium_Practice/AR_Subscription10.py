from argparse import Action

from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from python_selenium.Selenium_Practice.AR_Subscription10 import footer
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://automationexercise.com")
exp = "https://automationexercise.com/"
current = driver.current_url
print(current)
Action = ActionChains(driver)
footer = driver.find_element(By.XPATH,"//div[@class='footer-widget']")
Action.scroll_to_element(footer)
substext = driver.find_element(By.XPATH,"//div[@class='single-widget']//child::h2")
if substext.is_displayed():
    print("Subscription text displayed")
else:
    print("Subscription text not displayed")
mailbox = driver.find_element(By.XPATH,"//input[@id='susbscribe_email']").send_keys("muhi27@gmail.com")
sendbtn = driver.find_element(By.XPATH,"//button[@id='subscribe']").click()
