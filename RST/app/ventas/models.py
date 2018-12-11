from django.db import models

from ..usuario.models import Usuario,Tienda
from ..producto.producto.models import Codigo
from ..persona.models import  Proveedor, Cliente
# Create your models here.
class Historial(models.Model):
	tienda   	 	= models.ForeignKey(Tienda,on_delete=models.CASCADE)
	usuario 	 	= models.ForeignKey(Usuario,on_delete=models.DO_NOTHING)
	fecha		 	= models.DateField()
	credito			= models.BooleanField(default=False)
	total			= models.DecimalField(max_digits=100,decimal_places=2,default=0)
	listado			= models.ManyToManyField(Codigo)
	hoja			= models.IntegerField(default=0)
	

class Orden(models.Model):
	proveedor		= models.ForeignKey(Proveedor,on_delete=models.DO_NOTHING,blank=True,null=True)
	autoriza 	 	= models.ForeignKey(Usuario,on_delete=models.DO_NOTHING,related_name="autoriza_compra",blank=True,null=True)
	descripcion		= models.CharField(max_length=200,default="")
	autorizacion 	= models.BooleanField(default=False)
	enviado			= models.BooleanField(default=False)
	documento 		= models.ForeignKey(Historial,on_delete=models.CASCADE)
	osbservacion	= models.CharField(max_length=2000,default="")

class Compra(models.Model):
	orden	 		= models.ForeignKey(Orden,on_delete=models.DO_NOTHING)
	fecha			= models.DateField()
	documento		= models.CharField(max_length=200)

class Venta(models.Model):
	fecha		 	= models.DateField()
	cliente 		= models.ForeignKey(Cliente,on_delete=models.DO_NOTHING,blank=True,null=True)
	autoriza 	 	= models.ForeignKey(Usuario,on_delete=models.DO_NOTHING,blank=True,null=True,related_name="autoriza_venta")
	autorizacion 	= models.BooleanField(default=False)
	envio			= models.BooleanField(default=False)
	documento 		= models.ForeignKey(Historial,on_delete=models.CASCADE)

class Factura(models.Model):
	serie			= models.CharField(max_length=20)
	numero			= models.IntegerField()
	documento 		= models.ForeignKey(Venta,on_delete=models.DO_NOTHING)
	

	


	