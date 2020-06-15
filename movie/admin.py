from django.contrib import admin

from django import forms
from ckeditor.widgets import CKEditorWidget
# from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import Category, Actor, Ganre, Movie, StarRatings, Rating, MovieScene, Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'description', 'url']
    list_display_links = ['id', 'name']

class ReviewInline(admin.TabularInline):
    model = Review
    readonly_fields = ('name', 'email')
    extra=1


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'description', 'age', 'get_image']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'description']
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height:60px;">')

    get_image.short_description = "Изображение"

# ==== Кадры из фильма ====
@admin.register(MovieScene)
class MovieSceneAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'description', 'movie', 'get_image']
    list_display_links = ['id', 'name']
    readonly_fields = ('get_image',)


    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="width:50px;height:60px;">')

    get_image.short_description = "Изображение"


class MovieSceneInline(admin.TabularInline):
    model = MovieScene
    # fields = ('get_image',)
    readonly_fields = ('get_image',)
    extra=0

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="width:100px;height:auto;">')

    get_image.short_description = "Изображение"


# ==== Жанры ====
@admin.register(Ganre)
class GanreAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'description', 'url']
    list_display_links = ['id', 'name']


# ==== Фильм ====

class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание",widget=CKEditorWidget())
    class Meta:
        model = Movie
        fields = '__all__'

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display = ['id', 'title', 'category', 'year', 'draft','url', 'get_image']
    list_display_links = ['id', 'title']
    list_editable = ('draft',)
    search_fields = ['title', 'description', 'category__name']

    form = MovieAdminForm

    # fields = (('title', 'tagline'),)

    fieldsets = (
        (None, {
            'fields' : (('title', 'tagline', 'draft'),('category','url'))
        }),
        (None, {
            'fields' : ('description',)
        }),
        (None, {
            'fields' : (('poster','get_image'),)
        }),
        (None, {
            'fields' : (('year','country'),)
        }),
        (None, {
            'fields' : (('director','actors','ganre'),)
        }),
        ('Бюджет и дата выхода', {
            'fields' : ('premiere_world',('budget','fees_usa','fees_world'),)
        }),
        )
        
    

    list_filter =  ['title', 'year', 'category']
    # raw_id_fields = ['category']

    save_on_top = True

    save_as = True


    inlines = [MovieSceneInline, ReviewInline, ]

    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.poster.url}" style="max-height:100px;">')

    get_image.short_description = "Изображение"



# ==== Отзывы ====
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ['name', 'email', 'parent', 'movie', 'text', ]
    readonly_fields = ('name', 'email')
    # list_display_links = ['id', 'title']
    # search_fields = ['title', 'description', 'category__name']

    # list_filter =  ['title', 'year', 'category']


admin.site.register((
    # Category, 
    # Movie, 
    StarRatings, 
    Rating, 
    ))

# admin.site.register(Category)
# admin.site.register(Actor)
# Register your models here.

admin.site.site_title = "Django Movies"
admin.site.site_header = "Django Movies"