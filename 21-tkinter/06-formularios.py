from tkinter import *

ventana = Tk()
ventana.geometry("750x400")
ventana.title("Formularios / Alex Dehesa")


# Texto encabezado
encabezado = Label(ventana, text="Formularios con TKINTER")
encabezado.config(
    fg= "white",
    bg= "black",
    font=("Arial, 18"),
    padx=10,
    pady=10
)
#grid = Es como el pack pero ademas permite mayor control en cuanto a posiciones
encabezado.grid(row=0, column=0, sticky=W, columnspan=20)  
#sticky= Es para pegar el texto en la parte izquierda (W)
#columnspan= Es para crear columans para poder ajustar espacios, como si fueran margenes, cuantas mas haya mas junto puede estar



#Label para el campo de escribir texto
label= Label(ventana, text="Nombre")
label.grid(row=1, column=0,padx=5, pady=5, sticky=W )

# Campo para escribir texto
campo_texto=Entry(ventana)
campo_texto.grid(row=1, column=1, padx=5, pady=5, sticky=W)


#Label para  texto
label= Label(ventana, text="Apellidos")
label.grid(row=2, column=0,padx=5, pady=5, sticky=W )

# Campo para  texto
campo_texto=Entry(ventana)
campo_texto.grid(row=2, column=1, padx=5, pady=5, sticky=W)



#Label para  descripcion
label= Label(ventana, text="Descripción")
label.grid(row=3, column=0,padx=5, pady=5, sticky=W )

# Campo para  descripcion (grande)
campo_grande=Text(ventana)  # El campo text, es demasiado grande, por eso hay que recortarlo bastane, aun asi sigue siendo grande
campo_grande.grid(row=3, column=1, padx=5, pady=5, sticky=W)
campo_grande.config(
    width=30,
    height=4,
    font=("Arial", 12,),
    padx=15,
    pady=15
)


# Botones
boton = Button(ventana, text="Enviar")
boton.grid(row=3, column=2,padx=5, pady=5, sticky=W)
boton.config(
    width=3,
    height=3,
    fg= "white",
    bg= "black",
    font=("Arial", 16,),
    padx=15,
    pady=15
)

ventana.mainloop()