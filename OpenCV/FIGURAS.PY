import cv2
import numpy as np
import serial
# Establecer la comunicación serial con Arduino
arduino = serial.Serial('COM1', 9600)  # Ajusta el puerto y la velocidad según tu configuración
# Función para encender el LED correspondiente en Arduino
def encender_led(forma):
    if forma == "cuadro":
        arduino.write(b'1')  # Enviar "1" a Arduino
    elif forma == "triangulo":
        arduino.write(b'2')  # Enviar "2" a Arduino
    elif forma == "hexagono":
        arduino.write(b'3')  # Enviar "3" a Arduino
    elif forma=="Octagono":
        arduino.write(b'4')
    else:
        arduino.write(b'0')  # Enviar "0" a Arduino
# Captura de imagen desde la cámara
cap = cv2.VideoCapture(0)
while True:
    # Capturar un frame
    ret, frame = cap.read()
    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Aplicar detección de bordes utilizando Canny
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    # Realizar detección de contornos

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    
    
    
    # Iterar sobre los contornos detectados
    for contour in contours:
        # Aproximar el contorno a una forma más simple
        approx = cv2.approxPolyDP(contour, 0.03 * cv2.arcLength(contour, True), True)
        # Obtener el número de lados de la forma
        sides = len(approx)

        # Dibujar la forma detectada en la imagen original
        cv2.drawContours(frame, [approx], 0, (255, 0, 0), 2)
        #dibujar la forma detectada en la imagen de escala de grises
        cv2.drawContours(gray, [approx], 0, (0, 255, 0), 2)
        # Determinar el tipo de forma según el número de lados


        if sides == 4:
            forma = "cuadro"

        elif sides == 3:
            forma = "triangulo"

        elif sides == 6:
            forma = "hexagono"
        elif sides==8:
            forma="Octagono"
        else:
            forma = "otro"


        # Encender el LED correspondiente en Arduino
        encender_led(forma)

        # Mostrar el tipo de forma en la imagen
        cv2.putText(frame, forma, (approx.ravel()[0], approx.ravel()[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    
    
    # Mostrar la imagen con las formas detectadas en una ventana
    cv2.imshow("Shapes", frame)
    cv2.imshow('Escala de grises',gray)



    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Liberar la captura y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()
arduino.close()