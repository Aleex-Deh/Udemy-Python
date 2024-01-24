from tkinter import *

ventana =  Tk()
#ventana.geometry("1000x500")       #Comento para que sea automatico

texto = Label(ventana, text="Hola, this is mi programa")
texto.config(
    justify= RIGHT,        
    fg="white",              
    bg= "black",           
    padx=40,               
    pady=20,               
    font=("Lexend", 30),  
    )
texto.pack(anchor= CENTER)   



""" En funcion (pruebas) he definido el orden de parámetros, aqui con que ponga (variable="valor") se coloca automatico """
texto = Label(ventana, text="Basico1")
texto.config(
    justify= RIGHT,
    bg= "grey",
    height=1,        
    font=("Arial", 14),
    padx=10,
    pady=40,
    cursor="arrow"       
    )
texto.pack(side= TOP, fill=X, expand = YES)     # Medianete el fill relleno todo en x, y con el expand habilito que se exapnda la caja



texto = Label(ventana, text="Basico2")
texto.config(
    justify= RIGHT,
    bg= "yellow",
    height=1,         
    font=("Arial", 14),
    padx=10,
    pady=40,
    cursor="arrow"       
    )
texto.pack(side=LEFT, fill=X, expand = YES)   



texto = Label(ventana, text="Basico3")
texto.config(
    justify= RIGHT,
    bg= "orange",
    height=1,          
    font=("Arial", 14),
    padx=10,
    pady=40,
    cursor="arrow"       
    )
texto.pack(side=LEFT, fill=X, expand = YES)    





ventana.mainloop()       
