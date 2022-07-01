from cgitb import html
from re import template
from django.shortcuts import render
from django.template import ContextPopException
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from proyecto.models import Pelicula, Actor, Director
from itertools import chain

def BusquedaView(request):
   if request.method == 'POST':
      searched = request.POST['searched']
      filtros_peliculas = Pelicula.objects.filter(nombre__contains=searched)
      filtros_actores = Actor.objects.filter(nombre__contains=searched)
      filtros_directores = Director.objects.filter(nombre__contains=searched)
      filtro_universal = chain(filtros_peliculas, filtros_actores, filtros_directores)
      return render(request, 'busqueda.html',
         {'searched':searched,
          'filtros':filtro_universal})
   else:
      return render(request, 'busqueda.html',
         {})