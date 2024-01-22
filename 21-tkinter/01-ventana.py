"""
TKINTER
Es un modulo para crear interfaces gráficas que ya viene con python
"""

from tkinter import *
import os.path

class Progrma:
    def __init__(self):
        self.title = "Master en python"
        self.size = "770x470"
        self.resizable = False 

    def cargar(self):
        #Crear ventana principal / raiz
        ventana = Tk()
        self.ventana = ventana

        # Cambiar tamaño de la ventana, le asigno un tamaño inicial pero es totalmente moldeable graficamente
        ventana.geometry(self.size)

        # Bloquear el tamaño de la ventana, los parametros son (horizontal, vertical) si es 1 si deja moldearlo, si es 0 no.
        if self.resizable:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)
        

        # Logotipo / icono de la ventana.   La imagen tiene que ser .ico
        # ventana.iconbitmap("ruta absoluta")

        #Titulo de la ventana
        ventana.title(self.title)

    
    def addTexto(self, dato):
        texto = Label(self.ventana, text=(dato))
        texto.pack()

    def mostrar(self):
        #Iniciar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()

#Instanciar el programa
programa = Progrma()
programa. cargar()
programa.addTexto("Holaa, que haces guapo?")
programa.mostrar()