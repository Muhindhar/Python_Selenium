import select

from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.hyrtutorials.com/p/add-padding-to-containers.html")
arch = Select(driver.find_element(By.XPATH,"//select[@id='BlogArchive1_ArchiveMenu']"))
for opt in arch.options:
    print(opt.text)
arch.select_by_index(4)
url = driver.current_url
print(url)
expurl = "https://www.hyrtutorials.com/2023/01/"
assert expurl == url,"Navigated"
arch.select_by_value("https://www.hyrtutorials.com/2022/10/")
expurl="https://www.hyrtutorials.com/2022/10/"
curr = driver.current_url
assert expurl == curr,"success"