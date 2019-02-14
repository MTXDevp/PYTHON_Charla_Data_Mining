import pandas as pd
import numpy as np

# UTILIZACION DE DATAGRAMAS

#name_age = {'Nombre': ['Rafa', 'Guille', 'Victor', 'Oscar', 'Ervo'],
            #'Edad': [29, 20, 27, 24, 19]}

#data_frame = pd.DataFrame(name_age)
#print data_frame

#Orden de las columnas personalizado

#data_frame_2 = pd.DataFrame(name_age, columns=['Nombre', 'Edad'])

#print data_frame_2

#labels personalizados

#data_frame_3 = pd.DataFrame(name_age, columns=['Nombre', 'Edad'], index=['a', 'b', 'c', 'd', 'e'])

#print data_frame_3

# UTILIZACION DE SERIES Objeto dimensional 1D similar a una columna de una tabla

#series = pd.Series(['Ali', 'Bill', 'David', 'Hany', 'Ibtisam'],
#                   index=[1, 2, 3, 4, 5])
#print series

# FUNCIONES BASICAS HEAD Y TAIL permite OBSERVAR MUESTRAS

#series = pd.Series(np.random.randn(20000))
#print series.head(1)
#print series.tail(10)

# FUNCION DE AGREGACION ADD

#dictionary_1 = {'A': [5, 8, 10, 3, 9],
#                'B': [6, 1, 4, 8, 7]}
#dictionary_2 = {'A': [4, 3, 7, 6, 1],
#                'B': [9, 10, 10, 1, 2]}
#data_frame_1 = pd.DataFrame(dictionary_1)
#data_frame_2 = pd.DataFrame(dictionary_2)
#data_frame_3 = data_frame_1.add(data_frame_2)
#print data_frame_1
#print data_frame_2
#print data_frame_3

# INSERTAR DATOS MEDIANTE EL INDICE

#data_frame_3.loc[666] = ['123', 'Hola']
#print data_frame_3

# BORRAR DATOS

#data_frame_3 = data_frame_3.drop(666)
#print data_frame_3

#print("El total de filas es : ")
#print len(data_frame_3)


# FILTRADO DE DATOS

#df4 = data_frame_3[data_frame_3['A'] > 10]
#print df4

# lambda time :D

#d = {'SEX': ['male', 'female', 'male']}
#dremplazo = {'male': 'M', 'female': 'F'}

#dflambda = pd.DataFrame(d)
#dflambda['SEX'] = dflambda['SEX'].apply(lambda x: dremplazo[x])
#print dflambda['SEX']

#FUNCIONES MATEMATICAS MUY SIMPLES

#df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B'])
#print df

#raiz cuadrada

#dfr = df.apply(np.sqrt)
#print dfr

#funcion de reduccion axis 0 = filas arriba abajo, axis 1 = columnas n n-dimensional matrices
#print 'reduccion'

#dfsum = pd.DataFrame([[1,2,3], [4,5,6]], columns=['A', 'B', 'C'])
#print dfsum
#print '----------------------------'
#dfsum = dfsum.apply(np.sum, axis=0)
#dfsumy = dfsum.apply(np.sum, axis=1)
#print dfsum



#mean serie de un nivel especifico

#data = pd.read_csv("titanic.csv")

#print data.shape

#print list(data.columns.values)

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


# LEER DATOS EXTERNOS
#data = pd.read_csv("test.csv")
# print(data)
