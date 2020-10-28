from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.model):
    name = models.CharField(max_length=100)

class overview_tag(models.model):
    overview_t = models.CharField(max_length=255)

class movie_cast(models.model):
    movie_cast = models.CharField(max_length=255)

class Movie(models.Model):
    title = models.CharField(max_length=255)
    overview = models.CharField(max_length=255)
    poster_url = models.URLField()
    release_date = models.DateTimeField()
    adult = models.BooleanField()
    runningtime = models.TimeField()  # 상영시간 time필드 맞는지 확인좀
    vote_average = models.FloatField(max_length=11)
    rating = models.FloatField(max_length=11)
    genres = models.ManyToManyField(Genre, related_name='movie_genre')
    overview_tags = models.ManyToManyField(overview_tag, related_name='overview_tag')
    movie_casts = models.ManyToManyField(movie_cast, related_name='movie_cast')

