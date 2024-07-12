import cv2
import numpy as np
import matplotlib.pyplot as plt

def eliminar_manchas(ruta_imagen, ruta_guardado):
    # Leer la imagen en escala de grises
    imagen = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)
    
    # Aplicar un filtro Gaussiano para eliminar ruido
    imagen_suavizada = cv2.GaussianBlur(imagen, (5, 5), 0)
    
    # Aplicar umbralización para convertir la imagen a binaria
    _, imagen_umbralizada = cv2.threshold(imagen_suavizada, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Invertir la imagen umbralizada (opcional, dependiendo de si el dibujo es negro sobre blanco o viceversa)
    imagen_invertida = cv2.bitwise_not(imagen_umbralizada)
    
    # Guardar la imagen resultante
    cv2.imwrite(ruta_guardado, imagen_invertida)
    print(f"Imagen procesada y guardada en {ruta_guardado}")
    
    # Mostrar las imágenes
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 3, 1), plt.title('Original'), plt.imshow(imagen, cmap='gray'), plt.axis('off')
    plt.subplot(1, 3, 2), plt.title('Suavizada'), plt.imshow(imagen_suavizada, cmap='gray'), plt.axis('off')
    plt.subplot(1, 3, 3), plt.title('Umbralizada'), plt.imshow(imagen_invertida, cmap='gray'), plt.axis('off')
    plt.show()

# Ejemplo de uso
ruta_imagen = 'xd.jpg'
ruta_guardado = 'xd4.jpg'

eliminar_manchas(ruta_imagen, ruta_guardado)
