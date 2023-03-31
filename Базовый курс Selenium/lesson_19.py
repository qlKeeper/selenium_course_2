# Взаимодействие с ползунком

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

with webdriver.Firefox() as driver:
    driver.maximize_window()
    driver.get("https://html5css.ru/howto/howto_js_rangeslider.php")
    slider_square = driver.find_element(By.ID, "id2")
    action = ActionChains(driver)
    action.click_and_hold(slider_square).move_by_offset(100, 0).perform()

    time.sleep(2)