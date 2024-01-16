from io import open
import pathlib

"""Importamos open para abrir archivos con Python, también importamos pathlib
para usar rutas absolutas. Ahora asignaremos todo este conjunto a una variable
y le daremos los permisos.      """

ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta, "a+")

""" Esta .write sirve para escribir dentro del archivo que hemos abierto.
Lo que hay en esta variable se escribe automáticamente en el otro archivo.
Escribir dentro del archivo abierto.        """

archivo.write("Es el texto metido desde Python \n")

# Leer contenido. Mediante el seek(0), hacemos que antes de ller se posicione al inicio de tod, para que lo lea todo
archivo.seek(0)
lista = archivo.readlines()
print(lista)

# Cerrar archivo abierto.
archivo.close()


#Copiar achivos. Tiene la misma sintaxis que un scp de terminal. (copiar el archivo de esta ruta en esta)
import shutil       #Este se importa para poder copiar/renombrar archivos
ruta2 = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
"""
shutil.copyfile(ruta, ruta2)            """

# Mover archivo. Tiene la misma sintaxis que el move de terminal, es lo mismo en todos.
"""         
shutil.move(ruta,ruta2)      """

#Eliminar fichero
import os       #Este es para poner eliminar archivos. Igual que en teminal
os.remove(ruta2)
