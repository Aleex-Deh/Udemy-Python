from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

layout= """
<h1>Sitio web con DJango</h1>
<hr/>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
        <li>
        <a href="/hola-mundo">Hola mundo</a>
    </li>
        <li>
        <a href="/pagina-prueba">Pagina de prueba</a>
    </li>
</ul>
<hr/>
"""

def index(request):
    return HttpResponse(layout+"""
            <h1> Inicio </h1>
        """)

def hola_mundo(request):
    return HttpResponse(layout+"""
            <h1>Hola mundo con DJango</h1>
        
        """)

def pagina(request):
    
    return HttpResponse(layout+"""
            <h1>Página de la web</h1>
            <h3>Creado por Alex Dehesa</h3>
        """)
    