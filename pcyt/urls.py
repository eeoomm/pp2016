"""pcyt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from posts import views
from django.views.static import serve
from django.conf import settings
from accounts import urls as cuentasUrls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^noticias/(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name="detalle"),
    url(r'^listinv/', views.ListInvView.as_view(), name='inv'),
    url(r'^agenda/', views.AgendaView.as_view(), name='agenda'),
    url(r'^noticias/', views.ListView.as_view(), name='noti'),
    url(r'^nuevo/$', views.UpdateView.as_view(), name="nuevo"),
    url(r'^newinv/$', views.UpdateInvView.as_view(), name="newinv"),
    url(r'^nuevagn/$', views.UpdateAgeView.as_view(), name="nuevagen"),
    url(r'^$', views.List1View.as_view(), name="con"),
    url(r'^planta/', views.List2View.as_view(), name="planta"),
    url(r'^contacto/', views.List3View.as_view(), name="contacto"),
    url(r'^organigrama/', views.List4View.as_view(), name="organi"),
    url(r'^manuale_de_opereacion/', views.List5View.as_view(), name="ope"),
    url(r'^manual_de_procedimiento/', views.List6View.as_view(), name="pro"),
    url(r'^matriz_de_identificacion/', views.List7View.as_view(), name="idef"),
    url(r'^antecedentes/', views.AntecedenteView.as_view(), name="antecedentes"),
    url(r'^funciones/', views.FuncionesView.as_view(), name="funciones"),
    url(r'^mision_y_vision/', views.MisionView.as_view(), name="mision"),
    url(r'^objetivo/', views.ObjetivoView.as_view(), name="objetivo"),
    url(r'^accounts/',include(cuentasUrls)),
    url(
        regex=r'^imagenes/(?P<path>.*)/$',
        view=serve,
        kwargs={"document_root":settings.MEDIA_ROOT}
        )
]
