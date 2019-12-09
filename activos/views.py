from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Activo

class ActivosListView(LoginRequiredMixin, ListView):
	model = Activo
	template_name = 'activos_detail.html'
	context_object_name = 'activos'
	login_url = 'login'

class ActivosDetailView(LoginRequiredMixin, DetailView):
	model = Activo
	template_name = 'activo_detail.html'
	context_object_name = 'activo'
	login_url = 'login'

class ActivosUpdateView(LoginRequiredMixin, UpdateView):
	model = Activo
	fields = ('tipoactivo', 'nombre','descripcion','propietario','ubicacion','valor')
	template_name = 'editaractivo.html'
	context_object_name = 'activo'
	login_url = 'login'

	def dispatch(self, request, *args, **kwargs): # new
		obj = self.get_object()
		if obj.resp_seguridad != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)
# para que solo el autor pueda editar el activo
class ActivosDeleteView(LoginRequiredMixin, DeleteView):
	model = Activo
	template_name = 'eliminaractivo.html'
	success_url = reverse_lazy('lista_activos')
	context_object_name = 'activo'
	login_url = 'login'
	# para que solo el autor pueda eliminar el activo
	def dispatch(self, request, *args, **kwargs): # new
		obj = self.get_object()
		if obj.resp_seguridad != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)

# usamos mixin para evitar que un usuario no logueado acceda a la vista.
class ActivoCreateView(LoginRequiredMixin, CreateView):
	model = Activo
	template_name = 'nuevoact.html'
	fields = ('tipoactivo', 'nombre','descripcion','propietario','responsable','ubicacion','valor')
	login_url = 'login'
	# eliminamos de arriba el campo usuario y con la función de abajo decimos que el usuario logueado es el autor
	def form_valid(self, form):
		form.instance.resp_seguridad = self.request.user
		return super().form_valid(form)