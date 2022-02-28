
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from .models import Destination

# Create your views here.

def index(request):
    name = Destination.objects.all()
    return render(request,'index.html',{'name':name})

def About(request):
    return render(request,'About.html')

