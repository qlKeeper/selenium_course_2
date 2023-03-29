# Взаимодействие с Check box

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


with webdriver.Chrome() as driver:
    driver.maximize_window()
    driver.get("https://demoqa.com/checkbox")
    check_box = driver.find_element(By.XPATH, "//*[@aria-label='Toggle']")
    check_box.click()
    time.sleep(1)
    check_box_2 = driver.find_element(By.XPATH, \
    "//*[@id='tree-node']/ol/li/ol/li[3]/span/button")
    check_box_2.click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//label[@for='tree-node-excelFile']").click()
    test = driver.find_element(By.CLASS_NAME, "text-success").text
    assert test == "excelFile", "Bug incorrect text"
    time.sleep(2)
    
    
