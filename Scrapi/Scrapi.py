import time
import PyPDF2
import requests
from PyPDF2 import PdfFileReader

#https://prod.nais.nasa.gov/eps/eps_data/157263-SOL-001-036.pdf
# instalar TOR
# pip install PySocks
# pip install time

#POSIBLES
# pio install requests[socks]
# pip install requests requests[socks]

# leer en crudo r.raw

# COMANDOS DE PRUEBA
# print(r.text)
# print(r.content)
# print(r.json())
# print(r.raw)
# print(r.raw.read(10))

# tor --service remove
# tor --service install -options ControlPort 9051

# Session permite gestionar peticiones a paginas webs
# socks5h nos permite usar dominios normales mediante TOR (que no maten nuestra conexion mediante DNS)

# METODOS----------------------------------------------------------------------------------------------------------------------



def leerPDF(url):
    input = PdfFileReader(file(url, "rb"))
    for page in input.pages:
        print page.extractText()

def conectarA(url):
    page = session.get(url)
    print(page.text)


def descargarDocumento(nombre, url):  # cambia la URL a la que quieras descargar :D
    page = session.get(url)
    archivo = page.content
    try:
        with open(nombre, 'wb') as my_data:  # open devuelve un objeto del archivo, with cerrara automaticamente el archivo
            my_data.write(archivo)
    except Exception as e:
        print e

def leerText(url):
    archivo = open(url, 'rb')
    print(archivo.readlines())

#FIN METODOS --------------------------------------------------------------------------------------------------------------------

#EJEMPLOS LECTURAS----------------------------------------------------------
""""
leerPDF('Diploma.pdf')
leerText('hola.txt')
"""
#FIN EJEMPLOS LECTURAS----------------------------------------------------------
session = requests.session()

#EJEMPLO SCRAPING------------------------------------------------------------

miIP = 'http://httpbin.org/ip'
conectarA(miIP)


# proxy SOCKS predefinido al instalar TOR /// netstat -aon | findstr ":9050"
session.proxies = {'http':  'socks5://127.0.0.1:9050',
                   'https': 'socks5://127.0.0.1:9050'}

page = ''
while page == '':
    try:
        conectarA(miIP)
        descargarDocumento("justisia.pdf","http://www.poderjudicial.es/search/contenidos.action?action=contentpdf&databasematch=TS&reference=8641025&optimize=20190201&publicinterface=true")
        #descargarDocumento("laNasa.pdf", "https://www.nasa.gov/sites/default/files/files/CCP-mini-Spanish-2.pdf")
        print('Datos Descargados')
        break
    except Exception as e:
        print(e)
        print("Peticion rechazada por el servidor..")
        print("Dejame dormir por 5 segundos")
        print("ZZzzzz...")
        time.sleep(5)
        print("Me encuentro mejor, continuemos :D")
        continue


