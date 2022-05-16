from django.contrib import admin


from ProyectoGPS.models import Egresados

# Register your models here.

class EgresadosAdmin(admin.ModelAdmin):
    list_display=("nombre", "apellido_m", "apellido_p", "carrera")
    search_fields=("nombre",)

admin.site.register(Egresados, EgresadosAdmin)
