import tkinter as tk
from tkinter import messagebox
import random
import math
class Ruleta:
    def __init__(self, nombres):
        self.nombres = nombres
        self.girando = False
        self.ganador = None

        self.ventana = tk.Tk()
        self.ventana.title("Ruleta")
        
        self.canvas = tk.Canvas(self.ventana, width=400, height=400)
        self.canvas.pack()

        self.label_ganador = tk.Label(self.ventana, text="¡Presiona el botón para comenzar!")
        self.label_ganador.pack(pady=20)

        self.boton_girar = tk.Button(self.ventana, text="Girar", command=self.girar_ruleta)
        self.boton_girar.pack(pady=10)

    def girar_ruleta(self):
        if not self.girando:
            self.girando = True
            self.ganador = None
            self.boton_girar.config(state=tk.DISABLED)
            self.animar_ruleta()

    def animar_ruleta(self):
        velocidad = 100
        duracion = 2000
        incremento = 5
        num_vueltas = random.randint(5, 10)
        num_opciones = len(self.nombres)
        angulo_inicial = random.uniform(0, 360)

        incremento_angulo = 360 * num_vueltas + angulo_inicial
        total_frames = duracion // velocidad

        angulo_actual = angulo_inicial
        for frame in range(total_frames):
            angulo_actual += incremento
            if angulo_actual >= 360:
                angulo_actual -= 360

            self.canvas.delete("all")
            self.dibujar_ruleta(angulo_actual)

            if frame == total_frames - 1:
                opcion_ganador = int((angulo_actual + incremento_angulo) // (360 / num_opciones))
                self.ganador = self.nombres[opcion_ganador]

            self.ventana.update()
            self.ventana.after(velocidad)

        self.girando = False
        self.boton_girar.config(state=tk.NORMAL)
        self.mostrar_ganador()

    def dibujar_ruleta(self, angulo):
        x_centro = 200
        y_centro = 200
        radio = 150
        angulo_separacion = 360 / len(self.nombres)

        for i, nombre in enumerate(self.nombres):
            angulo_inicio = i * angulo_separacion - 90
            angulo_final = (i + 1) * angulo_separacion - 90

            self.canvas.create_arc(x_centro - radio, y_centro - radio, x_centro + radio, y_centro + radio,
                                   start=angulo_inicio, extent=angulo_separacion, fill="blue")

            angulo_medio = (angulo_inicio + angulo_final) / 2
            x_texto = x_centro + radio * 0.7 * math.cos(math.radians(angulo_medio))
            y_texto = y_centro + radio * 0.7 * math.sin(math.radians(angulo_medio))
            self.canvas.create_text(x_texto, y_texto, text=nombre, fill="white", font=("Arial", 10, "bold"))

        x_punta = x_centro + radio * 0.8 * math.cos(math.radians(angulo))
        y_punta = y_centro + radio * 0.8 * math.sin(math.radians(angulo))
        self.canvas.create_line(x_centro, y_centro, x_punta, y_punta, fill="red", width=5)

    def mostrar_ganador(self):
        messagebox.showinfo("Ganador", f"¡El ganador es: {self.ganador}!")

    def iniciar(self):
        self.ventana.mainloop()

# Nombres para la ruleta
nombres = [
    "Billy Daniel", "Sergio David", "Adrian Esteban", "Jesenia Raquel", "Angel Gabriel", "Ludvik Mauricio",
    "Johnny Eduardo", "Marvin Estuardo", "Jorge José Desiderio", "Stephany Guiselle", "Mario Alejandro",
    "Carlos Fernando", "Diego Gerardo", "Julio Cesar", "Mario Alejandro", "Oscar Josué", "Wagner Isaac Leví",
    "Mattew Ismael", "Edwin Geovanni", "Beverly Dayana", "José Miguel", "Erick Gerardo", "Angie Islena",
    "Justin Steve", "Pablo Esteban", "Rudy Gerald Eliú", "Alexis Guillermo", "Michael Josué", "Alan Misael",
    "Hesler Arnoldo", "Juan David", "Jose Angel", "Josué David", "Jose Pablo", "Angelo Alessandro", "Jose Angel",
    "Carlos Fernando", "Javier Rodolfo", "Monica Giselle", "Cesar Eduardo", "Josué Daniel", "Luis Diego",
    "Jose Angel", "Josué Daniel", "Diego Gerardo", "Jose Angel", "Josué Daniel", "Luis Alberto"
]


ruleta = Ruleta(nombres)
ruleta.iniciar()
