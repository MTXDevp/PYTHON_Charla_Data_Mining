from selenium import webdriver
from time import sleep


mobileEmulation = {'deviceName': 'iPhone 6 Plus'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)

driver = webdriver.Chrome(executable_path="C:/Users/USUARIO/PycharmProjects/Selenium/chromedriver.exe", options=options)

driver.get("https://www.instagram.com/")

