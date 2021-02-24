from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def list_des_hotel(request):
    return render(request,'hotel/hotel.html')