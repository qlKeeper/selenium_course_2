# Очистка содержимого полей

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as driver:
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    login_standard_user = "standard_user"
    password_all_users = "secret_sauce"

    username_form = driver.find_element(By.ID, 'user-name')
    username_form.send_keys(login_standard_user)
    print("Input login")
    time.sleep(0.5)

    password_form = driver.find_element(By.ID, 'password')
    password_form.send_keys(password_all_users)
    print("Input password")
    time.sleep(0.5)

    username_form.clear()
    password_form.clear()

    time.sleep(2)
    