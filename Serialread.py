import serial

# Establece la configuración del puerto serial
puerto = 'COM3'  # Reemplaza esto con el nombre de tu puerto serial (por ejemplo, 'COM3' en Windows)
baudios = 9600

# Inicia la comunicación serial
arduino = serial.Serial(puerto, baudios)


# Lee la línea recibida desde Arduino y la decodifica
linea = arduino.readline().decode('utf-8').rstrip()
print(linea)  # Muestra la línea en la consola

