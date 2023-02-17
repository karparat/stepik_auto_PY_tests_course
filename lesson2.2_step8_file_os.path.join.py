#2.2.6 Работа с файлами, списками и js-скриптами. Задание на file_os.path.join
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
	# Открыть страницу
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Заполнить текстовые поля: имя, фамилия, email
    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys("Nukky")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys("Thompson")
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys("NThompson@bl.us")
    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым.
    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла
    element=browser.find_element(By.CSS_SELECTOR, "[type='file']")
    file_path = os.path.join(current_dir, 'file.txt')
    element.send_keys(file_path)
    # Нажать на кнопку Submit
    button_submit=browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button_submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла