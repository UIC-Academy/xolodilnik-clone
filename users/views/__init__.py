from .template_views import (
    LoginUserView,
    LogoutUserView,
    ProfileUpdateView,
    RegisterUserView,
)
from .user_detail import UserDetailAPIView, UserProfileAPIView
from .user_list import UserListAPIView

__all__ = [
    "LoginUserView",
    "LogoutUserView",
    "ProfileUpdateView",
    "RegisterUserView",
    "UserDetailAPIView",
    "UserListAPIView",
    "UserProfileAPIView",
]
