from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
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

# Detail page for the movie selected


def detail(request, movie_id):
    '''
    try:
        movie = Movie.objects.get(id=movie_id)
        return render(request, 'detail.html', {'movie': movie})
    except Movie.DoesNotExist:
        raise Http404()
    '''
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'detail.html', {'movie': movie})
