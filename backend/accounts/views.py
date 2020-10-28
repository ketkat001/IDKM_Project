from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions, generics
from .serializers import CreateUserSerializer, UserSerializer, LoginUserSerializer

# Create your views here.

#회원가입
class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response (
            {
                'user' : UserSerializer(
                    user, context = self.get_serializer_context()
                ).data,
            }
        )

#로그인
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {
                'user': UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,

            }
        )