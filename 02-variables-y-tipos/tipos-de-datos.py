nada = None
cadena = "hola, soy Alex Dehesa WEB"                   #Una cadena es un stringht (es para texto)
cadena = "desarrolador WEB"
entero = 99
flotante = 4.2                                         #Valor decimal
booleano = False                                       #Valor verdadero o falso, no puede ser nada mas
array = [10, 20, 30, 40]
listaVariada = [10, "hola", 20, "adios", 30, "ayuda"]
tupla = ("master", "en", "python")                     #Valor que no puede cambiar
diccionario = {                                        #Tener una clave y valor, es como guardar datos
    "nombre": "Alex",
    "apellido": "Dehesa",
    "curso": "Master en Python"
}
rango = range(9)                                       #Hacer un rango con la FUNCION range
dato_byte = b"Probando"

#Imprimir variables
print (dato_byte)                                      #Se le pone una b para que su dato sea BYTE
#Mostrar tipo de dato con la FUNCION type
print(type(dato_byte))



"""
Cambiar el tipo de dato, estoy concatenando pero da error, ya que estoy juntando 
stringht con entero, para esto, al entero le cambio el valor a stringht de la siguiente manera
"""
texto = "Hola soy un texto"
numerito = str(776 )
print (texto + " "+ numerito)

