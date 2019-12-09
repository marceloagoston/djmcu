from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Activo

class ActivosListView(ListView):
	model = Activo
	template_name = 'activos_detail.html'
	context_object_name = 'activos'

class ActivosDetailView(DetailView): # new
	model = Activo
	template_name = 'activo_detail.html'
	context_object_name = 'activo'

class ActivosUpdateView(UpdateView): # new
	model = Activo
	fields = ('tipoactivo', 'nombre','descripcion','propietario','ubicacion','valor')
	template_name = 'editaractivo.html'
	context_object_name = 'activo'

class ActivosDeleteView(DeleteView):
	model = Activo
	template_name = 'eliminaractivo.html'
	success_url = reverse_lazy('lista_activos')
	context_object_name = 'activo'

class ActivoCreateView(CreateView):
	model = Activo
	template_name = 'nuevoact.html'
	fields = ('resp_seguridad', 'tipoactivo', 'nombre','descripcion','propietario','responsable','ubicacion','valor')