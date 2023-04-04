# Создание класса и метода

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Test_1:
    
    def test_select_product(self):
       with webdriver.Chrome() as driver:
            # Открываем url
            driver.maximize_window()
            driver.get("https://www.saucedemo.com/")
            driver.implicitly_wait(5)
            time.sleep(2)

            print("Start test")
            
            # Авторизация на сайте
            driver.find_element(By.ID, "user-name").send_keys("standard_user")
            driver.find_element(By.ID, "password").send_keys("secret_sauce")
            driver.find_element(By.ID, "login-button").click()
            print("Login completed\n")
            time.sleep(2)


test = Test_1()
test.test_select_product()