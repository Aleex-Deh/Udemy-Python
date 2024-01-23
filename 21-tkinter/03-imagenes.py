from tkinter import *
from PIL import Image, ImageTk        

ventana = Tk()
ventana.geometry("750x500")

Label(ventana, text="Hola, soy Alex").pack(anchor=W)

imagen = Image.open('21-tkinter/imagenes/perro.jpg')          
render = ImageTk.PhotoImage(imagen)                           

Label(ventana, image=render).pack()

ventana.mainloop()

