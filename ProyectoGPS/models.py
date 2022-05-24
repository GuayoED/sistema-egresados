from django.db import models
from django.forms import IntegerField

# Create your models here.

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
    
    nombre=models.CharField(max_length=50)
    apellido_m=models.CharField(max_length=25)
    apellido_p=models.CharField(max_length=25)
    email=models.EmailField()
    fech_naci=models.DateField()
    carrera=models.CharField(max_length=4, choices=carreras)

    def __str__(self):
        return self.nombre


class Usuarios(models.Model):
    email=models.ForeignKey('Egresados', on_delete=models.CASCADE)
    password=models.CharField(max_length=30)


class Personales(models.Model):
    sexos= (
        ('M', 'Mujer'),
        ('H', 'Hombre'),   
    )
    nombre=models.ForeignKey('Egresados', on_delete=models.CASCADE)
    apellido_m=models.CharField(max_length=25)
    apellido_p=models.CharField(max_length=25)
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
    carrera=models.ForeignKey('Egresados', on_delete=models.CASCADE)
    Univer=models.CharField(max_length=50)
