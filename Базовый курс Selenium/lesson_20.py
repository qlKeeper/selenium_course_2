# Отработка исключений

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

with webdriver.Firefox() as driver:
    driver.maximize_window()
    driver.get("https://demoqa.com/dynamic-properties")
    time.sleep(1)
    
    try:
        visible_btn = driver.find_element(By.ID, "visibleAfter")
        visible_btn.click()
    except NoSuchElementException:
        print("Unable to locate element: [id='visibleAfter'']")
        time.sleep(6)
        visible_btn = driver.find_element(By.ID, "visibleAfter")
        visible_btn.click()
        time.sleep(1)

    try:
        driver.get("https://demoqa.com/radio-button")
        btn = driver.find_element(By.XPATH, "//*[@for='impressiveRadio']")
        btn.click()
        btn_value = btn.text
        assert btn_value == 'Yes', "Wrong button!"
    except AssertionError:
        btn = driver.find_element(By.XPATH, "//*[@for='yesRadio']")
        btn.click()
        btn_value = btn.text
        assert btn_value == 'Yes', "AAAAAA you stupid!"
        print("All good, test is done!")
        time.sleep(1)



