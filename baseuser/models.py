from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to= 'users/', blank=True)



