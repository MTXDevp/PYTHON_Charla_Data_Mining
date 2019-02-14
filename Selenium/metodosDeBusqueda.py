from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException

mobileEmulation = {'deviceName': 'iPhone 6 Plus'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
options.add_argument("--incognito")
nav = webdriver.Chrome(executable_path="C:\Users\USUARIO\PycharmProjects\MTXDevp\Selenium\chromedriver.exe")

#nav = webdriver.Chrome(executable_path="C:\Users\USUARIO\PycharmProjects\MTXDevp\Selenium\chromedriver.exe")


def checkExistsByXpath(path):
    try:
        print("Checkeando ", path + " concreto")
        elem = nav.find_elements_by_xpath(path)
        # elem = nav.find_element_by_id("f3d44d5031fd228")
        # elem = nav.find_element_by_tag_name('emailOrPhone')
        # elem = nav.find_element_by_name(path)
    except NoSuchElementException:
        return False
    if len(elem) == 0:
        return False
    else:
        return elem


def getXpath(path):
    item = False
    count = 5
    while item == False and count >= 0:
        sleep(0.2)
        print("Buscando....", path)
        item = checkExistsByXpath(path)
        # count = count - 1
    if count <= 0:
        print(path + " No encontrado")
    else:
        print(path + " Encontrado")
        return item


def checkExistsByClassName(name):
    try:
        print("Buscando Clase ", name)
        elem = nav.find_element_by_class_name(name)
    except NoSuchElementException:
        return False
    return elem
