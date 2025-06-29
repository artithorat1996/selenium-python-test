from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_duckduckgo_search():
    driver = webdriver.Chrome()
    driver.get("https://duckduckgo.com")
    search = driver.find_element(By.NAME, "q")
    search.send_keys("Jenkins Selenium Python")
    search.submit()
    time.sleep(2)
    assert "Jenkins Selenium Python" in driver.title
    driver.quit()
