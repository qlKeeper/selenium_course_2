# Тестовое задание по Selenium №4

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    
    def __init__(self, driver) -> None:
        self.driver = driver
    
    def check_users(self, users: list, password: str) -> None:
        '''Функция для проверки авторизации списка пользователей'''
        for user in users:
            login_form = self.driver.find_element(By.ID, "user-name")
            login_form.clear()
            login_form.send_keys(user)
            pass_form = self.driver.find_element(By.ID, "password")
            pass_form.clear()
            pass_form.send_keys(password)
            self.driver.find_element(By.ID, "login-button").click()
            time.sleep(1)
            try:
                WebDriverWait(self.driver, 6).until(EC.text_to_be_present_in_element(
                    (By.XPATH, "//span[@class='title']"), 'Products'))
                print(f"[{user}] was able to log in")
                self.driver.back()
            except Exception:
                print(f"Error, [{user}] unable to login")


class Test1:
    
    def test_select_product(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        users = ['standard_user', 'locked_out_user', 
                'problem_user', 'performance_glitch_user']
        password_all_users = 'secret_sauce'
        print("Start test")

        login = LoginPage(driver)
        login.check_users(users, password_all_users)
        time.sleep(2)
        driver.quit()


test = Test1()
test.test_select_product()
