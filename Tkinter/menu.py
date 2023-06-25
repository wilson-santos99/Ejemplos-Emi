import tkinter as tk
ventana = tk.Tk()

def hacer_algo():
    print("¡Se hizo algo!")

menu = tk.Menu(ventana)

menu_archivo = tk.Menu(menu, tearoff=0)
menu_archivo.add_command(label="Abrir")
menu_archivo.add_command(label="Guardar")
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.quit)
menu.add_cascade(label="Archivo", menu=menu_archivo)

menu_edicion = tk.Menu(menu, tearoff=0)
menu_edicion.add_command(label="Cortar")
menu_edicion.add_command(label="Copiar")
menu_edicion.add_command(label="Pegar")
menu_edicion.add_separator() 
menu_edicion.add_command(label="Hacer algo", command=hacer_algo)
menu.add_cascade(label="Edición", menu=menu_edicion)

ventana.config(menu=menu)

ventana.mainloop() 