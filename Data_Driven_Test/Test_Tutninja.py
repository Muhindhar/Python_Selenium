import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from read_config import get_config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'''
driver = get_config("basic info","browser")
if driver == "chrome":
    driver = webdriver.Chrome()
elif driver == "firefox":
    driver = webdriver.Firefox()
elif driver == "edge":
    driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get(get_config("basic info","url"))
'''

@pytest.mark.usefixtures("setup_teardowns")
class Test_Login():
    def test_login(self):
    
    #driver = self.driver
        self.driver.find_element(By.XPATH,"//a[@id='login2']").click()
        self.driver.find_element(By.XPATH,"//input[@id='loginusername']").send_keys(get_config("login credentials","uname"))
        self.driver.find_element(By.XPATH,"//input[@id='loginpassword']").send_keys(get_config("login credentials","pass"))
        self.driver.find_element(By.XPATH,"//button[text()='Log in']").click()
        exp="Welcome admin"
        actual = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "nameofuser"))).text
        assert actual == exp
        self.driver.quit()