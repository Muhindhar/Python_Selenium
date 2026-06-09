import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from read_config import get_config


@pytest.mark.usefixtures("setup_teardown")
class TestLogin:
    def test_valid_login(self):
        wait = WebDriverWait(self.driver, 20)
        my_account = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='My Account']")))
        self.driver.execute_script("arguments[0].click();",my_account)
        self.driver.find_element(By.XPATH,"//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Login']",).click()
        self.driver.find_element(By.ID, "input-email").send_keys(get_config("valid login cred", "mail"))
        self.driver.find_element(By.ID, "input-password").send_keys(get_config("valid login cred", "pass"))
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        actual = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='My Account']"))).text
        assert actual == "My Account", "Login Failed"

    def test_invalid_login(self):
        wait = WebDriverWait(self.driver, 10)
        my_account = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='My Account']")))
        self.driver.execute_script("arguments[0].click();",my_account)
        self.driver.find_element(By.XPATH,"//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Login']",).click()
        self.driver.find_element(By.ID, "input-email").send_keys(get_config("invalid login cred", "mail"))
        self.driver.find_element(By.ID, "input-password").send_keys(get_config("invalid login cred", "pass"))
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        actual = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'alert-danger')]"))).text
        assert ("No match for E-Mail Address and/or Password" in actual), "Invalid Login Test Failed"
