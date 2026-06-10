from selenium.webdriver.common.by import By


class OrderPage:
    myacc = (By.XPATH,"//span[normalize-space()='My Account']")
    loginbtn = (By.XPATH,"//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Login']")
    email = (By.XPATH,"//input[@id='input-email']")
    password = (By.XPATH,"//input[@id='input-password']")
    loginok = (By.XPATH,"//input[@value='Login']")
    searchbar = (By.XPATH,"//input[@placeholder='Search']")
    search = (By.XPATH,"//button[@class='btn btn-default btn-lg']")
    lap = (By.XPATH,"//div[@class='caption']//a[contains(text(),'HP LP3065')]")
    addtocart = (By.XPATH,"//button[@id='button-cart']")
    shopcart = (By.XPATH,"//span[normalize-space()='Shopping Cart']")
    checkout = (By.XPATH,"//a[@class='btn btn-primary']")
    onecnt = (By.XPATH,"//input[@id='button-payment-address']")
    twocnt = (By.XPATH,"//input[@id='button-shipping-address']")
    threecnt = (By.XPATH,"//input[@id='button-shipping-method']")
    agree= (By.XPATH,"//input[@name='agree']")
    fourcnt = (By.XPATH,"//input[@id='button-payment-method']")
    confirmorder = (By.XPATH,"//input[@id='button-confirm']")
    check = (By.XPATH,"//h1[normalize-space()='Your order has been placed!']")
    