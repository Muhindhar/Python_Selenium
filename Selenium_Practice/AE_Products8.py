from ast import arguments

from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver,10)
driver.get("https://automationexercise.com/")
expurl = "https://automationexercise.com/"
currurl = driver.current_url
print(currurl)
assert expurl == currurl,"Homepage displayed"
productbtn = driver.find_element(By.XPATH,"//a[@href='/products']")
driver.execute_script("arguments[0].click();",productbtn)
expurl2 = "https://automationexercise.com/products"
print(expurl2)
currurl2 = driver.current_url
print(currurl2)
assert expurl2 == currurl2,"Product page displayed!"
prolist = driver.find_element(By.XPATH,"//div[@class='features_items']")
if prolist.is_displayed:
    print("Product List displayed")
else:
    print("Not displayed")
viewpro = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='col-sm-9 padding-right']//div[2]//div[1]//div[2]//ul[1]//li[1]//a[1]")))
driver.execute_script("arguments[0].click();",viewpro)
expectedurl = "https://automationexercise.com/product_details/1"
currenturl = driver.current_url
assert expectedurl == currenturl,"List details displayed"
prodet = driver.find_element(By.XPATH,"//div[@class='product-information']")
if prodet.is_displayed:
    print("details of product displayed")
else:
    print("Product details not displayed")
    
driver.quit()