from django import template
from movie.models import Category, Movie

register = template.Library()

@register.simple_tag()
def get_categories():
    '''Возвращает категории'''
    return Category.objects.all()


@register.inclusion_tag('movies/template_tags/last_movies.html')
def get_last_movies():
    '''Возвращает последние записи'''
    movies = Movie.objects.order_by('id')[:5]
    return {'last_movies' : movies}
