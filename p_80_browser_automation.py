from selenium import webdriver
import selenium
import time

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# driver location path geckodriver
driver = webdriver.Firefox(executable_path="/home/elsys/Documents/geckodriver_026/geckodriver")

driver.implicitly_wait(6)

# driver abre URl desejada
driver.get("https://github.com")

# open window max
driver.maximize_window()

web_title = driver.title

print(web_title)

# click button sign_in
time.sleep(1)
driver.find_element_by_xpath("//a[@class='HeaderMenu-link no-underline mr-3']").click()

# username login
time.sleep(1)
driver.find_element_by_id("login_field").clear()
time.sleep(1)
driver.find_element_by_id("login_field").send_keys("vpinho13")

driver.find_element_by_id("password").send_keys("130277@1977Vcx")

time.sleep(0.2)
driver.find_element_by_name("commit").submit()
print("button press now...")


driver.find_element_by_xpath("//summary[@class='Header-link']//img[contains(@class,'avatar')]").click()


time.sleep(2)
element = driver.find_element_by_xpath("//strong[@class='css-truncate-target']")
print(element.text)

assert "vpinho13" == element.text
print("Pass assert")

# close all browsers
time.sleep(6)
driver.close()
print("close all...")