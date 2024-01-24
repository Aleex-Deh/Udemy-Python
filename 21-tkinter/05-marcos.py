from tkinter import *

ventana = Tk()
ventana.title("Marcos, Master en Python")
ventana.geometry("750x700")


# El (Frame), es para hacer marcos
marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(
    bg= "black",
    bd = 6,
    relief="solid"
)
marco_padre.pack(side=TOP, fill=X, expand=YES)


marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg= "blue",
    bd = 6,
    relief="solid"
)
marco.pack(side=RIGHT, anchor= SE)



marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg= "orange",
    bd = 6,
    relief="solid"
)
marco.pack(side=RIGHT, anchor= SE)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg= "white",
    bd = 6,
    relief="solid"
)
marco.pack(side=RIGHT, anchor= SE)


marco = Frame(ventana, width=250, height=250)
marco.config(
    bg= "pink",
    bd = 6,
    relief="solid"
)
marco.pack(side=LEFT,)

marco = Frame(ventana, width=250, height=250)
marco.config(
    bg= "red",
    bd = 6,
    relief="solid"
)
marco.pack(side=LEFT,)

marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(
    bg= "purple",
    bd = 6,
    relief="solid"
)
marco_padre.pack( fill=X, expand=YES)





ventana.mainloop()