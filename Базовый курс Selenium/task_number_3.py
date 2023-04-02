# Тестовое задание по Selenium №3

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as driver:
    # Открываем url
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(5)
    print("Url open\n")

    # Авторизация на сайте
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    print("Login completed\n")

    # Выбор доступного товара пользователем
    products_name = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    products_price = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    products_to_cart = driver.find_elements(By.XPATH, "//button[text()='Add to cart']")
    print("Приветствую тебя в нашем интернет магазине")
    print("Выберете один из следующих товаров и укажите его номер: ")
    for i in range(len(products_name)):
        print(i + 1, products_name[i].text, products_price[i].text)
    prd_num = int(input()) - 1
    product_name = products_name[prd_num].text
    product_price = products_price[prd_num].text
    print(f"\nProduct selected: {product_name} {product_price}\n")
    
    # Проверка корзины
    products_to_cart[prd_num].click()
    driver.find_element(By.ID, "shopping_cart_container").click()
    product_in_cart = driver.find_element(By.CLASS_NAME, "inventory_item_name")
    price_in_cart = driver.find_element(By.CLASS_NAME, "inventory_item_price")
    assert product_in_cart.text == product_name, "Bug wrong name"
    assert price_in_cart.text == product_price, "Bug wrong price"
    print("Cart test done\n")
    
    # Заполнение информационных полей 
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Pasha")
    driver.find_element(By.ID, "last-name").send_keys("Rogov")
    driver.find_element(By.ID, "postal-code").send_keys("117405")
    driver.find_element(By.ID, "continue").click()
    print("Filling in the fields done\n")
    
    final_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    final_price = driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    assert final_price == product_price, "Bug final price"
    assert final_name == product_name, "Bug final name"
    driver.find_element(By.ID, "finish").click()
    complete_header = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert complete_header == "Thank you for your order!", "Bug complete header"
    print("Test is done, all good!")
    