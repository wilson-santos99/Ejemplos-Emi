import cv2
import sys

# Cargar los clasificadores XML para detección de caras y ojos
cas_path = "C:\\Users\\santo\\Documents\\GitHub\\Ejemplos-Emi\\OpenCV\\haarcascade_frontalface_default.xml"
eye_path = "C:\\Users\\santo\\Documents\\GitHub\\Ejemplos-Emi\\OpenCV\\haarcascade_eye.xml"
face_cascade = cv2.CascadeClassifier(cas_path)  # Clasificador de detección de caras
eye_cascade = cv2.CascadeClassifier(eye_path)  # Clasificador de detección de ojos

# Configurar la cámara web
webcam_id = 0
video_capture = cv2.VideoCapture(webcam_id)

# Bandera para la detección multi-escala
if cv2.__version__.startswith('2.4'):
    dmf_flag = cv2.cv.CV_HAAR_SCALE_IMAGE  # Bandera para la detección multi-escala (compatibilidad con OpenCV 2.4)
else:
    dmf_flag = cv2.CASCADE_SCALE_IMAGE  # Bandera para la detección multi-escala (OpenCV 3.x y versiones posteriores)

while True:
    # Capturar frame por frame desde la cámara
    ret, frame = video_capture.read()

    # Convertir la imagen a escala de grises
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar caras en la imagen
    faces = face_cascade.detectMultiScale(
        gray_image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=dmf_flag
    )

    # Dibujar un rectángulo alrededor de las caras detectadas
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Extraer la región de interés (ROI) de la cara para la detección de ojos
        roi_gray = gray_image[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # Detectar ojos en la región de interés
        eyes = eye_cascade.detectMultiScale(roi_gray)

        # Dibujar un rectángulo alrededor de los ojos detectados
        for (ex, ey, ew, eh) in eyes:                         #  R  G   B
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,0,0), 2)

    # Mostrar el frame resultante con las caras y ojos detectados
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Esperar por la tecla 'q' para salir del bucle
        break

# Liberar la captura de la cámara y cerrar las ventanas abiertas
video_capture.release()
cv2.destroyAllWindows()
