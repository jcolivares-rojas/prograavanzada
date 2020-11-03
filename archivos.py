#manejo de archivos

#leer archivo
#f = open("archivo.txt")
try:
	f = open("archivo.txt", "r", encoding="UTF-8")
except Exception as e:
	print("No existe el archivo...")
else:
	cont2 = f.readlines()

	#print(cont2)

	c = 1
	for linea in cont2:
		print(c,".", linea)
		c = c +1


	f.close()
#finally:
#	print("Siempre lo ejecuta")


""" leer archivo completo
contenido = f.read();

print("Contenido =\n", contenido)
"""



#print("Contador=", cont2)

#escritura
f = open("datos.txt", "w")

f.write("Hola archivos!!!")

#f.close()

#f = open("datos.txt", "w+")

f.write("Ejemplo")
print("Otra linea", file=f)

f.close()
