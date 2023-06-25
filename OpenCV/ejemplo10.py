import cv2  # Importar la biblioteca OpenCV
import numpy as np  # Importar la biblioteca NumPy para el procesamiento de imágenes
from matplotlib import pyplot as plt  # Importar la biblioteca Matplotlib para visualización
rutaimg="C:\\Users\\santo\\Documents\\GitHub\\Ejemplos-Emi\\OpenCV\\hobbiton.jpg"
rutatemplate="C:\\Users\\santo\\Documents\\GitHub\\Ejemplos-Emi\\OpenCV\\template.png"
img = cv2.imread(rutaimg, 0)  # Cargar una imagen en escala de grises
img2 = img.copy()  # Copiar la imagen cargada
template = cv2.imread(rutatemplate, 0)  # Cargar la imagen de la plantilla en escala de grises
w, h = template.shape[::-1]  # Obtener el ancho y alto de la plantilla

# Todos los 6 métodos de comparación en una lista
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED','cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()  # Restaurar la imagen original
    method = eval(meth)  # Convertir el nombre del método a su equivalente en OpenCV

    # Aplicar el Template Matching
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # Si el método es TM_SQDIFF o TM_SQDIFF_NORMED, se toma el mínimo
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img, top_left, bottom_right, 255, 2)  # Dibujar un rectángulo en la imagen original

    plt.subplot(121), plt.imshow(res, cmap='gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img, cmap='gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)  # Agregar el título del método
    plt.show()
