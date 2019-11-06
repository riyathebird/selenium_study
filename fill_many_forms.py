from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name("input") 
#the same using xpath selector
#    elements = browser.find_elements_by_xpath("//input[@type='text']")
    for element in elements:
       element.send_keys("HI!")

    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(30)
    browser.quit()
