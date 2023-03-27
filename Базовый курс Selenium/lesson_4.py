# Авторизация на сайте

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
user_name_form = driver.find_element(By.XPATH, "//*[@id='user-name']") # XPATH
user_name_form.send_keys("standard_user")
password_form = driver.find_element(By.CSS_SELECTOR, "input[name=password]")
password_form.send_keys("secret_sauce")
button_login = driver.find_element(By.XPATH, "//input[@value='Login']")
button_login.click()

time.sleep(3)
driver.quit()