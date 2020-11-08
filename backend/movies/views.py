from django.shortcuts import render
from .models import Movie, tagdatas
from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from backend.pagination import CustomPagination
from .serializers import MovieSerializer
# Create your views here.

class MovieListAPI(GenericAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    pagination_class = CustomPagination
    

    def get(self, request):
        # sort = request.GET.get('sort','')
        query = request.GET.get('query', '')
        # if sort == 'likes':
        #     queryset = Heritage.objects.annotate(like_count=Count('like_users')).order_by('-like_count')
        #     if query:
        #         queryset = queryset.filter(Q (k_name__icontains=query) | Q (content__icontains=query)).order_by('-hit')
        # else:
        #     queryset = self.filter_queryset(self.get_queryset())
        #     if query:
        #         queryset = queryset.filter(Q (k_name__icontains=query) | Q (content__icontains=query)).order_by('-hit')
        page = self.paginate_queryset(query)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            result = self.get_paginated_response(serializer.data)
            data = result.data # pagination data
        else:
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data
        payload = {
            'return_code': '0000',
            'return_message': 'Success',
            'data': data
        }
        return Response(data)