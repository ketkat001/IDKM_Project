from rest_framework import serializers
from .models import tagdatas, Movie, Movie_rating


# class GenreSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Genre
#         fields = ('__all__')


# class Overview_tagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Overview_tag
#         fields = ('__all__')

class tagdatasSerializer(serializers.ModelSerializer):
    class Meta:
        model = tagdatas
        fields = ('__all__')

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview', 'poster_url', 'release_date', 'runningtime', 'rating', 'genres', 'actors', 'nation', 'maker','director')

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('__all__')

class Movie_rating(serializers.ModelSerializer):
    class Meta:
        model = Movie_rating
        fields = ('__all__')

# 태그 데이터 제외하고 뮤비 정보 보내기
class MovieSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview', 'poster_url', 'release_date', 'runningtime', 'genres', 'nation', 'maker', 'director')


