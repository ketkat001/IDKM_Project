from rest_framework import serializers
from .models import Movie_cast, Movie, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('__all__')


# class Overview_tagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Overview_tag
#         fields = ('__all__')

class Movie_castSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_cast
        fields = ('__all__')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('__all__')