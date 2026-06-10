from pages.orderPage import OrderPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderAction(OrderPage):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
    def clk_myacc(self):
        self.wait.until(EC.element_to_be_clickable(self.myacc)).click()
    def clk_login(self):
        self.wait.until(EC.element_to_be_clickable(self.loginbtn)).click()
    def clck_mail(self):
        self.wait.until(EC.visibility_of_element_located(self.email)).send_keys("muhindhar27@gmail.com")
    def clk_pass(self):
        self.wait.until(EC.visibility_of_element_located(self.password)).send_keys("12345678")
    def clk_loginbtn(self):
        self.wait.until(EC.element_to_be_clickable(self.loginok)).click()
    def clk_searchbar(self):
        self.wait.until(EC.visibility_of_element_located(self.searchbar)).send_keys("hp")
    def clk_search(self):
        self.wait.until(EC.element_to_be_clickable(self.search)).click()
    def clk_laptop(self):
        self.wait.until(EC.element_to_be_clickable(self.lap)).click()
    def clk_addtocart(self):
        self.wait.until(EC.element_to_be_clickable(self.addtocart)).click()
    def clk_shopcart(self):
        self.wait.until(EC.element_to_be_clickable(self.shopcart)).click()
    def clk_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.checkout)).click()
    def clk_contbtn(self):
        self.wait.until(EC.element_to_be_clickable(self.onecnt)).click()
        self.wait.until(EC.element_to_be_clickable(self.twocnt)).click()
        self.wait.until(EC.element_to_be_clickable(self.threecnt)).click()
        self.wait.until(EC.element_to_be_clickable(self.agree)).click()
        self.wait.until(EC.element_to_be_clickable(self.fourcnt)).click()
        self.wait.until(EC.element_to_be_clickable(self.confirmorder)).click()
    def check_order(self):
        return self.wait.until(EC.visibility_of_element_located(self.check)).is_displayed()
