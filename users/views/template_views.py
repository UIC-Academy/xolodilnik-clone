from django.views.generic import FormView, View
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy

from users.forms import RegisterForm, LoginForm


class RegisterUserView(FormView):
    template_name = "auth/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('login-template')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = RegisterForm()

        return context
    

class LoginUserView(FormView):
    template_name = "auth/login.html"
    form_class = LoginForm
    success_url = reverse_lazy('home-template')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = LoginForm()

        return context
    
    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password:
            return JsonResponse(
                {"error": "Email and password are required"},
                status=400,
            )

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"message": "Login successful"})
        else:
            return JsonResponse(
                {"error": "Invalid credentials"}, status=401
            )
        

class LogoutUserView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return JsonResponse({"message": "Logout successful"})