# Создание модуля Авторизации

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class LoginPage:

    def __init__(self, driver) -> None:
        self.driver = driver

    def authorization(self, user_name, password):
        self.driver.find_element(By.ID, "user-name").send_keys(user_name)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        print("Login completed\n")
        time.sleep(2)