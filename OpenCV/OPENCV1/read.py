import cv2 as cv  # Importar el módulo cv2 y asignarle el alias "cv"

# Leyendo imágenes
'''img = cv.imread('Photos/cat.jpg')

cv.imshow('Cat', img)

cv.waitKey(0)
'''

# Leyendo videos
capture = cv.VideoCapture('C:\\Users\\santo\\Documents\\GitHub\\Ejemplos-Emi\\OpenCV\\OPENCV1\\Videos\\dog.mp4')  # Abrir el archivo de video especificado y asignarlo a la variable "capture"

while True:
    isTrue, frame = capture.read()  # Leer un fotograma del video y asignar el resultado a la variable "frame", y el resultado de la operación a la variable "isTrue"

    cv.imshow('Video', frame)  # Mostrar el fotograma en una ventana titulada "Video"

    if cv.waitKey(20) & 0xFF == ord('d'):  # Esperar 20 milisegundos para verificar si se presionó la tecla 'd' para detener el bucle
        break

capture.release()  # Liberar el recurso del archivo de video
cv.destroyAllWindows()  # Cerrar todas las ventanas
