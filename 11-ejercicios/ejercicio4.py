"""
EJERCICIO 5
Crear una lista en el contenido de esta tabla:
ACCION      AVENTURA        DEPORTES
GTA         ASSASINS        FIFA
COD         CRASH           PRO 21
PUGB        PRINCE OF PERCIA    MOTO GP 21

Mostrar esta información ordenada"""

tabla = [
    {
        "categoria": "ACCION",
        "juegos": ["GTA", "Call of duty", "PUGB"]
    },
    {
        "categoria": "Aventura",
        "juegos": ["ASSASINS", "Crash Bandicoot", "Prince of persia"]
    },
    {
        "categoria": "DEPORTES",
        "juegos": ["FIFA 21", "PES 21", "MOTO GP 21"]
    }
]

for categoria in tabla:
    print(f"{categoria['categoria']}")
    for juego in categoria['juegos']:
        print(juego)