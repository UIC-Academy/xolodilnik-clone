from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from blog.models import BlogCategory
from blog.serializers import BlogCategorySerializer


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    permission_classes = [IsAuthenticated]


class CategoryRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"