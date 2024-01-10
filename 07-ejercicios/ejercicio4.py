"""
Ejercicio 4

Pedir dos numeros al usario y hacer todas las operacioens basicas de una calculadora
"""
numero1 = int(input("El primer numero es ...: "))
numero2 = int(input("El segundo numero es ...: "))

sumar = numero1 + numero2
restar = numero1 - numero2
multiplicar = numero1 * numero2
dividir = numero1 / numero2  # Cambiado de % a /

print("Tiene las siguientes operaciones disponibles \n1= sumar  \n2= restar  \n3= multiplicar  \n4= dividir")
identificador = input("Introduzca su operación a realizar de forma numerica: ")

if identificador == '1':
    print(f"Resultado de la suma: {sumar}")
elif identificador == '2':
    print(f"Resultado de la resta: {restar}")
elif identificador == '3':
    print(f"Resultado de la multiplicación: {multiplicar}")
elif identificador == '4':
    print(f"Resultado de la división: {dividir}")
else:
    print("Operación no válida. Por favor, introduzca un número del 1 al 4.")
