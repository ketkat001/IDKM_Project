from rest_framework import serializers
from .models import Tagdatas, Movie, User_tagdatas, Actor, Genres


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('ko_name', 'profile_path')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ('__all__')


class TagdatasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tagdatas
        fields = ('__all__')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('__all__')

# 태그 데이터 제외하고 뮤비 정보 보내기


class MovieSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview', 'poster_url',
                  'release_date', 'genres', 'actors')


class User_tagdatasSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_tagdatas
        fields = ('__all__')


class MovieDetailSerializer(serializers.ModelSerializer):

    actors = ActorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('__all__')
