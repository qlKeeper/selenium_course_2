# Заполнение полей с помощью метода send_keys

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
user_name_form = driver.find_element(By.ID, "user-name")
user_name_form.send_keys("standard_user")


time.sleep(3)
driver.quit()

