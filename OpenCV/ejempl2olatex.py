import cv2
import numpy
import os

# Importar los módulos necesarios: cv2 para OpenCV, numpy para trabajar con arreglos y os para operaciones del sistema operativo.

# Crear un array de 120,000 bytes aleatorios.
random_byte_array = bytearray(os.urandom(120000))
# La función os.urandom() genera una secuencia de bytes aleatorios del tamaño especificado y se almacena en el bytearray random_byte_array.

flat_numpy_array = numpy.array(random_byte_array)
# El bytearray random_byte_array se convierte en un objeto numpy.array llamado flat_numpy_array.

# Convertir el array en una imagen en escala de grises de 400x300.
gray_image = flat_numpy_array.reshape(300, 400)
# La función reshape() se utiliza para cambiar la forma del array numpy. En este caso, se cambia a una matriz de 300 filas y 400 columnas, lo que representa una imagen en escala de grises de tamaño 400x300 píxeles.

cv2.imshow('Imagen en escala de grises aleatoria', gray_image)
# La función cv2.imshow() muestra la imagen en una ventana con el nombre especificado. En este caso, se muestra la imagen en escala de grises con el nombre 'Imagen en escala de grises aleatoria'.

# Convertir el array en una imagen en color de 400x100.
bgr_image = flat_numpy_array.reshape(100, 400, 3)
# Similar al paso anterior, se cambia la forma del array numpy a una matriz de 100 filas, 400 columnas y 3 canales de color (BGR), representando así una imagen en color de tamaño 400x100 píxeles.

cv2.imshow('Imagen en color aleatoria', bgr_image)
# Se muestra la imagen en color en una ventana con el nombre 'Imagen en color aleatoria'.

cv2.waitKey(0)
# La función cv2.waitKey() espera hasta que se presione una tecla en la ventana abierta. En este caso, se espera hasta que se presione cualquier tecla.

cv2.destroyAllWindows()
# La función cv2.destroyAllWindows() cierra todas las ventanas abiertas.
