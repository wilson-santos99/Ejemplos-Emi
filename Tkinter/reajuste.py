import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        x = int(entry.get())
        resultado = (65 * 115 - x * 115) / x
        if resultado <= 0:
            messagebox.showinfo("Resultado", "¡Felicidades! No se paga reajuste.")
        else:
            messagebox.showinfo("Resultado", f"El resultado es: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número entero válido.")

# Crear la ventana
window = tk.Tk()
window.title("Calculadora")
window.geometry("300x150")

# Crear los elementos de la interfaz
label = tk.Label(window, text="Ingrese el valor de x:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Calcular", command=calcular)
button.pack()

# Ejecutar la ventana
window.mainloop()
