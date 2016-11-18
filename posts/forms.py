from django import forms
from .models import Post, Inves, Agenda


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['titulo','cuerpo','imagen']

class InvesForm(forms.ModelForm):
	class Meta:
		model = Inves
		fields = ['nombre', 'institucion', 'email', 'telefono', 'ext', 'celular', 'linea_de_investigacion', 'sni']

class AgendaForm(forms.ModelForm):
	class Meta:
		model = Agenda
		fields = ['nombre', 'institucion_empresa', 'cargo', 'email', 'telefono', 'ext', 'celular', 'direccion', 'producto']