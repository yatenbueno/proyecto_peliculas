from django.contrib import admin
from .models import Actor, Director, Pelicula, Resenia
from django.utils.html import format_html
from django.utils.safestring import mark_safe
# Register your models here.

class ActorAdmin(admin.ModelAdmin): 

   readonly_fields = ['imagen',]

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

   list_display_links = ('imagen',
                         'nombre',
                         'apellido',
                        )

   list_per_page = 5

   def imagen(self, obj):
      return mark_safe('<img src={} width="115px" height="130px"/>'.format(obj.foto.url))


class DirectorAdmin(admin.ModelAdmin):
   readonly_fields = ['imagen',]

   ordering = ('apellido',
               )

   search_fields = ('nombre',
                    'apellido',
                    'anio_nacimiento',
                    'nacionalidad',
                    )
   list_filter = ('anio_nacimiento',
                  'nacionalidad',
                  )

   list_display = ('imagen',
                   'nombre',
                   'apellido',
                   'anio_nacimiento',
                   )

   list_display_links = ('imagen',
                         'nombre',
                         'apellido',
                        )

   list_per_page = 5

   def imagen(self, obj):
      return mark_safe('<img src={} width="115px" height="130px"/>'.format(obj.foto.url))

class PeliculaAdmin(admin.ModelAdmin):
   readonly_fields = ['imagen',]
   ordering = ('nombre',
               )
               
   search_fields = ('nombre',
                    'puntaje',
                    'anio_realizacion',
                    )
   list_filter = ('anio_realizacion',
                  'puntaje',
                  )

   list_display = ('imagen',
                   'nombre',
                   'anio_realizacion',
                   'puntaje',
                   )

   list_display_links = ('imagen',
                         'nombre',
                        )
               
   list_per_page = 5

   def imagen(self, obj):
      return mark_safe('<img src={} width="100px" height="130px"/>'.format(obj.foto.url))

class ReseniaAdmin(admin.ModelAdmin):
   ordering = ('puntaje',
               )
   search_fields = ('puntaje',
                    'pelicula',
                    )
   list_filter = ('puntaje',
                  'pelicula',
                  )

admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(Resenia, ReseniaAdmin)
