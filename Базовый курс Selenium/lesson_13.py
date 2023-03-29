# Перемещение в истории браузера (вперед-назад)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

with webdriver.Chrome() as driver:
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    assert "Swag Labs" in driver.title
    
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
    time.sleep(0.5)
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(0.5)
    driver.find_element(By.ID, "about_sidebar_link").click()
    time.sleep(0.5)
    driver.refresh() # Обновить страницу 
    time.sleep(0.5)
    driver.back()  # Вернуться назад
    time.sleep(0.5)
    driver.forward() # Вернуться вперед

    time.sleep(2)