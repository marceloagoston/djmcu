import django_filters
from .models import Activo, Amenaza

class ActivosFilter(django_filters.FilterSet):

	# CHOICES = (

	# 	('ascending', 'Ascending'),
	# 	('descending', 'Descending')

	# 	)

	seleccion = (
	    ('ascending', 'Mas Antiguo'),
	    ('descending', 'Mas Nuevo'),
		)

	ordering = django_filters.ChoiceFilter(label='Ordernar: ', method='filter_by_order', choices=seleccion)

	class Meta:
		model = Activo
		fields =('tipoactivo',)

	def filter_by_order(self, queryset, name, value):
		expression = 'date' if value == 'ascending' else '-date'
		return queryset.order_by(expression)

class AmenazasFilter(django_filters.FilterSet):

	# FALTA EL FILTRO DE RIEGOS bajo, medio alto

	amenaza = django_filters.CharFilter(label='Nombre Amenaza', lookup_expr='icontains')

	activo__TAid = django_filters.NumberFilter(label='ID Activo')

	class Meta:
		model = Amenaza
		fields =() #aca puedo meterle campos del modelo

