from django.urls import path,include
from .views import *

app_name="api-v1"

urlpatterns=[
    path('registration/',RegistrationAPIView.as_view(),name="registration"),
]