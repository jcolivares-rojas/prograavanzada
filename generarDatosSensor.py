#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/python
#Programa que genera datos de un sensor

#importar argumentos del sistema
import sys

if (len(sys.argv)!=3): 
	print("Sintaxis: ", sys.argv[0], "mes(fecha)", "tiempo(minuto)")
	exit()

mes = sys.argv[1]
t = int(sys.argv[2])

#utilizamos funciones de tiempo
#import time
import datetime as dt

#mes = mes + " 00:00:00"
#tiempo = time.strptime(mes, "%Y/%m/%d %H:%M:%S") 

#parsear cadena
anio, mes, dia = mes.split('/')

anio = int(anio)
mes = int(mes)
dia = int(dia)

#Año mes dia hora minuto segundo
fecha = dt.datetime(anio, mes, dia, 00,00,00)
limite = dt.datetime(anio, mes+1, dia, 00, 00, 00)
#print(fecha, t, limite)

#utilizamos numeros aleatorios
import random as r

#función que obtiene el valor del sensor*
def getValor():
	min = -5.6
	max = 47.53
	valor = r.uniform(min, max)
	return valor

#validar cantidad
#limite = (60*24*30)/15
#contador = 0;

#escribir en el archivo
with open("datos.csv", "w") as f:
	#escritura del encabezado
	f.write("timestamp,temperatura\n")

	#while(contador <= limite):
	while(fecha < limite):
		fecha_cadena = fecha.strftime("%Y/%m/%d %H:%M:%S")
		lectura = fecha_cadena + "," + str(getValor())+"\n"
		
		f.write(lectura)

		#contador = contador + 1
		fecha = fecha + dt.timedelta(minutes=t)

print("Archivo generado con éxito")
