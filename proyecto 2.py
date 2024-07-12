#inciso a
import numpy as np
import pandas as pd
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import tkinter
import filtro_aplicado as fap
# Cargar el dataset digits de sklearn
digitos = load_digits()

# Obtener las imágenes y los targets del dataset
imagenes = digitos.images
targets = digitos.target

# Crear una matriz para almacenar las imágenes promedio de cada dígito
promedios = np.zeros((10, 8, 8))

# Contar el número de ocurrencias de cada dígito
contador = np.zeros(10)

# Calcular la imagen promedio de cada dígito
for i in range(len(imagenes)):
    promedios[targets[i]] += imagenes[i]
    contador[targets[i]] += 1

for i in range(10):
    promedios[i] /= contador[i]

# Mostrar las imágenes promedio
#for i in range(10):
index = int(input("Ingrese el número del dígito que desea ver: "))
plt.imshow(promedios[index], cmap='gray')
plt.title(f'Dígito {index}')
plt.show()
#-----------------------------------------------------------------------------------------*

#inciso b
#las imagenes ya se muestran(matplotib)

#-----------------------------------------------------------------------------------------*

#inciso c
def leer_digito():
    digito = []
    print("Ingrese los 64 valores del dígito (8x8):")
    for i in range(8):
        fila = list(map(int, input().split()))
        digito.append(fila)
    return np.array(digito)

#inciso d
def calcular_distancia_euclidiana(img1, img2):
    altura1, ancho1 = len(img1), len(img1[0])
    altura2, ancho2 = len(img2), len(img2[0])

    if altura1 != altura2 or ancho1 != ancho2:
        print("Las imágenes deben tener las mismas dimensiones para calcular la distancia euclidiana.")
        return None

    distancia = 0
    for i in range(altura1):
        for j in range(ancho1):
            diferencia = img1[i][j] - img2[i][j]
            distancia += diferencia ** 2

    return np.sqrt(distancia)

def encontrar_mas_parecidos(nuevo_digito):
    distancias = []
    for i in range(len(imagenes)):
        distancia = calcular_distancia_euclidiana(nuevo_digito, imagenes[i])
        distancias.append((distancia, targets[i]))
    distancias.sort(key=lambda x: x[0])
    return distancias[:3]

# Leer el nuevo dígito
#nuevo_digito = leer_digito()
"""nuevo_digito = tkinter.filedialog.askopenfilename(
        title="Seleccionar archivo",
        filetypes=(("Archivos de imagenes jpg", "*.jpg"), ("all files", "*.*"))
)"""

#print(nuevo_digito)
nuevo_digito = fap.lista_limpia
# Encontrar los 3 dígitos más parecidos
parecidos = encontrar_mas_parecidos(nuevo_digito)
for distancia, digito in parecidos:
    print(f'Dígito: {digito}, Distancia: {distancia}')
"""
#-----------------------------------------------------------------------------------------*
#inciso f
"""
def clasificar_numero(nueva_imagen, prototipos, nombres_prototipos):
    min_distancia = float('inf')
    numero_clasificado = None

    for i in range(len(prototipos)):
        distancia = calcular_distancia_euclidiana(nueva_imagen, prototipos[i])
        if distancia is None:
            print("No se puede clasificar la imagen debido a diferencias en las dimensiones.")
            return None
        if distancia < min_distancia:
            min_distancia = distancia
            numero_clasificado = nombres_prototipos[i]

    return numero_clasificado

def clasificar_digito(parecidos):
    conteo = [0] * 10
    for distancia, digito in parecidos:
        conteo[digito] += 1
    clasificacion = np.argmax(conteo)
    if conteo[clasificacion] >= 2:
        print(f"Soy la inteligencia artificial, y he detectado que el dígito ingresado corresponde al número {clasificacion}")
    else:
        print("No se pudo clasificar el dígito con seguridad.")

# Clasificar el nuevo dígito
clasificar_digito(parecidos)

#-----------------------------------------------------------------------------------------*

#inciso g

def clasificar_con_promedio(nuevo_digito):
    distancias = []
    for i in range(10):
        distancia = calcular_distancia_euclidiana(nuevo_digito, promedios[i])
        distancias.append((distancia, i))
    distancias.sort(key=lambda x: x[0])
    clasificacion = distancias[0][1]
    print(f"Soy la inteligencia artificial versión 2, y he detectado que el dígito ingresado corresponde al número {clasificacion}")

# Clasificar con el método de promedios
clasificar_con_promedio(nuevo_digito)

#-----------------------------------------------------------------------------------------*
