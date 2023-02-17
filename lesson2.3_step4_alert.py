#2.3.4 Работа с окнами. Задание: принимаем alert
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
	# Открыть страницу
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #Нажать на кнопку
    button_submit=browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button_submit.click()
    #Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()
    #На новой странице решить капчу для роботов, чтобы получить число с ответом
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