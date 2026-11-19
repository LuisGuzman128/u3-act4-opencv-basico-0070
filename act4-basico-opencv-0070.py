# 0. IMPORTACIÓN DE LIBRERÍAS
# ==============================================================================
import cv2  # Importa la librería OpenCV para procesamiento de imágenes y visión artificial.
import numpy as np  # Importa NumPy para manejar las imágenes como arreglos/matrices matemáticas.
import sys  # Importa Sys para poder detener el programa de forma segura si ocurre un error.
import win32gui
import win32con
import win32api

# ==============================================================================
print("+-+-+-Axel Guzman NC 0070+-+-+-")

# 1. LECTURA DE LA IMAGEN DESDE LA CARPETA
# ==============================================================================
print("\n1. LECTURA DE IMÁGENES")  # Imprime el título de la sección en la consola.
nombre_ventana = 'Gpo 3H img carro rojo Axel Guzman 0070'  # linea nueva
imgperro_rojo = cv2.imread('perrorojo.png')  # Lee la imagen 'perrorojo.png' y la guarda como matriz en 'imgperro_rojo'.

# 3.crear ventana de openCV
cv2.namedWindow(nombre_ventana)  # linea nueva

if imgperro_rojo is None:  # Verifica si la variable 'imgperro_rojo' está vacía (es decir, si no encontró el archivo).
    print("Error: No se pudo leer 'perrorojo.png'. Revisa el nombre y ubicación.")
    sys.exit()
else:  # Si la imagen sí se cargó correctamente...
    print("Imagen cargada exitosamente.")

# =============================================================================
# 2. PROPIEDADES DE LA IMAGEN
# ==============================================================================
print("\n2. PROPIEDADES DE LA IMAGEN Axel Guzman 0070")
height, width, channels = imgperro_rojo.shape
print(f"Dimensiones de la imagen: {width}x{height} píxeles")
print(f"Número de canales de color: {channels}")
print(f"Tipo de dato de la imagen: {imgperro_rojo.dtype}")
print(f"Total de datos/píxeles: {imgperro_rojo.size}")
# =============================================================================
# 3. VISUALIZACIÓN DE LA IMAGEN ORIGINAL
# ==============================================================================
print("\n3. MOSTRANDO IMAGEN ORIGINAL del perro rojo")
print("Presiona cualquier tecla sobre la ventana de la imagen para continuar...")
cv2.imshow('Img perro rojo Original Axel Guzman 0070', imgperro_rojo)
cv2.waitKey(0)  # Pausa el programa infinitamente hasta que el usuario presione una tecla.
cv2.destroyAllWindows()
print("+-+-+-modificando pixeles+-+-+-")

# ==============================================================================
# 4. ACCESO Y MODIFICACIÓN DE PÍXELES INDIVIDUALES
# ==============================================================================
print("\n4. ACCEDIENDO Y MODIFICANDO PÍXELES")  # Imprime el título de la cuarta sección.

pixel_img = imgperro_rojo.copy()  # Crea una copia exacta de la imagen original para no dañarla.

y, x = 100, 150  # Define las coordenadas a analizar: fila (Y) = 100, columna (X) = 150.

if y >= pixel_img.shape[0] or x >= pixel_img.shape[1]:
    print("Error: Las coordenadas están fuera de la imagen.")
    sys.exit()

pixel = pixel_img[y, x]  # Obtiene los 3 valores de color [Azul, Verde, Rojo] del píxel.
print(f"Valor del píxel en ({x}, {y}): {pixel} (Formato BGR)")

pixel_img[y, x] = [0, 0, 255]  # Cambia el color de ese único píxel a rojo puro.
cv2.circle(pixel_img, (x, y), 15, (0, 255, 255), 2)  # Dibuja un círculo amarillo alrededor.

cv2.imshow('Pixel Modificado Axel Guzman 0070', pixel_img)
cv2.waitKey(0)
cv2.destroyAllWindows()