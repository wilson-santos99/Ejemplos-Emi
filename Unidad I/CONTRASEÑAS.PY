import tkinter as tk

def get_password():
    password = entry.get()
    print("Contraseña ingresada:", password)

root = tk.Tk()

label = tk.Label(root, text="Contraseña:")
label.pack()

entry = tk.Entry(root, show="*")
entry.pack()

button = tk.Button(root, text="Ingresar", command=get_password)
button.pack()

root.mainloop()