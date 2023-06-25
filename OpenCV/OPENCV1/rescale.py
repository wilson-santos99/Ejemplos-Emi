import cv2 as cv  # Importar el módulo cv2 y asignarle el alias "cv"


def rescaleFrame(frame, scale=0.75):
    # Escalar imágenes, videos y videos en vivo
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # Cambiar la resolución del video en vivo
    capture.set(3, width)
    capture.set(4, height)


# Leyendo videos
capture = cv.VideoCapture('C:\\Users\\santo\\Documents\\GitHub\\Ejemplos-Emi\\OpenCV\\OPENCV1\\Videos\\dog.mp4')  # Abrir el archivo de video especificado y asignarlo a la variable "capture"

while True:
    isTrue, frame = capture.read()  # Leer un fotograma del video y asignar el resultado a la variable "frame", y el resultado de la operación a la variable "isTrue"

    frame_resized = rescaleFrame(frame, scale=0.2)  # Redimensionar el fotograma utilizando la función "rescaleFrame" y asignar el resultado a la variable "frame_resized"

    cv.imshow('Video', frame)  # Mostrar el fotograma original en una ventana titulada "Video"
    cv.imshow('Video Resized', frame_resized)  # Mostrar el fotograma redimensionado en una ventana titulada "Video Resized"

    if cv.waitKey(20) & 0xFF == ord('d'):  # Esperar 20 milisegundos para verificar si se presionó la tecla 'd' para detener el bucle
        break

capture.release()  # Liberar el recurso del archivo de video
cv.destroyAllWindows()  # Cerrar todas las ventanas
