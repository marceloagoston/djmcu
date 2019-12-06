from django.urls import path
from .views import (
ActivosListView,
ActivosUpdateView,
ActivosDetailView,
ActivosDeleteView,
)

urlpatterns = [
	path('', ActivosListView.as_view(), name='lista_activos'),
	path('<int:pk>/', ActivosDetailView.as_view(), name='detalle_activo'),
	path('<int:pk>/editar/', ActivosUpdateView.as_view(), name='editar_activo'),
	path('<int:pk>/eliminar/', ActivosDeleteView.as_view(), name='eliminar_activo'),
]