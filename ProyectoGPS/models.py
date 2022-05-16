from django.db import models

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
    email=models.EmailField()
    password=models.CharField(max_length=30)
    
