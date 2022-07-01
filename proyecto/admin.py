from django.contrib import admin
from .models import Actor, Director, Pelicula, Resenia
from django.utils.html import format_html
# Register your models here.

class ActorAdmin(admin.ModelAdmin): 

   ordering = ('apellido',)

   search_fields = ('nombre',
                    'apellido',
                    'anio_nacimiento',
                    'nacionalidad',)

   list_filter = ('anio_nacimiento',
                  'nacionalidad',)

   list_display = ('imagen',
                   'nombre',
                   'apellido',
                   'anio_nacimiento',
                   )
                  
   def imagen(self, obj):
      return format_html('<img src={} />'.format(obj.foto.url))
   



class DirectorAdmin(admin.ModelAdmin):
   ordering = ('apellido',)
   search_fields = ('nombre','apellido','anio_nacimiento','nacionalidad',)
   list_filter = ('anio_nacimiento', 'nacionalidad',)
class PeliculaAdmin(admin.ModelAdmin):
   ordering = ('nombre',)
   search_fields = ('nombre','puntaje','anio_realizacion',)
   list_filter = ('anio_realizacion','puntaje')
class ReseniaAdmin(admin.ModelAdmin):
   ordering = ('puntaje',)
   search_fields = ('puntaje','pelicula',)
   list_filter = ('puntaje','pelicula',)

admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(Resenia, ReseniaAdmin)