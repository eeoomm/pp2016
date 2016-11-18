from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post, Inves, Agenda
from .forms import PostForm, InvesForm, AgendaForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify


# Create your views here.
class ListView(View):
	def get(self,request):
		template_name ='lista.html'
		posts = Post.objects.all()
		context={
			'posts':posts
		}
		return render (request,template_name,context)


class DetailView(View):
	def get(self,request,slug):
		template_name = 'detalle.html'
		post = Post.objects.get(slug=slug)
		
		context = {
		'post':post,
		

	}
		return render(request,template_name,context)

class ListInvView(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name ='listainv.html'
		posts = Inves.objects.all()
		context={
			'posts':posts
		}
		return render (request,template_name,context)


class AgendaView(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name ='agenda.html'
		posts = Agenda.objects.all()
		context={
			'posts':posts
		}
		return render (request,template_name,context)

class UpdateView(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = 'nuevo.html'
		form = PostForm()
		context = {
		'form':form,
		}
		return render(request,template_name,context)

	def post(self,request):
		form = PostForm(request.POST,request.FILES)
		new_post = form.save(commit=False)
		new_post.slug = slugify(new_post.titulo)
		new_post.save()
		return redirect('noti')


class UpdateInvView(View):
	def get(self,request):
		template_name = 'newinves.html'
		form = InvesForm()
		context = {
		'form':form,
		}
		return render(request,template_name,context)

	def post(self,request):
		form = InvesForm(request.POST,request.FILES)
		new_post = form.save(commit=False)
		new_post.slug = slugify(new_post.nombre)
		new_post.save()
		return redirect('con')

class UpdateAgeView(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = 'nueagen.html'
		form = AgendaForm()
		context = {
		'form':form,
		}
		return render(request,template_name,context)

	def post(self,request):
		form = AgendaForm(request.POST,request.FILES)
		new_post = form.save(commit=False)
		new_post.slug = slugify(new_post.nombre)
		new_post.save()
		return redirect('agenda')

class List1View(View):
	
	def get(self,request):
		template_name = 'con.html'
		return render(request,template_name)


class List2View(View):
	def get(self,request):
		template_name = 'planta.html'
		return render(request,template_name)


class List3View(View):
	def get(self,request):
		template_name = 'contacto.html'
		return render(request,template_name)

class List4View(View):
	def get(self,request):
		template_name = 'organigrama.html'
		return render(request,template_name)

class List5View(View):
	def get(self,request):
		template_name = 'opera.html'
		return render(request,template_name)


class List6View(View):
	def get(self,request):
		template_name = 'proced.html'
		return render(request,template_name)

class List7View(View):
	def get(self,request):
		template_name = 'identifi.html'
		return render(request,template_name)

class AntecedenteView(View):
	def get(self,request):
		template_name = 'antece.html'
		return render(request,template_name)

class FuncionesView(View):
	def get(self,request):
		template_name = 'funcion.html'
		return render(request,template_name)


class MisionView(View):
	def get(self,request):
		template_name = 'mision.html'
		return render(request,template_name)

class ObjetivoView(View):
	def get(self,request):
		template_name = 'obje.html'
		return render(request,template_name)

