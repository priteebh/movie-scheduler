from django.shortcuts import render
from .models import Movie, Genre
# Create your views here.


def movie_schedule(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()

    context = {
        'movies': movies,
        'genres': genres
    }

    return render(request, 'movies/movie_schedule.html', context)