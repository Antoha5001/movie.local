from django.db import models

class Category(models.Model):
    name = models.CharField('Категории', max_length=150)
    description = models.TextField()
    url = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# Create your models here.
