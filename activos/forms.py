from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Amenaza

class NuevaAmenazaForm(forms.ModelForm):
	class Meta:
		model = Amenaza
		fields = ('amenaza', 'probabilidad', 'impacto',)