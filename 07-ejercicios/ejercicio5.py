"""
Ejercicio 5
Script que muestre todos lo numero entre 2 inputs que ponga yo
"""

print("Solo puede introducir numeros positivos y enteros")
numero2 = int(input ("Porque número quiere empezar: "))
numero3 = int(input ("Porque número quiero finalizar: "))

for numero1 in range(numero2,numero3):
    print (numero1)
    numero1 = numero1 + 1
