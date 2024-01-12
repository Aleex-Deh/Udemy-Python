"""
FUNCIONES
Es un conjunto de instrucciones agrupadas bajo un nombre concreto que 
pueden reutilizarse a lo largo del codgio invocando dicha funcion, 

"def nombre(parámetros)"
"""

#Ejemplo 1
"""
def muestra_nombre():
    nombre = input ("Introduzca su nombre: ")
    print("\n")
    print (nombre)
    print("\n")
muestra_nombre()            """

#Ejemplo 2
"""
def mostrar_tu_nombre(nombre):
    print(f"Tu nombre es {nombre}")
    Print("\n)
nombre = input ("Introduce tu nombre: ")
mostrar_tu_nombre(nombre)       """

#Ejemplo 3
"""
def table(numero):
    print(f"Table de multiplicar del número {numero}")
    
    for contador in range (11):
        operacion = numero*contador
        print(f"{numero} x {contador} = {operacion}")
table(7)          """

#Ejemplo 4. Parámetros opcionales
"""
def get_empleado(nombre, dni = False):
    print("### EMPLEADO ###")
    print (f"{nombre} \n{dni}")
get_empleado("Alex Dehesa")         """


#Ejemplo 5. Parámetros opcionales y return / devolder datos
""""
def calculadora(numero1, numero2, basicos = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2
    
    if basicos != False:
        cadena = ""
        cadena += "Suma : " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicacion: " + str(multiplicacion)
        cadena += "\n"
        cadena += "Division: " + str(division)
        cadena += "\n"
    return cadena
print (calculadora(8,8,True))           """


#Ejemplo 6. Funcion LAMBDA
"""Las funciones lambda en Python son funciones anónimas y pequeñas que pueden definirse en una sola línea de código.
Se utilizan principalmente en situaciones donde necesitas una funcióntemporal para realizar una tarea específica y
no quieres crear una función completa usando la declaración def."""

dime_el_año = lambda year: f"El año es {year}"
print(dime_el_año(2024))