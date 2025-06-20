from . import views
from rest_framework.routers import DefaultRouter

app_name = "api-v1"

router = DefaultRouter()
router.register("post", views.PostViewSet, basename="post")
router.register("category", views.CategoryViewSet, basename="category")
urlpatterns = router.urls

"""
urlpatterns=[
    path('post/',PostViewSet.as_view({'get':'list','post':'create'}),name="post-list"),
    path('post/<int:pk>/',PostViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name="post-detail"),
]
"""
