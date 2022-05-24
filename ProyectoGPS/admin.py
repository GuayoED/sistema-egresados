from django.contrib import admin


from ProyectoGPS.models import Egresados, Personales, Profesional, Educacion

# Register your models here.

class EgresadosAdmin(admin.ModelAdmin):
    list_display=( "id" , "nombre", "apellido_m", "apellido_p", "carrera")
    search_fields=("nombre",)

admin.site.register(Egresados, EgresadosAdmin)

admin.site.register(Personales)

class ProfesionalAdmin(admin.ModelAdmin):
    list_display=( "id" , "id_em", "empleo_actual")
    search_fields=("nombre",)


admin.site.register(Profesional, ProfesionalAdmin)


admin.site.register(Educacion)
