"""
Ejercicio 6
Mostrar todas las tablas de multiplicar del 1 al 10, 
mostrando el titulo de la tabla y luego sus multiplicaciones
"""

tabla_multiplicar = 0
for numero in range (0,10):
    print ("\n")
    print (f" ### Table de multiplicar x {tabla_multiplicar} ### ")
    tabla_multiplicar = tabla_multiplicar + 1
    incremento = 0
    print("\n")
    for incremento in range(0,11):
        print (f"{tabla_multiplicar} x {incremento} = {tabla_multiplicar * incremento}")
        incremento = incremento + 1

