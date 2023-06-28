from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html' )

def profesores(request):
    return render(request, 'dashboard/profesores.html' )
        
def material(request):
    return render(request, 'dashboard/material.html' )

def pedido(request):
    return render(request, 'dashboard/pedido.html' )