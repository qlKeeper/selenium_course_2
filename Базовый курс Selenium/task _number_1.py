#  Тестовое задание по Selenium №1

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


with webdriver.Chrome() as driver: #  Инициализация драйвера
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")  # Открываем сайт
    assert "Swag Labs" in driver.title
    
    login_standard_user = "standard_user"
    password_all_users = "secret_sauce"

    username_form = driver.find_element(By.ID, 'user-name')
    username_form.send_keys(login_standard_user)  # Заполняем логин
    print("Input login")
    time.sleep(0.5)

    password_form = driver.find_element(By.ID, 'password')
    password_form.send_keys(password_all_users)  # Заполняем пароль
    print("Input password")
    time.sleep(0.5)

    password_form.send_keys(Keys.ENTER) # Нажатие клавиши Enter для авторизации
    main_shop_url = "https://www.saucedemo.com/inventory.html"
    assert driver.current_url == main_shop_url, "Не удалось авторизоваться!"
    print("Successful authorization")
    time.sleep(0.5)

    # Товар №1
    name_product_1 = driver.find_element(By.ID, "item_2_title_link").text
    price_product_1 = driver.find_element(By.XPATH, \
    "//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div").text
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    print("First product added to cart:", name_product_1, price_product_1)
    time.sleep(0.5)

    # Товар №2
    name_product_2 = driver.find_element(By.ID, "item_3_title_link").text
    price_product_2 = driver.find_element(By.XPATH, \
    "//*[@id='inventory_container']/div/div[6]/div[2]/div[2]/div").text
    driver.find_element(By.ID, \
    "add-to-cart-test.allthethings()-t-shirt-(red)").click()
    print("Second product added to cart:", name_product_2, price_product_2)
    time.sleep(0.5)
    
    # Проверка корзины
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    cart_name_product_1 = driver.find_element(By.ID, "item_2_title_link").text
    cart_name_product_2 = driver.find_element(By.ID, "item_3_title_link").text
    cart_price_product_1 = driver.find_element(By.XPATH, \
    "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div").text
    cart_price_product_2 = driver.find_element(By.XPATH, \
    "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div").text
    assert cart_name_product_1 == name_product_1, "Bug product name 1"
    assert cart_name_product_2 == name_product_2, "Bug product name 2"
    assert cart_price_product_1 == price_product_1, "Bug product price 1"
    assert cart_price_product_2 == price_product_2, "Bug prodcut price 2"
    print("In cart all good")
    time.sleep(0.5)

    # Заполнение полей для доставки
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Pasha")
    time.sleep(0.5)
    driver.find_element(By.ID, "last-name").send_keys("Rogov")
    time.sleep(0.5)
    driver.find_element(By.ID, "postal-code").send_keys("117405")
    time.sleep(0.5)
    driver.find_element(By.ID, "continue").click()
    print("\"Checkout: Your Information\" complete")
    
    # Последняя сверка информации имени и цены товаров
    last_name_product_1 = driver.find_element(By.ID, "item_2_title_link").text
    last_name_product_2 = driver.find_element(By.ID, "item_3_title_link").text
    last_price_product_1 = driver.find_element(By.XPATH, \
    "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div").text
    last_price_product_2 = driver.find_element(By.XPATH, \
    "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div").text
    
    assert last_name_product_1 == name_product_1, "Bug product name 1"
    assert last_name_product_2 == name_product_2, "Bug product name 2"
    assert last_price_product_1 == price_product_1, "Bug product price 1"
    assert last_price_product_2 == price_product_2, "Bug product price 2"
    
    total_price = driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
    total_price = float(total_price[total_price.index('$') + 1:])
    price_product_1 = float(price_product_1.replace('$', ''))
    price_product_2 = float(price_product_2.replace('$', ''))
    
    assert total_price == price_product_1 + price_product_2, "Bug total price"
    driver.find_element(By.ID, "finish").click()
    Complete_order = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert Complete_order == "Thank you for your order!", "Complete error"
    print("All good, test is done")
    
    time.sleep(2)