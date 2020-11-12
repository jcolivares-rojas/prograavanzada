#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Programa que permite calcular la varianza y desviacion estándar de una BD en SQLite
import sqlite3 as lite
import sys

#Para biblioteca matematica
import math

#revisamos argumentos
if (len(sys.argv)!=2): 
	print("Sintaxis: ", sys.argv[0], "archivo.bd")
	exit()

bd = sys.argv[1]

#establecemos conexion a la base de datos, sino existe se crea
con = lite.connect(bd)

#manejamos gestión de errores
with con:
	#Abrimos el cursor
	cur = con.cursor()

	#calculamos promedio
	cur.execute("SELECT avg(temp) from temperatura")
	promedio = cur.fetchone()[0]
	promedio = float(promedio)

	print("Promedio:",promedio) 

	#calculamos cantidad de datos
	cur.execute("SELECT count(temp) from temperatura")
	N = cur.fetchone()[0]
	N = int(N)

	print("N:",N, sep="\t", end=" ") 
	
	#Iteramos por cada valor de temperatura para aplicar la formula de varianza
	cur.execute("SELECT temp FROM temperatura ORDER BY temp")
	cursor = cur.fetchall()
	
	varianza = 0
	for fila in cursor:
		x = float(fila[0])
		varianza = varianza + math.pow((x - promedio), 2)

	varianza = varianza / N

	print("Varianza=", varianza)

	desviacion = math.sqrt(varianza)
	print("Desviacion estándar=", desviacion)