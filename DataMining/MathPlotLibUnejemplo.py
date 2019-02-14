import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#mean serie de un nivel especifico

data = pd.read_csv("titanic.csv")

#print data.shape

print list(data.columns.values)

#print data

#print data['Age'] ##acceder a las columnas

#print data.describe()

#print data[data['Fare']==0]

#APENAS SE VE, AGRUPEMOS

#print pd.crosstab(data['Survived'], data['Sex'])

#agrupar por varias columnas

#sexoClaseSuperviviente = data.groupby(['Pclass', 'Sex'])['Survived'].sum()

#print sexoClaseSuperviviente

#print data[data['Age']<1].value_counts() FALLA

#GRAFICAS


tags = ['riper', 'vivos']
filtroRipers = data['Survived'].value_counts()
x_pos = list(range(len(tags)))
width = 0.5
fig, ax = plt.subplots() # creamos la grafica
plt.bar(x_pos, filtroRipers, width, alpha=1, color='r')  # creamos las barras en X
ax.set_xticks([p + 0 * width for p in x_pos]) #configuracion del grid
ax.set_xticklabels(tags)
plt.grid()
plt.show()
print filtroRipers

#sexoClaseSuperviviente = data.groupby(['Pclass', 'Sex'])['Survived'].sum()
filtroVivosRiperSexo = data.groupby(['Sex'])['Survived'].sum()
print filtroVivosRiperSexo


#Bienvenidos a CONDA :D



#DATOS RANDOM
#np.random.seed(19680801)
#data = np.random.randn(2, 100)
#fig, axs = plt.subplots(2, 2, figsize=(5, 5))
#axs[0, 0].hist(data[0])
#axs[1, 0].scatter(data[0], data[1])
#axs[0, 1].plot(data[0], data[1])
#axs[1, 1].hist2d(data[0], data[1])

plt.show()