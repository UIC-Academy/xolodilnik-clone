from django.contrib.auth import get_user_model
from rest_framework import serializers

from blog.models import BlogPost

User = get_user_model()


class UserNestedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name"]


class PostListSerializer(serializers.ModelSerializer):
    user = UserNestedPostSerializer()

    class Meta:
        model = BlogPost
        fields = [
            "id",
            "title",
            "slug",
            "image",
            "user",
            "is_featured",
            "status",
            "published_at",
        ]


class PostDetailSerializer(serializers.ModelSerializer):
    user = UserNestedPostSerializer()

    class Meta:
        model = BlogPost
        fields = [
            "id",
            "title",
            "slug",
            "content",
            "image",
            "user",
            "is_featured",
            "status",
            "published_at",
            "created_at",
            "updated_at",
        ]


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            "title",
            "content",
            "image",
            "is_featured",
            "status",
        ]


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            "title",
            "content",
            "image",
            "is_featured",
            "status",
        ]
