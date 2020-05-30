from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.


# Main page of the app
def index(request):
    movies = Movie.objects.all()         # SELECT * FROM movies_movie
    # output = ','.join([m.title for m in movies])
    # Movie.objects.filter(release_year = 1984)
    # Movie.objects.get(id=1)
    return render(request, 'index.html', {'movies': movies})
    # return HttpResponse(output)
