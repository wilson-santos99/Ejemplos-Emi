import cv2 as cv  # Importar el módulo cv2 y asignarle el alias "cv"
import numpy as np  # Importar el módulo numpy y asignarle el alias "np"

blank = np.zeros((500,500,3), dtype='uint8')  # Crear una imagen en blanco de tamaño 500x500 con 3 canales de color (RGB) y tipo de datos uint8 (valores entre 0 y 255) y asignarla a la variable "blank"
cv.imshow('Blank', blank)  # Mostrar la imagen en blanco en una ventana titulada "Blank"

# 1. Pintar la imagen de un color determinado
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('Green', blank)

# 2. Dibujar un rectángulo
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)  # Dibujar un rectángulo en la imagen "blank" desde el punto (0,0) hasta la mitad del ancho y la mitad de la altura de la imagen, con color verde y grosor -1 (llenar completamente)
cv.imshow('Rectangle', blank)  # Mostrar la imagen con el rectángulo dibujado en una ventana titulada "Rectangle"

# 3. Dibujar un círculo
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)  # Dibujar un círculo en la imagen "blank" con centro en la mitad del ancho y la mitad de la altura de la imagen, radio de 40 píxeles, color rojo y grosor -1 (llenar completamente)
cv.imshow('Circle', blank)  # Mostrar la imagen con el círculo dibujado en una ventana titulada "Circle"

# 4. Dibujar una línea
cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)  # Dibujar una línea en la imagen "blank" desde el punto (100,250) hasta el punto (300,400), con color blanco y grosor 3
cv.imshow('Line', blank)  # Mostrar la imagen con la línea dibujada en una ventana titulada "Line"

# 5. Escribir texto
cv.putText(blank, 'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)  # Escribir el texto "Hello" en la imagen "blank" en la posición (255,255) utilizando la fuente FONT_HERSHEY_TRIPLEX, tamaño de fuente 1.0, color verde y grosor 2
cv.imshow('Text', blank)  # Mostrar la imagen con el texto escrito en una ventana titulada "Text"

cv.waitKey(0)  # Esperar hasta que se presione una tecla para cerrar todas las ventanas
