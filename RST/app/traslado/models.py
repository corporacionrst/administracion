from django.db import models

from ..usuario.models import Usuario,Tienda
from ..producto.producto.models import Codigo

class Traslados(models.Model):
	tienda_solicita = models.ForeignKey(Tienda,on_delete=models.DO_NOTHING,related_name="tienda_solicita")
	tienda_recibe   = models.ForeignKey(Tienda,on_delete=models.DO_NOTHING,related_name="tienda_recibe")
	fecha			= models.DateField()
	solicita 		= models.ForeignKey(Usuario,on_delete=models.DO_NOTHING,related_name="solicita")
	despacha 		= models.ForeignKey(Usuario,on_delete=models.DO_NOTHING,related_name="despachada",null=True,blank=True)
	enviada 		= models.BooleanField(default=False)
	total			= models.DecimalField(max_digits=100,decimal_places=2,default=0,null=True)
	lista	 		= models.ManyToManyField(Codigo)
