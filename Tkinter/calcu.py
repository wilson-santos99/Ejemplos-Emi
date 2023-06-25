#Calculadora basica
'''
Autor: Luis Cadena Campos
Creacion: 22/04/2023
'''


import tkinter as tk
HEIGHT= 5
WIDTH= 1

#Color de fondo 
color_fondo="black"
#Color de los botones 
color_botonNumerico="#6ea7df"
color_hover_botonNumerico = "#8cb5de"
color_botonBorrar="#f34343"
color_hover_botonBorrar="#f56969"
color_raiz2 = "#8b79dd"
color_hover_raiz2="#b3a8e3"
color_elevar2 = "#8b79dd"
color_hover_elevar2 = "#b3a8e3"
color_limpiar = "#8ae5c7"
color_hover_limpiar = "#c8e5dc"
color_punto = "#8b79dd"
color_hover_punto="#b3a8e3"
color_igual = "#90f273"
color_hover_igual = "#baf2aa"
#Color de botones para operaciones
color_suma  = "#ca7bdd"
color_resta = "#ca7bdd"
color_multi = "#ca7bdd"
color_div = "#ca7bdd"
color_hover_operador = "#d2a9db"
#Fuente
fuente_boton = ('Console',9,'bold')


#Creamos la ventana principal
calculadora = tk.Tk()
calculadora.title("Calculadora")
#calculadora.iconbitmap("Teclado.ico")
#Ancho  - Alto
calculadora.geometry("330x460")
calculadora.config(bg=color_fondo)
calculadora.resizable(False,False)


#Creacion del Entry
Entrada =tk.Entry(calculadora,justify='right')
Entrada.grid(row=0,columnspan=4,sticky="we")
Entrada.configure(width=25,font=('Arial',18))


indice = 0
#Obtener numero
def obtener_numero(numero):
    global indice
    indice+=1
    Entrada.insert(indice,numero)
    
#Recibe operadores matematicos ( - , + , x )
def obtener_operacion(operador):
    global indice
    #Obtenemos la longitud del operador, si es que abarca mas
    longitud_operador = len(operador)
    #Lo añadimos al Entry
    Entrada.insert(indice,operador)
    indice+=longitud_operador

#Creamos una funcion para limpiar
def limpiar_entrada():
    Entrada.delete(0,tk.END)

#Funcion para limpiar solo un elementos
def limpiar_un_elemento():
    #Obtenemos el valor actual de la ventana
    estado_entrada = Entrada.get()
    #Tomamos la longitud
    if (len(estado_entrada)):
    #Quito el ultimo numero de la DERECHA
        nuevo_estado_entrada = estado_entrada[:-1]
        limpiar_entrada()
        Entrada.insert(0,nuevo_estado_entrada)
    else:
        limpiar_entrada()
        
#Calcular el estado de la pantalla y hacer la operacion
def operaciones():
        #Obtenemos la expresion que esta en el entry entrada1
        Obtener = Entrada.get()
        try:
            #Con eval, pasamos una cadena de caracteres '3+5', se interpreta como expresion y regresa el resultado '8'
            resultado = eval(Obtener)
            #Llamamos a la funcion limpiar pantalla
            limpiar_entrada()
            #Despues ponemos el resultado '8' en la posicion 0
            Entrada.insert(0,resultado)
        except Exception:
            #En caso de mandar una expresion invalida '*/23' nos regresara un mensaje error en la posicion 0
            limpiar_entrada()
            Entrada.insert(0,'Error')
    



#Creacion de los botones
Boton_Elevar= tk.Button(calculadora,text="x²",command=lambda:obtener_operacion('**2'),height=HEIGHT,width=WIDTH,bg=color_elevar2,font=fuente_boton,activebackground=color_hover_elevar2)
Boton_Elevar.grid(row=1,column=0,sticky="we")
Boton_RaiazCuadrada = tk.Button(calculadora,text="²√",command=lambda:obtener_operacion('**1/2'),height=HEIGHT,width=WIDTH,bg=color_raiz2,activebackground=color_hover_raiz2)
Boton_RaiazCuadrada.grid(row=1,column=1,sticky="we")
Boton_LimpiarTodo   = tk.Button(calculadora,text="C",command=lambda:limpiar_entrada(),height=HEIGHT,width=WIDTH,bg=color_limpiar,activebackground=color_hover_limpiar)
Boton_LimpiarTodo.grid(row=1,column=2,sticky="we")
Boton_BorrarNumero  = tk.Button(calculadora,text="⌫",command=lambda:limpiar_un_elemento(),height=HEIGHT,width=WIDTH,bg=color_botonBorrar,activebackground=color_hover_botonBorrar)
Boton_BorrarNumero.grid(row=1,column=3,sticky="we")

#Botones numericos
Boton7 = tk.Button(calculadora,text="7",command=lambda:obtener_numero(7),height=HEIGHT,width=WIDTH,bg=color_botonNumerico,font=fuente_boton,activebackground=color_hover_botonNumerico)
Boton7.grid(row=2,column=0,sticky="we")
Boton8 = tk.Button(calculadora,text="8",command=lambda:obtener_numero(8),height=HEIGHT,width=WIDTH,bg=color_botonNumerico,font=fuente_boton,activebackground=color_hover_botonNumerico)
Boton8.grid(row=2,column=1,sticky="we")
Boton9 = tk.Button(calculadora,text="9",command=lambda:obtener_numero(9),height=HEIGHT,width=WIDTH,bg=color_botonNumerico,font=fuente_boton,activebackground=color_hover_botonNumerico)
Boton9.grid(row=2,column=2,sticky="we")
BotonDiv = tk.Button(calculadora,text="÷",command=lambda:obtener_operacion('/'),height=HEIGHT,width=WIDTH,bg=color_div,font=fuente_boton,activebackground=color_hover_operador)
BotonDiv.grid(row=2,column=3,sticky="we")

Boton4 = tk.Button(calculadora,text="4",command=lambda:obtener_numero(4),height=HEIGHT,width=WIDTH,bg=color_botonNumerico,font=fuente_boton,activebackground=color_hover_botonNumerico)
Boton4.grid(row=3,column=0,sticky="we")
Boton5 = tk.Button(calculadora,text="5",command=lambda:obtener_numero(5),height=HEIGHT,width=WIDTH,bg=color_botonNumerico,font=fuente_boton,activebackground=color_hover_botonNumerico)
Boton5.grid(row=3,column=1,sticky="we")
Boton6 = tk.Button(calculadora,text="6",command=lambda:obtener_numero(6),height=HEIGHT,width=WIDTH,bg=color_botonNumerico,font=fuente_boton,activebackground=color_hover_botonNumerico)
Boton6.grid(row=3,column=2,sticky="we")
BotonMult = tk.Button(calculadora,text="X",command=lambda:obtener_operacion('*'),height=HEIGHT,width=WIDTH,bg=color_multi,font=fuente_boton,activebackground=color_hover_operador)
BotonMult.grid(row=3,column=3,sticky="we")

Boton1 = tk.Button(calculadora,text="1",command=lambda:obtener_numero(1),height=HEIGHT,width=WIDTH,bg=color_botonNumerico,font=fuente_boton,activebackground=color_hover_botonNumerico)
Boton1.grid(row=4,column=0,sticky="we")
Boton2 = tk.Button(calculadora,text="2",command=lambda:obtener_numero(2),height=HEIGHT,width=WIDTH,bg=color_botonNumerico,font=fuente_boton,activebackground=color_hover_botonNumerico)
Boton2.grid(row=4,column=1,sticky="we")
Boton3 = tk.Button(calculadora,text="3",command=lambda:obtener_numero(3),height=HEIGHT,width=WIDTH,bg=color_botonNumerico,font=fuente_boton,activebackground=color_hover_botonNumerico)
Boton3.grid(row=4,column=2,sticky="we")
BotonRest = tk.Button(calculadora,text="−",command=lambda:obtener_operacion('-'),height=HEIGHT,width=WIDTH,bg=color_resta,font=fuente_boton,activebackground=color_hover_operador).grid(row=4,column=3,sticky="we")

BotonPunto = tk.Button(calculadora,text=".",command=lambda:obtener_operacion('.'),height=HEIGHT,width=WIDTH,bg=color_punto,font=fuente_boton,activebackground=color_hover_punto)
BotonPunto.grid(row=5,column=0,sticky="we")
Boton0 = tk.Button(calculadora,text="0",command=lambda:obtener_numero(0),height=HEIGHT,width=WIDTH,bg=color_botonNumerico,font=fuente_boton,activebackground=color_hover_botonNumerico)
Boton0.grid(row=5,column=1,sticky="we")
BotonIgual = tk.Button(calculadora,text="=",command=lambda:operaciones(),height=HEIGHT,width=WIDTH,bg=color_igual,font=fuente_boton,activebackground=color_hover_igual)
BotonIgual.grid(row=5,column=2,sticky="we")
BotonSuma = tk.Button(calculadora,text="+",command=lambda:obtener_operacion('+'),height=HEIGHT,width=WIDTH,bg=color_suma,font=fuente_boton,activebackground=color_hover_operador)
BotonSuma.grid(row=5,column=3,sticky="we")



#Ciclo principal
calculadora.mainloop()