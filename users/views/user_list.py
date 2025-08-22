from django_filters import rest_framework as filters
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserListSerializer


class UserListFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = ["profession", "is_active"]


class UserListAPIView(ListAPIView):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserListSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ("profession", "is_active")
