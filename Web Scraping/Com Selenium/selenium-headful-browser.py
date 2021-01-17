from selenium import webdriver
from os import path

DRIVER_PATH =  'C:/Users/skylu/Desktop/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://google.com')