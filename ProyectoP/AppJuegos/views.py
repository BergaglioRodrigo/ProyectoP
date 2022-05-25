from django.http import HttpResponse
from django.shortcuts import render
from AppJuegos.models import Juegos
from django.template import loader
# Create your views here.




  



def juegos (request):
    juegos = Juegos.objects.all()
    dicc = {"juegos":juegos}
    plantilla = loader.get_template("plantillaprueba.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)




