from django.contrib import admin
from .models import Activos, Amenazas, HistoricoAmenazas

class ActivoAdmin(admin.ModelAdmin):
	model = Activos
	list_display = ['TAid','resp_seguridad','date','tipoactivo','nombre','propietario','responsable','ubicacion','valor',]
	list_filter = ['resp_seguridad','tipoactivo',]
	search_fields = ['resp_seguridad__username','tipoactivo',]

class AmenazaAdmin(admin.ModelAdmin):
	model = Amenazas
	list_display = ['id_Amenaza','activo','amenaza','probabilidad','impacto','riesgo',]
	list_filter = ['activo__resp_seguridad','probabilidad','impacto','activo__nombre','activo__TAid',]
	search_fields = ['activo__nombre','activo__TAid',]

class HistoricoAmenazaaAdmin(admin.ModelAdmin):
	model = HistoricoAmenazas
	list_display = ['id_fk_amenaza','riesgoAnterior']
	# list_filter = ['id_f_amenaza__activo','id_f_amenaza',]
	# search_fields = ['id_f_amenaza','nombre_amenaza','riesgo',]

admin.site.register(Activos, ActivoAdmin)
admin.site.register(Amenazas, AmenazaAdmin)
admin.site.register(HistoricoAmenazas, HistoricoAmenazaaAdmin)