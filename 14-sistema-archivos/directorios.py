import os

"""Mediante el import os, se pueden adminitrar carpetas como si fuera una terminal, los comandos son muy parecidos,
en este caso creo un if para verificar que la carpeta no exista ya, si no que avise de que ya existe"""

#Crear carpeta
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("Ya existe esa carpeta")
    
#Eliminar carpeta. Mediante el remove, que resumido en python es rmdir, casi igual que por terminal
"""
os.rmdir("./mi_carpeta")        """
