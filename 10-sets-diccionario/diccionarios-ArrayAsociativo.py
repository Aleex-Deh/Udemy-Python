"""
DICCIONARIOS / ARRAY ASOCIATIVO
Un tipo de dato que almacena un conjunto de datos.
Es en formato clave > valor.
Es parecido a un array asociativo o un objeto json"""

"""
persona = {
    "nombre": "Alex",
    "apellidos": "Dehesa",
    "web": "adehesadelgado.web"
}
print (persona)
"""

#Listas dentro de diccionarios

contactos = [
    {
        "nombre": "Antonio",
        "email": "Antonio@gmail.com"
    },
    {
        "nombre": "Luis",
        "email": "Luis@gmail.com"
    },
    {
        "nombre": "Salvador",
        "eamil": "Salvador@gmail.com"
}
]
print (contactos)
# Tambien puedo iterarlo al igual que un array normal
print(contactos[1]["nombre"])