from cgitb import html
from re import template
from django.template import ContextPopException
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from proyecto.models import Director, Pelicula

class DirectorView(TemplateView):
   template_name = "director.html"
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['director'] = Director.objects.get(id=self.kwargs['id_director'])
      context['peliculas'] = Pelicula.objects.filter(director = context['director'])
      return context