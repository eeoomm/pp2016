from django.contrib import admin
from .models import Post, Inves, Agenda
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('titulo','slug','fecha','publicado')
	list_filter = ('publicado','fecha')
	search_fields = ('titulo','cuerpo')
	prepopulated_fields = {'slug':('titulo',)}


class InvesAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'institucion', 'email', 'telefono', 'ext', 'celular', 'linea_de_investigacion', 'sni')
	
	search_fields = ('nombre','sni')
	prepopulated_fields = {'slug':('nombre',)}

class AgendaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'institucion_empresa', 'cargo', 'email', 'telefono', 'ext', 'celular', 'direccion', 'producto')
	
	search_fields = ('nombre','institucion_empresa')
	prepopulated_fields = {'slug':('nombre',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Inves, InvesAdmin)
admin.site.register(Agenda, AgendaAdmin)