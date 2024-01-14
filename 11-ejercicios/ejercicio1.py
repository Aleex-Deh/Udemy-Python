"""
EJERCICIO 1
Hacer un programa que tenga una lista de 8 numeros enteros y haga lo siguientes :
- Recorrer la lista y mostrarla
- Hacer funcion que recorra listas de numeros y devuelvo un string
- Ordanarla y mostrarla
- Mostrar su longitud
- Buscar algun elemento (que el ususario pida haya pedido por teclado)"""

numeros = [21,45,63,17,95,1,51]


def mostrar_lista(lista):
    resultado = ""
    
    for elemento in lista:
        resultado += "Elemento " + str(elemento)
        resultado+= "\n"
    return resultado



for numero in numeros:
    print(numero)
    
print(mostrar_lista(numeros))