import tkinter as tk
import serial
import serial.tools.list_ports
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
from tkinter import ttk

# Variables globales
puerto_seleccionado = None
baudrate_seleccionado = None
credenciales = {"usuario": "admin", "contraseña": "password"}
puerto_serial = None

# Función para verificar las credenciales ingresadas
def verificar_credenciales():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    if usuario == credenciales["usuario"] and contraseña == credenciales["contraseña"]:
        ventana_login.destroy() # Cerrar la ventana de login
    else:
        label_error.config(text="Credenciales incorrectas") # Mostrar mensaje de error

# Función para actualizar la lista de puertos disponibles
def actualizar_puertos():
    global puerto_seleccionado
    puertos_disponibles = [p.device for p in serial.tools.list_ports.comports()]
    combo_puertos["values"] = puertos_disponibles
    if puerto_seleccionado not in puertos_disponibles:
        puerto_seleccionado = None

# Función para establecer la conexión serial
def establecer_conexion():
    global puerto_seleccionado, baudrate_seleccionado, puerto_serial
    puerto_seleccionado = combo_puertos.get()
    baudrate_seleccionado = combo_baudrate.get()
    try:
        puerto_serial = serial.Serial(puerto_seleccionado, baudrate_seleccionado, timeout=0.1)
    except:
        puerto_serial = None

# Función para actualizar los datos del gráfico
def actualizar_datos(frame):
    global puerto_seleccionado, puerto_serial, datos, ax
    if puerto_seleccionado is not None and puerto_serial is not None:
        try:
            valor = int(puerto_serial.readline().decode().strip())
            datos.append(valor)
            if len(datos) > 50:
                datos.pop(0)
            ax.clear()
            ax.plot(datos)
        except:
            pass

# Crear la ventana de login
ventana_login = tk.Tk()
ventana_login.title("Login")
label_usuario = tk.Label(ventana_login, text="Usuario:")
label_usuario.grid(row=0, column=0, padx=10, pady=10)
entry_usuario = tk.Entry(ventana_login)
entry_usuario.grid(row=0, column=1)
label_contraseña = tk.Label(ventana_login, text="Contraseña:")
label_contraseña.grid(row=1, column=0, padx=10, pady=10)
entry_contraseña = tk.Entry(ventana_login, show="*")
entry_contraseña.grid(row=1, column=1)
button_ingresar = tk.Button(ventana_login, text="Ingresar", command=verificar_credenciales)
button_ingresar.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
label_error = tk.Label(ventana_login, fg="red")
label_error.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Crear la ventana principal
ventana_principal = tk.Tk
# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Potenciómetro")
ventana_principal.rowconfigure(0, weight=1)
ventana_principal.columnconfigure(0, weight=1)

# Crear el gráfico en tiempo real
fig = plt.Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(1, 1, 1)
datos = []
animacion = FuncAnimation(fig, actualizar_datos, interval=100)

# Crear el lienzo del gráfico
canvas = FigureCanvasTkAgg(fig, master=ventana_principal)
canvas.draw()
canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Crear el combobox para seleccionar el puerto COM
label_puerto = tk.Label(ventana_principal, text="Puerto COM:")
label_puerto.grid(row=1, column=0, padx=10, pady=10, sticky="w")
combo_puertos = ttk.Combobox(ventana_principal, state="readonly")
combo_puertos.grid(row=1, column=0, padx=10, pady=10, sticky="e")
actualizar_puertos()
combo_puertos.current(0)

# Crear el combobox para seleccionar el baudrate
label_baudrate = tk.Label(ventana_principal, text="Baudrate:")
label_baudrate.grid(row=2, column=0, padx=10, pady=10, sticky="w")
combo_baudrate = ttk.Combobox(ventana_principal, state="readonly", values=["9600", "115200"])
combo_baudrate.grid(row=2, column=0, padx=10, pady=10, sticky="e")
combo_baudrate.current(0)

# Crear el botón para establecer la conexión serial
button_conectar = tk.Button(ventana_principal, text="Conectar", command=establecer_conexion)
button_conectar.grid(row=3, column=0, padx=10, pady=10)

ventana_principal.mainloop()