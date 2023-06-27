from django.db import models

# Create your models here.
class Programmer(models.Model): 
     nombre = models.CharField(max_length=100)
     alias = models.CharField(max_length=50)
     edad = models.PositiveSmallIntegerField
     activo = models.BooleanField(default = True)