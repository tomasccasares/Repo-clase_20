from django.contrib import admin
from django.urls import path
from app_manejador_contenido.views import home, profile

urlpatterns = [
    path('home/', home),
    path('profile/', profile)    
]
