# coding=utf-8
import json
import os
from os import path

import pandas as pd
import re
import matplotlib.pyplot as plt


tweets_data_path = 'datosLenguajes.txt'

tweets_data = []  # DICCIONARIO DEL JSON
tweets_file = open(tweets_data_path, "r")

# Leemos el json de la carpeta raiz del proyecto
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

#print(tweets_data)


# Metodo que filtra el mensaje en busca de la palabra prasada por parametro
# para pruebas mas complejas deberemos de tokenizar los datos
def filtroBusqueda(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

def extraer_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''

# Creamos mediante mapas una matriz de 3 columnas mediante pandas para trabajar con los Datos
print 'Estructurando Matriz'

datos = pd.DataFrame()
datos['text'] = map(lambda tweet: tweet['text'], tweets_data)
datos['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
#datos['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] is not None else None,
   #                    tweets_data)  # xq xddd

#print(datos)

# apply Aplicar una funcion a lo largo de un eje del DataFrame.
print 'Añadimos columnas y el verdadero o falso de nuestro método filtroBusqueda'

#stream.filter(track=['python', 'java', 'javascript', 'c#', 'c++'], is_async=True)


datos['python'] = datos['text'].apply(lambda tweet: filtroBusqueda('python', tweet))
datos['java'] = datos['text'].apply(lambda tweet: filtroBusqueda('java', tweet))
datos['javascript'] = datos['text'].apply(lambda tweet: filtroBusqueda('javascript', tweet))
datos['c#'] = datos['text'].apply(lambda tweet: filtroBusqueda('c#', tweet))
#datos['c++'] = datos['text'].apply(lambda tweet: filtroBusqueda('cococ', tweet))

#print(datos['python'])
#print(datos['java'])
#print(datos['javascript'])
#print(datos['c#'])
#print(datos['c++'])
#print(datos)

tags = ['python', 'java', 'javascript', 'c#']

#Recorremos la matriz en busca de la cuenta de todos los True de cada lenguaje
filtroMedianteLenguaje = [datos['python'].value_counts()[True],
                          datos['java'].value_counts()[True],
                          datos['javascript'].value_counts()[True],
                          datos['c#'].value_counts()[True]]
                          #datos['c++'].value_counts()[True]]

print(tags)
print(filtroMedianteLenguaje)

x_pos = list(range(len(tags)))
print(x_pos)
width = 0.3
fig, ax = plt.subplots() # creamos la grafica
plt.bar(x_pos, filtroMedianteLenguaje, width, alpha=1, color='g')  # creamos las barras en X
ax.set_ylabel('Numero de Tweets', fontsize=15)  # creamos label horizontal
ax.set_title('Los lenguajes de programacion mas populares (Datos en sucio)', fontsize=10, fontweight='bold')  # titulo
ax.set_xticks([p + 0 * width for p in x_pos]) #lineas interiores de las graficas
ax.set_xticklabels(tags)
plt.grid()
#plt.savefig('tweet_by_prg_language_1', format='png')
plt.show()



#añadimos nuevos valores a nuestra matriz de datos para que puedan ser analizados
#esto nos servira para hacer una busqueda mas precisa filtradno los datos
datos['programming'] = datos['text'].apply(lambda tweet: filtroBusqueda('programming', tweet))
datos['tutorial'] = datos['text'].apply(lambda tweet: filtroBusqueda('tutorial', tweet))
datos['relevant'] = datos['text'].apply(lambda tweet: filtroBusqueda('programming', tweet) or filtroBusqueda('tutorial', tweet))


filtroMedianteLenguajeRelevante = [datos[datos['relevant'] == True]['python'].value_counts()[True],
                      datos[datos['relevant'] == True]['java'].value_counts()[True],
                      datos[datos['relevant'] == True]['javascript'].value_counts()[True],
                      datos[datos['relevant'] == True]['c#'].value_counts()[True]]



x_pos = list(range(len(tags)))
width = 0.3
fig, ax = plt.subplots()
plt.bar(x_pos, filtroMedianteLenguajeRelevante, width,alpha=1,color='g')
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Lenguajes de programacion mas populares (Datos Filtrados)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0 * width for p in x_pos])
ax.set_xticklabels(tags)
plt.grid()
plt.show()
#plt.savefig('tweet_by_prg_language_2', format='png')


#Extraemos los links
datos['link'] = datos['text'].apply(lambda tweet: extraer_link(tweet))
tweets_relevant = datos[datos['relevant'] == True]
tweets_relevant_with_link = tweets_relevant[tweets_relevant['link'] != '']

print '\nMuestreo de Tutoriales de PYTHON\n'
print tweets_relevant_with_link[tweets_relevant_with_link['python'] == True]['link'].head()

print '\nMuestreo de Tutoriales de JAVA\n'
print tweets_relevant_with_link[tweets_relevant_with_link['java'] == True]['link'].head()

print '\nMuestreo de Tutoriales de JAVASCRIPT\n'
print tweets_relevant_with_link[tweets_relevant_with_link['javascript'] == True]['link'].head()

print '\nMuestreo de Tutoriales de C#\n'
print tweets_relevant_with_link[tweets_relevant_with_link['c#'] == True]['link'].head()