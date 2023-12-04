from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, math


def redirect_to_stepik(url, result):

    browser.get(url)
    time.sleep(5)

    enter = browser.find_element(By.CLASS_NAME, 'navbar__auth_login')
    enter.click()
    time.sleep(3)

    email = browser.find_element(By.CSS_SELECTOR, 'input[type=email]')
    email.send_keys('lorenditric@mail.ru')
    time.sleep(1)

    password = browser.find_element(By.CSS_SELECTOR, 'input[type=password]')
    password.send_keys('troy69battle')
    time.sleep(1)

    submit = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
    submit.click()
    time.sleep(3)

    browser.get(url)
    time.sleep(15)

    if browser.find_element(By.CSS_SELECTOR, 'div[data-type="string-quiz"]').get_attribute('data-state') == 'correct':
        again_button = browser.find_element(By.CLASS_NAME, 'again-btn')
        again_button.click()
        time.sleep(3)

    stepik_answer = browser.find_element(By.TAG_NAME, 'textarea')
    stepik_answer.send_keys(result)
    time.sleep(2)

    stepik_button = browser.find_element(By.CLASS_NAME, 'submit-submission')
    stepik_button.click()
    time.sleep(1)


with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    if price:
        browser.find_element(By.ID, 'book').click()

    x = browser.find_element(By.ID, 'input_value').text
    value = math.log(abs(12 * math.sin(int(x))))

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(value)

    button = browser.find_element(By.ID, "solve")
    button.click()

    confirm = browser.switch_to.alert
    required_num = confirm.text.split()[-1]
    confirm.accept()

    redirect_to_stepik("https://stepik.org/lesson/181384/step/8?unit=156009", required_num)
    time.sleep(5)