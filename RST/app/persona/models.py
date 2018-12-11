from django.db import models
from ..usuario.models import Tienda,Usuario
# Create your models here.
class Persona(models.Model):
	nit			 = models.CharField(max_length=15,primary_key=True)
	nombre 		 = models.CharField(max_length=250)
	direccion	 = models.CharField(max_length=500)
	def __unicode__(self):
		return self.nit+""
	def __str__(self):
		return self.nit+""

class Cliente(models.Model):
	persona = models.ForeignKey(Persona,on_delete=models.DO_NOTHING)
	tienda  = models.ForeignKey(Tienda,on_delete=models.DO_NOTHING)
	atiende = models.ForeignKey(Usuario,on_delete=models.DO_NOTHING,null=True)
	credito = models.DecimalField(max_digits=100,decimal_places=2,default=0)
	dias 	= models.IntegerField(default=0)
	def __unicode__(self):
		return self.persona.nit+""
	def __str__(self):
		return self.persona.nit+""


class Proveedor(models.Model):
	tienda  = models.ForeignKey(Tienda,on_delete=models.DO_NOTHING)
	persona = models.ForeignKey(Persona,on_delete=models.DO_NOTHING)
	credito = models.DecimalField(max_digits=100,decimal_places=2,default=0)
	dias 	= models.IntegerField(default=0)
	def __unicode__(self):
		return self.persona.nit+""
	def __str__(self):
		return self.persona.nit+""
