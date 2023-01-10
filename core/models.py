from django.db import models

# Create your models here.

class ContacUs(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    # number = models.IntegerField(max_length=30)
    message = models.TextField(max_length=200)
