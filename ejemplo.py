import tkinter as tk
import serial.tools.list_ports
import subprocess

def abrir_ventana2():
    ventana2 = tk.Toplevel(ventana1)
    ventana2.title("Ventana 2")

    puertos_disponibles = [port.device for port in serial.tools.list_ports.comports()]

    puerto_label = tk.Label(ventana2, text="Puerto:")
    puerto_label.pack()

    puerto_combobox = tk.ttk.Combobox(ventana2, values=puertos_disponibles)
    puerto_combobox.pack()

    baudrate_label = tk.Label(ventana2, text="Baudrate:")
    baudrate_label.pack()

    baudrate_combobox = tk.ttk.Combobox(ventana2, values=[9600, 115200, 230400])
    baudrate_combobox.pack()

    conectar_button = tk.Button(ventana2, text="Conectar", command=lambda: conectar_serial(ventana2, puerto_combobox.get(), baudrate_combobox.get()))
    conectar_button.pack()

def conectar_serial(ventana, puerto, baudrate):
    # Aquí puedes utilizar el puerto y baudrate seleccionados para establecer la conexión serial

    # Cerrar la ventana y ejecutar el script externo
    ventana.destroy()
    subprocess.call(["python", "script_externo.py"])

ventana1 = tk.Tk()
ventana1.title("Ventana 1")

button1 = tk.Button(ventana1, text="Button 1", command=abrir_ventana2)
button1.pack()

ventana1.mainloop()
