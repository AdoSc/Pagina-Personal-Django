from django.shortcuts import render, HttpResponse

# Create your views here.
#Aqui se pueden definir funciones en lenguaje Python.
#DSI E-Virtual - HASTA AQUI EN LECCION 6

html_pagina = """
    <h2>Mi pagina web</h2>
    <ul>
        <li><a href="/">Portada</a></li>
        <li><a href="/Acerca">Acerca de</a></li>
        <li><a href="/Portafolio">Portafolio</a></li>
        <li><a href="/Contacto">Contacto</a></li>
    </ul>
"""

def Inicio(request):
    #html_texto = "<h3>Aprendiendo a manejar servidores con VisualStudioCode</h3>"
    #for i in range(6):
    #    html_texto += "<h4>Tambien estoy aprendiendo Python</h4>"
    return render(request, "nucleo/Inicio.html")

def Acerca(request):
    return render(request, "nucleo/Acerca.html")

# La vista Portafolio(request): fue eliminada de vistas nucleo para ubicarla en la APP portafolio.

def Contacto(request):
    return render(request, "nucleo/Contacto.html")