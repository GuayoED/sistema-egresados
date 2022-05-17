from django.contrib import admin


from ProyectoGPS.models import Egresados, Personales, Profesional, Educacion

# Register your models here.

class EgresadosAdmin(admin.ModelAdmin):
    list_display=( "id" , "nombre", "apellido_m", "apellido_p", "carrera")
    search_fields=("nombre",)

admin.site.register(Egresados, EgresadosAdmin)

admin.site.register(Personales)

admin.site.register(Profesional)


admin.site.register(Educacion)
