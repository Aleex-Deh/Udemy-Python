"""
EJERCICIO 2
Programa que comprueba si una variable esta en minusculas y si esa vacia, 
rellenarla con texto en minuscula y mostralo en mayuscula"""

variable = " "

if len(variable.strip()) == 0:
    texto = "Soy texto en minúsculas"
    print(texto.upper())
else:
    print("La variable no está vacía")

