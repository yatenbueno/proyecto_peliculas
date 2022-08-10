from cgitb import html
from re import template
from django.shortcuts import render
from django.template import ContextPopException
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from proyecto.models import Pelicula, Actor, Director
from django.core.paginator import Paginator

def PaginatePeliculaView(request):
   listado_peliculas = Pelicula.objects.all().order_by('nombre')
   paginator = Paginator(listado_peliculas, 8)
   pagina = request.GET.get("page") or 1
   peliculas = paginator.get_page(pagina)
   pagina_actual = int(pagina)
   paginas = range(1, peliculas.paginator.num_pages + 1)
   return render(request, "peliculas.html", {"peliculas":peliculas,
                                             "paginas":paginas,
                                             "pagina_actual":pagina_actual})

def PaginateActoresView(request):
   listado_actores = Actor.objects.all().order_by('nombre')
   paginator = Paginator(listado_actores, 8)
   pagina = request.GET.get("page") or 1
   actores = paginator.get_page(pagina)
   pagina_actual = int(pagina)
   paginas = range(1, actores.paginator.num_pages + 1)
   return render(request, "actores.html", {"actores":actores,
                                             "paginas":paginas,
                                             "pagina_actual":pagina_actual})

def PaginateDirectoresView(request):
   listado_directores = Director.objects.all().order_by('nombre')
   paginator = Paginator(listado_directores, 8)
   pagina = request.GET.get("page") or 1
   directores = paginator.get_page(pagina)
   pagina_actual = int(pagina)
   paginas = range(1, directores.paginator.num_pages + 1)
   return render(request, "directores.html", {"directores":directores,
                                             "paginas":paginas,
                                             "pagina_actual":pagina_actual})