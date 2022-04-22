from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, "ProyectoGPS/home.html")


def egresados(request):

    return render(request, "ProyectoGPS/egresados.html")


def busqueda(request):

    return render(request, "ProyectoGPS/busqueda.html")

def contacto(request):

    return render(request, "ProyectoGPS/contacto.html")
