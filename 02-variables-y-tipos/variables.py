""" 
Las variables son cajas a las que se les pueden asignar valores
"""

#Crear las variables y asignarles valor
texto = "Master en python"
texto = "1"
texto2 = "Con la certificacion de python"
numero = "45"
decimal = "6,7"
#Ejecutar las variables
print(texto)
print (texto2)
print (numero)
print (decimal)



#Cambiar valor a las variables y volverlas a mostrar
numero = "77"
decimal = "8.9"
print (numero)
print (decimal)

#Concatenacion
nombre = "Alex"
apellidos = "Dehesa"
web = "AlexDehesaweb.es" 

#Concatenacion con +
print (nombre + " " + apellidos + " - " + web)
#Concatenacion usando la f  print(f"{variables} texto o espacios {variables}"    "Esta es la mejor, segun el profesor"
print (f"{nombre} {apellidos} - {web}")
#Concatenacion con FUNCION .format
print("Hola me llamo {} {} y mi web es: {}".format(nombre, apellidos, web))
#Conseguiremos lo mismo, pero distintas maneras

