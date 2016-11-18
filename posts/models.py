from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model):
	titulo = models.CharField(max_length=140)
	fecha = models.DateTimeField(auto_now=True)
	cuerpo = models.TextField()
	publicado = models.BooleanField(default=False)
	imagen = models.ImageField(upload_to="imagenes",blank=True,null=True)
	slug = models.SlugField(max_length=500,blank=True,null=True)

	def __str__(self):
		return self.titulo

	def get_absolute_url(self):
		return reverse('detalle',args=[self.slug])

class Inves(models.Model):
	nombre = models.CharField(max_length=140)
	institucion = models.CharField(max_length=140)
	
	email = models.CharField(max_length=140)
	telefono = models.IntegerField()
	ext = models.IntegerField(blank=True, null=True)
	celular = models.IntegerField(blank=True, null=True)
	linea_de_investigacion = models.TextField()
	fecha = models.DateTimeField(auto_now=True)
	sni = models.CharField(blank=True, null=True,max_length=140)
	slug = models.SlugField(max_length=500,blank=True,null=True)

	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse('con',args=[self.slug])

class Agenda(models.Model):
	nombre = models.CharField(max_length=140)
	institucion_empresa = models.CharField(max_length=140)
	cargo = models.CharField(max_length=140)
	email = models.CharField(max_length=140)
	telefono = models.IntegerField()
	ext = models.IntegerField(blank=True, null=True)
	celular = models.IntegerField(blank=True, null=True)
	direccion = models.TextField(blank=True, null=True)
	fecha = models.DateTimeField(auto_now=True)
	producto = models.CharField(blank=True, null=True,max_length=140)
	slug = models.SlugField(max_length=500,blank=True,null=True)

	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse('agenda',args=[self.slug])