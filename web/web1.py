# −*− coding: UTF−8 −*−

#ejemplo de servicio web

#utilizamos la biblioteca Web.py
#se puede descargar e instalar o bien utilizar:
#pip install Web.py

import web

#imprimimos la version del servidor Web
print(web.__version__)

# en la tupla urls se guardan las rutas de nuestro servidor Web
urls = (
	# 'regex para url', 'clase donde se envia la petición'
 	'/', 'index',
 	"/creditos", "Creditos",
 	"/servicio/(.*)", "Servicio"
)

# Aplicacion donde se especifican las urls.
app = web.application(urls, globals())

# Clase index
class index:
	def GET(self):
		return "Hola, Mundo!"

#Clase Creeditos
class Creditos:
	def GET(self):
		return """<html>
			<head>
				<title>Créditos</title>
			</head>
			<body>
				<h1 style='align: center; color: red'>Progra Avanzada<h1>
			</body>
		</html>"""

#Para el manejo de fechas
import datetime as dt

class Servicio:
	def GET(self,name):
		#Hacer consulta a base de datos
		#Consultar archivos
		#verificar sensores
		#etc...

		if not name:
			name = 'actual/text'

		#obtenemos argumentos
		argumentos = name.split("/")
		
		#verificamos formato
		if argumentos[1] == "text":
			if argumentos[0] == "actual":
				return dt.datetime.now()
			else:
				return dt.date.today()
		else: #formato json
			if argumentos[0] == "actual":
				hoy = dt.datetime.now()
				cadena ="{'dia':"+str(hoy.day)+",\n"
				cadena+="'mes':"+str(hoy.month)+",\n"
				cadena+="'año':"+str(hoy.year)+",\n"
				cadena+="'hora':"+str(hoy.hour)+",\n"
				cadena+="'minuto':"+str(hoy.minute)+",\n"
				cadena+="'segundo':"+str(hoy.second)+"}"
				return cadena
			else:
				hoy = dt.date.today()
				cadena ="{'dia':"+str(hoy.day)+",\n"
				cadena+="'mes':"+str(hoy.month)+",\n"
				cadena+="'año':"+str(hoy.year)+"}"
				return cadena

# corremos el servidor Web por default en puerto 8080
if __name__ == "__main__":
	app.run()
