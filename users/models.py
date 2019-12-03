from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
	edad = models.PositiveIntegerField(null=True, blank=True)
	dependencia = models.CharField(max_length=50)
