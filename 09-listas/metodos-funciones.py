cantantes = ["Duki", "BadBunny", "E-Legante"]
numeros = [1,2,5,8,3,4]

#Ordenar listas.    Mediante funcion .sort
print(numeros)
numeros.sort()
print (numeros)

#Añadir elementos
"""
Primera forma. Con el append, simplemente añade el valor a la lista y lo posiciona en ultimo lugar

Segunda forma. Con el insert, añado el valor a la lista y ediante el paámetro le elijo la posicion,
en el ejemplo iria en segunda posicion"""
cantantes.append("Aitana")
cantantes.insert(1,"David Bisbal")
print(cantantes)

#Eliminar elementos
"""
Primera forma. Con el pop, es muy simple y comodo

Segunda opcion. COn el remove, es muy util ya que puedo elegir el contenido a eliminar, pero debe de estar igual escrito
"""
cantantes.pop(1)
cantantes.remove("BadBunny")
print(cantantes)


#Buscar dentro de una lista. Mediante esta sintaxis nos devolvera la respuesta en booleano (TRUE / FALSE)
print("Duki" in cantantes)

#Contar elementos. Mediante el len
print(cantantes)
print(len(cantantes))

#Cuantas vaces aparece un valor. Le hemos pedido que en numeros cuente las veces del parámetro (8)
print(numeros.count(8))