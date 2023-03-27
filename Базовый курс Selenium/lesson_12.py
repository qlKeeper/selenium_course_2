# Взаимодействие со скрытыми элементами

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

    password_form.send_keys(Keys.ENTER) # Нажатие клавиши Enter
    main_shop_url = "https://www.saucedemo.com/inventory.html"
    assert driver.current_url == main_shop_url, "Не удалось авторизоваться!"
    print("Successful authorization")

    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    menu.click()
    print("Click menu button")
    time.sleep(2)

    about_btn = driver.find_element(By.ID, "about_sidebar_link")
    about_btn.click()
    print("Click link button")
    time.sleep(1)

    assert "https://saucelabs.com/" in driver.current_url, "Переход fail"
    time.sleep(2)