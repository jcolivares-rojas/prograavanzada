#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Biblioteca para acceso a BD
import sqlite3 as lite
import sys

#revisamos argumentos
if (len(sys.argv)!=5): 
	print("Sintaxis: ", sys.argv[0], "archivo.bd fechaInicio fechaFin tiempo")
	exit()

bd = sys.argv[1]
fechaInicio = sys.argv[2]
fechaFin = sys.argv[3]
t = int(sys.argv[4])

import datetime as dt

#parseamos fechas
anio, mes, dia = fechaInicio.split('/')

anio = int(anio)
mes = int(mes)
dia = int(dia)

anioF, mesF, diaF = fechaFin.split('/')

anioF = int(anioF)
mesF = int(mesF)
diaF = int(diaF)

#Año mes dia hora minuto segundo
fecha = dt.datetime(anio, mes, dia, 00,00,00)
limite = dt.datetime(anioF, mesF, diaF, 00, 00, 00)

import random as r

#función que obtiene el valor del sensor*
def getValor():
	min = -5.6
	max = 47.53
	valor = r.uniform(min, max)
	return valor

#establecemos conexion a la base de datos, sino existe se crea
con = lite.connect(bd)

#manejamos gestión de errores
with con:
	#Abrimos el cursor
	cur = con.cursor()

	#creamos la tabla base de datos, checamos primero que no exista
	#si existe se borra
	cur.execute("DROP TABLE IF EXISTS temperatura")
	cur.execute("CREATE TABLE temperatura(timestamp TEXT, temp REAL)")

	#Comprometemos datos
	con.commit()

	#insertamos datos...
	while(fecha < limite):
		fecha_cadena = fecha.strftime("%Y/%m/%d %H:%M:%S")
		lectura = "INSERT INTO temperatura VALUES('"+fecha_cadena + "'," + str(getValor())+")"
		
		cur.execute(lectura)

		#contador = contador + 1
		fecha = fecha + dt.timedelta(minutes=t)

	con.commit();
	print("Base de datos generada con éxito")
	#verificamos numero de datos creados
	cur.execute("SELECT count(*) from temperatura")
	datos = cur.fetchone()[0]
	#datos = cur.fetchone()

	print("Cantidad de datos:{}".format(datos))
	print("A continuación se muestra un ejemplo de los datos\n")
	
	#Mostrar los 10 primeros registros
	#cursor = con.execute("SELECT * FROM temperatura limit 10")

	cur.execute("SELECT * FROM temperatura limit 100")
	cursor = cur.fetchall()

	print("#\tTimestamp\t\tTemperatura")
	contador = 1
	
	for fila in cursor:
		print(contador, "\t", fila[0], "\t", fila[1])
		#print(fila)
		contador = contador + 1
