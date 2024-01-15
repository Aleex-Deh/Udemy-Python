"""
EJERCICIO 3
Crear script que tenga 4 variblaes. 1 lista. 1 string. 1 entero. 1 booleano.
Debe imprimir un mensaje segun el tipo de dato que sea cada varible. Usar funciones
"""

def script():
    if type(titulo) == str:
        print("Esta variable es una cadena")
    elif type(numero) == int:
        print("Esta variable es un número entero")
    elif type(lista) == list:
        print(" La variable lista es un formato lista")
    elif type(verdadero) == bool:
        print("La variable verdadero es un formato booleano")
    else:
        print("No reconocemos que formato es")

# He de ir cambiando el valor de las variable manualmente
lista = ["Duko"]
titulo = 1
numero = 33
verdadero = True
script()
