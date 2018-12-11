from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Tienda(models.Model):
	nombre    = models.CharField(max_length=200)
	ubicacion = models.CharField(max_length=200)
	nit		  = models.CharField(max_length=30)
	telefono  = models.CharField(max_length=20)
	admin     = models.OneToOneField(User,on_delete=models.CASCADE,related_name="admin")
	def __unicode__(self):
		return self.nombre+""
	def __str__(self):
		return self.nombre+""


class Usuario(models.Model):
	usuario 	  			= models.OneToOneField(User,on_delete=models.CASCADE,related_name="usuario")
	nombre  	  			= models.CharField(max_length=200)
	apellido	  			= models.CharField(max_length=200)
	tienda  	  			= models.ForeignKey(Tienda,related_name="tienda_labora",on_delete=models.CASCADE,null=True)
	telefono	  			= models.CharField(max_length=20)
	email   	  			= models.CharField(max_length=300)
	birthday	  			= models.DateField()
	fecha_ingreso 			= models.DateField()
	cui     	  			= models.CharField(max_length=50)
	
	# ver los precios
	ver_costos				= models.BooleanField(default=False)
	ver_distribuidor		= models.BooleanField(default=False)
	ver_mayorista			= models.BooleanField(default=False)
	ver_efectivo			= models.BooleanField(default=False)
	ver_tarjeta				= models.BooleanField(default=False)



	# ADMINISTRADOR
	crear_usuario 			= models.BooleanField(default=False)

	crear_clientes			= models.BooleanField(default=False)
	modificar_clientes		= models.BooleanField(default=False)
	historial_clientes 		= models.BooleanField(default=False)
	autorizar_orden			= models.BooleanField(default=False)


	crear_proveedor			= models.BooleanField(default=False)
	# BODEGA
	crear_marca	  			= models.BooleanField(default=False)
	crear_producto			= models.BooleanField(default=False)
	combinar_productos		= models.BooleanField(default=False)
	cargar_compra			= models.BooleanField(default=False)
	solicitar_traslados		= models.BooleanField(default=False)
	autorizar_traslados		= models.BooleanField(default=False)
	listar_traslados		= models.BooleanField(default=False)
	# VENTAS
	orden_de_compra			= models.BooleanField(default=False)
	inventario 				= models.BooleanField(default=False)
	facturacion				= models.BooleanField(default=False)
	def __unicode__(self):
		return self.usuario.username+""
	def __str__(self):
		return self.usuario.username+""

	