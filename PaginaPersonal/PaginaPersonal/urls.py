"""PaginaPersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from nucleo import views as vista_nucleo
from portafolio import views as vista_portafolio

from django.conf import settings

urlpatterns = [
    path('', vista_nucleo.Inicio, name="Inicio"),
    path('Acerca/', vista_nucleo.Acerca, name="Acerca"),
    path('Portafolio/', vista_portafolio.Portafolio, name="Portafolio"),
    path('Contacto/', vista_nucleo.Contacto, name="Contacto"),
    
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
