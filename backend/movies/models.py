from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)

class Overview_tag(models.Model):
    tags = models.CharField(max_length=255)

class Movie_cast(models.Model):
    actors = models.CharField(max_length=255)

class Movie(models.Model):
    title = models.CharField(max_length=255)
    overview = models.CharField(max_length=255)
    poster_url = models.URLField()
    release_date = models.DateTimeField()
    adult = models.BooleanField()
    runningtime = models.TimeField()  # 상영시간 time필드 맞는지 확인좀
    vote_average = models.FloatField(max_length=11)
    rating = models.FloatField(max_length=11, default=null)
    genres = models.ManyToManyField(Genre, related_name='movie_genre')
    overview_tags = models.ManyToManyField(Overview_tag, related_name='overview_tag')
    movie_casts = models.ManyToManyField(Movie_cast, related_name='movie_cast')

