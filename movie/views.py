from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie
from .forms import ReviewPost

# Create your views here.


def homepage(request):
    return render(request, template_name='homepage.html')


class Homepage(ListView):

    model = Movie
    template_name = 'movies/movies.html'
    
    context_object_name = 'movies'
    queryset = Movie.objects.filter(draft=False)

    # def get(self, request, *args, **kwargs):

    #     movies = Movie.objects.all()

    #     context = {
    #         'movies': movies
    #     }

    #     return render(request, 'movies/movies.html', context=context)


class HomepageDetail(DetailView):

    model = Movie


    slug_field = 'url'

    template_name = 'movies/movie_detail.html'

    # def get(self, request, slug):

    #     movie = Movie.objects.get(url=slug)

    #     context = {
    #         'movie': movie
    #     }

    #     return render(request, 'movies/movie_detail.html', context=context)


class PostComment(View):

    def post(self, request, pk):
        form = ReviewPost(request.POST)
        if form.is_valid():
            movie = Movie.objects.get(id=pk)
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                print(request.POST.get('parent'))
                form.parent_id = int(request.POST.get('parent'))
            form.movie = movie
            form.save()
        print(request.POST)
        return redirect(movie.get_absolute_url())
