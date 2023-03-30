# Взаимодействие с календарем

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

with webdriver.Chrome() as driver:
    driver.maximize_window()
    driver.get("https://demoqa.com/date-picker")
    time.sleep(0.5)

    new_date = driver.find_element(By.ID, "datePickerMonthYearInput")
    # for i in range(10):
    #     new_date.send_keys(Keys.BACKSPACE)
    time.sleep(0.5)
    
    new_date.click()
    driver.find_element(By.XPATH, "//*[text()='29']").click()
    time.sleep(3)