"""egresado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include


from ProyectoGPS.views import  EgresadosDetalle , EgresadosCrear, EgresadosActualizar, EgresadosEliminar, EgresadosRegistro, EgreDetalle, ProfileUpdatePersonales, registerPage, ProfileUpdate 
from ProyectoGPS import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('egresados/', views.EgresadosListado.as_view(template_name = 'ProyectoGPS/egresado.html'), name='leer'),
    path('egresados/detalle/<int:pk>', EgresadosDetalle.as_view(template_name= 'ProyectoGPS/detalle.html'), name='detalles'),
    path('egresados/editar/<int:pk>', EgresadosActualizar.as_view(template_name= 'egresados/actualizar.html'), name='actualizar'),
    path('egresados/elminar/<int:pk>', EgresadosEliminar.as_view(), name='eliminar'),
    path('', EgresadosRegistro.as_view(template_name= 'ProyectoGPS/registro.html'), name='registro'),
    path('egresados/perfil', ProfileUpdate.as_view(), name='profile'),
    path('egresados/perfilPer', ProfileUpdatePersonales.as_view(), name='profilePersonal'),

    path('egresados/registrar', registerPage ),


    path('listar/', views.EgresadosListado.as_view(template_name = 'ProyectoGPS/index.html'), name='leerEjem'),
    path('listar/crear', EgresadosCrear.as_view(template_name= 'ProyectoGPS/crear.html'), name='crearEjem'), 
    path('listar/detalle/<int:pk>', EgreDetalle.as_view(template_name= 'ProyectoGPS/detalle.html'), name='detallesEjem'),
    path('listar/editar/<int:pk>', EgresadosActualizar.as_view(template_name = "ProyectoGPS/actualizar.html"), name='actualizarEjem'),
    path('listar/elimiar/<int:pk>', EgresadosEliminar.as_view(template_name = "ProyectoGPS/index.html"), name='eliminarEjem'),
 


]


urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    
]