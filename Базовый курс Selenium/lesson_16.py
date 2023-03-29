# Взаимодействие с Radio Button

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


with webdriver.Chrome() as driver:
    driver.maximize_window()
    driver.get("https://demoqa.com/radio-button")
    driver.find_element(By.XPATH, "//label[@for='yesRadio']").click()
    time.sleep(1)
    test = driver.find_element(By.CLASS_NAME, "text-success").text
    assert test == 'Yes', "Bug incorrect text"
    time.sleep(1)
