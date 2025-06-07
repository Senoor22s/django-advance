from django.urls import path,include
from ..views import *
from rest_framework_simplejwt.views import (TokenRefreshView,TokenVerifyView)

urlpatterns=[
    path('registration/',RegistrationAPIView.as_view(),name="registration"),
    path('token/login/', CustomObtainAuthToken.as_view(),name='token-login'),
    path('token/logout/',CustomDiscardAuthToken.as_view(),name='token-logout'),
    path('jwt/create/',CustomTokenObtainPairView.as_view(),name='jwt-create'),
    path('jwt/refresh/',TokenRefreshView.as_view(),name='jwt-refresh'),
    path('jwt/verify/',TokenVerifyView.as_view(),name='jwt-verify'),
    path('change-password',ChangePasswordAPIView.as_view(),name='change-password'),
    path('test-email',TestEmailSend.as_view(),name='test-email'),
    path('activation/confirm/<str:token>',ActivationAPIView.as_view(),name='activation'),
    path('activation/resend',ActivationResendAPIView.as_view(),name='activation'),
]