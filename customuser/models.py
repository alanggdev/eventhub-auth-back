from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    full_name = models.CharField(null=True, max_length=50)
    is_provider = models.BooleanField(null=True)
    firebase_token = models.TextField(null=True, blank=True)