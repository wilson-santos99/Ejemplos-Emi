import serial
import matplotlib.pyplot as plt
from drawnow import *
import tkinter as tk

# Crear lista vacía para almacenar los valores de temperatura
temperaturas = []
humedad=[]
distancia=[]

# Crear función que generará la gráfica en tiempo real
def plot_temperature():
    plt.figure()
    plt.title('Temperatura en tiempo real')
    plt.ylabel('Temperatura (°C)')
    plt.plot(temperaturas, 'ro-', label='Temperatura')
    plt.legend(loc='upper left')
    plt.figure()
    plt.title('Humedad en tiempo real')
    plt.ylabel('Humedad (%)')
    plt.plot(humedad, 'H-', label='Humead')
    plt.legend(loc='upper left')
    plt.figure()
    plt.title('Distancia en tiempo real')
    plt.ylabel('Distancia (cm)')
    plt.plot(distancia, 'H-', label='Distancia')
    plt.legend(loc='upper left')


# Crear función que lee los datos del puerto serial
def read_serial():
    # Abrir puerto serial
    ser = serial.Serial('COM3', 9600)
    
    # Leer datos del puerto serial
    while True:
        # Leer una línea del puerto serial y convertirla a string
        data = ser.readline().decode().strip()
        print("los datos recibidos son: "+str(data))
        # Separar los valores de temperatura y humedad
        datos = data.split(',')
        print("datos separados: "+str(datos))
        #dato=[] 6 datos
        temperature=datos[0]
        humidity=datos[1]
        sensor=datos[2]
        print("temperatura : "+str(temperature))
        print("humedad: "+str(humidity))
        print("Distancia es: "+str(sensor)+" Cm")
        # Convertir la temperatura a float y agregarla a la lista de temperaturas
        temperaturas.append(float(temperature))
        humedad.append(float(humidity))
        distancia.append(float(sensor))
        # Generar la gráfica en tiempo real
        drawnow(plot_temperature)
        drawnow(plot_temperature)
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