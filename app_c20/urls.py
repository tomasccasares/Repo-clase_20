
from django.contrib import admin
from django.urls import path
from app_c20.views import estudiante

urlpatterns = [
    path('estudiante/', estudiante)    
]
