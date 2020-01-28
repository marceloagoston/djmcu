from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Activo, Amenaza
from django.views import generic
from .filters import ActivosFilter, AmenazasFilter

# esta clase esta al pedo me parece
class TipoActivosListView(LoginRequiredMixin ,ListView):
	model = Activo
	template_name = 'categorias.html'
	context_object_name = 'activos'
	login_url = 'login'


class ActivosListView(LoginRequiredMixin, ListView):
	model = Activo
	template_name = 'activos_detail.html'
	context_object_name = 'activos'
	login_url = 'login'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['filter'] = ActivosFilter(self.request.GET, queryset=self.get_queryset())
		return context

	def get_queryset(self):
		return Activo.objects.filter(resp_seguridad=self.request.user.id)
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

class ActivosDetailView(LoginRequiredMixin, DetailView):
	model = Activo
	template_name = 'activo_detail.html'
	context_object_name = 'activo'
	login_url = 'login'
	def dispatch(self, request, *args, **kwargs): # new
		obj = self.get_object()
		if obj.resp_seguridad != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)

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

# Vistas Amenazas

# !!!!! PROBAR QUE SOLO EL DUEÑO DE UN ACTIVO PUEDA BORRAR SUS AMENAZAS

class AmenazasListView(LoginRequiredMixin, ListView):
	model = Amenaza
	template_name = 'amenazas_detail.html'
	context_object_name = 'amenazas'
	login_url = 'login'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['filter'] = AmenazasFilter(self.request.GET, queryset=self.get_queryset())
		return context

	def get_queryset(self):
		return  Amenaza.objects.filter(activo__resp_seguridad=self.request.user.id)

class AmenazasCreateView(LoginRequiredMixin, CreateView):
	model = Amenaza
	template_name = 'nueva_amenaza.html'
	fields = ('id_Amenaza','amenaza','probabilidad','impacto',)
	login_url = 'login'
	success_url = reverse_lazy('lista_amenazas')
	# eliminamos de arriba el campo usuario y con la función de abajo decimos que el usuario logueado es el autor
	def form_valid(self, form):
		form.instance.resp_seguridad = self.request.user
		return super().form_valid(form)

	# def getActivoPk --> traer el PK de un activo que esta en la URL para guardarlo en el campo correspondiente

	# def getPKActivo(self, request, *args, **kwargs):
 #      self.activo = request.POST["parametro"]

class AmenazasUpdateView(LoginRequiredMixin, UpdateView):
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
class AmenazasDeleteView(LoginRequiredMixin, DeleteView):
	model = Amenaza
	template_name = 'eliminar_amenaza.html'
	success_url = reverse_lazy('lista_amenazas')
	context_object_name = 'amenaza'
	login_url = 'login'
	# para que solo el autor pueda eliminar el activo
	# def dispatch(self, request, *args, **kwargs): # new
	# 	obj = self.get_object()
	# 	if obj.resp_seguridad != self.request.user:
	# 		raise PermissionDenied
	# 	return super().dispatch(request, *args, **kwargs)


