from rest_framework import serializers
from .models import tagdatas, Movie


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


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('__all__')