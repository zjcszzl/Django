from django.urls import path
from . import views

# movies/
# movies/1/details

app_name = 'movies'

urlpatterns = [
    # root of the app, relative urls
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail')
]
