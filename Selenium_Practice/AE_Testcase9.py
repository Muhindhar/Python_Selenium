from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

driver.maximize_window()
driver.get("https://automationexercise.com")

wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='Website for automation practice']")))
print("Home page displayed")
products_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Products')]")))
driver.execute_script("arguments[0].click();", products_btn)
if "#google_vignette" in driver.current_url:
    driver.back()
wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'All Products')]")))
print("Products page displayed")
search_box = wait.until(EC.visibility_of_element_located((By.ID, "search_product")))
search_box.send_keys("shirt")
driver.find_element(By.ID, "submit_search").click()
searched_products = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Searched Products')]")))
if searched_products.is_displayed():
    print("Searched Products displayed")
products = driver.find_elements(By.XPATH, "//div[@class='productinfo text-center']/p")
for product in products:
    print(product.text)
assert len(products)>0
print("Relevant products displayed successfully")
driver.quit()
