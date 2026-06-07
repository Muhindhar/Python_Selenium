from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

driver.maximize_window()
driver.get("https://automationexercise.com/")

assert driver.current_url == "https://automationexercise.com/"
products = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/products']")))
driver.execute_script("arguments[0].click();", products)
first_product = wait.until(EC.presence_of_element_located((By.XPATH, "(//a[@data-product-id='1'])[1]")))

driver.execute_script("arguments[0].click();", first_product)

continue_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Continue Shopping')]")))
driver.execute_script("arguments[0].click();", continue_btn)

second_product = wait.until(EC.presence_of_element_located((By.XPATH, "(//a[@data-product-id='2'])[1]")))
driver.execute_script("arguments[0].click();", second_product)

view_cart = wait.until(EC.presence_of_element_located((By.XPATH, "//u[normalize-space()='View Cart']")))
driver.execute_script("arguments[0].click();", view_cart)

product1 = wait.until(EC.visibility_of_element_located((By.ID, "product-1")))

if product1.is_displayed():
    print("Product 1 Displayed")
else:
    print("Product 1 Not Displayed")

product2 = wait.until(EC.visibility_of_element_located((By.ID, "product-2")))
if product2.is_displayed():
    print("Product 2 Displayed")
else:
    print("Product 2 Not Displayed")
print("Test Case Passed")
driver.quit()
