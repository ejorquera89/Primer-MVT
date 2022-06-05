from django.shortcuts import render
from .models import Hermanos, Padres, Tios
# Create your views here.

def hermanos(request):
    hermanos_ficha = Hermanos.objects.all()
    return render(request, 'Hermanos.html', {'hermanos': hermanos_ficha}) 

def padres(request):
    padres_ficha = Padres.objects.all()
    return render(request, 'Padres.html', {'padres': padres_ficha})

def tios(request):
    tios_ficha = Tios.objects.all()
    return render(request, 'Tios.html', {'tios': tios_ficha})


