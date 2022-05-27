import re
from django.http import HttpResponse
from django.shortcuts import render
from AppJuegos.models import Altajuego, Juegos, Trucos
from django.template import loader
from AppJuegos.forms import Formulario_trucos, Juegos_formulario
from AppJuegos.forms import Formulario_listajuegos
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

def trucos(request):
    listatrucos= Trucos.objects.all()
    dicc={"listatrucos":listatrucos}
    plantilla = loader.get_template("trucos.html")
    documento=plantilla.render(dicc)
    return HttpResponse(documento)   




   # return render (request  ,"listadejuegos.html")

def altajuego(request):
    altajuego=Altajuego.objects.all()
    dicc={"altajuego":altajuego}
    plantilla = loader.get_template("proximasreviews.html")
    documento=plantilla.render(dicc)
    return HttpResponse(documento)  




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





"""
def juegos_formulario(request):

    if request.method =="POST":
    

        mi_formulario = Juegos_formulario(request.POST)

        if mi_formulario.is_valid():
            print(mi_formulario.cleaned_data)

"""



def agregarjuegos(request):

    if request.method == "POST":

        juegos_formulario = Juegos_formulario(request.POST)

        if juegos_formulario.is_valid():
            print(juegos_formulario.cleaned_data)


        juego=Altajuego(nombre=request.POST['nombre'],desarrollador=request.POST['desarrollador'],genero=request.POST['genero'])
        juego.save()
        return render (request,"formulariojuegos.html")

    return render (request,"formulariojuegos.html")    





def agregarlistajuegos(request):

    if request.method == "POST":

        formulario_listajuegos = Formulario_listajuegos (request.POST)

        if formulario_listajuegos.is_valid():
            print(formulario_listajuegos.cleaned_data)


        listajuego=Juegos(nombre=request.POST['nombre'],desarrollador=request.POST['desarrollador'],genero=request.POST['genero'],lanzamiento=request.POST['lanzamiento'],puntuacion=request.POST['puntuacion'])
        listajuego.save()
        return render (request,"formularioaltajuegos.html")

    return render (request,"formularioaltajuegos.html")



def agregartrucos(request):

    if request.method == "POST":

        formulario_trucos = Formulario_trucos(request.POST)

        if formulario_trucos.is_valid():
            print(formulario_trucos.cleaned_data)


        truco=Trucos(juego=request.POST['juego'],codigo=request.POST['codigo'],accion=request.POST['accion'])
        truco.save()
        return render (request,"formulariotrucos.html")

    return render (request,"formulariotrucos.html")        






def buscador(request):

    return render (request,"buscador.html")


def buscar(request):
    if request.GET ['nombre']:
        nombre = request.GET['nombre']
        game = Juegos.objects.filter(nombre__icontains = nombre) 
        return render (request,"resultadobusqueda.html",{"games":game})
    else:
        return HttpResponse("campo vacio")


     
   




  



