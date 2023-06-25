import cv2
import mediapipe as mp
import serial # Configurar la comunicación serial
ser = serial.Serial('COM1', baudrate=9600)  # Reemplaza 'puerto_serial' con el puerto COM correspondiente
cap = cv2.VideoCapture(0)
mp_Hands = mp.solutions.hands
hands = mp_Hands.Hands()
mpDraw = mp.solutions.drawing_utils
finger_coord = [(8, 6), (12, 10), (16, 14), (20, 18)]
thumb_coord = (4, 2)
while True:
    success, image = cap.read()
    RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(RGB_image)
    multiLandmarks = results.multi_hand_landmarks
    if multiLandmarks:
        handList = []
        for handLms in multiLandmarks:
            mpDraw.draw_landmarks(image, handLms, mp_Hands.HAND_CONNECTIONS)
            for idx, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                handList.append((cx, cy))
        for point in handList:
            cv2.circle(image, point, 10, (255, 255, 0), cv2.FILLED)
        upCount = 0
        for coordinate in finger_coord:
            if handList[coordinate[0]][1] < handList[coordinate[1]][1]:
                upCount += 1
        if handList[thumb_coord[0]][0] > handList[thumb_coord[1]][0]:
            upCount += 1
        cv2.putText(image, str(upCount), (150, 150), cv2.FONT_HERSHEY_PLAIN, 12, (0, 255, 0), 12)
        cv2.imshow("Contando", image)
        # Enviar el conteo a través de la comunicación serial
        ser.write(str(upCount).encode())
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Cerrar la comunicación serial y liberar recursos
ser.close()
cap.release()
cv2.destroyAllWindows()
