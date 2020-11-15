from django.db import models
from django.conf import settings

# Create your models here.
class actor(models.Model):
    actor_id = models.IntegerField()
    name = models.CharField(max_length=50, null=True)
    profile_path = models.TextField(null=True)
    ko_name = models.TextField(null=True)

class tagdatas(models.Model):
    tags = models.CharField(max_length=50, null=True)

class Movie(models.Model):
    title = models.CharField(max_length=255) 
    overview = models.TextField(null=True) 
    poster_url = models.TextField(null=True)
    release_date = models.CharField(max_length = 30, null=True)
    rating = models.BooleanField()
    genres = models.CharField(max_length= 255, null=True)
    tagdatas = models.ManyToManyField(tagdatas, related_name='movie_tagdatas')
    actors = models.ManyToManyField(actor, related_name='movie_actor')
    user_dib = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='movie_user_dib')
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='movie_user_like')
    user_watched = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='movie_user_watched')
    searchdata = models.TextField()

class User_tagdatas(models.Model):
    tagdata = models.ForeignKey(tagdatas, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)

# class User_Overview(models.Model):
#     overview_tags = models.ForeignKey(Overview_tag, on_delete=models.CASCADE)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     weight = models.IntegerField(default=0)


# class User_Genre(models.Model):
#     genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     weight = models.IntegerField(default=0)


# class User_Movie_cast(models.Model):
#     movie_cast = models.ForeignKey(Movie_cast, on_delete=models.CASCADE)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     weight = models.IntegerField(default=0)





    
