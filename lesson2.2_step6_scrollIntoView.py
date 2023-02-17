#2.2.6 Работа с файлами, списками и js-скриптами. Задание на execute_script
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
	# Открыть страницу
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Считать значение для переменной x. 
    x=browser.find_element(By.ID, "input_value").text
    #Посчитать математическую функцию от x.
    y = calc(x)
    # Ввести ответ в текстовое поле.
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)
    # Проскроллить страницу вниз.
    button_submit=browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button_submit)
    #Отметить checkbox "I'm the robot"
    checkbox_element=browser.find_element(By.ID, "robotCheckbox")
    checkbox_element.click()
    #Выбрать radiobutton "Robots rule!".
    radiobutton_element=browser.find_element(By.ID, "robotsRule")
    radiobutton_element.click()
    # Нажать на кнопку Submit
    button_submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла