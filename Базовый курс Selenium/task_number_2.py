# Тестовое задание по Selenium №2

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, datetime

with webdriver.Chrome() as driver:
    driver.maximize_window()
    driver.get("https://demoqa.com/date-picker")  # Открываем url с календарем
    header_text = driver.find_element(By.CLASS_NAME, "main-header").text
    assert header_text == "Date Picker", "Bug wrong url" # Проверка верного url
    time.sleep(1)

    date_form = driver.find_element(By.ID, "datePickerMonthYearInput")
    current_form_value = date_form.get_attribute("value") # значение формы даты
    for i in current_form_value:
        date_form.send_keys(Keys.BACKSPACE)  # Очищаем поле для ввода даты
    assert '' == date_form.get_attribute("value"), "Error form not empty"
    print("Form clear")
    time.sleep(0.5)

    now_date = datetime.date.today()  # Текущая дата
    delta = datetime.timedelta(days=10)  # Для разницы между двумя датами
    delta_date = (now_date + delta).strftime("%d/%m/%Y")  # Текущая дата + 10д
    date_form.send_keys(str(delta_date))  # Заполняем форму новой датой
    date_form.send_keys(Keys.ENTER)  # Подтверждаем ввод
    assert date_form.get_attribute("value") == str(delta_date), "err value form"
    print("New date entered, all good test is done")
    time.sleep(5)