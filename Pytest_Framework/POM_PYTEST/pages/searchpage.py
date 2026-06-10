from selenium.webdriver.common.by import By

class Searchpage:
    searchbar = (By.XPATH,"//input[@placeholder='Search']")
    search = (By.XPATH,"//button[@class='btn btn-default btn-lg']")
    check= (By.XPATH,"//h1[normalize-space()='Search - hp']")