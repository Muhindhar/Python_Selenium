import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from read_config import get_config

@pytest.mark.usefixtures("setup_teardown")
class TestLogin():
    def test_valid_login(self):
        self.driver.find_element(By.XPATH,"//span[normalize-space()='My Account']").click()
        self.driver.find_element(By.XPATH,"//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Login']").click()
        self.driver.find_element(By.XPATH,"//input[@id='input-email']").send_keys(get_config("valid login cred","mail"))
        self.driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys(get_config("valid login cred","pass"))
        self.driver.find_element(By.XPATH,"//input[@value='Login']").click()
        exp = "Qafox.com"
        curr = self.driver.find_element(By.XPATH,"//a[text()='Qafox.com']").text
        assert exp==curr,"LoggedIn"
        
    def test_invalid_login(self):
        self.driver.find_element(By.XPATH,"//span[normalize-space()='My Account']").click()
        self.driver.find_element(By.XPATH,"//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Login']").click()
        self.driver.find_element(By.XPATH,"//input[@id='input-email']").send_keys(get_config("invalid login cred","mail"))
        self.driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys(get_config("invalid login cred","pass"))
        self.driver.find_element(By.XPATH,"//input[@value='Login']").click()
        exp="Warning: No match for E-Mail Address and/or Password."
        current = self.driver.find_element(By.XPATH,"//div[@class='alert alert-danger alert-dismissible']").text
        assert exp== current,"Not loggedIn"
        
    