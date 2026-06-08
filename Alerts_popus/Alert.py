import time
from selenium import webdriver
import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

driver = webdriver.Chrome()
driver.maximize_window()
wait =WebDriverWait(driver,10)
driver.execute_cdp_cmd("Network.enable", {})

driver.execute_cdp_cmd(
    "Network.setBlockedURLs",
    {
        "urls": [
            "*googlesyndication.com*",
            "*doubleclick.net*",
            "*googleadservices.com*",
            "*adservice.google.com*",
            "*pagead2.googlesyndication.com*",
            "*googleads.g.doubleclick.net*",
            "*tpc.googlesyndication.com*",
            "*adsystem.com*"
        ]
    }
)
driver.get("https://demoqa.com/alerts")
time.sleep(4)
#normal alert
alert = driver.find_element(By.XPATH,"//a[@href='/alerts']").click()
time.sleep(4)
alertbtn = driver.find_element(By.XPATH,"//button[@id='alertButton']").click()
alert = driver.switch_to.alert
time.sleep(4)
alert.accept()
print("alert accepted")

#alert after 5 sec
fivsecalert= driver.find_element(By.XPATH,"//button[@id='timerAlertButton']").click()
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
time.sleep(4)
alert.accept()
print("Alert after 5 secs handles")

#confrim alert
confmalert = driver.find_element(By.XPATH,"//button[@id='confirmButton']").click()
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
time.sleep(4)
alert.accept()
print("alert accpeted")

#confirm-dismiss
confmalert = driver.find_element(By.XPATH,"//button[@id='confirmButton']").click()
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
time.sleep(4)
alert.dismiss()
print("Alert dismissed")

