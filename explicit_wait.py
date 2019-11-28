from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    booking_button = browser.find_element_by_id("book")
    booking_button.click()
    x_value = browser.find_element_by_id("input_value").text
    answer = browser.find_element_by_id("answer")
    answer.send_keys(calc(x_value))
    submit_button = browser.find_element_by_id("solve")
    submit_button.click()
finally:
    time.sleep(30)
    browser.quit()
