from django import forms


class Profile(forms.Form):
	nit=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nit','onchange':'check_nit()'}))
	nombre=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','Disabled':'true','placeholder':'Nombre',}))
	direccion=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Dirección','Disabled':'true'}))
	telefono=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Telefono (opcional)'}))
	email=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Correo electrónico (opcional)'}))
	dias_credito=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Días de crédito'}))
	monto_credito=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Monto autorizado'}))
	credito=forms.BooleanField(required=False)

class byNit(forms.Form):
	nit_a_registrar=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nit','onchange':'registrado()'}))
	nombre_a_registrar=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'nombre'}))
	direccion_a_registrar=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Dirección'}))
	telefono_a_registrar=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Telefono (opcional)'}))
	correo_a_registrar=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Correo electrónico (opcional)'}))
	credito=forms.BooleanField(required=False)

class Registrar(forms.Form):
	documento=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el numero del documento'}))
	fecha=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'yyyy-mm-dd',"type":"date"}))
	nit_a_registrar=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nit','onchange':'registrado()'}))
	nombre_a_registrar=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'nombre'}))
	direccion_a_registrar=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Dirección'}))
	telefono_a_registrar=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Telefono (opcional)'}))
	correo_a_registrar=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Correo electrónico (opcional)'}))
	credito=forms.BooleanField(required=False)
	