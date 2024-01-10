#Ejemplo 1
"""
# Condicional IF
-----------------------------------------------------
SI se cumple esta condición:
    Ejecuta un grupo de instrucciones
SI NO : 
    Se ejecuta otro grupo de instrucciones
------------------------------------------------------
IF condición
    intrucciones
else: 
    otras instrucciones
"""
print ("###### EJEMPLO 1 ######")

# Variable es rojo:  Si la variable color es rojo escribir "El color es rojo", si no "El color no es rojo"
color = input("Escriba un color, porfavor : ")
if color == "rojo":
    print ("El color es rojo")
else:
    print ("El color no es rojo")

#Ejemplo 2
"""
#Operadores de comparacion 
==    igual
!=    diferente que 
<     menor que
>     mayor que 
<=    menor o igual que 
>=    mayor o igual que 
"""


print ("###### EJEMPLO 2 ######")

year = int(input (" En que año estamos"))
if year >= 2021:
    print ("Estamos de 2021 hacia adelante")
else:
    print ("Estamos de 2022 hacia abajo")


#Ejemplo 3

nombre = "Alex Dehesa"
ciudad = "Barcelona"
continente = "Europa"
edad = "18"
mayoria_edad >= "18"

if edad >= mayoria_edad:
    print (f"{nombre} es mayor de edad")

    if continente != Europa:
        print (f"{nombre} no es Europeo, es extranjero")
    else :
        print (f"{nombre} es Europeo, es de {ciudad}")

else:
    print (f"{nombre} no es mayor de edad")


# Tambien estan los ELIF, son de misma sintaxis
# Tambien metemos los and, para meter varios if dentro de un if (esto es solo un ejemplo, tiene multiples opciones)


# Ejemplo 4  (con operadores logicos (and, or, not , etc....)
pais = "Alemania"

if pais == "España" or pais == "Francia" or pais == "Alemania":
    print ("El pais encontrado es Alemania")
else:
    print ("Alemania no esta en esa lista de paises")



# Siguiendo con al continuacion del 4, puedo añadsir un () + un NOT para cambairle el enfoque
pais = "Alemania"

if not (pais == "España" or pais == "Francia" or pais == "Alemania"):
    print ("El pais encontrado es Alemania")
else:
    print ("Alemania no esta en esa lista de paises")