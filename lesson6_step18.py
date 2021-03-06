from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    button = browser.find_element_by_id('book')
    button.click()
    h3 = browser.find_element_by_id('simple_text')
    browser.execute_script("return arguments[0].scrollIntoView(true);", h3)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    input = browser.find_element_by_id('answer')
    input.send_keys(calc(x))
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()



