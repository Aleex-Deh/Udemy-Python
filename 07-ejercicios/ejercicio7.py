"""
Ejercicio 7
Hacer un programa que muestre todos los numeros impares
entre dos inputs que decida el usario
"""

numero1 = 0
numero2 = int(input("¿Con qué número quieres empezar?: "))
numero3 = int(input("¿Con qué número quieres acabar?: "))

for numero1 in range(numero2, numero3):
    if numero1 % 2 != 0:
        print(numero1)

    
        