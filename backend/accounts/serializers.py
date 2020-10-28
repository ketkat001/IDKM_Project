from rest_framework import serializers
from .models import User
# from django.contrib.auth import authenticate


# 회원가입
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'name', 'nickname', 'password', 'profile_image')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['email'], validated_data['nickname'], validated_data['password']
        )
        return user