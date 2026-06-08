import time

from selenium import webdriver

driver = webdriver.Chrome()
#ad block
driver.execute_cdp_cmd("Network.enable", {})

driver.execute_cdp_cmd(
    "Network.setBlockedURLs",
    {
        "urls": [
            "*googlesyndication.com*",
            "*doubleclick.net*",
            "*googleadservices.com*",
            "*adsystem.com*"
        ]
    }
)

driver.get("https://automationexercise.com")
time.sleep(6)