import cv2 as cv  # Importar el módulo cv2 y asignarle el alias "cv"

img = cv.imread('C:\\Users\\santo\\Documents\\GitHub\\Ejemplos-Emi\\OpenCV\\OPENCV1\\Photos\\park.jpg')  # Leer la imagen especificada y asignarla a la variable "img"

cv.imshow('Park', img)  # Mostrar la imagen en una ventana titulada "Park"

# Convertir a escala de grises
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Desenfoque
def blur(img):
    blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)  # Aplicar un desenfoque gaussiano a la imagen utilizando un kernel de 7x7 y un borde predeterminado
    cv.imshow('Blur', blur)  # Mostrar la imagen desenfocada en una ventana titulada "Blur"

show = blur(img)  # Llamar a la función "blur" pasando la imagen "img" como argumento y asignar el resultado a la variable "show"

cv.waitKey(0)  # Esperar hasta que se presione una tecla para cerrar todas las ventanas
