import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities import excelutilites
from read_config import get_config


@pytest.mark.parametrize("order",excelutilites.get_data(r"D:\Python_Selenium\Pytest_Framework\TutorialsNinja\ExcelFiles\order.xlsx","Sheet1"))
@pytest.mark.usefixtures("setup_teardown")
class Test_order:
    def test_product(self, order):
        wait = WebDriverWait(self.driver, 20)
        my_account = wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='My Account']")))
        self.driver.execute_script("arguments[0].click();",my_account)
        self.driver.find_element(By.LINK_TEXT,"Login").click()
        self.driver.find_element(By.ID,"input-ex`mail").send_keys(get_config("valid login cred", "mail"))
        self.driver.find_element(By.ID,"input-password").send_keys(get_config("valid login cred", "pass"))
        self.driver.find_element(By.XPATH,"//input[@value='Login']").click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='My Account']")))
        self.driver.get(get_config("basic info", "url"))

        search_box = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
        search_box.clear()
        search_box.send_keys(order[0])
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='product-thumb']//h4/a)[1]"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "button-cart"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Shopping Cart')]"))).click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Checkout"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "button-payment-address"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "button-shipping-address"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "button-shipping-method"))).click()

        wait.until(EC.element_to_be_clickable((By.NAME, "agree"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "button-payment-method"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "button-confirm"))).click()
        actual = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Your order has been placed')]"))).text
        assert actual == "Your order has been placed!"