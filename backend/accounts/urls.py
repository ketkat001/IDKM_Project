from django.urls import path
from .views import RegistrationAPI, LoginAPI

urlpatterns = [
    path('auth/register/', RegistrationAPI.as_view()),
    path('auth/login/', LoginAPI.as_view()),
]