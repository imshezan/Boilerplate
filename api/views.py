from django.shortcuts import render
from .models import *

def index(request):
    info = "Welcome to my blog"
    title = "Home"
   
    context = {
        'title': title,
        'info': info,
    }
    return render(request, 'index.html', context)