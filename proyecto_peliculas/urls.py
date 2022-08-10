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
from proyecto.views import ActorView, DirectorView, BaseView, PeliculaView, ComentarioView, AgregarCriticaView, PeliculasView, BusquedaView, HomeView, PaginatePeliculaView, PaginateActoresView, PaginateDirectoresView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(),name='vista-home'),
    path('admin/', admin.site.urls),
    path('actor/<int:id_actor>', ActorView.as_view(),name='vista-actor'),
    path('director/<int:id_director>', DirectorView.as_view(),name='vista-director'),
    path('pelicula/<int:id_pelicula>', PeliculaView.as_view(), name='vista-pelicula'),
    path('peliculas/', PaginatePeliculaView,name='vista-peliculas'),
    path('actores/', PaginateActoresView,name='vista-actores'),
    path('directores/', PaginateDirectoresView,name='vista-directores'),
    path('busqueda/', BusquedaView,name='vista-busqueda'),
    path('pelicula/<int:id_pelicula>/critica/', AgregarCriticaView.as_view(),name='vista-critica'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
