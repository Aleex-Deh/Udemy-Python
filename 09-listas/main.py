"""
LISTAS 
Son coleciones o conjuntos de datos/valores, bajo un único nombre.
Para acceder a esos valores podemos usar un indice numérico. """

# Definir la lista. Se pueden definir por 2 metodos.

# Definir lista. Método 1.  Usando []
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
#Definir lista. Método 2.   Usando la funcion list. Aqui hay un range de ejemplo, tambien se puede hacer en el otro metodo
pelicula = list(range(0,20))

"""
print (peliculas)
print (pelicula)
"""
# Indices
""" Los indices son para sacar un valor determinado de la lista, mediante su posicion, en el primer caso
sacamos el primero, es decir el primero de la izquierda.
En el segundo caso sacaremos el -1, es decir el ultimo e la izquierda(el primero de la derecha)
En el tercer caso es para sacar valores consucutivs, en este caso es del 0 hasta el 2"""

print (peliculas[1])
print (peliculas[-1])
print (peliculas[0:2])

"""Se pueden modificar lo de dentro de las listas, mediante la siguiente sintaxis"""
peliculas[1] = "El señor de la noche"
print(peliculas)

# Añadir elementos a una lista
cantantes = ["Nissa", "BadBunny"]
cantantes.append("Duko")
print (cantantes)

"""
Recorrer lista. Para iterar/recorrer una lista mediante el for, es lo mas util.
Me salen estos numeros pero porque he pueso un rango antes
"""
for peliculas in peliculas:
    print (pelicula)
