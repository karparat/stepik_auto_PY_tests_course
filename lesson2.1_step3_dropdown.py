#2.2 работа с выпадающим списком
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    # Открыть страницу
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Найти числа
    num1=browser.find_element(By.ID, "num1").text
    num2=browser.find_element(By.ID, "num2").text
    #Посчитать сумму чисел.
    y = str(int(num1)+int(num2))
    # Выбрать правильный ответ из списка
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(y) # ищем элемент с текстом "y"
    # Нажать на кнопку Submit
    button_submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button_submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла