from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    x = browser.find_element(By.ID, 'input_value').text
    total = math.log(abs(12 * math.sin(int(x))))

    input_field = browser.find_element(By.ID, 'answer')

    input_field.location_once_scrolled_into_view
    input_field.send_keys(total)

    checkbox1 = browser.find_element(By.CSS_SELECTOR, '[type=checkbox]')
    checkbox1.click()

    radiobutton1 = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radiobutton1.click()

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()