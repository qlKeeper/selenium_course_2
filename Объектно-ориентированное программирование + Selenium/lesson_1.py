# Создание класса и метода

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Test_1:
    def test_select_product(self):
       with webdriver.Chrome() as driver:
            driver.maximize_window()
            driver.get("https://www.saucedemo.com/")
            time.sleep(2)

test = Test_1()
test.test_select_product()