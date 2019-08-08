from django.db import models

# Create your models here.
class Book(models.Model):
    bookname = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    press = models.CharField(max_length=64)
