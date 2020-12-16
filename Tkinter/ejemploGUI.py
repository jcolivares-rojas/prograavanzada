"""
Ejemplo de GUI en Python utilizando Tkinter
MCIE Programación Avanzada Diciembre 2020
@jcolivares
"""

#importamos biblioteca
#from tkinter import *
import tkinter as tk

#Esta biblioteca tiene otros controles...
import tkinter.ttk as ttk

#Esta para cuadros de diálogo
import tkinter.messagebox as msg

#definimos manejadores de eventos...

#Lo asociaremos a un botón...
def presioname():
	valor = txt.get()
	fase = combo.get()
	op = opcion.get()

	mensaje ="Me presionaste---"+valor
	mensaje = mensaje +"\nFase: " + fase

	lbl.configure(text=mensaje)

	mensaje = "Opcion=" +str(op)
	msg.showinfo('Advertencia', mensaje)

def creditos():
	res = msg.askyesnocancel('Que deseas hacer?','Escoge tu opcion')
	mensaje = "Respuesta " + str(res)
	lbl.configure(text=mensaje)

#Construimos una ventana Tk
window = tk.Tk()

#Título de la ventana
window.title("Uso de Servicio Web")

#Se puede configurar el tamaño de la ventana
window.geometry('800x600')

#Agregamos una barra de menú
menu = tk.Menu(window)

#Agreamos opciones
new_item = tk.Menu(menu)

new_item.add_command(label='Acerca de...', command=creditos)

#Definimos el nombre del menú
menu.add_cascade(label='Ayuda', menu=new_item)

#Lo agregamos a la ventana
window.config(menu=menu)

#Construimos una etiqueta de texto
lbl = tk.Label(window, text="Este programa permite introducir datos de forma gráfica para nuestro servicio Web...", font=("Arial Bold", 18))

#Se agrega utilizando grid
"""
Nota:
Existen varias formas de colocar controles, pack() los va poniendo en bloques
Con grid los dibuja en una reticula o bien se pueden posicionar
En forma absoluta
"""
lbl.grid(column=0, row=0)

#Agregamos ahora un botón
btn = tk.Button(window, text="Click Me", bg="orange", fg="red", command=presioname)

#Nótese que se esta agregando en la siguiente columna y en la misma fila que la etiqueta...
btn.grid(column=1, row=0)

#Agregamos una caja de texto
txt = tk.Entry(window,width=10)

#La ponemos en la segunda fila
txt.grid(column=0, row=1)

#posicionamos el foco al control de la caja de texto
txt.focus()

#Agregamos un combo box
combo = ttk.Combobox(window)

#Se coloca en el diccionario los valores
combo['values']= (1, 2, 3, "Todos")

#Se escoge la selección por default
combo.current(3) 

combo.grid(column=1, row=1)

#Se va a agregar un boton de check
#Para ello se define primero un componente booleano
chk_state = tk.BooleanVar()

#Se coloca en True el estado
chk_state.set(True) 

#Se define el botón de check con el estado definido
chk = tk.Checkbutton(window, text='Selecciona', var=chk_state)

#lo agregamos en la segunda fila tercera columa
chk.grid(row=1, column=2)

#Agregamos un radio botón...

#ponemos la variable para las opciones
opcion = tk.IntVar()

#Para ello definimos las opciones
rad1 = tk.Radiobutton(window,text='Potencia', value=1, variable=opcion)
rad2 = tk.Radiobutton(window,text='Frecuencia', value=2, variable=opcion)
rad3 = tk.Radiobutton(window,text='Energia', value=3, variable=opcion)

#Los agregamos en una tercera fila...
rad1.grid(column=0, row=2)
rad2.grid(column=1, row=2)
rad3.grid(column=2, row=2)

#Este ciclo controla el manejo de eventos
window.mainloop()

