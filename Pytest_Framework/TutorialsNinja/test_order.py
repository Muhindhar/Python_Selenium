import pytest
from selenium.webdriver.common.by import By
from Utilities import csvReader

@pytest.mark.parametrize("product", csvReader.get_data(r"D:\Python_Selenium\Pytest_Framework\TutorialsNinja\Utilities\products.csv"))
@pytest.mark.usefixtures("setup_teardown")

class Test_search:
    def test_search(self, product):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(product)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
