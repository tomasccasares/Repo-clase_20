from django.shortcuts import render
from app_c20.models import Estudiante

def estudiante(request):
    contexto = {}
    contexto['estudiante'] = Estudiante.objects.all()
    return render(request, 'app_c20/index.html', contexto)
    