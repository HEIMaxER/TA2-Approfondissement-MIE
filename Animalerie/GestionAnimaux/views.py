from django.shortcuts import render
from .models import Animal, Equipement
from .controleur import *


# Create your views here.

def home(request):
    animaux = Animal.objects.all()

    return render(request, 'home.html', {'animaux': animaux })