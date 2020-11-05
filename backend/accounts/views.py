from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import permissions, generics
from .serializers import CreateUserSerializer, UserSerializer, LoginUserSerializer, UserDetailSerializer
from knox.models import AuthToken
from .models import User
import requests
# Create your views here.

#회원가입
class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = AuthToken.objects.create(user)[1]
        return Response (
            {
                'user' : UserSerializer(
                    user, context = self.get_serializer_context()
                ).data,
                'token': token,
            }
        )


#로그인
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = AuthToken.objects.create(user)[1]
        return Response(
            {
                'user': UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                'token': token,

            }
        )

class UserDetailAPI(generics.GenericAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    def get(self, request, nickname):
        # user = User.objects.get(nickname=nickname)
        user = get_object_or_404(User, nickname=nickname)
        # profile = get_object_or_404(Profile, pk=user.id)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, nickname):
        user = User.objects.get(nickname=nickname)
        # profile = get_object_or_404(Profile, pk=user.id)
        if type(request.data) == dict:
            ordinary_dict = request.data
            query_dict = QueryDict('', mutable=True)
            query_dict.update(ordinary_dict)
        else:
            query_dict = request.data
        serializer = UserDetailSerializer(user, data=query_dict)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        

        return Response(serializer.errors, status=400)
    
    def delete(self, request, nickname):
        user = User.objects.get(nickname=nickname)
        user.delete()
        return Response(True)


class CheckAPI(generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def emailcheck(self, request, check):
        # email = request.check
        if User.objects.filter(nickname=check).exists() or User.objects.filter(email=check).exists():
            return Response(False)
        else:
            return Response(True)


def kakaologin(request):
    REDIRECT_URI = 'http://127.0.0.1:8000/accounts/kakao/login/callback/'
    hp = f'/oauth/authorize?client_id=499848&redirect_uri={REDIRECT_URI}&response_type=code'
    rdata = requests.get(hp)
    print(rdata)