from django.urls import path

from users.views import RegisterUserView, LoginUserView, LogoutUserView


urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register-template"),
    path("login/", LoginUserView.as_view(), name="login-template"),  
    path("logout/", LogoutUserView.as_view(), name="logout-template"),
]
