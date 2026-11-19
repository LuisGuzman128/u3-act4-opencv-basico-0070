
# 0. IMPORTACIÓN DE LIBRERÍAS
# ==============================================================================
import cv2  # Importa OpenCV para procesamiento de imágenes.
import numpy as np  # Importa NumPy para manejar matrices.
import sys  # Permite detener el programa si ocurre un error.

# ==============================================================================
print("+-+-+-Axel Guzman NC 0070+-+-+-")

# ==============================================================================
# MARCA DE AGUA PERSONALIZADA
# ==============================================================================
def agregar_marca(imagen):
    imagen = imagen.copy()
    cv2.putText(
        imagen,
        "Axel Guzman 0070",
        (10, imagen.shape[0] - 15),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 255),
        2
    )
    return imagen

# 1. LECTURA DE LA IMAGEN DESDE LA CARPETA
# ==============================================================================
print("\n1. LECTURA DE IMÁGENES")

nombre_ventana = 'Gpo 3H img carro rojo Axel Guzman 0070'
imgperro_rojo = cv2.imread('perrorojo.png')

# 3. crear ventana de OpenCV
cv2.namedWindow(nombre_ventana)

if imgperro_rojo is None:
    print("Error: No se pudo leer 'perrorojo.png'. Revisa el nombre y ubicación.")
    sys.exit()
else:
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

# ==============================================================================
# 3. VISUALIZACIÓN DE LA IMAGEN ORIGINAL
# ==============================================================================
print("\n3. MOSTRANDO IMAGEN ORIGINAL del perro rojo")
print("Presiona cualquier tecla sobre la ventana de la imagen para continuar...")

cv2.imshow(
    'Img perro rojo Original Axel Guzman 0070',
    agregar_marca(imgperro_rojo)
)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("+-+-+-modificando pixeles+-+-+-")

# ==============================================================================
# 4. ACCESO Y MODIFICACIÓN DE PÍXELES INDIVIDUALES
# ==============================================================================
print("\n4. ACCEDIENDO Y MODIFICANDO PÍXELES")

pixel_img = imgperro_rojo.copy()

y, x = 100, 150

if y >= pixel_img.shape[0] or x >= pixel_img.shape[1]:
    print("Error: Las coordenadas están fuera de la imagen.")
    sys.exit()

pixel = pixel_img[y, x]
print(f"Valor del píxel en ({x}, {y}): {pixel} (Formato BGR)")

pixel_img[y, x] = [0, 0, 255]
cv2.circle(pixel_img, (x, y), 15, (0, 255, 255), 2)

cv2.imshow(
    'Pixel Modificado Axel Guzman 0070',
    agregar_marca(pixel_img)
)
cv2.waitKey(0)

# ==============================================================================
# 5. REGIÓN DE INTERÉS (ROI - REGION OF INTEREST)
# ==============================================================================
print("\n5. REGIÓN DE INTERÉS (ROI)")

roi_img = imgperro_rojo.copy()

roi = roi_img[50:200, 100:300]
cv2.rectangle(roi_img, (100, 50), (300, 200), (0, 255, 0), 2)

cv2.imshow('Imagen con ROI marcada Axel Guzman NC 0070', agregar_marca(roi_img))
cv2.waitKey(0)

cv2.imshow('ROI Extraida (Recorte)Axel Guzman NC 0070', agregar_marca(roi))
cv2.waitKey(0)

# ==============================================================================
# 6. SEPARACIÓN Y FUSIÓN DE CANALES DE COLOR (BGR)
# ==============================================================================
print("\n6. SEPARANDO Y FUSIONANDO CANALES")

b, g, r = cv2.split(imgperro_rojo)

cv2.imshow('Canal Azul (Escala de grises)Axel Guzman NC 0070', agregar_marca(b))
cv2.imshow('Canal Verde (Escala de grises)Axel Guzman NC 0070', agregar_marca(g))
cv2.imshow('Canal Rojo (Escala de grises)Axel Guzman NC 0070', agregar_marca(r))
cv2.waitKey(0)

zeros = np.zeros_like(b)

blue_img = cv2.merge([b, zeros, zeros])
green_img = cv2.merge([zeros, g, zeros])
red_img = cv2.merge([zeros, zeros, r])

cv2.imshow('Canal Azul (Coloreado)Axel Guzman NC 0070', agregar_marca(blue_img))
cv2.imshow('Canal Verde (Coloreado)Axel Guzman NC 0070', agregar_marca(green_img))
cv2.imshow('Canal Rojo (Coloreado)Axel Guzman NC 0070', agregar_marca(red_img))
cv2.waitKey(0)

# ==============================================================================
# 7. REDIMENSIONAMIENTO DE IMÁGENES (RESIZING)
# ==============================================================================
print("\n7. REDIMENSIONANDO IMÁGENES")

resized_img = cv2.resize(imgperro_rojo, (400, 300))
cv2.imshow('Redimensionada a 400x300 Axel Guzman NC 0070', agregar_marca(resized_img))
cv2.waitKey(0)

half_size = cv2.resize(imgperro_rojo, None, fx=0.5, fy=0.5)
double_size = cv2.resize(imgperro_rojo, None, fx=1.5, fy=1.5)

cv2.imshow('Mitad de tamano (0.5x)', agregar_marca(half_size))
cv2.waitKey(0)

cv2.imshow('Ampliada (1.5x)', agregar_marca(double_size))
cv2.waitKey(0)

# ==============================================================================
# 8. ROTACIÓN DE IMÁGENES
# ==============================================================================
print("\n8. ROTANDO IMÁGENES")

height, width = imgperro_rojo.shape[:2]

rotation_matrix = cv2.getRotationMatrix2D(
    (width / 2, height / 2), 45, 1
)

rotated_img = cv2.warpAffine(
    imgperro_rojo, rotation_matrix, (width, height)
)

cv2.imshow('Imagen Rotada (45 grados)Axel Guzman NC 0070', agregar_marca(rotated_img))
cv2.waitKey(0)

# ==============================================================================
# 9. VOLTEO / ESPEJO DE IMÁGENES (FLIPPING)
# ==============================================================================
print("\n9. VOLTEANDO IMÁGENES")

horizontal_flip = cv2.flip(imgperro_rojo, 1)
cv2.imshow('Volteo Horizontal (Espejo)', agregar_marca(horizontal_flip))
cv2.waitKey(0)

vertical_flip = cv2.flip(imgperro_rojo, 0)
cv2.imshow('Volteo Vertical (De cabeza)', agregar_marca(vertical_flip))
cv2.waitKey(0)

both_flip = cv2.flip(imgperro_rojo, -1)
cv2.imshow('Volteo en Ambos Ejes', agregar_marca(both_flip))
cv2.waitKey(0)

# ==============================================================================
# 10. GUARDADO DE RESULTADOS Y LIMPIEZA
# ==============================================================================
print("\n10. GUARDANDO IMAGEN RESULTANTE")

result = cv2.imwrite(
    'rotated_image.jpg Axel Guzman NC 0070',
    agregar_marca(rotated_img)
)

if result:
    print("Imagen rotada guardada exitosamente como 'rotated_image.jpg'")
else:
    print("Error: No se pudo guardar la imagen rotada.")

cv2.destroyAllWindows()

print("\n¡Todas las operaciones se completaron con éxito!")
print("+-+-+-Axel Guzman NC 0070+-+-+-")
