# -*- coding: utf-8 -*-
"""
Spyder Editor

Programa para el maenjo de pandas y base de datos SQLite

This is a temporary script file.
"""

import sqlite3
import pandas as pd

# Otra forma de importar bibliotecas
from matplotlib import pyplot as plt

#Conexión a la base de datos
conn = sqlite3.connect('mediciones.db')
cur = conn.cursor()

#lanzar la consulta
query = 'SELECT * FROM nvo_reg LIMIT 10;'

cur.execute(query)

#iterar para mostrar los resultados y guardarlos en una lista
lista = []

for row in cur:
    lista.append(row)
    print(row) 
    
#Para obtener datos en pandas se tiene que crear una estructura particular

# obtenemos del encabezado el nombre de la columna
columnas = [member[0] for member in cur.description]

# ignoramos el indice para la columna
#columns = columnas[1:]    
#print(columnas)

#obtener estructura en pandas
#se crea un marco de de datos solo con las columnas
df = pd.DataFrame(columns=columnas, data=lista)

#df.append(lista, ignore_index=True)
#df.head()
print(df.head())

#Procesar datos con pandas
#guardar resultados en BD con SQL
#unir marcos de datos en pandas. Se verá más adelante

plt.figure(figsize=(20,10))
plt.plot(df.index, df[['produccion','consumo']], 'o')