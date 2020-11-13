from rest_framework import serializers
from .models import tagdatas, Movie, User_tagdatas


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
        fields = ('title', 'overview', 'poster_url', 'release_date', 'rating', 'genres', 'actors')

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('__all__')

# 태그 데이터 제외하고 뮤비 정보 보내기
class MovieSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview', 'poster_url', 'release_date', 'genres')

class User_tagdatasSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_tagdatas
        fields = ('__all__')