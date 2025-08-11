from django.urls import path

from users.views import (
    LoginUserView,
    LogoutUserView,
    ProfileUpdateView,
    RegisterUserView,
    UserDetailAPIView,
    UserListAPIView,
    UserProfileAPIView,
)

urlpatterns = [
    # APIs
    path("", UserListAPIView.as_view(), name="user-list"),
    path("<int:pk>/", UserDetailAPIView.as_view(), name="user-detail"),
    path("profile/", UserProfileAPIView.as_view(), name="profile"),
    # Templates
    path("template/register/", RegisterUserView.as_view(), name="register-template"),
    path("template/login/", LoginUserView.as_view(), name="login-template"),
    path("template/logout/", LogoutUserView.as_view(), name="logout-template"),
    path("template/profile/", ProfileUpdateView.as_view(), name="profile-template"),
]
