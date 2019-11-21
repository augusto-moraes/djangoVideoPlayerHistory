from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request,'history.html')

def add():
    return render('add.html')
