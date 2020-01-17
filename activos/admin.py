from django.contrib import admin
from .models import Activo

class ActivoAdmin(admin.ModelAdmin):
	model = Activo
	list_display = ['TAid','resp_seguridad','date','tipoactivo','nombre','propietario','responsable','ubicacion','valor',]
	list_filter = ['resp_seguridad','tipoactivo',]
	search_fields = ['resp_seguridad__username','tipoactivo',]

admin.site.register(Activo, ActivoAdmin)