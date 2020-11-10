from django.urls import path
from .views import RegistrationAPI, LoginAPI, UserDetailAPI, CheckAPI
from . import views

urlpatterns = [
    path('auth/register/', RegistrationAPI.as_view()),
    path('auth/login/', LoginAPI.as_view()),
    path('auth/detail/<nickname>/', UserDetailAPI.as_view()),
    path('check/', CheckAPI.as_view()),
    path('auth/social/kakao/', views.kakaologin),
]