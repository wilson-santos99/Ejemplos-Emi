import tkinter as tk #
ventana = tk.Tk()


def saludar():
    print("¡Hola, mundo!")


boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()
ventana.mainloop() 