from cgitb import html
from re import template
from django.template import ContextPopException
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from proyecto.models import Actor, Pelicula

class ActorView(TemplateView):
   template_name = "actor.html"
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['actor'] = Actor.objects.get(id = self.kwargs['id_actor'])
      context['peliculas'] = Pelicula.objects.filter(actores = context['actor'])
      return context
