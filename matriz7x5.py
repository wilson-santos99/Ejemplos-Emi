import serial
import serial.tools.list_ports
import tkinter as tk

# Configuración de Arduino
arduino_port = None
baudrate = 9600
led_matrix = [[0] * 5 for _ in range(7)]

# Función para conectar al puerto serial
def conectar():
    global arduino_port
    try:
        arduino_port = serial.Serial(port=combo_ports.get(), baudrate=int(combo_baudrate.get()))
        desconectar_button.config(state=tk.NORMAL)
        conectar_button.config(state=tk.DISABLED)
        for row in range(7):
            for col in range(5):
                led_buttons[row][col].config(state=tk.NORMAL)
    except serial.SerialException:
        print("Error al conectar al puerto serial.")

# Función para desconectar del puerto serial
def desconectar():
    global arduino_port
    try:
        arduino_port.close()
        desconectar_button.config(state=tk.DISABLED)
        conectar_button.config(state=tk.NORMAL)
        for row in range(7):
            for col in range(5):
                led_buttons[row][col].config(state=tk.DISABLED)
    except serial.SerialException:
        print("Error al desconectar el puerto serial.")

# Función para enviar los datos de la matriz LED a Arduino
def enviar_datos():
    global arduino_port, led_matrix
    if arduino_port is not None and arduino_port.is_open:
        data = ""
        for row in range(7):
            for col in range(5):
                data += str(led_matrix[row][col])
        arduino_port.write(data.encode())

# Función para cambiar el estado de un LED en la matriz
def cambiar_estado(row, col):
    led_matrix[row][col] = 1 - led_matrix[row][col]
    if led_matrix[row][col] == 1:
        led_buttons[row][col].config(bg="red")
    else:
        led_buttons[row][col].config(bg="white")
    enviar_datos()

# Crear la ventana principal
window = tk.Tk()
window.title("Matriz LED 7x5")

# Crear los widgets de la interfaz
label_ports = tk.Label(window, text="Puertos seriales:")
label_ports.grid(row=0, column=0, sticky=tk.W)

ports = [port.device for port in serial.tools.list_ports.comports()]
combo_ports = tk.StringVar(window)
combo_ports.set(ports[0] if ports else "")
combo_ports_dropdown = tk.OptionMenu(window, combo_ports, *ports)
combo_ports_dropdown.grid(row=0, column=1, padx=5, pady=5)

label_baudrate = tk.Label(window, text="Baudrate:")
label_baudrate.grid(row=1, column=0, sticky=tk.W)

baudrates = ["9600", "19200", "38400", "57600", "115200"]
combo_baudrate = tk.StringVar(window)
combo_baudrate.set(baudrates[0])
combo_baudrate_dropdown = tk.OptionMenu(window, combo_baudrate, *baudrates)
combo_baudrate_dropdown.grid(row=1, column=1, padx=5, pady=5)

conectar_button = tk.Button(window, text="Conectar", command=conectar)
conectar_button.grid(row=2, column=0, padx=5, pady=5)

desconectar_button = tk.Button(window, text="Desconectar", command=desconectar, state=tk.DISABLED)
desconectar_button.grid(row=2, column=1, padx=5, pady=5)

led_buttons = []
for row in range(7):
    row_buttons = []
    for col in range(5):
        button = tk.Button(window, width=2, state=tk.DISABLED,
                          command=lambda r=row, c=col: cambiar_estado(r, c))
        button.grid(row=row+3, column=col+2, padx=2, pady=2)
        row_buttons.append(button)
    led_buttons.append(row_buttons)

# Iniciar el bucle principal de la ventana
window.mainloop()