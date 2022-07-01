from cgitb import html
from re import template
from django.template import ContextPopException
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from proyecto.models import Pelicula

class BaseView(TemplateView):
   template_name = "base.html"
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context[''] = None
      return context