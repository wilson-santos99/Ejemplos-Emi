import serial
import matplotlib.pyplot as plt
from drawnow import *
import tkinter as tk

# Crear lista vacía para almacenar los valores de temperatura
temperaturas = []
# Crear función que generará la gráfica en tiempo real
def plot_temperature():
    plt.title('Temperatura en tiempo real')
    plt.ylabel('Temperatura (°C)')
    plt.plot(temperaturas, 'ro-', label='Temperatura')
    plt.legend(loc='upper left')

# Crear función que lee los datos del puerto serial
def read_serial():
    # Abrir puerto serial
    ser = serial.Serial('COM3', 9600)
    # Leer datos del puerto serial
    while True:
        # Leer una línea del puerto serial y convertirla a string
        data = ser.readline().decode().strip()
        #print("los datos recibidos son: "+str(data))
        # Separar los valores de temperatura y humedad
        temperature, humidity = data.split(',')
        # Convertir la temperatura a float y agregarla a la lista de temperaturas
        temperaturas.append(float(temperature))
        # Generar la gráfica en tiempo real
        drawnow(plot_temperature)

# Crear función principal del programa
def main():
    # Crear ventana de Tkinter
    #root = tk.Tk()
    #root.title('Temperatura en tiempo real')
    # Ejecutar función para leer datos del puerto serial
    read_serial()
    # Ejecutar loop principal de Tkinter
    #root.mainloop()

# Ejecutar función principal del programa
if __name__ == '__main__':
    main()