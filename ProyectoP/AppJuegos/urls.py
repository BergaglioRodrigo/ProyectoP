
from django.urls import path
from.import views



urlpatterns = [

        
        path("juegos", views.juegos),
        path("",views.inicio , name="inicio"),
        path("listadejuegos",views.listadejuegos,name="listadejuegos"),
        path("login",views.login,name="login"),
        path("reviews",views.reviews , name="reviews"),
        path("acercademi",views.acercademi , name="acercademi"),
        path("contacto",views.contacto , name="contacto"),
        path("agregarjuegos",views.agregarjuegos,name="agregarjuegos"),
        path("proximasreviews",views.altajuego,name="proximasreviews"),
        path("buscador",views.buscador,name="buscador"),
        path("buscar",views.buscar),
        path("agregarlistajuegos",views.agregarlistajuegos),
        path("trucos",views.trucos,name="trucos"),
        path("agregartrucos",views.agregartrucos,name="agregartrucos")
       

    
]
