from tkinter import *

# Configuración de la ventana principal
ventana = Tk()
ventana.title("Marcos, Master en Python")
ventana.geometry("750x700")

# Creación de un marco principal
marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(
    bg="black",
    bd=6,
    relief="solid"
)
marco_padre.pack(side=TOP, fill=X, expand=YES)  # Empaquetar el marco principal en la parte superior

# Creación de marcos secundarios dentro del marco principal
marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="blue",
    bd=6,
    relief="solid"
)
marco.pack(side=RIGHT, anchor=SE)  # Empaquetar el marco secundario en el lado derecho

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="orange",
    bd=6,
    relief="solid"
)
marco.pack(side=RIGHT, anchor=SE)  # Empaquetar otro marco secundario en el lado derecho

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="white",
    bd=6,
    relief="solid"
)
marco.pack(side=RIGHT, anchor=SE)  # Empaquetar otro marco secundario en el lado derecho

# Desactivar autoformato al introducir texto en el marco
marco.pack_propagate(False)
texto = Label(marco, text="Primer marco")
texto.config(
    bg="white",
    fg="black",
    font=("Arial", 16),
    anchor=CENTER,
    height=10,
    width=10,
    bd=3
)
texto.pack()  # Empaquetar el texto en el marco

# Creación de marcos independientes
marco = Frame(ventana, width=250, height=250)
marco.config(
    bg="pink",
    bd=6,
    relief="solid"
)
marco.pack(side=LEFT)  # Empaquetar un marco independiente en el lado izquierdo

marco = Frame(ventana, width=250, height=250)
marco.config(
    bg="red",
    bd=6,
    relief="solid"
)
marco.pack(side=LEFT)  # Empaquetar otro marco independiente en el lado izquierdo

# Creación de otro marco principal
marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(
    bg="purple",
    bd=6,
    relief="solid"
)
marco_padre.pack(fill=X, expand=YES)  # Empaquetar otro marco principal

# Iniciar el bucle principal de la ventana
ventana.mainloop()
