from pages.searchpage import Searchpage

class search(Searchpage):
  
    def __init__(self,driver):
        self.driver =  driver
    def click_bar(self):
        self.driver.find_element(*self.searchbar).send_keys("hp")
    def clic_search(self):
        self.driver.find_element(*self.search).click()
    def check_search(self):
        return self.driver.find_element(*self.check).is_displayed()
    
    
        
    