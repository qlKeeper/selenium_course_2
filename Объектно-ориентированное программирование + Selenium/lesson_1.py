# Создание класса и метода

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from login_page import LoginPage

class Test_1:
    
    def test_select_product(self):
        driver = webdriver.Chrome()
        # Открываем url
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        driver.implicitly_wait(5)
        time.sleep(2)

        print("Start test")
            
        login = LoginPage(driver)
        login.authorization(user_name="standard_user", password="secret_sauce")



test = Test_1()
test.test_select_product()