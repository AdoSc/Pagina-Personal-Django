from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Proyecto(models.Model):
    titulo=models.CharField(max_length=200, verbose_name='Título del proyecto')
    descripcion=models.TextField(verbose_name='Descripción del proyecto')
    imagen=models.ImageField(verbose_name='Imagen del proyecto', upload_to="ProyectosWeb")
    creado=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación del proyecto')
    actualizado=models.DateTimeField(auto_now=True, verbose_name='Última actualización del proyecto')

    class Meta:
        verbose_name = 'ProyectoWeb'
        verbose_name_plural = 'ProyectosWeb'
        ordering = ['-creado']
    def __str__(self):
        return self.titulo
