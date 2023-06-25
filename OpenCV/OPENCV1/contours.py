import cv2 as cv  # Importar el módulo cv2 y asignarle el alias "cv"
import numpy as np  # Importar el módulo numpy y asignarle el alias "np"

img = cv.imread('C:\\Users\\santo\\Documents\\GitHub\\Ejemplos-Emi\\OpenCV\\OPENCV1\\Photos\\cats.jpg')  # Leer la imagen especificada y asignarla a la variable "img"
cv.imshow('Cats', img)  # Mostrar la imagen en una ventana titulada "Cats"

blank = np.zeros(img.shape, dtype='uint8')  # Crear una imagen en blanco del mismo tamaño que "img" y con tipo de datos uint8 (valores entre 0 y 255) y asignarla a la variable "blank"
cv.imshow('Blank', blank)  # Mostrar la imagen en blanco en una ventana titulada "Blank"

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # Convertir la imagen a escala de grises y asignarla a la variable "gray"
cv.imshow('Gray', gray)  # Mostrar la imagen en escala de grises en una ventana titulada "Gray"

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)  # Aplicar un desenfoque gaussiano a la imagen en escala de grises y asignarla a la variable "blur"
cv.imshow('Blur', blur)  # Mostrar la imagen desenfocada en una ventana titulada "Blur"

canny = cv.Canny(blur, 125, 125)  # Aplicar el algoritmo Canny para detectar bordes en la imagen desenfocada y asignar el resultado a la variable "canny"
cv.imshow('Canny', canny)  # Mostrar los bordes detectados en una ventana titulada "Canny"

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)  # Encontrar contornos en la imagen de bordes utilizando el método RETR_LIST y sin aproximar los contornos, y asignar los contornos encontrados a la variable "contours" y las jerarquías a la variable "hierarchies"
print(f'{len(contours)} contour(s) found!')  # Imprimir el número de contornos encontrados

cv.drawContours(blank, contours, -1, (0,0,255), 1)  # Dibujar todos los contornos encontrados en la imagen en blanco utilizando el color rojo y un grosor de 1 píxel
cv.imshow('Contours Drawn', blank)  # Mostrar la imagen con los contornos dibujados en una ventana titulada "Contours Drawn"

cv.waitKey(0)  # Esperar hasta que se presione una tecla para cerrar todas las ventanas
