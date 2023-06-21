from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Olá Django - index')

def ola(request):
    #return HttpResponse('Olá Django')#
    return render(request, 'index.html')

# Create your views here.
