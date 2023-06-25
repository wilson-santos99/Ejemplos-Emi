import cv2
import sys

# Cargar los clasificadores XML
cas_path = "C:\\Users\\santo\\Documents\\GitHub\\Ejemplos-Emi\\OpenCV\\haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cas_path)

# Configurar la cámara web
webcam_id = 0
video_capture = cv2.VideoCapture(webcam_id)

# Bandera para la detección multi-escala
if cv2.__version__.startswith('2.4'):
    dmf_flag = cv2.cv.CV_HAAR_SCALE_IMAGE
else:
    dmf_flag = cv2.CASCADE_SCALE_IMAGE

while True:
    # Capturar frame por frame
    ret, frame = video_capture.read()

    # Convertir la imagen a escala de grises
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar caras
    faces = face_cascade.detectMultiScale(
        gray_image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=dmf_flag
    )

    # Dibujar un rectángulo alrededor de las caras detectadas
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Mostrar el frame resultante
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cuando se finalice, liberar la cámara
video_capture.release()
cv2.destroyAllWindows()
