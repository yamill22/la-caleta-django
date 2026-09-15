from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')

def detalle(request):
    return render(request, 'detalle.html')