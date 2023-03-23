from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField(max_length=4)
    author = models.CharField(max_length=30,null=True,blank=True)
    date = models.DateField(auto_now_add=True)