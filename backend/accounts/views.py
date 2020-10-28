from django.shortcuts import render
from rest_framework import permissions, generics
from .serializers import CreateUserSerializer
from knox.models import AuthToken
# Create your views here.


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
