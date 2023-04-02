# Явное и Неявное ожидание

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as driver:
    driver.get("https://demoqa.com/dynamic-properties")
    # driver.implicitly_wait(10) # неявное ожидание

    print("Start test")
    
    # Явное ожидание
    btn = WebDriverWait(driver, 30).\
    until(expected_conditions.element_to_be_clickable((By.ID, "visibleAfter")))
    
    print("Done")