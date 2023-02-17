#2.3.7 Настройка ожиданий. Задание: ждем нужный текст на странице
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
	# Открыть страницу
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID,"price"),"$100")
    )
    # Нажать кнопку Book
    button_book=browser.find_element(By.ID, "book")
    button_book.click()
    # Считать значение для переменной x.    
    x=browser.find_element(By.ID, "input_value").text
    #Посчитать математическую функцию от x.
    y = calc(x)
    # Ввести ответ в текстовое поле.
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)
    # Нажать на кнопку Submit
    button_submit=browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button_submit.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла