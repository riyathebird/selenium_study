from selenium import webdriver
import time
import math

'''
some remarks about executing formula exactly from the browser & how to maximize the window

lst = 'Чему равно ln(abs(12*sin(x))), где x ='.split(' ')
formula  = lst[2][:-1]
result = eval(formula.replace('ln', 'math.log').replace('sin', 'math.sin').replace('x', numX)) 

options = ChromeOptions()
options.add_argument("--start-maximized")
browser = webdriver.Chrome(options=options)
'''

def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_value = browser.find_element_by_id("input_value").text
    input1 = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1) #scroll until the field is visible
    input1.send_keys(calc(x_value))
    radio = browser.find_element_by_css_selector("[value='robots']")
    radio.click()
    check = browser.find_element_by_css_selector("[for='robotCheckbox']")
    check.click()
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(30)
    browser.quit()
