from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return HttpResponse("Home")


def egresados(request):

    return HttpResponse("Egresados")


def busqueda(request):

    return HttpResponse("Busqueda")

def contacto(request):

    return HttpResponse("Contacto")
