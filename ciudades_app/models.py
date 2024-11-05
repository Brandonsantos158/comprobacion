from django.db import models

# Create your models here.                       # UNO A MUCHOS
class Region(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    ordinal = models.CharField(max_length=3, null=True)

class Ciudad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    poblacion = models.IntegerField(default=0)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)