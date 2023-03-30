# Двойной клик и клик правой клавишей мыши

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

with webdriver.Chrome() as driver:
    driver.maximize_window()
    driver.get("https://demoqa.com/buttons")
    time.sleep(0.5)
    
    action = ActionChains(driver)
    btn_double_click = driver.find_element(By.ID, "doubleClickBtn")
    action.double_click(btn_double_click).perform()
    time.sleep(0.5)

    btn_right_click = driver.find_element(By.ID, "rightClickBtn")
    action.context_click(btn_right_click).perform()
    time.sleep(3)