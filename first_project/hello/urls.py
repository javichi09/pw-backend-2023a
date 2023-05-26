#Importar una biblioteca 
#admisitradora de rutas
from django.urls import path

# Importando vistas
from . import  views

# Declarando las rutas valias
urlpatterns = [
#GET /hello/    
path("", views.index, name="index")
#GET/Hello/author
path("author/", views.author, name="author")

] 