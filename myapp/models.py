from django.db import models
from django.contrib.auth.models import AbstractUser

class Custom_User(AbstractUser):
    DOB = models.DateField(null=True)

    class Meta:
        verbose_name = 'Custom_User'
