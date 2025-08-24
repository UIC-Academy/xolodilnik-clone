from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters import rest_framework as filters
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

from blog.models import BlogPost
from blog.choices import BlogPostStatus
from blog.serializers import PostListSerializer, PostDetailSerializer, PostCreateSerializer, PostUpdateSerializer, UserNestedPostSerializer


class PostListAPIView(generics.ListAPIView):
    queryset = BlogPost.objects.filter(status=BlogPostStatus.PUBLISHED).order_by("-published_at")
    serializer_class = PostListSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ("category", "tags")


class MyPostsListAPIView(generics.ListAPIView):
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ("category", "tags")

    def get_queryset(self):
        return BlogPost.objects.filter(status=BlogPostStatus.PUBLISHED, user=self.request.user).order_by("-published_at")


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = BlogPost.objects.filter(status=BlogPostStatus.PUBLISHED)
    serializer_class = PostDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "slug"


class PostCreateAPIView(generics.CreateAPIView):
    queryset = BlogPost.objects.filter(status=BlogPostStatus.PUBLISHED)
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]


class PostUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PostUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "slug"

    def get_queryset(self):
        return BlogPost.objects.filter(status=BlogPostStatus.PUBLISHED, user=self.request.user)


class PostDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = "slug"

    def get_queryset(self):
        return BlogPost.objects.filter(status=BlogPostStatus.PUBLISHED, user=self.request.user)