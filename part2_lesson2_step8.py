from selenium import webdriver
from selenium.webdriver.common.by import By

import time, os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys('Ivan')

    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys('Petrov')

    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys('ivanpetrov@mail.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'Empty_file.txt')

    attach_button = browser.find_element(By.ID, 'file')
    attach_button.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()