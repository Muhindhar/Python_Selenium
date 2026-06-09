import pytest
from selenium.webdriver.common.by import By
from Utilities import excelutilites



@pytest.mark.parametrize("order",excelutilites.get_data(r"D:\Python_Selenium\Pytest_Framework\TutorialsNinja\ExcelFiles\order.xlsx","Sheet1",),)
@pytest.mark.usefixtures("setup_teardown")
class Test_order:
    def test_product(self, order):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(order[0])
        self.driver.find_element(By.XPATH,"//i[@class='fa fa-search']").click()
        self.driver.find_element(By.XPATH,"//div[@class='product-layout product-grid col-lg-3 col-md-3 col-sm-6 col-xs-12']//button[1]").click()
        self.driver.find_element(By.XPATH,"//button[@id='button-cart']").click()
        self.driver.find_element(By.XPATH,"//span[normalize-space()='Shopping Cart']").click()
        self.driver.find_element(By.XPATH,"//a[@class='btn btn-primary']").click()
        self.driver.find_element(By.XPATH,"//input[@id='button-payment-address']").click()
        self.driver.find_element(By.XPATH,"//input[@id='button-shipping-address']").click()
        self.driver.find_element(By.XPATH,"//input[@id='button-shipping-method']").click()
        self.driver.find_element(By.XPATH,"//input[@name='agree']").click()
        self.driver.find_element(By.XPATH,"//input[@id='button-payment-method']").click()
        self.driver.find_element(By.XPATH,"//input[@id='button-confirm']").click()
        exp="Your order has been placed!"
        curr = self.driver.find_element(By.XPATH,"//h1[text()='Your order has been placed!']").text
        assert exp==curr,"order placed"
        
        
    
