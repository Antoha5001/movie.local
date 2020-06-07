from django.contrib import admin

from .models import Category, Actor, Ganre, Movie, StarRatings, Rating, MovieScene, Review

admin.site.register((
    Category, 
    Actor, 
    Ganre, 
    Movie, 
    StarRatings, 
    Rating, 
    MovieScene, 
    Review
    ))

# admin.site.register(Category)
# admin.site.register(Actor)
# Register your models here.
