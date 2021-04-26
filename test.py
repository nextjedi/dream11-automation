print("hello")
print("hello")
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('./chromedriver')
browser.get("https://www.dream11.com/leagues")
print(browser.title)
time.sleep(1)
browser.find_element_by_class_name("js--home-login-btn").click()
time.sleep(1)
browser.find_element_by_class_name("input-field").send_keys("8095743867")
browser.find_element_by_xpath('//button[text()="PROCEED"]').click()
time.sleep(1)
otp = input("enter otp")
browser.find_element_by_class_name("input-field").send_keys(otp)
browser.find_element_by_xpath('//button[text()="VERIFY OTP"]').click()

time.sleep(1)