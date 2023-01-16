from django.contrib import admin

# Register your models here.
from .models import Movie, MovieInstance, Director, Genre

admin.site.register(Movie)
admin.site.register(MovieInstance)
admin.site.register(Director)
admin.site.register(Genre)
