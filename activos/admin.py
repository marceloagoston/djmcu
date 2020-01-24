from django.contrib import admin
from .models import Activo, Amenaza

class ActivoAdmin(admin.ModelAdmin):
	model = Activo
	list_display = ['TAid','resp_seguridad','date','tipoactivo','nombre','propietario','responsable','ubicacion','valor',]
	list_filter = ['resp_seguridad','tipoactivo',]
	search_fields = ['resp_seguridad__username','tipoactivo',]

class AmenazaAdmin(admin.ModelAdmin):
	model = Amenaza
	list_display = ['id_Amenaza','activo','amenaza','probabilidad','impacto','riesgo',]
	list_filter = ['probabilidad','impacto',]

admin.site.register(Activo, ActivoAdmin)
admin.site.register(Amenaza, AmenazaAdmin)