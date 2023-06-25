#Captura de vídeo desde la webcam
import numpy as np  # Importar la biblioteca numpy para el manejo de arrays
import cv2  # Importar la biblioteca OpenCV para el procesamiento de imágenes y videos

webcam_id = 0  # Identificador de la webcam a capturar (0 por defecto)
cap = cv2.VideoCapture(webcam_id)  # Crear un objeto de tipo VideoCapture para capturar desde la webcam

while(cap.isOpened()):  # Bucle principal para leer y procesar cada fotograma de la webcam
    ret, frame = cap.read()  # Leer un fotograma de la webcam. La variable 'ret' indica si la lectura fue exitosa

    if ret == True:  # Si la lectura del fotograma fue exitosa
        v_frame = cv2.flip(frame, 1)  # Voltear el fotograma verticalmente
        h_frame = cv2.flip(frame, 0)  # Voltear el fotograma horizontalmente

        cv2.imshow("Original", frame)  # Mostrar el fotograma original en una ventana con el título "Original"
        cv2.imshow("Vertical flip", v_frame)  # Mostrar el fotograma volteado verticalmente
        cv2.imshow("Horizontal flip", h_frame)  # Mostrar el fotograma volteado horizontalmente

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Esperar por la tecla 'q' para salir del bucle
            break
    else:
        break

cap.release()  # Liberar los recursos utilizados para la captura de la webcam
cv2.destroyAllWindows()  # Cerrar todas las ventanas abiertas por OpenCV
