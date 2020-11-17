# -*- coding: utf-8 -*-
#realizar gráficos desde la estructura de datos
import matplotlib.pyplot as plt

#biblioteca para redes complejas
import networkx as nx

y=[2,3,10,0,3,5]

#se utiliza una cuadrícula en el gráfico
plt.grid(True)

#se pasa la lista a graficar
plt.plot(y)
plt.show()

#Ahora graficamos un histograma
y=[2,3,10,2,4,5]

plt.bar(range(len(y)),
        y,
        width=0.2,
        align='center')
plt.show()

#impresión de grafos
P=nx.Graph([('a','b'),('b','c')])
nx.draw(P,with_labels=True)
plt.show()

#impresión de características de los grafos
print("Nodos ", P.nodes())
print("Gradod e nodo b", P.degree('b'))


#grafo más complejo
G=nx.Graph([(0,1),(0,2),(1,2),
            (2,3),(2,4),(2,5),
            (3,4),(4,5)])
nx.draw(G,with_labels=True)
plt.show()