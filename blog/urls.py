from django.urls import path

from blog.views import (
    CommentCreateAPIView,
    CommentDeleteAPIView,
    MyPostsListAPIView,
    PostCommentListAPIView,
    PostCreateAPIView,
    PostDeleteAPIView,
    PostDetailAPIView,
    PostListAPIView,
    PostUpdateAPIView,
)

urlpatterns = [
    # posts
    path("", PostListAPIView.as_view(), name="post-list"),
    path("my/", MyPostsListAPIView.as_view(), name="my-post-list"),
    path("<slug:slug>/", PostDetailAPIView.as_view(), name="post-detail"),
    path("create/", PostCreateAPIView.as_view(), name="post-create"),
    path("<slug:slug>/update/", PostUpdateAPIView.as_view(), name="post-update"),
    path("<slug:slug>/delete/", PostDeleteAPIView.as_view(), name="post-delete"),
    # comments
    path(
        "<int:post_id>/comments/",
        PostCommentListAPIView.as_view(),
        name="post-comments",
    ),
    path("comments/create/", CommentCreateAPIView.as_view(), name="comment-create"),
    path(
        "comments/delete/<int:id>/",
        CommentDeleteAPIView.as_view(),
        name="comment-delete",
    ),
]
