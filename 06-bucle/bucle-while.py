"""
#Bucle while 
Estreuctura de control que itera / repite la ejecucion de una serie de instrucciones
tantas veces como sea necesario, hasta que deje de cumplirse la condicion

while condicion:
    bloque de instrucciones 
    actualizacion de contador

"""

"""
#Ejemplo 1      Lista desde 0 hasta el 100
contador = 1
while contador <= 100:
    print (f"Estoy en el número {contador}")
    contador = contador + 1
"""

# Ejemplo 2     # Tabla de multiplicar
print ("#### Ejemplo 2")
numero_usuario= int(input("De que numero quieres que sea la tabla : "))


contador = 1
while contador <= 10:
    print (f"{numero_usuario} x {contador} = {numero_usuario * contador}")
    contador = contador + 1 