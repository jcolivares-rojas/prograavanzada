#-*- coding: utf-8 -*-
# Estructura de datos manual

#Para manejo de datos con pandas
import pandas as pd

#Para manejo de gráficos
import matplotlib.pyplot as plt

datos = {
	'Equipo':['Licuadora', 'Horno de Microondas', '2 DVD Player', '2Tv Color (19-21")', 'Lavadora Automática', 'Plancha de ropa', 'Equipo de Cómputo', 'Refrigerador'],
	'Potencia': [350, 1200, 50, 140, 700, 1000, 300, 500],
	'TiempoUsoDia': ['10 min/dia', '15 min/dia', '3hr 4 veces x semana', '6 hr dia', '4 hr 2 vec semana', '3 hr 2 vec/sem', '4 hr dia', '9 hr dia'],
	'TiempoUsoMes': [5, 10, 48, 180, 32, 24, 120, 270],
	'ConsumoMensual': [1.75, 12, 2.4, 25.2, 22.4, 24, 36, 135]
}

#Así muestra primera y última columna
tabla = pd.DataFrame(datos)

#Se listan las columnas y su orden
#tabla = pd.DataFrame(datos, columns = ['Equipo', 'Potencia', 'Tiempo de uso al día', 'Tiempo uso mes (hrs)', 'Consumo mensual'], )

#Si no se le indica solo se despliegan las columnas que caben en el ancho
pd.set_option('display.max_columns', None)

#impresion
print(tabla)

#tamaño de la matriz de datos
print("Tamaño de datos ", tabla.shape)

#imprimir conteo de columnas (para ver si hay nulos = None)
print(tabla.count())

#mostrar información de la tabla 
#tabla.info()

#Obtener estadística descriptiva
print(tabla.describe())

#mostrar datos de la tabla (5 primeros registros)
print(tabla.head())

correlacion = tabla.corr(method='pearson')
#se puede cambiar el método de correlación

#impresión de la matriz de correlación
#print(correlacion)

#se pueden borrar columnas, filas
tabla.drop('TiempoUsoDia', axis=1, inplace=True)
tabla.drop([5, 6], axis=0, inplace=True)

#se pueden modificar datos en particular, por ejemplo del registro con id 3 (cuarto elemento)
tabla.loc[3] = ['MCIE', 0, 0, 0]

print(tabla)

#imprimiendo valores nulos de las columnas
col_names = tabla.columns.tolist()

for columnas in col_names:
	print ("Valores nulos de <{0}>: {1}".format(columnas, tabla[columnas].isnull().sum()))

#Accder a columnas por su nombre
print(tabla.Equipo)

#La recomendación es que tengan las colunas datos sin espacio
#Se pueden hacer filtros
consumoMax = tabla[tabla.Potencia>=500]

print(consumoMax)

#impresión de gráficos
#definimos el tamaño de la imagen de 300x100 px
#fig = plt.figure(figsize=(300,100))

#definimos el título de la imagen
plt.title('Consumo Mensual por Electrodoméstico')

#Se define la fuente de los datos y tipo de gráfica
tabla.plot(kind='bar', alpha=0.5)

#se visualiza la gráfica
plt.show()

