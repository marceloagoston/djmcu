from django.urls import path
from .views import (
ActivosListView,
ActivosUpdateView,
ActivosDetailView,
ActivosDeleteView,
ActivoCreateView,
TipoActivosListView,
ActivosListView,
AmenazasListView,
)

urlpatterns = [
	path('', ActivosListView.as_view(), name='lista_activos'),
	path('categorias/', TipoActivosListView.as_view(), name='categorias_activo'),
	path('<int:pk>/', ActivosDetailView.as_view(), name='detalle_activo'),
	path('<int:pk>/editar/', ActivosUpdateView.as_view(), name='editar_activo'),
	path('<int:pk>/eliminar/', ActivosDeleteView.as_view(), name='eliminar_activo'),
	path('nuevoactivo/', ActivoCreateView.as_view(), name='nuevo_activo'),
	path('amenazas/', AmenazasListView.as_view(), name='lista_amenazas'),
]