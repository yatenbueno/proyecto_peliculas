from audioop import reverse
from cgitb import html
from re import template
from django.template import ContextPopException
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from proyecto.models import Resenia, Pelicula
from proyecto.forms import forms
from proyecto.views import pelicula

class AgregarCriticaView(CreateView):
   model = Resenia
   form_class = forms.ReseniaForm
   template_name = 'critica.html'

   def form_valid(self, form):
      form.instance.pelicula_id = self.kwargs['id_pelicula']
      return super().form_valid(form)

   # success_url = reverse_lazy('vista-pelicula', kwargs=['id_pelicula'] )