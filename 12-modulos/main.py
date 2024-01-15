"""
Modulos
Son funcionalidades ya hechas para reutilizar.

En python hay muchos modulos, en este link hay muchos de ellos
https://docs.python.org/3/library/math.html#module-math

Estos modulos se pueden conseguir y reutilizar, modulos de internet, o tambien se pueden crear
"""

"""         Importo el contenido del archivo mimodulo.py, mediante 2 formas, 
la primera inporto solo el hola mundo, la segunda importo todo el documento         """

from mimodulo import holamundo
print(holamundo("Alex Dehesa"))

import mimodulo
print(mimodulo.calculadora(3,5,True))

#Modulo fechas.  Hay muchas posibilidades de modulos, rr mirando cual nos conviene mas en cada caso. Esta es la sintaxis.
import datetime
print(datetime.date.today())

#Modulo matematicas.
import math
print("Raiz cuadrada de 10: ",math.sqrt(10))  #Modulo de raiz cuadrada, esta dentro de matematicas
print("EL número pi és: ", float(math.pi))    #Modulo de número pi, esta dentro de matemáticas

