import email
from turtle import st
from django.conf import settings
from django.shortcuts import render, HttpResponse, redirect


#Vistas generiacas de django
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#Importamos los modelos

from .models import Egresados, Educacion, Personales, Profesional

# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse, reverse_lazy
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
 
# Habilitamos los formularios en Django
from .forms import profileForm, createUserForm


# Aqui emepizan las vistas

#Vista par listar algun modelo

class EgresadosListado(ListView):
    model = Egresados

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        e = Egresados.objects.all()
        r = Profesional.objects.filter(id_em_id = self.request.user.pk - 1)
        context['profesional_list'] = r
        return context

def listar(request):

    egre = Egresados.objects.all()

    pro = Profesional.objects.all()

    context = {

        'egre':egre,
        'pro':pro,
        
    }

    return render(request, 'ProyectoGPS/egresado.html', context=context)

    
#Vista especial para mostrar los detalles de dos modeleos
class EgresadosDetalle( LoginRequiredMixin, DetailView):
    model = Egresados   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profesional_list'] = Profesional.objects.all()
        return context

#Vista especial para mostrar los detalles de un modelo
class EgreDetalle( DetailView):
    model = Egresados   

def detalle(request,pk):

    egre = Egresados.objects.filter(id=pk)

    pro = Profesional.objects.filter(id=pk)

    per = Personales.objects.filter(id=pk)

    edu = Educacion.objects.filter(id=pk)

    context = {

        'egre':egre,
        'pro':pro,
        'per':per,
        'edu':edu,
        
    }

    return render(request, 'ProyectoGPS/detalle.html', context=context)  

          

#Vista para crear un registro de un modelo

class EgresadosCrear(SuccessMessageMixin, CreateView):
    model = Egresados
    form = Egresados
    fields = "__all__"
    success_message = 'Egreasdo creado correctamente'

    def get_success_url(self):
        return reverse('leer')

class EgresadosRegistro(SuccessMessageMixin, CreateView):
    model = Egresados
    form = Egresados
    fields = "__all__"
    success_message = 'Egreasdo registrado correctamente'

    def get_success_url(self):
        return reverse('leer')



#Vista para actualizar un registro de un modelo

class EgresadosActualizar(SuccessMessageMixin, UpdateView):
    model = Egresados
    form = Egresados
    fields = "__all__"
    success_message = 'Egreasdo actualizado correctamente'

    def get_success_url(self):
        return reverse('leer')


#Vista para eliminar un registro de un modelo
class EgresadosEliminar(SuccessMessageMixin, DeleteView): 
    model = Egresados 
    form = Egresados
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro 
    def get_success_url(self): 
        success_message = 'Egresado Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

#Esta vista maneja el envio de emails
def contacto(request):

    if request.method=="POST":

        subject=request.POST["emaill"]

        email_from=settings.EMAIL_HOST_USER

        return render(request, "password_reset_done.html")

#Esta vista maneja el registro de usuarios
def registerPage(request):
        form = "Dummy String"
        profile_form = "Dummy String"
    
        form = createUserForm(request.POST)
        profile_form = profileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            messages.success(request,  'Your account has been successfully created')

            return redirect('login')

        context = {'form': form, 'profile_form': profile_form}
        return render(request, 'ProyectoGPS/register.html', context)

#Esta vista muestra el perfil del usuaruo
@method_decorator(login_required, name='dispatch')
class ProfileUpdate(TemplateView):
    template_name = "ProyectoGPS/profile_form.html"

#Esta vista maneja la edicion de los datos del usuario
@method_decorator(login_required, name='dispatch')
class ProfileUpdatePersonales(UpdateView):
    model = Personales

    def get_object(self):
        profile, created = Personales.objects.get_or_create(id_em_id = self.request.user.pk - 1)
        return profile
    fields = [ 'edad', 'sexo', 'ciudad_radica', 'ciudad_origen']
    success_url = reverse_lazy('profile')

    template_name = "ProyectoGPS/profile_form_personales.html"

@method_decorator(login_required, name='dispatch')
class ProfileUpdateProfesional(UpdateView):
    model = Profesional

    def get_object(self):
        profile, created = Profesional.objects.get_or_create(id_em_id = self.request.user.pk - 1)
        return profile
    fields = [ 'empleo_actual', 'empleo_previ']
    success_url = reverse_lazy('profile')

    template_name = "ProyectoGPS/profile_form_profesionales.html"

@method_decorator(login_required, name='dispatch')
class ProfileUpdateEducacion(UpdateView):
    model = Educacion

    def get_object(self):
        profile, created = Educacion.objects.get_or_create(id_em_id = self.request.user.pk - 1)
        return profile
    fields = [ 'Univer', ]
    success_url = reverse_lazy('profile')

    template_name = "ProyectoGPS/profile_form_educacion.html"




