from django.db import models

# Create your models here.
class Persona(models.Model):
    id = models.BigAutoField(primary_key=True) #clave primaria 
    nombre = models.CharField(max_length=50)   #colocacion de varchar
    edad = models.IntegerField()
    hibilitada = models.BooleanField(null=True, default=0)
    fecha_nacimientos = models.DateField(null=True)
    