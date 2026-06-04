from os import wait

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver,10)
driver.get("http://automationexercise.com")
homepg = driver.find_element(By.XPATH,"//img[@alt='Website for automation practice']").is_displayed()
if(homepg):
    print("Displayed")
else:
    print("Not displayed")
ctctus = driver.find_element(By.XPATH,"//a[normalize-space()='Contact us']").click()
name= driver.find_element(By.XPATH,"//input[@placeholder='Name']").send_keys("Muhindhar")
email = driver.find_element(By.XPATH,"//input[@placeholder='Email']").send_keys("muhi2701@gmail.com")
sub = driver.find_element(By.XPATH,"//input[@placeholder='Subject']").send_keys("Demo")
msg = driver.find_element(By.XPATH,"//textarea[@id='message']").send_keys("Text as demo msg!!!")
choosefile = driver.find_element(By.XPATH, "//input[@name='upload_file']")
choosefile.send_keys(r"C:\Users\Muhindhar S V\OneDrive\Documents\GCE pp certit.pdf")
submit = driver.find_element(By.XPATH,"//input[@name='submit']")
submit.click()
wait.until(EC.alert_is_present())   
alert = driver.switch_to.alert
alert.accept()
wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='status alert alert-success']")))
succ = driver.find_element(By.XPATH,"//div[@class='status alert alert-success']").text
if succ:
    print("Success")
else:
    print("Failed")
homepg2 = driver.find_element(By.XPATH,"//img[@alt='Website for automation practice']").is_displayed()
if(homepg2):
    print("Displayed")
else:
    print("Not displayed")