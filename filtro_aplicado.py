"""import imageio
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
image_path = 'xd.jpg'
image = Image.open(image_path)

# Convertir la imagen a escala de grises
gray_image = image.convert('L')

# Convertir la imagen a una matriz de numpy
image_array = np.array(gray_image)

# Aplicar un umbral para convertir la imagen a blanco y negro (contraste absoluto)
threshold = 128
bw_image_array = (image_array > threshold) * 255

# Convertir de nuevo la matriz a una imagen PIL
bw_image = Image.fromarray(bw_image_array.astype('uint8'), 'L')
bw_image.save("final.jpg")"""
# Mostrar la imagen resultante
"""plt.figure(figsize=(8, 8))
plt.imshow(bw_image, cmap='gray')
plt.axis('off')
plt.show()"""


import numpy as np
import matplotlib.pyplot as plt

def Reescalar_Img(image, nuevo_ancho, nuevo_alto):
    alto_original, ancho_original, canales = image.shape
    image_reescalada = np.zeros((nuevo_alto, nuevo_ancho, canales), dtype=np.uint8)

    for i in range(nuevo_alto):
        for j in range(nuevo_ancho):
            x_original = int(j * ancho_original / nuevo_ancho)
            y_original = int(i * alto_original / nuevo_alto)
            image_reescalada[i][j] = image[y_original][x_original]

    return image_reescalada

def escala_de_grises_método_luminisidad(image):
    alto, ancho, canales = image.shape
    grayscale_image = np.zeros((alto, ancho), dtype=np.uint8)

    for i in range(alto):
        for j in range(ancho):
            r, g, b = image[i][j]
            grayscale_value = int(0.3 * r + 0.59 * g + 0.11 * b)
            grayscale_image[i][j] = grayscale_value

    return grayscale_image

def ConvertirImg(image, filename):
    nuevo_ancho = 8
    nuevo_alto = 8
    rescaled_image = Reescalar_Img(image, nuevo_ancho, nuevo_alto)
    grayscale_image = escala_de_grises_método_luminisidad(rescaled_image)
    plt.imsave(filename, grayscale_image, cmap='gray')
    print(f"Imagen guardada como {filename}")


image = plt.imread("xd.jpg")
ConvertirImg(image, "final.jpg")

import imageio
import numpy as np


def leer_imagen(ruta):
    """
    La función leer_imagen recibe un string con la ruta
    de una imagen en formato BMP y retorna una lista de
    tres dimensiones con el mapa de bits de la imagen.
    Asimismo, convertimos la lista de numpy a una lista
    común y corriente.
    """
    np_array = np.array(imageio.imread(ruta), dtype='int')
    # noinspection PyTypeChecker
    lista_3d = np_array.tolist()
    return lista_3d
lrd = leer_imagen("final.jpg")
print(lrd)

lista_limpia = []
for i in lrd:
    fila = []
    for j in i:
        fila.append(j[0])
    lista_limpia.append(fila)
    
print("-------------------")
print(lista_limpia)    
print(len(lista_limpia), len(lista_limpia[0]))

for i in range(len(lista_limpia)):
    for j in range(len(lista_limpia[i])):
        lista_limpia[i][j] = 16 -int(lista_limpia[i][j] * (16/255))

lista_limpia = np.array(lista_limpia)