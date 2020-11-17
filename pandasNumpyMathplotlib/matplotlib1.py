#-*- coding: utf-8 -*-
#Programa para manejo de gráficos elementales usando pylab

#biblioteca para el manejo de números
import numpy as np

#gráficos interactivos
import pylab as pl

#Se obtiene un espacio de 256 valores desde -pi hasta +pi incluyendo los límites
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)

#se calcula seno y coseno de estos espacios en forma de lista
C, S = np.cos(X), np.sin(X)

#se grafica cada línea
pl.plot(X, C)
pl.plot(X, S, color="blue", linewidth=1.0, linestyle="-")

indice=np.arange(-3, 3, 1)
pl.xticks(indice, ("A", "B", "C", "AA", "X", "Y", "Z"))

pl.show()

