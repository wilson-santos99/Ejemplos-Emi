import numpy as np  # Importar la biblioteca numpy para el manejo de arrays
import cv2  # Importar la biblioteca OpenCV para el procesamiento de imágenes y videos

video_file = 'C:\\Users\\santo\\Documents\\GitHub\\Ejemplos-Emi\\OpenCV\\ejemplo1.mp4'  # Ruta del archivo de video
cap = cv2.VideoCapture(video_file)  # Crear un objeto de tipo VideoCapture para abrir el video
while cap.isOpened():  # Bucle principal para leer y procesar cada fotograma del video
    ret, frame = cap.read()  # Leer un fotograma del video. La variable 'ret' indica si la lectura fue exitosa

    if ret:  # Si la lectura del fotograma fue exitosa
        imagenoriginal=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        cv2.imshow('Original',imagenoriginal)
        colorgris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convertir el fotograma a escala de grises
        cv2.imshow('Ejemplo 1', colorgris)  # Mostrar el fotograma en una ventana con el título 'frame'
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Esperar por la tecla 'q' para salir del bucle
            break

cap.release()  # Liberar los recursos utilizados para la captura del video
cv2.destroyAllWindows()  # Cerrar todas las ventanas abiertas por OpenCV
