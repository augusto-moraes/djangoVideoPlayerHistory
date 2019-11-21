from django.shortcuts import render, HttpResponseRedirect
from .models import inputUrl

def index(request):
    history = inputUrl.youtubeUrl
    return render(request,'history.html')

def add(request):
    if request.method == 'POST':
        form = inputUrl(request.POST)
        return HttpResponseRedirect('../')
    else:
        form = inputUrl()

    return render(request,'add.html', {'form':form})
