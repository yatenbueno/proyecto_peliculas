from ast import For
from django.urls import reverse
from django.db import models
from proyecto_peliculas import settings
from django.contrib import admin
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Persona(models.Model):
   nombre = models.CharField(max_length=30, null=False)
   apellido = models.CharField(max_length=30, null=False)
   nacionalidad = models.CharField(max_length=30, null=False)
   anio_nacimiento = models.DateField(verbose_name='año nacimiento')
   resumen_biografico = models.CharField(max_length=300)

   def __str__(self) -> str:
      return f"{self.nombre} {self.apellido}, {self.nacionalidad}, {self.anio_nacimiento}" 

class Actor(Persona):
   foto = models.ImageField(blank=True, upload_to='actores/',verbose_name="foto")

class Director(Persona):
   foto = models.ImageField(blank=True, upload_to='directores/',verbose_name="foto")

class PeliculaManager(models.Manager):
   def get_10_mejores_peliculas(self):
      return self.all().order_by('-puntaje')[:12]
      # return self.all()[0]

class Pelicula(models.Model):
   objects = PeliculaManager()
   nombre = models.CharField(max_length=60, null=False)
   resumen = models.CharField(max_length=500, null=False)
   anio_realizacion = models.IntegerField(verbose_name='año realizacion')
   actores = models.ManyToManyField(Actor, related_name="pelicula")
   director = models.ForeignKey(Director, related_name="pelicula", on_delete=models.CASCADE)
   puntaje = models.IntegerField(blank=True, null=True)
   foto = models.ImageField(blank=True, upload_to='peliculas/',verbose_name="foto")

   def __str__(self):
       return self.nombre

   def calcularPuntaje(self):
      resenias = self.reseñas.all()
      cantidad = 0
      puntaje = 0
      for resenia in resenias:
         cantidad += 1
         puntaje += resenia.puntaje
      self.puntaje = puntaje/cantidad if cantidad > 0 else 0
      self.save()

class Resenia(models.Model):
   comentario = models.CharField(max_length=300, verbose_name="comentario")
   puntaje = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="puntaje")
   pelicula = models.ForeignKey(Pelicula, related_name="reseñas", on_delete=models.CASCADE, verbose_name="pelicula")
   email_usuario = models.EmailField(default="random@email.com", max_length=255, verbose_name="email")
   nombre_usuario = models.CharField(default="Anonimo", max_length=150, verbose_name="nombre")
   estado_resenia = models.BooleanField(default=False, verbose_name="estado")
   

   def __str__(self):
       return self.pelicula.nombre + ' - Puntaje: ' + str(self.puntaje)

   def get_absolute_url(self):
      return reverse('vista-pelicula', args=(str(self.pelicula.id)))

   def save(self) :
      a= super().save()
      self.pelicula.calcularPuntaje()
      return a

   