from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_num = browser.find_element(By.CSS_SELECTOR, '#num1')
    second_num = browser.find_element(By.CSS_SELECTOR, '#num2')
    total = int(first_num.text) + int(second_num.text)

    selection = Select(browser.find_element(By.TAG_NAME, 'select'))
    selection.select_by_value(str(total))

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()