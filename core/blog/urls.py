from django.urls import path, include
from . import views

app_name = "blog"

urlpatterns = [
    path("fbv-index", views.index_view, name="fbv-index"),
    path("cbv-index", views.IndexView.as_view(), name="cbv-index"),
    path("go-to-maktabkhooneh2", views.redirect_view, name="redirect-to-maktabkhooneh2"),
    path(
        "go-to-maktabkhooneh/<int:pk>/",
        views.Redirectview.as_view(),
        name="redirect-to-maktabkhooneh",
    ),
    path("post/", views.PostList.as_view(), name="post-list"),
    path("post/<int:pk>/", views.PostDetail.as_view(), name="post-detail"),
    path("post/create", views.PostCreate.as_view(), name="post-create"),
    path("post/create2", views.PostCreateView.as_view(), name="post-create2"),
    path("post/<int:pk>/edit", views.PostEdit.as_view(), name="post-edit"),
    path("post/<int:pk>/delete", views.PostDelete.as_view(), name="post-delete"),
    path("api/v1/", include("blog.api.v1.urls")),
]
