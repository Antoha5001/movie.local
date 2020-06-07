from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie

# Create your views here.

def homepage(request):
    return render(request, template_name='homepage.html')



class Homepage(ListView):

    model=Movie

    template_name='movies/movies.html'
    
    context_object_name = 'movies'

    # def get(self, request, *args, **kwargs):

    #     movies = Movie.objects.all()

    #     context = {
    #         'movies': movies
    #     }

    #     return render(request, 'movies/movies.html', context=context)

class HomepageDetail(View):

    def get(self, request, slug):

        movie = Movie.objects.get(url=slug)

        context = {
            'movie': movie
        }

        return render(request, 'movies/movie_detail.html', context=context)