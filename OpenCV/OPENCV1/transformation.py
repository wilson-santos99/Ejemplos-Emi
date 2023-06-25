import cv2 as cv  # Importar el módulo cv2 y asignarle el alias "cv"
import numpy as np

img = cv.imread('C:\\Users\\santo\\Documents\\GitHub\\Ejemplos-Emi\\OpenCV\\OPENCV1\\Photos\\park.jpg')  # Leer la imagen especificada y asignarla a la variable "img"

cv.imshow('Boston', img)  # Mostrar la imagen en una ventana titulada "Boston"

# Traslación
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])  # Crear una matriz de transformación para la traslación
    dimensions = (img.shape[1], img.shape[0])  # Obtener las dimensiones de la imagen
    return cv.warpAffine(img, transMat, dimensions)  # Aplicar la traslación a la imagen utilizando la matriz de transformación

# -x --> Izquierda
# -y --> Arriba
# x --> Derecha
# y --> Abajo

translated = translate(img, 100, 100)  # Llamar a la función "translate" pasando la imagen "img" y las coordenadas de traslación (100, 100) como argumentos, y asignar el resultado a la variable "translated"
cv.imshow('Translated', translated)  # Mostrar la imagen trasladada en una ventana titulada "Translated"

# Rotación
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]  # Obtener la altura y el ancho de la imagen

    if rotPoint is None:
        rotPoint = (width//2, height//2)  # Si no se especifica un punto de rotación, utilizar el punto central de la imagen

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)  # Obtener la matriz de rotación utilizando el punto de rotación y el ángulo de rotación
    dimensions = (width, height)  # Obtener las dimensiones de la imagen

    return cv.warpAffine(img, rotMat, dimensions)  # Aplicar la rotación a la imagen utilizando la matriz de rotación

rotated = rotate(img, -45)  # Llamar a la función "rotate" pasando la imagen "img" y el ángulo de rotación (-45) como argumentos, y asignar el resultado a la variable "rotated"
cv.imshow('Rotated', rotated)  # Mostrar la imagen rotada en una ventana titulada "Rotated"

rotated_rotated = rotate(img, 90)  # Llamar a la función "rotate" pasando la imagen "img" y el ángulo de rotación (90) como argumentos, y asignar el resultado a la variable "rotated_rotated"
cv.imshow('Rotated_Rotated', rotated_rotated)  # Mostrar la imagen rotada nuevamente en una ventana titulada "Rotated_Rotated"

# Redimensionamiento
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)  # Redimensionar la imagen a un tamaño de 500x500 utilizando la interpolación cúbica
cv.imshow('Risized', resized)  # Mostrar la imagen redimensionada en una ventana titulada "Risized"

# Volteo
flip = cv.flip(img, 0)  # Voltear la imagen verticalmente utilizando el código 0
cv.imshow('Flip', flip)  # Mostrar la imagen volteada en una ventana titulada "Flip"

# Recorte
cropped = img[200:400, 300:400]  # Recortar un área rectangular de la imagen
cv.imshow('Cropped', cropped)  # Mostrar el área recortada en una ventana titulada "Cropped"

cv.waitKey(0)  # Esperar hasta que se presione una tecla para cerrar todas las ventanas
