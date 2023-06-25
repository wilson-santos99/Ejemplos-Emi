import tkinter as tk
import serial

# Definir el puerto y la velocidad de baudios para la conexión serial
puerto = serial.Serial('COM3', 9600)

# Funciones para encender y apagar el LED
def encender():
    puerto.write('1'.encode())
def apagar():
    puerto.write('0'.encode())

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Control de LED con Arduino")

# Crear el botón de encender y colocarlo en la rejilla
boton_encender = tk.Button(ventana, text="Encender", command=encender)
boton_encender.grid(row=0, column=0)

# Crear el botón de apagar y colocarlo en la rejilla
boton_apagar = tk.Button(ventana, text="Apagar", command=apagar)
boton_apagar.grid(row=0, column=1)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()

# Cerrar el puerto serial al salir de la aplicación
puerto.close()
