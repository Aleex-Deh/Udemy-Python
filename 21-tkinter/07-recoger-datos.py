from tkinter import *

ventana = Tk()

ventana.geometry("750x500")
ventana.config(
    bd=50,
    bg="yellow"
)

# Función getDato: Obtiene el valor de la variable dato y lo asigna a la variable resultado
def getDato():
    resultado.set(dato.get())

# Variables StringVar para almacenar datos
dato = StringVar()
resultado = StringVar()

# Etiqueta y cuadro de entrada para introducir un texto
Label(ventana, text="Introduce un texto :").pack(anchor=NW)
Entry(ventana, textvariable=dato).pack(anchor=NW)

# Etiqueta para mostrar el dato recogido
Label(ventana, text="Dato recogido :").pack(anchor=NW)

# Etiqueta dinámica que muestra el valor de la variable resultado
Label(ventana, textvariable=resultado).pack(anchor=NW)

# Botón que al ser presionado ejecuta la función getDato
Button(ventana, text="Mostrar datos", command=getDato).pack(anchor=NW)

ventana.mainloop()
