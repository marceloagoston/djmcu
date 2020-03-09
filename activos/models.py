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
    ('INF', 'Información'),
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
	informe = models.FileField(blank=True,null=True,upload_to="documentos/%Y/%m/")

	riesgo = [
    ('1','1'),
    ('2','2'),
    ('3','3'),
    # ('Crítico','5'),
    # ('Crítico','6'),
	]

	valor = models.CharField(max_length=7,
                  choices=riesgo,
                  default='1')

	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse('lista_activos')

	@property
	def informe_url(self):
	    if self.informe and hasattr(self.informe, 'url'):
	        return self.informe.url
from django.db.models.signals import post_save
class Amenaza(models.Model):
	id_Amenaza = models.AutoField(primary_key=True)
	# Restriccion de Clave con Activos
	activo = models.ForeignKey(Activo, on_delete=models.CASCADE, related_name='amenazas_activo')
	amenaza = models.CharField(max_length=100,blank=False, null=False)
	valores = [(1,1),(2,2),(3,3)]
	
	probabilidad = models.IntegerField(choices=valores,default=1)
	impacto = models.IntegerField(choices=valores,default=1)
	riesgo = models.IntegerField(blank=True, null=True)
	
	@property
	def riesgo(self):
		return self.probabilidad * self.impacto

	def __str__(self):
		return str(self.id_Amenaza)

def save_Amenaza(sender, instance, **kwargs):
	print('AGUARA TECH')

post_save.connect(save_Amenaza, sender=Amenaza)
class HistoricoAmenaza(models.Model):
	# el ID me lo da Django
	# Restriccion de Clave con Amenaza (entidad debil)
	id_f_amenaza = models.ForeignKey(Amenaza, on_delete=models.CASCADE)
	nombre_amenaza  = models.CharField(max_length=100,blank=False, null=False)
	valores = [(1,1),(2,2),(3,3)]
	
	probabilidad = models.IntegerField(choices=valores,default=1)
	impacto = models.IntegerField(choices=valores,default=1)
	riesgo = models.IntegerField(blank=True, null=True)
	
	@property
	def riesgo(self):
		return self.probabilidad * self.impacto

	def __str__(self):
		return str(self.id)