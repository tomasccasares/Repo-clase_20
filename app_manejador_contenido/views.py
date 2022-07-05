from django.shortcuts import render

def home(request):
    return render(request, 'app_manejador_contenido/home.html', {}) # pasar un contexto vacio: {}

def profile(request):
    return render(request, 'app_manejador_contenido/profile.html', {})

