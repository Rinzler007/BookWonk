from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello( request ) :
    return render(request, 'members/login.html')

def index( request ):
    return render(request, 'members/index.html')