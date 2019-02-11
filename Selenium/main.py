from threading import Thread

from selenium.webdriver.common.keys import Keys

from metodosDeBusqueda import *
import time
import names

#url = 'https://www.instagram.com/accounts/emailsignup/?hl=es'
#urlLogin = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
#url = "https://www.instagram.com/accounts/signup/email"
#urlRegistrar = "https://www.instagram.com/accounts/signup/email"

url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'

nombreCompleto = names.get_full_name()
primerNombre = names.get_first_name()
apellido = names.get_last_name()

print(nombreCompleto)
print(apellido)


nav.get(url)
nav.set_window_position(0, 0)
nav.set_window_size(1200, 800)

input = getXpath('//input')
input[0].send_keys('Afrosinto2018')
input[1].send_keys('Qwer1234')

nav.set_page_load_timeout(5)

button = getXpath('//button[contains(text(), "Entrar")]')
button[0].click()
#button = getXpath('//button[contains(text(), "Ahora no")]')
#button[0].click()

input = getXpath("//input[@placeholder='Busca']")
input[0].send_keys('alonsito112')
time.sleep(2000)
input[0].click()
input[0].send_keys(Keys.ENTER)


#boton 444
#input[0].send_keys(apellido + primerNombre + apellido + '@hotmail.com');
#input[1].send_keys(nombreCompleto);
#input[2].send_keys(apellido + "Py2DAM");
#input[3].send_keys('voyaaprobaraunqueseaenrepesca');





#input = getXpath('//input')
#input[0].send_keys('rafa-valls@hotmail.com')
#input[1].send_keys('moriralos69')
#button = getXpath('//button[contains(text(), "Entrar")]')
#button[0].click()
#nav.set_page_load_timeout(5)

