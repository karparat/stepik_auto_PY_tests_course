#2.1.5 Уникальность селекторов: часть 2
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	# Открыть страницу
	link = "http://suninjuly.github.io/get_attribute.html"
	browser = webdriver.Chrome()
	browser.get(link)
	# Найти картинку
	x_element=browser.find_element(By.ID, "treasure")
	# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи
	x = x_element.get_attribute("valuex")
	#Посчитать математическую функцию от x.
	y = calc(x)
	# Ввести ответ в текстовое поле.
	input_answer = browser.find_element(By.ID, "answer")
	input_answer.send_keys(y)
	#Отметить checkbox "I'm the robot"
	checkbox_element=browser.find_element(By.ID, "robotCheckbox")
	checkbox_element.click()
	#Выбрать radiobutton "Robots rule!".
	radiobutton_element=browser.find_element(By.ID, "robotsRule")
	radiobutton_element.click() 
	# Нажать на кнопку Submit
	button_submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
	button_submit.click()

finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(15)
	# закрываем браузер после всех манипуляций
	browser.quit()

# не забываем оставить пустую строку в конце файла