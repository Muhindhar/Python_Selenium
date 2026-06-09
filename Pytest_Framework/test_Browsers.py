import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


@pytest.mark.parametrize("input_browser", ["chrome", "firefox", "edge"])
@pytest.mark.parametrize("input_url", ["https://www.flipkart.com", "https://www.amazon.in"])
def test_url(input_browser, input_url):

    if input_browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless=new")
        web_driver = webdriver.Chrome(options=options)

    if input_browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        web_driver = webdriver.Firefox(options=options)
    
    if input_browser == "edge":
        options = EdgeOptions()
        options.add_argument("--headless")
        web_driver = webdriver.Edge(options=options)
        
    web_driver.get(input_url)
    print(f"Browser: {input_browser}")
    print(f"Title: {web_driver.title}")
    web_driver.quit()
