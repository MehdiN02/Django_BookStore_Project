from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):  # sakht modelemon baraye zakhire dar database
    age = models.PositiveIntegerField(null=True, blank=True)
