from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=32)
    addr = models.CharField(max_length=32)
    # email = models.EmailField(null=True)