from django.db import models

# Create your models here.

class Producto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30) #varchar
    precio = models.FloatField(default=0)   #float
    stock = models.IntegerField(default=0)    #int


class Cliente(models.Model):
    id = models.BigAutoField(primary_key=True)  
    nombre = models.CharField(max_length=50)   #varchar
    direccion = models.CharField(max_length=100) #varchar
    habilitados = models.BooleanField(null=True, default=0) #boolean

    producto = models.ManyToManyField(Producto)  #relacion n..m  (relacion muchos a muchos) 
                                                 
class Credencial(models.Model):
    id = models.BigAutoField(primary_key=True)  
    serie = models.CharField(max_length=20)      #varchar
    fecha_emision = models.DateField(null=True)  #fecha


    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE) # 1..1 (relacion 1 a 1)