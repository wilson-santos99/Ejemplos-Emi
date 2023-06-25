import tkinter as tk
import subprocess
from tkinter import ttk
login = tk.Tk()
texto = tk.Label(login, text="Usuario")
texto.pack()
entradausuario=tk.Entry(login)
entradausuario.pack()
texto1 = tk.Label(login, text="Contraseña")
texto1.pack()
entradacontrasena=tk.Entry(login,show="*")
entradacontrasena.pack()

def iniciarsesion():
    print("INICIANDO SESION")
    usuario1=entradausuario.get()
    contrasena1=entradacontrasena.get() ##debe de ocultarse
    print("el usuario es: "+str(usuario1))
    print("la contraseña es: "+str(contrasena1)) #
    #usuario = animal  contraseña=gato
    #si usuario es animal y contraseña es gato ===== inicia sesión
    if(usuario1=="animal" and contrasena1=="gato"):
        print("Inicio sesión correctamente") 
       
        ventana2 = tk.Toplevel(login)
        ventana2.title("Ventana 2")
        puertos_disponibles = ['COM1','COM2','COM3','COM4','COM5']

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
        login.withdraw()
        
    else:
        print("datos incorrectos")
def conectar_serial(ventana, puerto, baudrate):
    # Aquí puedes utilizar el puerto y baudrate seleccionados para establecer la conexión serial

    # Cerrar la ventana y ejecutar el script externo
    ventana.destroy()
    subprocess.call(["python", "final.py"])

aceptar =tk.Button(login,text="Iniciar Sesion",command=iniciarsesion)
aceptar.pack()
login.mainloop() #permite mostrar la ventana