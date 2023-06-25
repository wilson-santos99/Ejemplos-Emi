import cv2
import mediapipe as mp

def detectar_dedos():
    cap = cv2.VideoCapture(0)  # Iniciar la captura de video desde la cámara

    # Inicializar la detección de manos
    mp_dedos = mp.solutions.hands.Hands()

    while True:
        ret, frame = cap.read()  # Leer un frame de video

        # Convertir el frame de BGR a RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detectar manos en el frame
        resultados = mp_dedos.process(frame_rgb)

        # Comprobar si se detectaron manos
        if resultados.multi_hand_landmarks:
            for mano in resultados.multi_hand_landmarks:
                # Contar los dedos levantados
                dedos_levantados = 0
                for dedo in mano.landmark[1:]:
                    # Comprobar si el dedo está levantado
                    if dedo.y < mano.landmark[0].y:
                        dedos_levantados += 1

                # Mostrar la cantidad de dedos levantados en pantalla
                cv2.putText(frame, f'Dedos: {dedos_levantados}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Mostrar el frame en una ventana
        cv2.imshow('Detector de dedos', frame)

        # Salir si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

detectar_dedos()
