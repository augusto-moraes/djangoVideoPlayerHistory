from django.shortcuts import render, HttpResponseRedirect
from .forms import formUrl
from .models import modelUrl

def index(request):
    history = modelUrl.objects.all()
    return render(request,'history.html', {'history':history})

def add(request):
    if request.method == 'POST':
        form = formUrl(request.POST)
        if form.is_valid():
            model = modelUrl()
            model.save()
            return HttpResponseRedirect('/')
    else:
        form = formUrl()

    return render(request,'add.html', {'form':form})
