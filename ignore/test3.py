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

# Mostrar la imagen resultante
plt.figure(figsize=(8, 8))
plt.imshow(bw_image, cmap='gray')
plt.axis('off')
plt.show()