# Имитация нажатия клавиш на клавиатуре с помощью Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

with webdriver.Chrome() as driver:
    
    base_url = "https://www.saucedemo.com/"
    main_shop_url = "https://www.saucedemo.com/inventory.html"
    driver.maximize_window()
    driver.get(base_url)
    
    login_standard_user = "standard_user"
    password_all_users = "secret_sauce"

    username_form = driver.find_element(By.ID, 'user-name')
    username_form.send_keys(login_standard_user)
    print("Input login")
    time.sleep(1)
    username_form.send_keys(Keys.BACKSPACE) # Нажатие клавиши BACKSPACE
    username_form.send_keys('r')
    time.sleep(1)

    password_form = driver.find_element(By.ID, 'password')
    password_form.send_keys(password_all_users)
    print("Input password")
    time.sleep(1)
    password_form.send_keys(Keys.ENTER) # Нажатие клавиши Enter
    
    assert driver.current_url == main_shop_url, "Не удалось авторизоваться!"
    print("Successful authorization")
    
    time.sleep(1)
    filter = driver.find_element(By.CLASS_NAME, 'product_sort_container')
    filter.click()
    print("Click filter")
    time.sleep(1)
    filter.send_keys(Keys.DOWN)
    time.sleep(1)
    filter.send_keys(Keys.RETURN)

    time.sleep(2)