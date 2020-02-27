from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Amenaza, Activo

class NuevaAmenazaForm(forms.ModelForm):
	class Meta:
		model = Amenaza
		fields = ('amenaza', 'probabilidad', 'impacto',)

class UpdateActivoForm(forms.ModelForm):

    class Meta:
        model = Activo
        fields = ('tipoactivo','nombre','descripcion','propietario','ubicacion','valor','informe')