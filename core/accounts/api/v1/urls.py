from django.urls import path,include
from .views import *
from rest_framework_simplejwt.views import (TokenRefreshView,TokenVerifyView)

app_name="api-v1"

urlpatterns=[
    path('registration/',RegistrationAPIView.as_view(),name="registration"),
    path('token/login/', CustomObtainAuthToken.as_view(),name='token-login'),
    path('token/logout/',CustomDiscardAuthToken.as_view(),name='token-logout'),
    path('jwt/create/',CustomTokenObtainPairView.as_view(),name='jwt-create'),
    path('jwt/refresh/',TokenRefreshView.as_view(),name='jwt-refresh'),
    path('jwt/verify/',TokenVerifyView.as_view(),name='jwt-verify'),
    path('change-password',ChangePasswordAPIView.as_view(),name='change-password'),
    path('profile/',ProfileAPIView.as_view(),name='profile'),
]