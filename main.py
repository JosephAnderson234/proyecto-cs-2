from sklearn import datasets
import pandas as pd

from sklearn import datasets
import pandas as pd

##Pregunta a:
"""Manipular el dataset digits de sklearn para generar una matriz de 8x8 con la
imagen promedio de cada uno de los 10 dígitos disponibles en este dataset. Puede
generarlas todas juntas, o generarlas en base a un menú, o generarlas en base al
número que el usuario ingrese por teclado"""

misdatos = datasets.load_digits()
#ultimos datos "012...898"

#Imprimimos data
print(misdatos['data'])

