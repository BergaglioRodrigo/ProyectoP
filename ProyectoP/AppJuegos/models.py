from django.db import models

class Cargarlistadejuegos (models.Model):
    nombre=models.CharField(max_length=40)
    desarrollador=models.CharField(max_length=40)
    genero=models.CharField(max_length=40)
    lanzamiento=models.DateField()
    puntuacion=models.IntegerField()# Create your models here.




class Juegos (models.Model):

    nombre=models.CharField(max_length=40)
    desarrollador=models.CharField(max_length=40)
    genero=models.CharField(max_length=40)
    lanzamiento=models.DateField()
    puntuacion=models.IntegerField()




class Altajuego(models.Model):
    nombre=models.CharField(max_length=40)
    desarrollador=models.CharField(max_length=40)
    genero=models.CharField(max_length=40)


class Trucos(models.Model):
    juego=models.CharField(max_length=40)
    codigo=models.CharField(max_length=40)
    accion=models.CharField(max_length=40)




