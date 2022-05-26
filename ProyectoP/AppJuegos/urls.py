
from django.urls import path
from.import views



urlpatterns = [

        
        path("juegos", views.juegos),
        path("",views.inicio , name="inicio"),
        path("listadejuegos",views.listadejuegos,name="listadejuegos"),
        path("login",views.login,name="login"),
        path("reviews",views.reviews , name="reviews"),
        path("acercademi",views.acercademi , name="acercademi"),
        path("contacto",views.contacto , name="contacto")
       

    
]
