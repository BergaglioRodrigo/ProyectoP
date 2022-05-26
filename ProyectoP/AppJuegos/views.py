from django.http import HttpResponse
from django.shortcuts import render
from AppJuegos.models import Juegos
from django.template import loader
# Create your views here.





  



def juegos (request):
    juegos = Juegos.objects.all()
    dicc = {"juegos":juegos}
    plantilla = loader.get_template("plantillatabla.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)



def listadejuegos(request):
    listadejuegos=Juegos.objects.all()
    dicc={"listadejuegos":listadejuegos}
    plantilla = loader.get_template("listadejuegos.html")
    documento=plantilla.render(dicc)
    return HttpResponse(documento)
   # return render (request  ,"listadejuegos.html")


def inicio(request):

    return render (request,"inicio.html")



def login(request):

    return render (request,"login.html")





def reviews(request):

    return render (request,"reviews.html")    




def acercademi(request):

    return render (request,"acercademi.html")    



def contacto(request):

    return render (request,"contacto.html")        