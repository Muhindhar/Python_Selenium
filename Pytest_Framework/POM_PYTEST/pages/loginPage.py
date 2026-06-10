from selenium.webdriver.common.by import By


class LoginPage:
    myacc = (By.XPATH,"//span[normalize-space()='My Account']")
    loginbtn = (By.XPATH,"//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Login']")
    email = (By.XPATH,"//input[@id='input-email']")
    password = (By.XPATH,"//input[@id='input-password']")
    loginok = (By.XPATH,"//input[@value='Login']")
    myacccheck = (By.XPATH, "//h2[text()='My Account']")
    invalidlogin = (By.XPATH,"//div[@class='alert alert-danger alert-dismissible']")