from django.urls import path,include
from .views import *

app_name="api-v1"

urlpatterns=[
    path('post/',post_list,name="post-list"),
    path('post/<int:pk>/',post_detail,name="post-detail"),
]