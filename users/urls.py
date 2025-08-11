from django.urls import path

from users.views import (
    LoginUserView,
    LogoutUserView,
    ProfileUpdateView,
    RegisterUserView,
)

urlpatterns = [
    path("template/register/", RegisterUserView.as_view(), name="register-template"),
    path("template/login/", LoginUserView.as_view(), name="login-template"),
    path("template/logout/", LogoutUserView.as_view(), name="logout-template"),
    path("template/profile/", ProfileUpdateView.as_view(), name="profile-template"),
]
