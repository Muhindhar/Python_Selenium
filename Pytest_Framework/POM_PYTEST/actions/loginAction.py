from pages.loginPage import LoginPage

class LoginActions(LoginPage):
    def __init__(self, driver):
        self.driver = driver
    def click_myacc(self):
        self.driver.find_element(*self.myacc).click()
    def click_login_link(self):
        self.driver.find_element(*self.loginbtn).click()
    def enter_email(self,mail):
        self.driver.find_element(*self.email).send_keys(mail)
    def enter_password(self,pwd):
        self.driver.find_element(*self.password).send_keys(pwd)
    def click_login(self):
        self.driver.find_element(*self.loginok).click()
    def check_login(self):
        return self.driver.find_element(*self.myacccheck).is_displayed()
    def invalid_login(self):
        return self.driver.find_element(*self.invalidlogin).is_displayed()

