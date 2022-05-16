from django.shortcuts import render, HttpResponse


#Vistas generiacas de django
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#Importamos el modelo 

from .models import Egresados

# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms

# Create your views here.

class EgresadosListado(ListView):
    queryset = Egresados.objects.all()


class EgresadosDetalle(DetailView):
    model = Egresados   


class EgresadosCrear(SuccessMessageMixin, CreateView):
    model = Egresados
    form = Egresados
    fields = "__all__"
    success_message = 'Egreasdo creado correctamente'

    def get_success_url(self):
        return reverse('leer')





class EgresadosActualizar(SuccessMessageMixin, UpdateView):
    model = Egresados
    form = Egresados
    fields = "__all__"
    success_message = 'Egreasdo actualizado correctamente'

    def get_success_url(self):
        return reverse('leer')



class EgresadosEliminar(SuccessMessageMixin, DeleteView): 
    model = Egresados 
    form = Egresados
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Egresado Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'


def home(request):

    return render(request, "ProyectoGPS/home.html")


def egresados(request):

    return render(request, "ProyectoGPS/egresados.html")


def busqueda(request):

    return render(request, "ProyectoGPS/busqueda.html")

def contacto(request):

    return render(request, "ProyectoGPS/contacto.html")
