from django.http import JsonResponse
from django.shortcuts import render

from .models import movies


# Create your views here.
def movie_list(request):
    movie = movies.objects.all()
    data = {
        'movie': list(movie.values())
    }
    return JsonResponse(data)
