import django_filters
from .models import Activo

class ActivosFilter(django_filters.FilterSet):

	# CHOICES = (

	# 	('ascending', 'Ascending'),
	# 	('descending', 'Descending'), 

	# 	)

	# ordering = django_filters.ChoiceFilter(label='Ordering', choices='CHOICES', method='filter_by_ordering')

	class Meta:
		model = Activo
		fields = ('tipoactivo',)

	# def filter_by_ordering(self, queryset, name, value):
	# 	expression = 'date' if value == 'ascending' else '-date'
	# 	return queryset.order_by(expression)	