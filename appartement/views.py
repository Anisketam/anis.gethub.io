from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def list_des_appartements(request):
    return render(request,'appartement/appartement.html')