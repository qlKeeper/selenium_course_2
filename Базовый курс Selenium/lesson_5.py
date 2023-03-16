# Построение первых тестов

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
base_url = "https://www.saucedemo.com/"
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
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
# text_products = driver.find_element(By.XPATH, "//span[@class='title']")
# value_text_products = text_products.text
# print(value_text_products)
# assert value_text_products == "Products"
# print("GOOD")

url_login = "https://www.saucedemo.com/inventory.html"
assert url_login == driver.current_url
print("Good url")

time.sleep(3)
driver.quit()

