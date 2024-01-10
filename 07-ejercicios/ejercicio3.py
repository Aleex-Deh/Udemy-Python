"""
Ejercicio 3

Escribir un script que muestre los cuadrados de los primeros 60 numeros naturales. Son del 1 al 60
Hay que hacerlo para for y para while

"""

# Con el for
numero_natural = 1
for numero_natural in range (0,60):
    print (f"El cuadrado de {numero_natural} es {numero_natural * numero_natural}")


# Con el while 
contador = 1
while contador <= 61:
    print(f"El cuadrado de {contador} es {contador * contador}")
    contador = contador +1