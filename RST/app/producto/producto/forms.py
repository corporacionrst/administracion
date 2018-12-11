from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Marca,Producto


class MarcaForm(ModelForm):
	class Meta:
		model = Marca
		fields = ['nombre']
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['nombre'].widget.attrs.update({'class': 'form-control'})

class ProductoForm(ModelForm):
	class Meta:
		model=Producto
		fields=[
			'codigo',
			'descripcion',
			'marca'
			]
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['codigo'].widget.attrs.update({'class': 'form-control'})
		self.fields['descripcion'].widget.attrs.update({'class': 'form-control'})
		self.fields['marca'].widget.attrs.update({'class': 'form-control'})