from django.urls import path

from blog.views import (
    PostListAPIView,
    PostDetailAPIView,
    MyPostsListAPIView,
    PostCreateAPIView,
    PostUpdateAPIView,
    PostDeleteAPIView
)


urlpatterns = [
    path("", PostListAPIView.as_view(), name="post-list"),
    path("my/", MyPostsListAPIView.as_view(), name="my-post-list"),
    path("<slug:slug>/", PostDetailAPIView.as_view(), name="post-detail"),
    path("create/", PostCreateAPIView.as_view(), name="post-create"),
    path("<slug:slug>/update/", PostUpdateAPIView.as_view(), name="post-update"),
    path("<slug:slug>/delete/", PostDeleteAPIView.as_view(), name="post-delete"),
]
