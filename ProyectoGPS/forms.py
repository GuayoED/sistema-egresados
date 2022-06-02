import email
from django.contrib.auth import get_user_model 
#User = get_user_model()
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Egresados, User



class createUserForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

    class Meta:
        model = User
        # Note - include all *required* CustomUser fields here,
        # but don't need to include password1 and password2 as they are
        # already included since they are defined above.
        fields = ("email", "username")

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            msg = "Passwords don't match"
            raise forms.ValidationError("Password mismatch")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


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