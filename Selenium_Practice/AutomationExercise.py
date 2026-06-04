from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://automationexercise.com")
signup = driver.find_element(By.XPATH,"//a[normalize-space()='Signup / Login']")
signup.click()
name = driver.find_element(By.XPATH,"//input[@placeholder='Name']").send_keys("demomuhi9")
email = driver.find_element(By.XPATH,"//input[@data-qa='signup-email']").send_keys("demomuhi9@gmail.com")
signupbtn = driver.find_element(By.XPATH,"//button[normalize-space()='Signup']").click()
title = driver.find_element(By.ID,"uniform-id_gender1").click()
password = driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Muhindhar12345")
fname = driver.find_element(By.XPATH,"//input[@id='first_name']").send_keys("Muhindhar")
lname = driver.find_element(By.XPATH,"//input[@id='last_name']").send_keys("SV")
address = driver.find_element(By.XPATH,"//input[@id='address1']").send_keys("gugai")
state = driver.find_element(By.XPATH,"//input[@id='state']").send_keys("Tamilnadu")
city = driver.find_element(By.XPATH,"//input[@id='city']").send_keys("salem")
zipcode = driver.find_element(By.XPATH,"//input[@id='zipcode']").send_keys("656776")
mob = driver.find_element(By.XPATH,"//input[@id='mobile_number']").send_keys("9087654345")
createbtn = driver.find_element(By.XPATH,"//button[normalize-space()='Create Account']")
createbtn.click()
acccrea = driver.find_element(By.XPATH,"//b[normalize-space()='Account Created!']").text
print(acccrea)
contbtn = driver.find_element(By.XPATH,"//a[@class='btn btn-primary']")
contbtn.click()

userName = driver.find_element(By.XPATH, "//ul[@class = 'nav navbar-nav']/descendant::a[text() = ' Logged in as ']").text
print(userName)
checkuser = userName
if "Logged in as demomuhi9" in checkuser:
    print("The Logged username is show")
else:
    print("The logged username is not show")

delacc = driver.find_element(By.XPATH,"//a[normalize-space()='Delete Account']")
if(delacc.is_displayed):
    print("Delete button displayed")
else:
    print("Displayed")
delacc.click()
deldisp = driver.find_element(By.XPATH,"//b[normalize-space()='Account Deleted!']").text
print(deldisp)
delcont = driver.find_element(By.XPATH,"//a[@class='btn btn-primary']").click()