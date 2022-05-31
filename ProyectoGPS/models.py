from django.db import models
from django.forms import IntegerField
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    

class Egresados(models.Model):
    
    carreras= (
        ('IBQ', 'Ingeniería Bioquimica'),
        ('IEN', 'Ingeniería Electrónica'),
        ('IE', 'Ingeniería Eléctrica'),
        ('II', 'Ingeniería Industrial'),
        ('IMT', 'Ingeniería Mecatrónica'),
        ('IM', 'Ingeniería Mecánica'),
        ('IGE', 'Ingeniería en Gestión Empresarial'),
        ('IMR', 'Ingeniería en Materiales'),
        ('ISC', 'Ingeniería en Sistemas Computacionales'),
        ('ITIC', 'Ingeniería en Tecnologias de la Informacion y Comunicaciones'),
        ('CP', 'Contador Público'),
        ('A', 'Administración'),    
    )
    user= models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
    nombre=models.CharField(max_length=50)
    apellido_m=models.CharField(max_length=25)
    apellido_p=models.CharField(max_length=25)
    email=models.EmailField('Email address', unique=True)
    fech_naci=models.DateField(null=True)
    carrera=models.CharField(max_length=4, choices=carreras)



    def __str__(self):
        return self.nombre



class Personales(models.Model):
    sexos= (
        ('M', 'Mujer'),
        ('H', 'Hombre'),   
    )
    id_em=models.ForeignKey('Egresados', on_delete=models.CASCADE)
    edad=models.IntegerField(blank=True, null=True)
    sexo=models.CharField(max_length=2, choices=sexos, blank=True, null=True)
    ciudad_radica=models.CharField(max_length=25, blank=True, null=True)
    ciudad_origen=models.CharField(max_length=25,blank=True, null=True)


class Profesional(models.Model):
    
    id_em=models.ForeignKey('Egresados', on_delete=models.CASCADE)
    empleo_actual=models.CharField(max_length=50)
    empleo_previ=models.CharField(max_length=50)

    def __str__(self):
        return self.empleo_actual

class Educacion(models.Model):
    id_em=models.ForeignKey('Egresados', on_delete=models.CASCADE)
    Univer=models.CharField(max_length=50)
