from django.db import models
from datetime import date
from django.urls import reverse

class Category(models.Model):
    name = models.CharField('Категории', max_length=150)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Actor(models.Model):

    name = models.CharField('Имя и Фамилия', max_length=100)
    age = models.PositiveSmallIntegerField('Возраст')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Фотография', upload_to='actors/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Актёр или режисёр'
        verbose_name_plural='Актёры или режисёры'


class Ganre(models.Model):
    name = models.CharField('Название жанра',max_length=100)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class MovieManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(draft=False)
        

class Movie(models.Model):
    title = models.CharField('Название', max_length=100)
    tagline = models.CharField('Слоган',max_length=100, default="")
    description = models.TextField('Описание')
    poster = models.ImageField(upload_to='movies/', verbose_name="Постер фильма")
    year = models.PositiveSmallIntegerField('Дата выхода', default=2019)
    country = models.CharField('Страна',max_length=30)
    director = models.ManyToManyField(Actor, related_name='movie_director', verbose_name='Режисет')
    actors = models.ManyToManyField(Actor, related_name='movie_actors', verbose_name='Актеры')
    ganre = models.ManyToManyField(Ganre, related_name='movie_ganre', verbose_name='Жанр')
    premiere_world = models.DateField(verbose_name='Премьера в мире', default=date.today )
    budget = models.PositiveIntegerField('Бюджет', default=0, help_text='Указывать кол-во в долларах')
    fees_usa = models.PositiveIntegerField('Сборы в США', default=0, help_text='Указывать кол-во в долларах')
    fees_world = models.PositiveIntegerField('Сборы в мире', default=0, help_text='Указывать кол-во в долларах')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='movie_category', verbose_name='Категории', null=True)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField(verbose_name="Черновик", default=False)

    objects = MovieManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home_detail", kwargs={"slug": self.url})
    

    class Meta:
        verbose_name='Фильм'
        verbose_name_plural='Фильмы'



class StarRatings(models.Model):
    rating = models.SmallIntegerField(verbose_name='Значение', default=0)

    def __str__(self):
        return self.rating

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'

class Rating(models.Model):
    ip = models.CharField('IP адрес',max_length=15)
    stars = models.ForeignKey(StarRatings, on_delete=models.CASCADE, null=True, verbose_name='Звезда', related_name='star_rating')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Фильм')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинг'



class MovieScene(models.Model):

    name = models.CharField('Название фильма', max_length=100)
    description = models.TextField('Описание')
    image = models.ImageField(verbose_name='Кадры из фильма', upload_to='movie_scenes/')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Фильм')

    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name = 'Кадры из фильма'
        verbose_name_plural = 'Кадры из фильма'

class Review(models.Model):
    email= models.EmailField()
    name = models.CharField('Имя', max_length=150)
    text = models.TextField('Сообщение', max_length=5000)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Родитель')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Фильм')

    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'



# Create your models here.
