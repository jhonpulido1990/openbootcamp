from django.shortcuts import render

# Create your views here.

from .models import Movie, MovieInstance, Director, Genre

def index(request):
    num_movies = Movie.objects.all().count()
    num_instance = MovieInstance.objects.all().count()
    num_directors = Director.objects.all().count()

    return render(
        request,
        'index.html',
        context={
            'num_movies': num_movies,
            'num_directors': num_directors,
            'num_instance': num_instance,
            'all_movies': Movie
        }
    )
