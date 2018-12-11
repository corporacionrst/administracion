from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario,Tienda
from django.forms import ModelForm

class TiendaForm(ModelForm):
	 class Meta:
	 	model = Tienda
	 	fields = ['nombre','ubicacion','nit','admin']

class UsuarioForm(UserCreationForm):
	nombre   		      	= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'nombre'}))
	apellido 		      	= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'apellido'}))
	telefono 		      	= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'telefono'}))
	cui 				  	= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Numero de DPI'}))
	email    		      	= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'mail@dominio.com'}))
	fecha_de_nacimiento   	= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'yy-mm-dddd','type':'date'}))
	fecha_ingreso         	= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'yy-mm-dddd','type':'date'}))
	# ver precios
	ver_costos				= forms.BooleanField(required=False)
	ver_distribuidor		= forms.BooleanField(required=False)
	ver_mayorista			= forms.BooleanField(required=False)
	ver_efectivo			= forms.BooleanField(required=False)
	ver_tarjeta				= forms.BooleanField(required=False)
	# Administrador
	crear_usuario		  	= forms.BooleanField(required=False)
	crear_clientes		  	= forms.BooleanField(required=False)
	modificar_clientes		= forms.BooleanField(required=False)
	historial_clientes		= forms.BooleanField(required=False)
	crear_proveedor 		= forms.BooleanField(required=False)
	autorizar_orden			= forms.BooleanField(required=False)
	# Bodega
	crear_marca			  	= forms.BooleanField(required=False)
	crear_producto		  	= forms.BooleanField(required=False)
	combinar_productos	  	= forms.BooleanField(required=False)
	cargar_compra		  	= forms.BooleanField(required=False)
	solicitar_traslados		= forms.BooleanField(required=False)
	autorizar_traslados		= forms.BooleanField(required=False)
	listar_traslados		= forms.BooleanField(required=False)
	# Ventas
	orden_de_compra		  	= forms.BooleanField(required=False)
	inventario 				= forms.BooleanField(required=False)
	facturacion				= forms.BooleanField(required=False)