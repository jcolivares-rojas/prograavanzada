#-*- coding: utf-8 -*-
# Estructura de datos manual

import pandas as pd
import matplotlib.pyplot as plt

#leer datos desde archivo csv
mediciones = pd.read_csv("mediciones.csv");
print(mediciones)

#Estadisticas individuales
media = mediciones.mean()
print("LA media es: ", media)

mediaRedondea = mediciones["1"].mean()
print('Media redondeada ', round(mediaRedondea)) 

suma = mediciones.sum()
conteo = mediciones.count()
print("Suma = {0} \n Conteo= {1}", suma, conteo)

mediana= mediciones.median()
desviacion = mediciones.std()

print(mediana, desviacion)

maximo = mediciones.max()
minimo = mediciones.min()

print(maximo, minimo)

maximo = mediciones['Medidor'].max()
print("Maximo de medidor ", maximo)

def imc(x):
	return x+10

#mediciones["1"] = mediciones.apply(imc, axis=1)	
#print(mediciones)



#se pueden obtener estructuras mas simples
mediciones.plot(linestyle='-', linewidth=2.0, color='red')
plt.xlabel("X", fontsize=20)
plt.ylabel("Y", fontsize=20)
plt.title("Otro")
plt.show()


m = mediciones.transpose()
print(m)
m.plot(linestyle='-', linewidth=2.0, color='blue')
plt.show()

"""
lecturas = mediciones.loc(0)['1']['2']
lecturas.plot()
plt.show()
"""