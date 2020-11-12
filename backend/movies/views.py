from django.shortcuts import render
from .models import Movie, tagdatas, Movie_rating
from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, permissions
from backend.pagination import CustomPagination
from .serializers import MovieSerializer, Movie_rating, tagdatasSerializer , MovieSerializer2, MovieDetailSerializer
# Create your views here.

class MovieListAPI(GenericAPIView):
    serializer_class = MovieSerializer2
    queryset = Movie.objects.all()
    pagination_class = CustomPagination
    
    def get(self, request):
        # sort = request.GET.get('sort','')
        query = request.GET.get('query', '')
        queryset = self.filter_queryset(self.get_queryset())
      
        # if sort == 'likes':
        #     queryset = Heritage.objects.annotate(like_count=Count('like_users')).order_by('-like_count')
        #     if query:
        #         queryset = queryset.filter(Q (k_name__icontains=query) | Q (content__icontains=query)).order_by('-hit')
        # else:
        #     queryset = self.filter_queryset(self.get_queryset())
        #     if query:
        #         queryset = queryset.filter(Q (k_name__icontains=query) | Q (content__icontains=query)).order_by('-hit')
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
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer

    

    def get(self, request, pk):
 
        movie = get_object_or_404(Movie, pk=pk)

        
        # if request.session.get("h_hit", False) == False:
        #     request.session["h_hit"] = []
        # hit_l = request.session["h_hit"]
        # if pk not in hit_l:
        #     hit_l.append(pk)
        #     request.session["h_hit"] = hit_l
        #     heritage.hit += 1

        m_data = MovieDetailSerializer(movie).data


        serializer = MovieDetailSerializer(movie, data = m_data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.data)




# class HeritageDetailAPI(generics.GenericAPIView):
#     queryset = Heritage.objects.all()
#     serializer_class = HeritageDetailSerializer

#     def get(self ,request, pk):
#         heritage = get_object_or_404(Heritage, pk=pk)
#         if request.session.get("h_hit", False) == False:
#             request.session["h_hit"] = []
#         hit_l = request.session["h_hit"]
#         if pk not in hit_l:
#             hit_l.append(pk)
#             request.session["h_hit"] = hit_l
#             heritage.hit += 1
        
#         h_data = HeritageDetailSerializer(heritage).data
#         serializer = HeritageDetailSerializer(heritage, data = h_data)
#         if serializer.is_valid():
#             serializer.save()
            
#             return Response(serializer.data)

        return Response(serializer.data)