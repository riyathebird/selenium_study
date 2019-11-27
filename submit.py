from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_class_name("btn")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_value = browser.find_element_by_id("input_value").text
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(calc(x_value))
    button = browser.find_element_by_class_name("btn")
    button.click()
finally:
    time.sleep(30)
    browser.quit()
