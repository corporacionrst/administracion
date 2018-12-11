from __future__ import unicode_literals

from django.db import models
from ...usuario.models import Tienda


class Marca(models.Model):
	nombre       = models.CharField(max_length=200)
	def __unicode__(self):
		return self.nombre+""
	def __str__(self):
		return self.nombre+""

class Producto(models.Model):
	codigo	     = models.CharField(max_length=200)
	descripcion  = models.CharField(max_length=1000)
	marca 		 = models.ForeignKey(Marca, on_delete=models.CASCADE)
	def __unicode__(self):
		return self.codigo+""
	def __str__(self):
		return self.codigo+""

class Combinacion(models.Model):
	producto     = models.ForeignKey(Producto,on_delete=models.CASCADE)
	cantidad     = models.IntegerField()
	def __unicode__(self):
		return self.producto.codigo+""
	def __str__(self):
		return self.producto.codigo+""

class Imagen(models.Model):
	nombre		 = models.CharField(max_length=200)
	imagen 		 = models.FileField(null=True,blank=True)
	def __unicode__(self):
		return self.nombre+""
	def __str__(self):
		return self.nombre+""


class Detalle(models.Model):
	tipo 		 = models.CharField(max_length=200)
	info		 = models.CharField(max_length=500)
	def __unicode__(self):
		return self.tipo+":"+self.info
	def __str__(self):
		return self.tipo+":"+self.info

class TipoDeProducto(models.Model):
	nombre 		 = models.CharField(max_length=50)
	detalle		 = models.CharField(max_length=300)
	def __unicode__(self):
		return self.nombre
	def __str__(self):
		return self.nombre

class Lista(models.Model):
	producto 	 = models.OneToOneField(Producto,on_delete=models.CASCADE,related_name="producto")
	combinacion  = models.ManyToManyField(Combinacion)
	tipo 		 = models.ForeignKey(TipoDeProducto,on_delete=models.CASCADE,null=True,blank=True)
	imagenes 	 = models.ManyToManyField(Imagen)
	detalles	 = models.ManyToManyField(Detalle)
	def __unicode__(self):
		return self.producto.codigo+""
	def __str__(self):
		return self.producto.codigo+""

class Codigo(models.Model):
	producto 	 = models.ForeignKey(Lista,on_delete=models.CASCADE,related_name="producto_a_lista")
	cantidad 	 = models.DecimalField(max_digits=100,decimal_places=2,default=0)
	precio		 = models.DecimalField(max_digits=100,decimal_places=2,default=0,null=True)
	def __unicode__(self):
		return str(self.cantidad)+":"+self.producto.producto.codigo+":"+str(self.precio)
	def __str__(self):
		return str(self.cantidad)+":"+self.producto.producto.codigo+":"+str(self.precio)
class Inventario(models.Model):
	tienda 		 = models.ForeignKey(Tienda,on_delete=models.CASCADE)
	producto 	 = models.ForeignKey(Lista,on_delete=models.CASCADE)
	cantidad	 = models.IntegerField()
	costo		 = models.DecimalField(max_digits=100,decimal_places=2,default=0,null=True)
	distribuidor = models.DecimalField(max_digits=100,decimal_places=2,default=0,null=True)
	mayorista	 = models.DecimalField(max_digits=100,decimal_places=2,default=0,null=True)
	efectivo	 = models.DecimalField(max_digits=100,decimal_places=2,default=0,null=True)
	tarjeta		 = models.DecimalField(max_digits=100,decimal_places=2,default=0,null=True)
	
	