from django.urls import path,include
from ..views import *

urlpatterns=[
    path('',ProfileAPIView.as_view(),name='profile'),
]