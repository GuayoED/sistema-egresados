from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Egresados

class createUserForm(UserCreationForm):
    class meta:
        model = User
        fields = ['username', 'password1', 'password2']


class profileForm(forms.ModelForm):
    class Meta:
        model = Egresados
        fields = ['nombre', 'apellido_m', 'apellido_p', 'email', 'fech_naci', 'carrera', ]
#The labels attribute is optional. It is used to define the labels of the form fields created   
        labels = {
                "nombre": _("Nombre"),
                "apellido_m": _("Apellido Materno"),
                "apellido_p": _("Apellido Paterno"),
                "email": _("Correo Electronico"),
                "fech_naci": _("Fecha de nacimiento"),
                "carrera": _("Carrera"),
                }