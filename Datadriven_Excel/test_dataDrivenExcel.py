import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities import excelReader
from Utilities.logCreator import log_creator

@pytest.mark.parametrize("username,password,case",excelReader.get_data(r"D:\Python_Selenium\Datadriven_Excel\ExcelFiles\loginData.xlsx", "login"),)

class Test_Login1:
    logcreator = log_creator()
    def test_validlogin(self, username, password, case):
        driver = webdriver.Chrome()
        self.logcreator.info("Chrome browser initiated")
        driver.maximize_window()
        driver.get("https://www.demoblaze.com/index.html")
        self.logcreator.info("website launched")
        driver.find_element(By.ID, "login2").click()
        self.logcreator.info("login clicked")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "loginusername"))).send_keys(username)
        self.logcreator.info("username typed")
        driver.find_element(By.ID, "loginpassword").send_keys(password)
        self.logcreator.info("password typed")
        driver.find_element(By.XPATH, "//button[text()='Log in']").click()
        if case.lower() == "pass":
            actual = (WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@id='nameofuser']"))).text)
            exp = f"Welcome {username}"
            assert actual == exp
            self.logcreator.info("pass case passed")

        else:
            alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
            assert alert.text == "User does not exist."
            alert.accept()
            self.logcreator.info("fail case passed")
            driver.close()
        driver.quit()
