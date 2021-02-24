from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def meteoAffichage(request):
    return render(request,'meteo/meteo.html')