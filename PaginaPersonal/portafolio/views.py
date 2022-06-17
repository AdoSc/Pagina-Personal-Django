from django.shortcuts import render
from .models import Proyecto

# Create your views here.
# Esta vista fue traida desde las vistas de nucleo.
def Portafolio(request):
    proyecto = Proyecto.objects.all()
    return render(request, "portafolio/Portafolio.html", {'proyecto': proyecto})
