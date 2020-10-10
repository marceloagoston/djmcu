from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Amenazas, Activos

class NuevaAmenazaForm(forms.ModelForm):
	class Meta:
		model = Amenazas
		fields = ('amenaza', 'probabilidad', 'impacto',)

class UpdateActivoForm(forms.ModelForm):

    class Meta:
        model = Activos
        fields = ('tipoactivo','nombre','descripcion','propietario','ubicacion','valor','informe')