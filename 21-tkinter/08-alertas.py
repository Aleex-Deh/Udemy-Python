from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()

def sacarAlerta():
    MessageBox.showwarning("Alerta", "¡Esto es una alerta!")

Button(ventana, text="Mostrar alerta", command=sacarAlerta).pack()

def salir():
    resultado = MessageBox.askquestion("Salir", "¿Desea seguir con el proceso?")
    if resultado == "no":
        ventana.destroy()

Button(ventana, text="Salir", command=salir).pack()

ventana.mainloop()
