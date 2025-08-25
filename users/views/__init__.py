from .profession import (
    ProfessionCreateAPIView,
    ProfessionDestroyAPIView,
    ProfessionListAPIView,
    ProfessionRetrieveAPIView,
    ProfessionUpdateAPIView,
)
from .template_views import (
    LoginUserView,
    LogoutUserView,
    ProfileUpdateView,
    RegisterUserView,
)
from .user_detail import UserDetailAPIView, UserProfileAPIView
from .user_list import UserListAPIView
from .register import UserRegisterAPIView, EmailConfirmAPIView

__all__ = [
    "LoginUserView",
    "LogoutUserView",
    "ProfessionCreateAPIView",
    "ProfessionDestroyAPIView",
    "ProfessionListAPIView",
    "ProfessionListAPIView",
    "ProfessionRetrieveAPIView",
    "ProfessionUpdateAPIView",
    "ProfileUpdateView",
    "RegisterUserView",
    "UserDetailAPIView",
    "UserListAPIView",
    "UserProfileAPIView",
    "UserRegisterAPIView",
    "EmailConfirmAPIView",
]
