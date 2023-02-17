#2.1.5 Уникальность селекторов: часть 2
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try: 
	link = "https://suninjuly.github.io/math.html"
	browser = webdriver.Chrome()
	browser.get(link)
	#Считать значение для переменной x
	x_element=browser.find_element(By.ID, "input_value")
	x = x_element.text
	#Посчитать математическую функцию от x.
	y = calc(x)
	# Ввести ответ в текстовое поле.
	input_answer = browser.find_element(By.ID, "answer")
	input_answer.send_keys(y)
	#Отметить checkbox "I'm the robot"
	checkbox_element=browser.find_element(By.ID, "robotCheckbox")
	checkbox_element.click()
	#Выбрать radiobutton "Robots rule!".
	radiobutton_element=browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
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