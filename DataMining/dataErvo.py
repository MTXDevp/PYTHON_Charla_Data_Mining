import json
import os
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd



tweets_data_path = 'ervo.txt'

tweets_data = []  # DICCIONARIO DEL JSON
tweets_file = open(tweets_data_path, "r")

# Leemos el json de la carpeta raiz del proyecto
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

for key in tweets_data:
    try:
        print key['text']
        texto = key['text']
    except:

        print 'el twitter no tiene texto'

wordcloud = WordCloud().generate(texto)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
wordcloud = WordCloud(max_font_size=40).generate(texto)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
