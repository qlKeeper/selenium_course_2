# Негативное тестирование

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
base_url = "https://www.saucedemo.com/"
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_use"
password_users = "secret_sauce"

user_name_form = driver.find_element(By.XPATH, "//*[@id='user-name']")
user_name_form.send_keys(login_standard_user)
print("Input Login")
password_form = driver.find_element(By.CSS_SELECTOR, "input[name=password]")
password_form.send_keys(password_users)
print("Input password")
button_login = driver.find_element(By.XPATH, "//input[@value='Login']")
button_login.click()
print("Click Login Button")

warning_text = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
assert warning_text == "Epic sadface: Username and password do not match any \
    user in this service"

time.sleep(2)
driver.quit()