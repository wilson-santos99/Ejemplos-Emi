import cv2 as cv  # Importar el módulo cv2 y asignarle el alias "cv"

img = cv.imread('C:\\Users\\santo\\Documents\\GitHub\\Ejemplos-Emi\\OpenCV\\OPENCV1\\Photos\\park.jpg')  # Leer la imagen especificada y asignarla a la variable "img"

cv.imshow('Park', img)  # Mostrar la imagen en una ventana titulada "Park"


# Convertir a escala de grises
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # Convertir la imagen a escala de grises y asignarla a la variable "gray"
cv.imshow('Gray', gray)  # Mostrar la imagen en escala de grises en una ventana titulada "Gray"

# Desenfoque
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)  # Aplicar un desenfoque gaussiano a la imagen y asignarla a la variable "blur"
cv.imshow('Blur', blur)  # Mostrar la imagen desenfocada en una ventana titulada "Blur"

# Detección de bordes
canny = cv.Canny(blur, 125, 175)  # Aplicar el algoritmo Canny para detectar bordes en la imagen desenfocada y asignar el resultado a la variable "canny"
cv.imshow('Canny Edges', canny)  # Mostrar los bordes detectados en una ventana titulada "Canny Edges"

# Dilatar la imagen
dilated = cv.dilate(canny, (7,7), iterations=3)  # Dilatar la imagen con un kernel de 7x7 y 3 iteraciones, y asignar el resultado a la variable "dilated"
cv.imshow('Dilated', dilated)  # Mostrar la imagen dilatada en una ventana titulada "Dilated"

# Erosionar
eroded = cv.erode(dilated, (7,7), iterations=3)  # Erosionar la imagen dilatada con un kernel de 7x7 y 3 iteraciones, y asignar el resultado a la variable "eroded"
cv.imshow('Eroded', eroded)  # Mostrar la imagen erosionada en una ventana titulada "Eroded"

# Cambiar tamaño
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)  # Cambiar el tamaño de la imagen a 500x500 utilizando la interpolación cúbica, y asignar el resultado a la variable "resized"
cv.imshow('Resized', resized)  # Mostrar la imagen redimensionada en una ventana titulada "Resized"

# Recortar
cropped = img[50:200, 200:400]  # Recortar una región de interés (ROI) de la imagen y asignarla a la variable "cropped"
cv.imshow('Cropped', cropped)  # Mostrar la imagen recortada en una ventana titulada "Cropped"

cv.waitKey(0)  # Esperar hasta que se presione una tecla para cerrar todas las ventanas
