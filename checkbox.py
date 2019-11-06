from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #find the x value in the string
    x_value = browser.find_element_by_id("input_value").text
    #find the text fieal & add calculated value for x
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(calc(x_value))
    #check the radio and checkbox
    radio = browser.find_element_by_css_selector("[value='robots']")
    radio.click()
    check = browser.find_element_by_css_selector("[for='robotCheckbox']")
    check.click()

finally:
    time.sleep(30)
    browser.quit()
