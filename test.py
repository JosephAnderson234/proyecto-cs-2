import imageio
import numpy as np

def aplicar_contraste_imagio(ruta_imagen, factor_contraste, ruta_guardado):
    """
    Aplica contraste a una imagen utilizando imageio y numpy, y guarda la imagen resultante.
    
    Parámetros:
    ruta_imagen (str): La ruta de la imagen a la que se le aplicará el contraste.
    factor_contraste (float): El factor de contraste a aplicar. 1.0 es el valor original,
                              menos de 1.0 reduce el contraste, más de 1.0 lo aumenta.
    ruta_guardado (str): La ruta donde se guardará la imagen resultante.
    """
    # Leer la imagen
    imagen = imageio.imread(ruta_imagen)
    
    # Convertir la imagen a float para realizar las operaciones
    imagen = imagen.astype(np.float32)
    
    # Calcular el promedio de los píxeles de la imagen
    promedio = np.mean(imagen)
    
    # Aplicar el factor de contraste
    imagen_mejorada = (imagen - promedio) * factor_contraste + promedio
    
    # Asegurarse de que los valores de los píxeles estén en el rango [0, 255]
    imagen_mejorada = np.clip(imagen_mejorada, 0, 255).astype(np.uint8)
    
    # Guardar la imagen resultante
    imageio.imwrite(ruta_guardado, imagen_mejorada)
    print(f"Imagen guardada en {ruta_guardado}")

# Ejemplo de uso
ruta_imagen = "xd.jpg"
factor_contraste = 0.2  # Aumenta el contraste
ruta_guardado = "xd3.jpg"

aplicar_contraste_imagio(ruta_imagen, factor_contraste, ruta_guardado)
