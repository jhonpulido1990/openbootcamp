from django.db import models
from django.urls import reverse
from uuid import uuid4

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=64, help_text='agrga el nombre del genero')

    def __str__(self) -> str:
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100, help_text='titulo de la pelicula')
    Release = models.DateField(null=True, blank=True)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=100, help_text='descripcion de la pelicula')
    company = models.CharField(max_length=100, help_text='agrega el nombre de la compañia de produccion')
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie-detail', args=[str(self.id)])

class MovieInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, help_text='ID unico para cada pelicula')
    movie = models.ForeignKey('movie', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '%s (%s)' % (self.id, self.movie.title)

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reversed('director-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)
