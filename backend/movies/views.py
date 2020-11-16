from django.shortcuts import render
from .models import Movie, Tagdatas, User_tagdatas, Genres
from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, permissions
from backend.pagination import CustomPagination
from .serializers import MovieSerializer, TagdatasSerializer, MovieSerializer2, MovieDetailSerializer, User_tagdatasSerializer, GenreSerializer
from .newrecommend import recommend_sys, recommend_sys2
from accounts.models import User
# Create your views here.


class MovieListAPI(GenericAPIView):
    serializer_class = MovieSerializer2
    queryset = Movie.objects.all()
    pagination_class = CustomPagination

    def get(self, request):

        query = request.GET.get('query', '')
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            result = self.get_paginated_response(serializer.data)
            data = result.data  # pagination data
        else:
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data
        payload = {
            'return_code': '0000',
            'return_message': 'Success',
            'data': data
        }

        return Response(data)


class MovieDetailAPI(generics.GenericAPIView):
    serializer_class = MovieDetailSerializer
    queryset = Movie.objects.all()

    def get(self, request, pk):

        movie = get_object_or_404(Movie, pk=pk)
        m_data = MovieDetailSerializer(movie).data
        serializer = MovieDetailSerializer(movie, data=m_data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.data)


class MoviesearchAPI(generics.GenericAPIView):
    serializer_class = MovieDetailSerializer
    queryset = Movie.objects.all()

    def get(self, request):
        movies = request.GET.get('query', '')
        moviesearch = recommend_sys(movies)
        queryset = Movie.objects.filter(pk__in=moviesearch)
        serializer = MovieDetailSerializer(queryset, many=True)
        return Response(serializer.data)


class MovierecommendAPI(generics.GenericAPIView):
    serializer_class = MovieDetailSerializer
    queryset = Movie.objects.all()

    def get(self, request, user_pk):
        moviesearch = recommend_sys2(user_pk)
        queryset = Movie.objects.filter(pk__in=moviesearch)
        serializer = MovieDetailSerializer(queryset, many=True)
        return Response(serializer.data)


class MoviedibAPI(generics.GenericAPIView):
    serializer_class = MovieDetailSerializer
    queryset = Movie.objects.all()

    def get(self, request, user_pk, movie_pk):
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = get_object_or_404(User, pk=user_pk)
        queryset = Movie.objects.filter(pk=movie_pk)
        if user in movie.user_dib.all():
            movie.user_dib.remove(user)
        else:
            movie.user_dib.add(user)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)


class MovielikeAPI(generics.GenericAPIView):
    serializer_class = MovieDetailSerializer
    queryset = Movie.objects.all()

    def get(self, request, user_pk, movie_pk):
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = get_object_or_404(User, pk=user_pk)
        queryset = Movie.objects.filter(pk=movie_pk)
        if user in movie.user_like.all():
            movie.user_like.remove(user)
            minusweight(user_pk, movie_pk)
        else:
            movie.user_like.add(user)
            plusweight(user_pk, movie_pk)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)


class MoviewatchedAPI(generics.GenericAPIView):
    serializer_class = MovieDetailSerializer
    queryset = Movie.objects.all()

    def get(self, request, user_pk, movie_pk):
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = get_object_or_404(User, pk=user_pk)
        queryset = Movie.objects.filter(pk=movie_pk)
        if user in movie.user_watched.all():
            movie.user_watched.remove(user)
            minusweight(user_pk, movie_pk)
        else:
            movie.user_watched.add(user)
            plusweight(user_pk, movie_pk)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)


def plusweight(user_pk, movie_pk):
    tag_queryset = Movie.objects.filter(pk=movie_pk).values('tagdatas')
    user_queryset = User_tagdatas.objects.filter(
        user_id=user_pk).values('tagdata_id')
    tagging = []
    u_tagging = []
    for tag in tag_queryset:
        tagging.append(tag['tagdatas'])
    for u_tag in user_queryset:
        u_tagging.append(u_tag['tagdata_id'])
    for tag in tagging:
        if tag in u_tagging:
            user_tag = User_tagdatas.objects.get(
                user_id=user_pk, tagdata_id=tag)
            user_tag.weight += 1
            user_tag.save()
        else:
            user_tag = User_tagdatas.objects.create(
                user_id=user_pk, tagdata_id=tag)
            user_tag.weight += 1
            user_tag.save()
    return


def minusweight(user_pk, movie_pk):
    tag_queryset = Movie.objects.filter(pk=movie_pk).values('tagdatas')
    user_queryset = User_tagdatas.objects.filter(
        user_id=user_pk).values('tagdata_id')
    tagging = []
    u_tagging = []

    for tag in tag_queryset:
        tagging.append(tag['tagdatas'])
    for u_tag in user_queryset:
        u_tagging.append(u_tag['tagdata_id'])
    for tag in tagging:
        if tag in u_tagging:
            user_tag = User_tagdatas.objects.get(
                user_id=user_pk, tagdata_id=tag)
            user_tag.weight -= 1
            user_tag.save()
        else:
            user_tag = User_tagdatas.objects.create(
                user_id=user_pk, tagdata_id=tag)
            user_tag.weight -= 1
            user_tag.save()
    return
