# Открытие браузера с помощью Selenium

from selenium import webdriver
import time 

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(2)
driver.quit()