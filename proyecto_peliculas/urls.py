"""proyecto_peliculas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from proyecto.views import ActorView, BaseView, PeliculaView, BusquedaView, HomeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(),name='vista-home'),
    path('admin/', admin.site.urls),
    path('actor/<int:id_actor>', ActorView.as_view(),name='vista-actor'),
    path('director/<int:id_director>', ActorView.as_view(),name='vista-director'),
    path('pelicula/<int:id_pelicula>', PeliculaView.as_view(), name='vista-pelicula'),
    path('busqueda/', BusquedaView,name='busqueda'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
