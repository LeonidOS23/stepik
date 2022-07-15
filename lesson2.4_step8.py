from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book = browser.find_element(By.ID, "book")
    book.click()
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
        
    element = browser.find_element(By.ID, "input_value")
    value = element.text

    field = browser.find_element(By.ID, "answer")
    field.send_keys(calc(value))
    
    button = browser.find_element(By.ID, "solve")
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()
    