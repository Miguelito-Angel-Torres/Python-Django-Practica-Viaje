from django.shortcuts import render
from .models import Turismo

def home(request):
    turismo= Turismo.objects.all()
    return render(request, 'ProyectoWeb/home.html',{"turismos":turismo})
