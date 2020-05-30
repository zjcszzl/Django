from django.urls import path
from . import views

# movies/
# movies/1/details

urlpatterns = [
    # root of the app, relative urls
    path('', views.index, name='index')
]
