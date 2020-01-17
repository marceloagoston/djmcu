from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser
	list_display = ['email','username','edad','dependencia','is_staff',]

admin.site.register(CustomUser, CustomUserAdmin)
# Personalizado del Backend
admin.site.site_header = 'Seguridad Chaco - Panel de Administración'
admin.site.site_title = 'Seguridad Chaco'
admin.site.index_title = 'Panel de Administración'