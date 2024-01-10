"""
#for

for variable in elemento_iterable (lista, rango, etc)
    BLOQUE DE INSTRUCCIONES
"""

#Ejemplo de lo de arriba
contador = 0
for contador in range (0,5):
    print (f"Voy por el {contador}")




#####   Ejemplo tablas de multiplicar
print ("\n")
numero_usuario = int(input ("De que numero quieres ver la tabla:"))
if numero_usuario < 1:
    numero_usuario = 1

print (f"#### Tabla de multiplicar del numero {numero_usuario} ####")
for numero_tabla in range(0,10):
    print (f"{numero_usuario} x {numero_tabla} = {numero_usuario * numero_tabla}")
else:
    print ("Tabla finalizada")