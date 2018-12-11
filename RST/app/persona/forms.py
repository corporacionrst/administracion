from django import forms
from .models import Persona

class PersonaForm(forms.Form):
	nit			= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nit'}))
	nombre		= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}))
	direccion 	= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Direccion'}))
	dias		= forms.DecimalField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Dias autorizados para cancelar el credito'}))
	credito 	= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Monto de credito disponible para gastar'}))
	