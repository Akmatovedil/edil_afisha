from django.shortcuts import render, HttpResponse
from datetime import datetime

# Create your views here.

def about_us(request):
    return render(request, 'about_us.html')

def date_now(request):
    return render(request, 'date_now.html')
