"""
EJERCICIO 1
Programa que añada valores una lista mientras que su longitud sea menor a 120, y luego mostrar la lista.
Hacer con while y tmbien con el for"""


#Ejercicio con FOR

lista = []
for contador in range(0,120):
    lista.append(f"{contador}")
    print(lista[contador])


#Ejercicio con WHILE
contador1 = 0
lista1 = []
while contador1 <= 120:
    lista1.append(contador1)
    print(lista1[contador1])
    contador1 = contador1 + 1