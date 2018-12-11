from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import TemplateView
from ..usuario.models import Usuario

class index(TemplateView):
	plantilla="main/index.html"
	sitio="main/inicio.html"
	def get(self,request,*args,**kwargs):
		if not request.user.is_authenticated:
			context={

			}
			return render(request,self.plantilla,context)
		else:
			usu = Usuario.objects.filter(usuario=request.user)
			if usu.exists():
				usu=usu[0]
				head=""
				nav=""
				# administrador
				if usu.crear_usuario:
					return redirect('/admin')
			return redirect("/blocked")