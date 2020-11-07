from django.db import models
from django.conf import settings

# Create your models here.
# class Genre(models.Model):
#     name = models.CharField(max_length=100)

# class Overview_tag(models.Model):
#     tags = models.CharField(max_length=255)

class Movie_cast(models.Model):
    movie_actors = models.CharField(max_length=255)

class Movie(models.Model):
    title = models.CharField(max_length=255) 
    overview = models.TextField(null=True) 
    # poster_url = models.URLField()
    release_date = models.CharField(max_length = 30, null = True)
    runningtime = models.CharField(max_length = 10, null = True)  # 상영시간 time필드 맞는지 확인좀
    # vote_average = models.FloatField(max_length=11, null=False, blank=True)
    rating = models.CharField(max_length=11, null=True)
    # genre = models.ManyToManyField(Genre, related_name='movie_genre')
    # overview_tags = models.ManyToManyField(Overview_tag, related_name='overview_tags', null=True)
    actors = models.ManyToManyField(Movie_cast, related_name='movie_casts', blank=True)
    nation = models.CharField(max_length=255, null=True)
    maker = models.CharField(max_length=255, null=True)
    director = models.CharField(max_length=255, null=True)


class User_Overview(models.Model):
    overview_tags = models.ForeignKey(Overview_tag, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)


class User_Genre(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)


class User_Movie_cast(models.Model):
    movie_cast = models.ForeignKey(Movie_cast, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)


class Movie_rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True)


    