from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Activo, Amenaza, HistoricoAmenaza
from django.views import generic
from .filters import ActivosFilter, AmenazasFilter
from .forms import NuevaAmenazaForm

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.conf import settings
from django.db.models import Max


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
	fields = ('tipoactivo', 'nombre','descripcion','propietario','responsable','ubicacion','valor','informe',)
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

	def get_context_data(self, **kwargs):
		ctx = super().get_context_data(**kwargs)
		ctx['amenaza_activos'] = Amenaza.objects.filter(activo=self.kwargs['pk'])
		ctx['historico_amenaza'] = HistoricoAmenaza.objects.all()
		ctx['historico_ultimos'] = HistoricoAmenaza.objects.values('id_f_amenaza').annotate(Max('id'))
		# borrar
		print('PRUEBA nueva')
		print('-----------------------------')
		print(ctx['historico_amenaza'])
		return ctx

	def dispatch(self, request, *args, **kwargs):
		obj = self.get_object()
		if obj.resp_seguridad != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)

class ActivosUpdateView(LoginRequiredMixin, UpdateView):
	model = Activo
	fields = ('tipoactivo', 'nombre','descripcion','propietario','ubicacion','valor','informe',)
	template_name = 'editaractivo.html'
	context_object_name = 'activo'
	login_url = 'login'

	def dispatch(self, request, *args, **kwargs): # new
		obj = self.get_object()
		if obj.resp_seguridad != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)

	def upload_image_view(request):
	    if request.method == 'POST':
	        form = UpdateActivoForm(request.POST, request.FILES)
	        if form.is_valid():
	            form.save()
	            message = "¡¡Archivo subido exitosamente!!"
	    else:
	        form = UpdateActivoForm()

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

class AmenazasListView(LoginRequiredMixin, ListView):
	model = Amenaza
	template_name = 'amenazas/amenazas_detail.html'
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
	form_class = NuevaAmenazaForm
	template_name = 'amenazas/nueva_amenaza.html'
	context_object_name = 'amen'
	login_url = 'login'
	success_url = reverse_lazy('lista_activos')
	# eliminamos de arriba el campo usuario y con la función de abajo decimos que el usuario logueado es el autor
	def form_valid(self, form):
		form.instance.resp_seguridad = self.request.user
		f = form.save(commit=False)
		f.activo = Activo.objects.get(TAid=self.kwargs['pk'])
		return super(AmenazasCreateView, self).form_valid(form)

class AmenazasUpdateView(LoginRequiredMixin, UpdateView):
	model = Amenaza
	fields = ('amenaza','probabilidad','impacto',)
	template_name = 'amenazas/editaramenaza.html'
	success_url = reverse_lazy('detalle_activo')
	context_object_name = 'amenaza'
	login_url = 'login'

	def get_success_url(self):
	 	amen_act=Amenaza.objects.filter(id_Amenaza=self.kwargs['pk']).get()
	 	return reverse_lazy('detalle_activo',args={amen_act.activo.pk})

# para que solo el autor pueda editar el activo
	def dispatch(self, request, *args, **kwargs):
		obj = self.get_object()
		if obj.activo.resp_seguridad != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)

# DETAIL

class AmenazasDetailView(LoginRequiredMixin, DetailView):
	model = Amenaza
	template_name = 'amenazas/amenaza_detail.html'
	context_object_name = 'amenazas'
	login_url = 'login'
	def dispatch(self, request, *args, **kwargs):
		obj = self.get_object()
		if obj.activo.resp_seguridad != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)

class AmenazasDeleteView(LoginRequiredMixin, DeleteView):
	model = Amenaza
	template_name = 'amenazas/eliminar_amenaza.html'
	success_url = reverse_lazy('lista_amenazas')
	context_object_name = 'amenaza'
	login_url = 'login'
	# para que solo el autor pueda eliminar el activo
	def dispatch(self, request, *args, **kwargs): # new
		obj = self.get_object()
		if obj.activo.resp_seguridad != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)


# Historico

class HistAmenazasListView(LoginRequiredMixin, DetailView):
	pass
	# model = HistoricoAmenaza
	# template_name = 'amenazas/hist_amenaza_detail.html'
	# context_object_name = 'amenazas'
	# login_url = 'login'
	# def dispatch(self, request, *args, **kwargs):
	# 	obj = self.get_object()
	# 	if obj.activo.resp_seguridad != self.request.user:
	# 		raise PermissionDenied
	# 	return super().dispatch(request, *args, **kwargs)