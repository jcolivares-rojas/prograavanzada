#Programa que calcula probabilidades...

import pandas as pd 
import matplotlib.pyplot as plt

#Cargar datos
datos = pd.read_csv("nvo_reg.csv")

print(datos)

#mostrar los datos descriptivos
print(datos.describe())

#restriccion
print("Estadisticos de consumo") 
print(datos["consumo"].describe())

#restringe columnas -->select columnas
df = datos[["consumo", "produccion"]]
print(df)

#restringimos filas -->where
df = df.loc[:100]
#df = df["consumo" > 100]

#vamos a graficar el conjunto de datos
df.plot()
plt.show()

#mostrar histograma
df.hist()

plt.show()