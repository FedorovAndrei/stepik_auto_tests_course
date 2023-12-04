from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def redirect_to_stepik(url, result):
    browser.get(url)
    time.sleep(5)

    enter = browser.find_element(By.ID, 'ember59')
    enter.click()
    time.sleep(2)

    email = browser.find_element(By.CSS_SELECTOR, 'input[type=email]')
    email.send_keys('lorenditric@mail.ru')
    time.sleep(1)

    password = browser.find_element(By.CSS_SELECTOR, 'input[type=password]')
    password.send_keys('troy69battle')
    time.sleep(1)

    submit = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
    submit.click()
    time.sleep(7)

    new_link = "https://stepik.org/lesson/184253/step/4?unit=158843"
    browser.get(new_link)
    time.sleep(15)

    if browser.find_element(By.CSS_SELECTOR, 'div[data-type="string-quiz"]').get_attribute('data-state') == 'correct':
        again_button = browser.find_element(By.CLASS_NAME, 'again-btn')
        again_button.click()
        time.sleep(6)

    stepik_answer = browser.find_element(By.TAG_NAME, 'textarea')
    stepik_answer.send_keys(result)
    time.sleep(2)

    stepik_button = browser.find_element(By.CLASS_NAME, 'submit-submission')
    stepik_button.click()


with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/alert_accept.html")
    time.sleep(1)

    redirect_to_alert = browser.find_element(By.CLASS_NAME, 'btn')
    redirect_to_alert.click()
    time.sleep(1)

    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)

    x = browser.find_element(By.ID, 'input_value').text
    value = math.log(abs(12 * math.sin(int(x))))

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(value)
    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()
    time.sleep(5)

    confirm = browser.switch_to.alert
    required_num = confirm.text.split()[-1]
    confirm.accept()

    redirect_to_stepik("https://stepik.org/lesson/184253/step/4?unit=158843", required_num)
    time.sleep(10)