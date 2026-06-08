import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("test_setup_teardown")
class TestSearch:    
    def test_valid(self):
        self.driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("hp")
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
        assert self.driver.find_element(By.XPATH,"//a[normalize-space()='HP LP3065']").is_displayed()
    
    def test_invalid(self):
        self.driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("honda")
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
        exp = "There is no product that matches the search criteria."
        actual = self.driver.find_element(By.XPATH,"//p[contains(text(),'There is no product')]").text
        assert actual == exp
    
    def test_noproduct(self):
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
        exp = "There is no product that matches the search criteria."
        actual = self.driver.find_element(By.XPATH,"//p[contains(text(),'There is no product')]").text
        assert actual == exp