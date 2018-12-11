from django.shortcuts import render


from ..logica.bodega import bodega
from django.views.generic import TemplateView
from django.contrib import messages

class index(TemplateView):
	plantilla="main/inicio.html"
	@bodega
	def get(self,request,head,nav,tienda,usu):
		context={
			"head":head,
			"nav":nav,
			"tienda":tienda,
		}
		return render(request,self.plantilla,context)
