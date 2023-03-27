# Smoke testing всего бизнес пути

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

with webdriver.Chrome() as driver:
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    assert "Swag Labs" in driver.title
    
    login_standard_user = "standard_user"
    password_all_users = "secret_sauce"

    username_form = driver.find_element(By.ID, 'user-name')
    username_form.send_keys(login_standard_user)
    print("Input login")
    time.sleep(0.5)

    password_form = driver.find_element(By.ID, 'password')
    password_form.send_keys(password_all_users)
    print("Input password")
    time.sleep(0.5)

    password_form.send_keys(Keys.ENTER) # Нажатие клавиши Enter
    main_shop_url = "https://www.saucedemo.com/inventory.html"
    assert driver.current_url == main_shop_url, "Не удалось авторизоваться!"
    print("Successful authorization")

    # INFO Product №1
    product_1 = driver.find_element(By.ID, "item_4_title_link")
    product_1_value = product_1.text
    print("Product_name:", product_1.text)
    
    price_product_1 = driver.find_element(By.XPATH, \
    "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
    price_product_1_value = price_product_1.text
    print("Product price:", price_product_1.text)

    select_product_1 = driver.find_element(By.ID, \
    "add-to-cart-sauce-labs-backpack")
    select_product_1.click()
    print("Add to cart product 1")
    time.sleep(1)

    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart.click()
    print("Enter cart")
    time.sleep(1)

    # INFO cart product №1
    cart_product_1 = driver.find_element(By.CLASS_NAME, "inventory_item_name")
    cart_product_1_price = driver.find_element(By.CLASS_NAME, \
    "inventory_item_price")
    
    assert product_1_value == cart_product_1.text, "Bug name!"
    assert price_product_1_value == cart_product_1_price.text, "Bug price!"
    print("cart good")
    time.sleep(1)

    checkout = driver.find_element(By.ID, "checkout")
    checkout.click()

    # Select user info
    driver.find_element(By.ID, "first-name").send_keys("Pasha")
    time.sleep(0.5)
    driver.find_element(By.ID, "last-name").send_keys("Rogov")
    time.sleep(0.5)
    driver.find_element(By.ID, "postal-code").send_keys("117405")
    time.sleep(0.5)
    driver.find_element(By.ID, "continue").click()
    time.sleep(0.5)
    
    # Final
    final_name_product_1 = driver.find_element(By.CLASS_NAME, \
    "inventory_item_name").text
    assert final_name_product_1 == product_1_value

    final_price_product_1 = driver.find_element(By.CLASS_NAME, \
    "inventory_item_price").text
    assert final_price_product_1 == price_product_1_value

    item_total_price = driver.find_element(By.CLASS_NAME, \
    "summary_subtotal_label").text
    assert price_product_1_value in item_total_price
    time.sleep(0.5)
    
    driver.find_element(By.ID, "finish").click()
    print("End test")

    time.sleep(2)
    