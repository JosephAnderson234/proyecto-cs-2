    import imageio
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
import filtro_pecador as fp
import os


# Funciones ya implementadas

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


def leer_imagen(ruta):
    np_array = np.array(imageio.imread(ruta), dtype='int')
    lista_3d = np_array.tolist()
    return lista_3d


def array_custom(ruta):
    image = plt.imread(ruta)
    ConvertirImg(image, "final.jpg")
    lrd = leer_imagen("final.jpg")

    lista_limpia = []
    for i in lrd:
        fila = []
        for j in i:
            fila.append(j[0])
        lista_limpia.append(fila)

    for i in range(len(lista_limpia)):
        for j in range(len(lista_limpia[i])):
            lista_limpia[i][j] = 16 - int(lista_limpia[i][j] * (16 / 255))

    lista_limpia = np.array(lista_limpia)
    return lista_limpia


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


def mostrar_imagen_promedio(index):
    plt.imshow(promedios[index], cmap='gray')
    plt.title(f'Dígito {index}')
    plt.show()


def leer_digito():
    digito = []
    print("Ingrese los 64 valores del dígito (8x8):")
    for i in range(8):
        fila = list(map(int, input().split()))
        digito.append(fila)
    return np.array(digito)


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


def clasificar_digito(parecidos):
    conteo = [0] * 10
    for distancia, digito in parecidos:
        conteo[digito] += 1
    clasificacion = np.argmax(conteo)
    if conteo[clasificacion] >= 2:
        print(
            f"Soy la inteligencia artificial, y he detectado que el dígito ingresado corresponde al número {clasificacion}")
    else:
        print("No se pudo clasificar el dígito con seguridad.")


def clasificar_con_promedio(nuevo_digito):
    distancias = []
    for i in range(10):
        distancia = calcular_distancia_euclidiana(nuevo_digito, promedios[i])
        distancias.append((distancia, i))
    distancias.sort(key=lambda x: x[0])
    clasificacion = distancias[0][1]
    print(
        f"Soy la inteligencia artificial versión 2, y he detectado que el dígito ingresado corresponde al número {clasificacion}")


# Menú principal
def menu():
    while True:
        print("\nMenú:")
        print("1. Mostrar imágenes promedio de los dígitos")
        print("2. Ingresar un nuevo dígito desde el teclado")
        print("3. Ingresar un nuevo dígito desde una imagen")
        print("4. Encontrar dígitos similares")
        print("5. Clasificar dígito basado en dígitos similares")
        print("6. Clasificar dígito basado en imágenes promedio")
        print("7. Salir")
        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            index = int(input("Ingrese el número del dígito que desea ver (0-9): "))
            mostrar_imagen_promedio(index)

        elif opcion == '2':
            nuevo_digito = leer_digito()
            parecidos = encontrar_mas_parecidos(nuevo_digito)
            for distancia, digito in parecidos:
                print(f'Dígito: {digito}, Distancia: {distancia}')
            clasificar_digito(parecidos)
            clasificar_con_promedio(nuevo_digito)

        elif opcion == '3':
            archivo_imagen = input("Ingrese la ruta del archivo de la imagen: ")
            nuevo_digito = fp.array_custom(os.path.normpath(archivo_imagen))
            parecidos = encontrar_mas_parecidos(nuevo_digito)
            for distancia, digito in parecidos:
                print(f'Dígito: {digito}, Distancia: {distancia}')
            clasificar_digito(parecidos)
            clasificar_con_promedio(nuevo_digito)

        elif opcion == '4':
            archivo_imagen = input("Ingrese la ruta del archivo de la imagen: ")
            nuevo_digito = fp.array_custom(os.path.normpath(archivo_imagen))
            parecidos = encontrar_mas_parecidos(nuevo_digito)
            for distancia, digito in parecidos:
                print(f'Dígito: {digito}, Distancia: {distancia}')

        elif opcion == '5':
            archivo_imagen = input("Ingrese la ruta del archivo de la imagen: ")
            nuevo_digito = fp.array_custom(os.path.normpath(archivo_imagen))
            parecidos = encontrar_mas_parecidos(nuevo_digito)
            clasificar_digito(parecidos)

        elif opcion == '6':
            archivo_imagen = input("Ingrese la ruta del archivo de la imagen: ")
            nuevo_digito = fp.array_custom(os.path.normpath(archivo_imagen))
            clasificar_con_promedio(nuevo_digito)

        elif opcion == '7':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

menu()
