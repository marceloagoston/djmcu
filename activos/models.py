from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Activo(models.Model):
	#ID del activo
	TAid = models.AutoField(primary_key=True)
	date = models.DateTimeField(auto_now_add=True)
	# representante de seguridad
	resp_seguridad = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
	)
	tipo = [
    ('SW', 'Software'),
    ('HW', 'Hardware'),
    ('INF', 'Informació'),
    ('RRHH', 'RRHH'),
    ('SC', 'Servicios Contratados'),
	]

	tipoactivo = models.CharField(max_length=20,choices=tipo,default='SW')
	nombre=models.CharField(max_length=100,blank=False)
	descripcion=models.TextField(blank=False)
	propietario=models.CharField(max_length=100,blank=False)
	responsable=models.CharField(max_length=100,blank=False)
	ubicacion=models.CharField(max_length=100,blank=False)
	valor=models.CharField(max_length=20,blank=False)

	riesgo = [
    ('Leve','1'),
    ('Leve','2'),
    ('Grave','4'),
    ('Crítico','5'),
    ('Crítico','6'),
	]

	valor = models.CharField(max_length=7,
                  choices=riesgo,
                  default='1')

	def __str__(self):
		return 'ID: '+str(self.TAid)+' '+self.tipoactivo+' '+self.nombre+' '+self.propietario+' '+self.valor

	def get_absolute_url(self):
		return reverse('lista_activos')

	