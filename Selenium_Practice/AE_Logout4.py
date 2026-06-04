from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)
driver.maximize_window()
driver.get("http://automationexercise.com")
homepg = driver.find_element(By.XPATH,"//img[@alt='Website for automation practice']").is_displayed()
if(homepg):
    print("Displayed")
else:
    print("Not displayed")
signupbtn = driver.find_element(By.XPATH,"//a[normalize-space()='Signup / Login']").click()
email = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@data-qa='login-email']")))
email.send_keys("muhi2701@gmail.com")
password = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Password']")))
password.send_keys("1234567890")
clicksign = driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
userName = driver.find_element(By.XPATH, "//ul[@class = 'nav navbar-nav']/descendant::a[text() = ' Logged in as ']").text
print(userName)
checkuser = userName
if "Logged in as muhi" in checkuser:
    print("The Logged username is show")
else:
    print("The logged username is not show")
    
logoutbtn= driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()
expurl = "https://automationexercise.com/login"
currurl = driver.current_url
assert expurl == currurl,"Not Redirected to login page"
driver.close()