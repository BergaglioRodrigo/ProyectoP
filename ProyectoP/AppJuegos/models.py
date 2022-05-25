from django.db import models

# Create your models here.
class Juegos (models.Model):

    nombre=models.CharField(max_length=40)
    desarrollador=models.CharField(max_length=40)
    genero=models.CharField(max_length=40)
    lanzamiento=models.DateField()
    puntuacion=models.IntegerField()