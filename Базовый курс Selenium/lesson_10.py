# Скроллинг экрана

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime

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
    time.sleep(0.5)
    username_form.send_keys(Keys.BACKSPACE) # Нажатие клавиши BACKSPACE
    username_form.send_keys('r')
    time.sleep(0.5)

    password_form = driver.find_element(By.ID, 'password')
    password_form.send_keys(password_all_users)
    print("Input password")
    time.sleep(0.5)
    password_form.send_keys(Keys.ENTER) # Нажатие клавиши Enter
    
    assert driver.current_url == main_shop_url, "Не удалось авторизоваться!"
    print("Successful authorization")

    time.sleep(0.5)
    # driver.execute_script("window.scrollTo(0, 500)") # Скроллинг скрипт JS

    action = ActionChains(driver)
    twitter_ref = driver.find_element(By.XPATH, \
    "//a[@href='https://twitter.com/saucelabs']")
    action.move_to_element(twitter_ref).perform() # Наведение на элемент
    time.sleep(1)
    
    now_date = datetime.now()
    driver.save_screenshot(f'./Screenshots/screenshot_{now_date}.png')
    
    time.sleep(1.5)
    