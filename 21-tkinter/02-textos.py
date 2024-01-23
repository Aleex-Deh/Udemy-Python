from tkinter import *

ventana =  Tk()
ventana.geometry("1000x500")

texto = Label(ventana, text="Hola, this is mi programa")
texto.config(
    justify= RIGHT,         #Justificacion del texto  
    fg="white",              #Color de letra
    bg= "black",             #Color de subrayado
    padx=40,                # Eje X
    pady=20,                # Eje Y
    font=("Lexend", 30),    # Fuente de letra y  nº de letra
    )
texto.pack(anchor= CENTER)    #Para que se muestre el resultado de ese momento del codigo

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos} con nacionalidad de {pais}"  #Marco el orden de los parámetros en la frase

""" En funcion (pruebas) he definido el orden de parámetros, aqui con que ponga (variable="valor") se coloca automatico """
texto = Label(ventana, text=pruebas(nombre="Mauro", pais="Argentina", apellidos="Lombardo"))
texto.config(
    justify= RIGHT,
    bg= "grey",
    height=1,          #Altura, he metido el color para diferenciarlo mejor
    font=("Arial", 14),
    padx=10,
    pady=40,
    cursor="arrow"         #Si el cursor al pasar por encima de ese campo, se transofrma en lo que queramos el cursor
    )

texto.pack(anchor= W)    # anchor "Orientacion del texto (Norte, Sur, Este, Oeste, etc....)""
    


ventana.mainloop()        # Se cree y funcione hasta que la ventana se cierre
