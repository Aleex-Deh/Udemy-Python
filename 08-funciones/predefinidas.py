nombre = "Alex Dehesa"

#Funciones generales
print(type(nombre))

#Detectar el tipado (isinstance)
"""La funcion isinstance verifica el tipo de dato, en este caso verifica si la variable nombre es un int, 
y dependiendo sea true o false hara el if o el else"""

comprobar = isinstance(nombre, int)
if comprobar:
    print("Esa vriable es un string")
else:
    print("Esa variable no es un string")
    
    
#Limpiar espacio de la frase, poner bien los margenes
"""Se hace mediante la variable le añades.strip(), es lo que hace es que te eliminda 
los espacios vacios  de los márgenes, haciendolo mas visual"""

frase = "       mi contenido        "
print(frase)
print(frase.strip())


#Eliminar variables
"""Se hace mediante el del "del variable"       """
year = 2020
print(year)
del year
#print (year )     La comento ya que como la he eliminado no existe y me henera error

#Comprobar variable vacia  (len)
"""Mediante la funcion "len" se cuentan los caracteres de alguna variable"""
texto = "ff"
if len(texto) <= 0:
    print("La variable esta vacia")
else:
    print(f"La variable tienen contenido de {len(texto)}")
    
    
#Encontrar caracteres (find)
"""Mediante la funcion. finda se pueden encontar palabras y saber apartir de que caracter esta"""
frase = "La vida es bella"
print(frase.find("vida"))

#Reemplazar palabrasde un string
"""Mediante la funcion .replace se puede remplazar una palabra por otra"""
nueva_frase = frase.replace("vida", "bicicleta")
print (nueva_frase)


#Pasar a mayusculas o minusculas (.lower) o (.upper)
"""Mediante estas 2 funciones se pueden pasar todo a mayusculas o todo a minsculas,
esto es util para evitar errores"""
print (nombre)
print (nombre.lower())
print (nombre.upper())