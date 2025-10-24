from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE
    )
    occupation = models.CharField(max_length=256, blank=True)
    phone = models.CharField(max_length=16, blank=True)
