import cv2  # Importar la biblioteca OpenCV
import numpy as np  # Importar la biblioteca NumPy para el procesamiento de imágenes

webcam_id = 0  # ID de la cámara web a utilizar
cap = cv2.VideoCapture(webcam_id)  # Crear un objeto VideoCapture para capturar los fotogramas de la cámara

# Umbrales del detector de bordes Canny
threshold_one =100  # Primer umbral
threshold_two = 200  # Segundo umbral
aperture_size = 3  # Tamaño del apertura

while(cap.isOpened()):  # Bucle principal para capturar los fotogramas
    # Capturar el fotograma
    ret, frame = cap.read()
    if ret == True:
        # Operaciones en el fotograma
        edges = cv2.Canny(frame, threshold_one, threshold_two, aperture_size)  # Aplicar el detector de bordes Canny al fotograma
        
        # Mostrar las imágenes en ventanas separadas
        cv2.imshow("Canny edge detection", edges)  # Mostrar los bordes detectados por el algoritmo de Canny en una ventana llamada "Canny edge detection"
        cv2.imshow("Original",frame)
        count="hola"
        cv2.putText(frame, str(count), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 5)
        # Salir del bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Liberar los recursos y cerrar las ventanas al finalizar
cap.release()  # Liberar el objeto VideoCapture
cv2.destroyAllWindows()  # Cerrar todas las ventanas abiertas por OpenCV
