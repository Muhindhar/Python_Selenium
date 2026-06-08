from operator import imod

from selenium import webdriver
import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")
fname = driver.find_element(By.XPATH,"//input[@id='firstName']")
driver.execute_script("arguments[0].value='muhindhar'",fname)
lname = driver.find_element(By.XPATH,"//input[@id='lastName']")
driver.execute_script("arguments[0].value='sv'",lname)
email = driver.find_element(By.XPATH,"//input[@id='userEmail']")
driver.execute_script("arguments[0].value='muhi27@gmail.com'",email)
gender = driver.find_element(By.XPATH,"//input[@id='gender-radio-1']")
driver.execute_script("arguments[0].click();",gender)
number = driver.find_element(By.XPATH,"//input[@id='userNumber']")
driver.execute_script("arguments[0].value='9087654563';",number)
hobby = driver.find_element(By.XPATH,"//input[@id='hobbies-checkbox-1']").click()
file = driver.find_element(By.XPATH,"//input[@id='uploadPicture']")
file.send_keys(r"C:\Users\Muhindhar S V\Downloads\Gemini_Generated_Image_t2bbw7t2bbw7t2bb.png")
address = driver.find_element(By.XPATH,"//textarea[@id='currentAddress']")
driver.execute_script("arguments[0].value='salem';",address)
'''(its an div tag not select/dropdown)
state = Select(driver.find_element(By.XPATH,"//div[@id='state']"))
state.deselect_by_visible_text("NCR")
city = Select(driver.find_element(By.XPATH,"//div[@id='react-select-4-placeholder']"))
city.select_by_visible_text("Delhi")'''

state = driver.find_element(By.ID,"react-select-3-input")
state.send_keys("NCR")
state.send_keys(Keys.ENTER)
city = driver.find_element(By.ID,"react-select-4-input")
city.send_keys("Delhi")
city.send_keys(Keys.ENTER)
submitbtn = driver.find_element(By.XPATH,"//button[@id='submit']")
driver.execute_script("arguments[0].click()",submitbtn)

