from django.urls import path
from .views import *

app_name='blog'

urlpatterns=[
    path('fbv-index',index_view,name='fbv-index'),
    path('cbv-index',IndexView.as_view(),name='cbv-index'),
    path('go-to-maktabkhooneh2',redirect_view,name='redirect-to-maktabkhooneh2'),
    path('go-to-maktabkhooneh/<int:pk>/',Redirectview.as_view(),name='redirect-to-maktabkhooneh'),
    path('post/',PostList.as_view(),name='post-list'),
    path('post/<int:pk>/',PostDetail.as_view(),name='post-detail'),
]